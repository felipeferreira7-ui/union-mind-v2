#!/usr/bin/env python3
"""
add_article_schema.py
Adds Schema.org Article markup to all Insights pages and
updates lastmod dates in sitemap.xml
"""

import os
import re
import glob
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.now().strftime("%Y-%m-%d")

# ── Map of insight slugs to article metadata ────────────────────────────────
ARTICLES = {
    "agencia-boutique-times-senior.html": {
        "title": "Por Que Agências Boutique com Times Sênior Entregam Mais — Union Mind",
        "desc": "Entenda por que o modelo boutique com times sênior garante mais qualidade, menos surpresas e melhor ROI em eventos corporativos.",
        "keywords": "agência boutique eventos, times sênior, live marketing"
    },
    "boutique-vs-fabrica-live-marketing.html": {
        "title": "Boutique vs Fábrica de Live Marketing: Qual a Diferença Real?",
        "desc": "A diferença entre uma agência boutique e uma grande fábrica de eventos corporativos — e por que isso impacta diretamente a qualidade da entrega.",
        "keywords": "agência boutique vs grande agência, live marketing, eventos corporativos"
    },
    "checklist-convencao-corporativa.html": {
        "title": "Checklist Completo para Convenção Corporativa — Union Mind",
        "desc": "Guia prático com checklist completo para organizar uma convenção corporativa de sucesso. Da escolha do espaço ao dia do evento.",
        "keywords": "checklist convenção corporativa, como organizar convenção, agência eventos SP"
    },
    "estande-300m2-fast-track.html": {
        "title": "Estande de 300m² em Fast Track — Como Fazer em Menos de 30 Dias",
        "desc": "Como a Union Mind entrega um estande de 300m² em menos de 30 dias, com qualidade premium e sem comprometer segurança ou criatividade.",
        "keywords": "estande 300m2, fast track evento, agência estandes São Paulo"
    },
    "grandes-marcas-meetings-vip.html": {
        "title": "Meetings VIP para Grandes Marcas — O Que Elas Exigem — Union Mind",
        "desc": "Conheça os requisitos e o nível de produção que grandes marcas como Danone, Natura e Toyota exigem em meetings VIP e eventos de liderança.",
        "keywords": "meetings VIP, eventos liderança, grandes marcas eventos corporativos"
    }
}

ARTICLE_SCHEMA_TEMPLATE = '''
    <!-- Schema: Article (GEO + Google Discover) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{desc}",
      "author": {{
        "@type": "Person",
        "name": "Felipe Ferreira",
        "jobTitle": "Fundador, Union Mind",
        "url": "https://unionmind.solutions"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Union Mind Eventos e Comunicação",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://unionmind.solutions/assets/logos/logo-principal.png"
        }}
      }},
      "datePublished": "2026-01-01",
      "dateModified": "{today}",
      "inLanguage": "pt-BR",
      "isPartOf": {{
        "@type": "Blog",
        "name": "Union Mind Insights",
        "url": "https://unionmind.solutions/insights/"
      }},
      "speakable": {{
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", ".article-intro", ".article-lead"]
      }}
    }}
    </script>'''

print("=" * 54)
print("  Union Mind — Article Schema + Sitemap Updater")
print("=" * 54)

# ── 1. Add Article schemas to each insight page ─────────────────────────────
for filename, meta in ARTICLES.items():
    path = os.path.join(BASE, "insights", filename)
    if not os.path.exists(path):
        print(f"  ⚪ Not found: insights/{filename}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "\"@type\": \"Article\"" in content or '"@type":"Article"' in content:
        print(f"  ✅ Already has Article schema: {filename}")
        continue

    schema_block = ARTICLE_SCHEMA_TEMPLATE.format(
        title=meta["title"],
        desc=meta["desc"],
        today=TODAY
    )

    # Add Article schema meta tags and schema before </head>
    meta_tags = f"""    <meta name="author" content="Felipe Ferreira, Union Mind">
    <meta name="ai-content-declaration" content="human-generated">
    <link rel="alternate" type="text/plain" href="/llms.txt" title="LLMs.txt — Union Mind AI Profile">"""

    # Insert before </head>
    content = content.replace("</head>", meta_tags + schema_block + "\n</head>", 1)

    # Also add keywords if not present
    if 'name="keywords"' not in content:
        content = content.replace(
            '</head>',
            f'    <meta name="keywords" content="{meta["keywords"]}">\n</head>',
            1
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅ Article schema added: insights/{filename}")

# ── 2. Update lastmod in sitemap.xml ──────────────────────────────────────
sitemap_path = os.path.join(BASE, "sitemap.xml")
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap = f.read()

    # Replace all lastmod dates with today
    sitemap_updated = re.sub(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", f"<lastmod>{TODAY}</lastmod>", sitemap)

    # Make sure llms.txt and llms-full.txt are in sitemap
    if "llms.txt" not in sitemap:
        insert_before = "</urlset>"
        sitemap_updated = sitemap_updated.replace(
            insert_before,
            f"""  <url>
    <loc>https://unionmind.solutions/llms.txt</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://unionmind.solutions/llms-full.txt</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
{insert_before}"""
        )

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_updated)

    url_count = sitemap_updated.count("<url>")
    print(f"\n  ✅ sitemap.xml atualizado: {url_count} URLs, lastmod = {TODAY}")
else:
    print("  ⚠️  sitemap.xml não encontrado")

print("\n" + "=" * 54)
print("  Concluído!")
print("=" * 54)
