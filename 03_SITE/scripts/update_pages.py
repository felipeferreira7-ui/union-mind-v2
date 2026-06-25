#!/usr/bin/env python3
"""
Union Mind — Site-wide nav/footer/CSS updater
Applies new design system (v2) to all secondary pages.
"""

import os
import re
import glob

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── NEW NAV HTML ────────────────────────────────────────────
# Used for ESPACOS pages (relative path: ../)
NAV_ESPACOS = '''<header>
    <div class="container header-inner">
        <a href="../index.html" class="logo-area">
            <img src="../assets/logos/logo-principal.png" alt="Union Mind" width="28" height="28">
            <span class="logo-wordmark">UNION MIND</span>
        </a>
        <button class="mobile-menu-btn" aria-label="Abrir menu"
            onclick="document.querySelector('nav').classList.toggle('active')">
            <span></span><span></span><span></span>
        </button>
        <nav>
            <a href="../index.html#expertise" onclick="document.querySelector('nav').classList.remove('active')">Expertise</a>
            <a href="../index.html#cases" onclick="document.querySelector('nav').classList.remove('active')">Cases</a>
            <a href="../index.html#metodologia" onclick="document.querySelector('nav').classList.remove('active')">Metodologia</a>
            <a href="../labs.html" class="labs-link" onclick="document.querySelector('nav').classList.remove('active')">Union Labs</a>
            <a href="#contato" class="btn-cta" onclick="document.querySelector('nav').classList.remove('active')">Fale com um Especialista →</a>
        </nav>
    </div>
</header>'''

# Used for INSIGHTS pages (relative path: ../)
NAV_INSIGHTS = '''<header>
    <div class="container header-inner">
        <a href="../index.html" class="logo-area">
            <img src="../assets/logos/logo-principal.png" alt="Union Mind" width="28" height="28">
            <span class="logo-wordmark">UNION MIND</span>
        </a>
        <button class="mobile-menu-btn" aria-label="Abrir menu"
            onclick="document.querySelector('nav').classList.toggle('active')">
            <span></span><span></span><span></span>
        </button>
        <nav>
            <a href="../index.html#expertise" onclick="document.querySelector('nav').classList.remove('active')">Expertise</a>
            <a href="../index.html#cases" onclick="document.querySelector('nav').classList.remove('active')">Cases</a>
            <a href="../index.html#metodologia" onclick="document.querySelector('nav').classList.remove('active')">Metodologia</a>
            <a href="../labs.html" class="labs-link" onclick="document.querySelector('nav').classList.remove('active')">Union Labs</a>
            <a href="../index.html#configurador" class="btn-cta" onclick="document.querySelector('nav').classList.remove('active')">Fale com um Especialista →</a>
        </nav>
    </div>
</header>'''

# ─── NEW FOOTER HTML ─────────────────────────────────────────
# Footer for ESPACOS (../ paths)
FOOTER_ESPACOS = '''<footer>
    <div class="container">
        <div class="footer-top">
            <div>
                <div class="footer-logo-area">
                    <img src="../assets/logos/logo-principal.png" alt="Union Mind">
                </div>
                <div class="footer-wordmark">UNION MIND</div>
                <div class="footer-tagline-text">Boutique Soul · AI Engine</div>
            </div>
            <div class="footer-links-section">
                <strong>Espaços Especializados</strong>
                <div class="footer-venues">
                    <a href="../espacos/royal-palm-plaza.html">Royal Palm Plaza</a>
                    <a href="../espacos/grand-hyatt-sao-paulo.html">Grand Hyatt SP</a>
                    <a href="../espacos/expo-center-norte.html">Expo Center Norte</a>
                    <a href="../espacos/costao-do-santinho.html">Costão do Santinho</a>
                    <a href="../espacos/bourbon-atibaia-resort.html">Bourbon Atibaia</a>
                    <a href="../espacos/sao-paulo-expo.html">São Paulo Expo</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <span>© 2026 Union Mind Eventos e Comunicação | CNPJ 21.024.508/0001-08</span>
            <span>felipe@unionmind.solutions</span>
        </div>
    </div>
</footer>'''

