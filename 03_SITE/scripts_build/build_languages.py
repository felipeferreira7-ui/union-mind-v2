"""Build static PT/EN pairs from the maintained bilingual Portuguese pages.

Stdlib only. Language follows the URL; translated content and metadata are present
without running JavaScript. The source remains the PT file plus its dictionaries.
Run after generate_seo.py, then run check_site.py before preparing publication.
"""
from html.parser import HTMLParser
from html import escape, unescape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, urljoin
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://unionmind.solutions'
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
LEGACY = {'sobre-nos': '/#fundador', 'portfolio': '/#cases',
          'servicos/organizacao-de-eventos': '/servicos/eventos-corporativos.html',
          'servicos/cenografia-e-estandes': '/servicos/estandes-e-cenografia.html'}


class Node:
    def __init__(self, tag='', attrs=(), raw=''):
        self.tag, self.attrs, self.raw, self.children = tag, dict(attrs), raw, []

    def render(self):
        if not self.tag:
            return self.raw + ''.join(c.render() for c in self.children)
        attrs = ''.join(' ' + k + ('' if v is None else '="' + escape(v, quote=True) + '"') for k, v in self.attrs.items())
        start = '<' + self.tag + attrs + '>'
        return start if self.tag in VOID else start + ''.join(c.render() for c in self.children) + '</' + self.tag + '>'

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()

    def content(self, text):
        self.children = [Node(raw=text)]


class Tree(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.root = Node()
        self.stack = [self.root]
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        self.stack[-1].children.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, text): self.stack[-1].children.append(Node(raw=text))
    def handle_entityref(self, name): self.handle_data('&' + name + ';')
    def handle_charref(self, name): self.handle_data('&#' + name + ';')
    def handle_comment(self, text): self.handle_data('<!--' + text + '-->')
    def handle_decl(self, text): self.handle_data('<!' + text + '>')


def route(path):
    return path + 'index.html' if path.endswith('/') else path


def plain(text):
    return unescape(re.sub('<[^>]+>', '', text))


def metadata(source, translations):
    match = re.search(r'const pageMetadata = (\{[^\n]+\});', source)
    if match: return json.loads(match.group(1))
    if 'class="union-home"' in source:
        return {
            'pt': {'title': 'Union Mind | Agência boutique de eventos e live marketing', 'description': 'Agência boutique de eventos corporativos, convenções, ativações e estandes. Criação, planejamento e produção com liderança próxima. Union Mind, São Paulo.'},
            'en': {'title': 'Union Mind | Boutique corporate events agency in São Paulo', 'description': 'Boutique event agency in São Paulo. Conventions, brand experiences and exhibition booths, with creative work, planning and hands-on production leadership.'}
        }
    if '<title>Union Labs' in source:
        tree = Tree(source).root
        desc = next(n.attrs['content'] for n in tree.walk() if n.tag == 'meta' and n.attrs.get('name') == 'description')
        return {'pt': {'title': 'Union Labs | Tecnologia para Eventos', 'description': desc}, 'en': {'title': 'Union Labs | Event Technology', 'description': 'Guest management, apps, automations and reporting integrated with your event production. Meet Union Labs.'}}
    raise ValueError('Missing page metadata')


