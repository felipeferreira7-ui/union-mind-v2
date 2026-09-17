"""Check public routes, canonical URLs, local links/assets and inline JavaScript.

Usage: UNION_NODE=/path/to/node python3 scripts_build/check_site.py
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import os
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://unionmind.solutions'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.assets, self.ids, self.canonicals, self.scripts = [], [], set(), [], []
        self.script = None
        self.hreflang, self.language = {}, ''
        self.translation_keys = set()
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.language = a.get('lang', '')
        if tag == 'link' and a.get('hreflang'): self.hreflang[a['hreflang']] = a.get('href')
        if 'data-i18n' in a: self.translation_keys.add(a['data-i18n'])
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ['img', 'script'] and a.get('src'): self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet': self.assets.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a['href'])
        if tag == 'script' and not a.get('src'): self.script = [a.get('type', ''), '']

    def handle_data(self, text):
        if self.script is not None: self.script[1] += text

    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            self.scripts.append(self.script)
            self.script = None


def route(url):
    path = unquote(urlsplit(url).path)
    return path + 'index.html' if path.endswith('/') else path


def check():
    errors, scripts = [], []
    urls = [e.text for e in ET.parse(ROOT / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert len(urls) == len(set(urls)), 'Duplicate sitemap URLs'
    pages = {ROOT / route(url).lstrip('/'): Page(ROOT / route(url).lstrip('/')) for url in urls}
    for path, page in pages.items():
        relative = str(path.relative_to(ROOT))
        expected = ORIGIN + '/' + (relative[:-10] if relative.endswith('index.html') else relative)
        if [u.rstrip('/') for u in page.canonicals] != [expected.rstrip('/')]: errors.append(f'{relative}: canonical {page.canonicals}')
        english = relative.startswith('en/')
        pt_url = expected.replace(ORIGIN + '/en/', ORIGIN + '/', 1) if english else expected
        alternatives = {'pt-BR': pt_url, 'en': pt_url.replace(ORIGIN + '/', ORIGIN + '/en/', 1), 'x-default': pt_url}
        if page.hreflang != alternatives: errors.append(f'{relative}: invalid language alternatives {page.hreflang}')
        if page.language != ('en' if english else 'pt-BR'): errors.append(f'{relative}: wrong HTML language')
        for code, href in page.hreflang.items():
            target = ROOT / route(href).lstrip('/')
            if not target.exists(): errors.append(f'{relative}: missing hreflang target {href}')
            elif (pages.get(target) or Page(target)).hreflang != alternatives: errors.append(f'{relative}: non-reciprocal hreflang {href}')
        for href in page.links + page.assets:
            u = urlsplit(href)
            if u.scheme or u.netloc: continue
            target = (ROOT / u.path.lstrip('/') if u.path.startswith('/') else path.parent / u.path) if u.path else path
            if target.is_dir(): target /= 'index.html'
            target = target.resolve()
            if not target.exists(): errors.append(f'{relative}: missing {href}')
            elif u.fragment and target.suffix == '.html':
                target_page = pages.get(target) or Page(target)
                if unquote(u.fragment) not in target_page.ids: errors.append(f'{relative}: missing anchor {href}')
        for kind, script in page.scripts:
            if kind == 'application/ld+json': json.loads(script)
            elif kind in ['', 'text/javascript']: scripts.append({'file': relative, 'code': script})
            match = re.search(r'const (?:translations|localTranslations) = (\{.*?\n\});', script, re.S)
            if match:
                translations = json.loads(match.group(1))
                for lang in ['pt', 'en']:
                    missing = page.translation_keys - translations.get(lang, {}).keys()
                    if missing: errors.append(f'{relative}: {lang} missing translations {sorted(missing)}')
    scripts.append({'file': 'scripts/site-ui.js', 'code': (ROOT / 'scripts/site-ui.js').read_text()})
    scripts.append({'file': 'scripts/analytics.js', 'code': (ROOT / 'scripts/analytics.js').read_text()})
    node = os.environ.get('UNION_NODE', 'node')
    result = subprocess.run([node, '-e', "const vm=require('node:vm'),fs=require('node:fs');let fail=false;for(const s of JSON.parse(fs.readFileSync(0,'utf8'))){try{new vm.Script(s.code,{filename:s.file})}catch(e){console.error(e.message+' in '+s.file);fail=true}}process.exit(fail?1:0)"], input=json.dumps(scripts), text=True, capture_output=True)
    if result.returncode: errors.append(result.stderr)
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} public pages; canonical URLs, local links/assets, JSON-LD and {len(scripts)} JavaScript sources checked.')


if __name__ == '__main__': check()