# Footer for INSIGHTS (../ paths)
FOOTER_INSIGHTS = '''<footer>
    <div class="container">
        <div class="footer-top">
            <div>
                <div class="footer-logo-area">
                    <img src="../assets/logos/logo-principal.png" alt="Union Mind">
                </div>
                <div class="footer-wordmark">UNION MIND</div>
                <div class="footer-tagline-text">Boutique Soul · AI Engine</div>
            </div>
            <div class="footer-links-section">
                <strong>Insights</strong>
                <div class="footer-venues">
                    <a href="../insights/checklist-convencao-corporativa.html">Checklist Convenção</a>
                    <a href="../insights/boutique-vs-fabrica-live-marketing.html">Boutique vs Fábrica</a>
                    <a href="../insights/grandes-marcas-meetings-vip.html">Meetings VIP</a>
                    <a href="../insights/agencia-boutique-times-senior.html">Times Sênior</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <span>© 2026 Union Mind Eventos e Comunicação | CNPJ 21.024.508/0001-08</span>
            <span>felipe@unionmind.solutions</span>
        </div>
    </div>
</footer>'''

# ─── NEW FONT + CSS LINKS ────────────────────────────────────
FONTS_LINK = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Space+Mono:wght@400;700&display=swap">'''

CSS_LINK_ESPACOS = '    <link rel="stylesheet" href="../style-v2.css">'
CSS_LINK_INSIGHTS = '    <link rel="stylesheet" href="../style-v2.css">'


def update_file(filepath, nav_html, footer_html, css_link, fonts_link):
    """Update nav, footer, CSS link and fonts in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace CSS stylesheet link (style.css → style-v2.css)
    content = re.sub(
        r'<link[^>]+href=["\']\.\.\/style\.css["\'][^>]*>',
        css_link,
        content
    )

    # 2. Replace (or add) font preconnect + Google Fonts
    # Remove old League Spartan font
    content = re.sub(
        r'<link[^>]+fonts\.googleapis\.com/css2[^>]+League\+Spartan[^>]*>',
        '',
        content
    )
    # Remove old bare preconnect lines that may be duplicated
    content = re.sub(
        r'    <link rel="preconnect" href="https://fonts\.googleapis\.com">\n',
        '',
        content
    )
    content = re.sub(
        r'    <link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\n',
        '',
        content
    )
    # Insert new fonts before </head>
    if fonts_link not in content:
        content = content.replace('</head>', fonts_link + '\n</head>', 1)

    # 3. Replace <header>…</header>
    content = re.sub(
        r'<header>.*?</header>',
        nav_html,
        content,
        flags=re.DOTALL
    )

    # 4. Replace <footer>…</footer>
    content = re.sub(
        r'<footer>.*?</footer>',
        footer_html,
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  ✅ Updated: {os.path.relpath(filepath, SITE_DIR)}')
    else:
        print(f'  ⚠️  No changes: {os.path.relpath(filepath, SITE_DIR)}')


def main():
    print('\n══════════════════════════════════════')
    print('   Union Mind — Site-wide v2 Updater')
    print('══════════════════════════════════════\n')

    # ── ESPACOS ─────────────────────────────
    print('▶ Updating espacos/ pages...')
    espacos_files = glob.glob(os.path.join(SITE_DIR, 'espacos', '*.html'))
    for fp in sorted(espacos_files):
        update_file(fp, NAV_ESPACOS, FOOTER_ESPACOS, CSS_LINK_ESPACOS, FONTS_LINK)
    print(f'   Done: {len(espacos_files)} files\n')

    # ── INSIGHTS ────────────────────────────
    print('▶ Updating insights/ pages...')
    insights_files = glob.glob(os.path.join(SITE_DIR, 'insights', '*.html'))
    for fp in sorted(insights_files):
        update_file(fp, NAV_INSIGHTS, FOOTER_INSIGHTS, CSS_LINK_INSIGHTS, FONTS_LINK)
    print(f'   Done: {len(insights_files)} files\n')

    print('══════════════════════════════════════')
    print('   All pages updated successfully! 🚀')
    print('══════════════════════════════════════\n')


if __name__ == '__main__':
    main()