def build(source, path, paths, lang):
    dictionary = re.search(r'const (?:translations|localTranslations) = (\{.*?\n\});', source, re.S)
    if not dictionary: raise ValueError('Missing dictionaries: ' + path)
    translations = json.loads(dictionary.group(1))
    meta = metadata(source, translations)[lang]
    t = translations[lang]
    en_path = '/en' + path
    canonical = ORIGIN + (en_path if lang == 'en' else path)
    tree = Tree(source).root
    head = next(n for n in tree.walk() if n.tag == 'head')
    # Replace the unverified legacy GTM container with the verified GA4 destination.
    # Do not load two owners of page_view/lead events. Clarity is kept unchanged.
    for parent in list(tree.walk()):
        parent.children = [n for n in parent.children if not (
            (n.tag == 'script' and 'GTM-M2MTZZXD' in ''.join(c.render() for c in n.children)) or
            (n.tag == 'noscript' and 'GTM-M2MTZZXD' in n.render()) or
            (n.tag == 'script' and n.attrs.get('src','').startswith('/scripts/analytics.js'))
        )]
    head.children.append(Node('script', [('src','/scripts/analytics.js?v=20260917d'),('defer',None)]))
    head.children = [n for n in head.children if not (n.tag == 'link' and n.attrs.get('hreflang'))]
    for code, href in [('pt-BR', ORIGIN+path), ('en', ORIGIN+en_path), ('x-default', ORIGIN+path)]:
        head.children.append(Node('link', [('rel','alternate'),('hreflang',code),('href',href)]))
    mapping = {plain(v): plain(translations['en'][k]) for k,v in translations['pt'].items() if k in translations['en']}
    mapping.update({'Brasil': 'Brazil'})
    mapping.update({'Eventos corporativos':'Corporate events', 'Convenções de vendas':'Sales conventions',
                    'Ativações de marca':'Brand activations', 'Estandes e cenografia':'Exhibition booths and scenography'})
    def schema(value, top=True):
        if isinstance(value,list): return [schema(v, False) for v in value]
        if isinstance(value,dict):
            value = {k:schema(v, False) for k,v in value.items()}
            if top and value.get('@type') in ['WebPage','Article','BlogPosting','Service']:
                value['inLanguage'] = 'en' if lang == 'en' else 'pt-BR'
                if value.get('@type') == 'Service':
                    value['name'] = plain(t.get('service-name', meta['title'].split(' | ')[0]))
                elif value.get('@type') in ['Article','BlogPosting']:
                    value['headline'] = meta['title'].split(' | ')[0]
                else: value['name'] = meta['title']
                value['description'] = meta['description']
                value['url'] = canonical
            if isinstance(value.get('@type'),list): value['description'] = meta['description']
            if top and value.get('@type')=='Person' and lang=='en':
                value['jobTitle']='Founder and operations director'
                value['description']='Felipe Ferreira is the founder and operations director of Union Mind, a boutique corporate events agency based in São Paulo.'
            return value
        if isinstance(value,str):
            if lang == 'en' and value in mapping: return mapping[value]
            if lang == 'en' and value.startswith(ORIGIN):
                u=urlsplit(value)
                if u.path in paths: return urlunsplit((u.scheme,u.netloc,'/en'+u.path,u.query,u.fragment))
            return value
        return value
    for n in list(tree.walk()):
        a=n.attrs
        if n.tag == 'html': a['lang']='en' if lang == 'en' else 'pt-BR'
        if a.get('data-i18n'):
            key=a['data-i18n']
            if key not in t: raise ValueError(path+': missing '+lang+' '+key)
            n.content(t[key])
        if 'data-placeholder-'+lang in a: a['placeholder']=a['data-placeholder-'+lang]
        if 'data-alt-'+lang in a: a['alt']=a['data-alt-'+lang]
        if n.tag == 'title': n.content(escape(meta['title']))
        if n.tag == 'form' and 'formspree.io' in a.get('action',''):
            if not any(c.tag=='input' and c.attrs.get('name')=='_gotcha' for c in n.children):
                n.children.append(Node('input', [('type','text'),('name','_gotcha'),('tabindex','-1'),('autocomplete','off'),('aria-hidden','true'),('style','display:none')]))
        if n.tag == 'meta':
            key=a.get('property') or a.get('name')
            if key in ['description','og:description','twitter:description']: a['content']=meta['description']
            if key in ['og:title','twitter:title']: a['content']=meta['title']
            if key == 'og:url': a['content']=canonical
            if key == 'og:locale': a['content']='en_US' if lang == 'en' else 'pt_BR'
            if key == 'og:locale:alternate': a['content']='pt_BR' if lang == 'en' else 'en_US'
        if n.tag == 'link' and a.get('rel')=='canonical': a['href']=canonical
        if n.tag == 'script' and a.get('type')=='application/ld+json':
            n.content(json.dumps(schema(json.loads(''.join(c.render() for c in n.children))),ensure_ascii=False,indent=2))
        # Resolve media relative to the source, not /en/; preserve all query strings.
        for attr in ['src','href']:
            url=a.get(attr)
            if not url or url.startswith(('#','mailto:','tel:','data:')): continue
            u=urlsplit(url)
            if u.netloc and u.netloc != 'unionmind.solutions': continue
            if u.scheme and u.scheme not in ['http','https']: continue
            resolved=urlsplit(urljoin(ORIGIN+path,url))
            target=resolved.path
            query=resolved.query
            if n.tag=='a' and path.startswith('/servicos/') and target=='/' and resolved.fragment=='configurador' and not query:
                query='service='+Path(path).stem
            if n.tag=='a' and target in paths:
                target=('/en'+target) if lang=='en' else target
            if not u.netloc:
                a[attr]=urlunsplit(('', '',target,query,resolved.fragment))
                if target in ['/style-v2.css', '/scripts/site-ui.js']:
                    a[attr]=target+'?v=20260917f'
        if a.get('id') in ['btn-pt','btn-en']:
            selected = a['id']=='btn-'+lang
            n.tag='a';a.pop('onclick',None);a.pop('type',None);a.pop('aria-pressed',None)
            a['href']=path if a['id']=='btn-pt' else en_path
            a['lang']='pt-BR' if a['id']=='btn-pt' else 'en'
            a['hreflang']=a['lang']
            a['class']='active' if selected else ''
            if selected:a['aria-current']='page'
            else:a.pop('aria-current',None)
    return '\n'.join(line.rstrip() for line in tree.render().splitlines()).rstrip()+'\n'


def main():
    # Ignore previous /en/ entries so repeated builds are deterministic.
    paths = [urlsplit(e.text).path for e in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc') if not urlsplit(e.text).path.startswith('/en/')]
    paths += ['/servicos/'+p.name for p in sorted((ROOT/'servicos').glob('*.html'))]
    paths = list(dict.fromkeys(paths))
    for path in paths:
        p=ROOT/route(path).lstrip('/')
        source=p.read_text(encoding='utf-8')
        p.write_text(build(source,path,set(paths),'pt'),encoding='utf-8')
        target=ROOT/route('/en'+path).lstrip('/')
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(build(source,path,set(paths),'en'),encoding='utf-8')
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap+=''.join('  <url><loc>'+ORIGIN+p+'</loc></url>\n' for p in paths+['/en'+p for p in paths])
    (ROOT/'sitemap.xml').write_text(sitemap+'</urlset>\n',encoding='utf-8')
    # GitHub Pages has no custom HTTP redirect rules. Immediate meta refresh is
    # the supported static fallback; sources are excluded from the sitemap.
    for old, target in LEGACY.items():
        p=ROOT/old/'index.html';p.parent.mkdir(parents=True,exist_ok=True)
        canonical=ORIGIN+target.split('#')[0]
        p.write_text('<!DOCTYPE html>\n<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Union Mind</title><meta name="robots" content="noindex, follow"><link rel="canonical" href="'+canonical+'"><meta http-equiv="refresh" content="0;url='+target+'"></head><body><p>Esta página mudou de endereço. <a href="'+target+'">Continue no site da Union Mind.</a></p></body></html>\n',encoding='utf-8')
    # Both development mirrors retain noindex and the production canonical.
    home=(ROOT/'index.html').read_text(encoding='utf-8')
    for name in ['index-v2.html','index-v2-preview.html']:
        (ROOT/name).write_text(home.replace('<head>', '<head>\n<meta name="robots" content="noindex, follow">',1),encoding='utf-8')
    print(f'Built {len(paths)} static PT/EN pairs, reciprocal hreflang, sitemap ({len(paths)*2} URLs) and {len(LEGACY)} legacy redirects.')


if __name__=='__main__': main()
