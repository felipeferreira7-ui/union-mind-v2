import os
import urllib.parse

base_dir = os.path.dirname(os.path.abspath(__file__))
catA_path = os.path.join(base_dir, 'templates/template_resort.html')
catB_path = os.path.join(base_dir, 'templates/template_expo.html')

with open(catA_path, 'r', encoding='utf-8') as f:
    catA_HTML = f.read()

with open(catB_path, 'r', encoding='utf-8') as f:
    catB_HTML = f.read()

catC_path = os.path.join(base_dir, 'templates/template_urbano.html')
with open(catC_path, 'r', encoding='utf-8') as f:
    catC_HTML = f.read()

venuesA = [
    { 'id': 'almenat-tapestry', 'name': 'Almenat Tapestry Collection', 'short': 'Almenat' },
    { 'id': 'hotel-vila-rossa', 'name': 'Hotel Vila Rossa', 'short': 'Vila Rossa' },
    { 'id': 'clara-resorts', 'name': 'Clara Resorts', 'short': 'Clara Resorts' },
    { 'id': 'windsor-copacabana', 'name': 'Windsor Copacabana', 'short': 'Windsor Copacabana' },
    { 'id': 'royal-palm-plaza', 'name': 'Royal Palm Plaza Resort', 'short': 'Royal Palm Plaza' },
    { 'id': 'taua-atibaia', 'name': 'Tauá Hotel & Convention', 'short': 'Tauá Atibaia' },
    { 'id': 'hotel-fazenda-dona-carolina', 'name': 'Hotel Fazenda Dona Carolina', 'short': 'Dona Carolina' },
    { 'id': 'beach-hotel-maresias', 'name': 'Beach Hotel Maresias', 'short': 'Beach Hotel Maresias' },
    { 'id': 'costao-do-santinho', 'name': 'Costão do Santinho Resort', 'short': 'Costão do Santinho' },
    { 'id': 'lk-design-hotel', 'name': 'LK Design Hotel', 'short': 'LK Design Hotel' },
    { 'id': 'bourbon-cataratas', 'name': 'Bourbon Cataratas do Iguaçu', 'short': 'Bourbon Cataratas' },
    { 'id': 'rafain-palace', 'name': 'Rafain Palace Hotel & Convention', 'short': 'Rafain Palace' },
    { 'id': 'wish-foz', 'name': 'Wish Foz do Iguaçu', 'short': 'Wish Foz do Iguaçu' },
    { 'id': 'iberostar-praia-do-forte', 'name': 'Iberostar Praia do Forte', 'short': 'Iberostar Praia do Forte' },
    { 'id': 'costa-do-sauipe', 'name': 'Costa do Sauípe Resorts', 'short': 'Costa do Sauípe' },
    { 'id': 'tivoli-ecoresort', 'name': 'Tivoli Ecoresort Praia do Forte', 'short': 'Tivoli Ecoresort' },
    { 'id': 'fiesta-bahia-hotel', 'name': 'Fiesta Bahia Hotel', 'short': 'Fiesta Bahia Hotel' },
    { 'id': 'windsor-barra', 'name': 'Windsor Barra Convention Center', 'short': 'Windsor Barra' },
    { 'id': 'fairmont-copacabana', 'name': 'Fairmont Rio de Janeiro', 'short': 'Fairmont Copacabana' },
    { 'id': 'grand-hyatt-rj', 'name': 'Grand Hyatt Rio de Janeiro', 'short': 'Grand Hyatt RJ' },
    { 'id': 'bourbon-atibaia-resort', 'name': 'Bourbon Atibaia Resort', 'short': 'Bourbon Atibaia' }
]

venuesB = [
    { 'id': 'sao-paulo-expo', 'name': 'São Paulo Expo' },
    { 'id': 'transamerica-expo', 'name': 'Transamerica Expo Center' },
    { 'id': 'distrito-anhembi', 'name': 'Distrito Anhembi' },
    { 'id': 'pro-magno', 'name': 'Pro Magno Centro de Eventos' },
    { 'id': 'riocentro', 'name': 'Riocentro' },
    { 'id': 'centro-convencoes-salvador', 'name': 'Centro de Convenções Salvador' },
    { 'id': 'expo-unimed-curitiba', 'name': 'Expo Unimed Curitiba' },
    { 'id': 'expo-d-pedro', 'name': 'Expo D. Pedro' },
    { 'id': 'expo-center-norte', 'name': 'Expo Center Norte' }
]

# Categoria C: Espaços Urbanos Premium SP
venuesC = [
    { 'id': 'um-rooftop', 'name': 'UM Rooftop', 'bairro': 'Vila Olímpia' },
    { 'id': 'wtc-events-center', 'name': 'WTC Events Center', 'bairro': 'Berrini' },
    { 'id': 'grupo-bisutti', 'name': 'Grupo Bisutti', 'bairro': 'Vila Olímpia' },
    { 'id': 'jk-iguatemi-eventos', 'name': 'JK Iguatemi Espaços', 'bairro': 'Jardins' },
    { 'id': 'palacio-tangara', 'name': 'Palácio Tangará', 'bairro': 'Morumbi' },
    { 'id': 'arca-eventos-pinheiros', 'name': 'Arca Eventos Pinheiros', 'bairro': 'Pinheiros' },
    { 'id': 'grand-hyatt-sao-paulo', 'name': 'Grand Hyatt São Paulo', 'bairro': 'Vila Olímpia' },
    { 'id': 'blue-tree-faria-lima', 'name': 'Blue Tree Premium Faria Lima', 'bairro': 'Pinheiros' },
    { 'id': 'infinito-na-vela-leopoldina', 'name': 'Infinito na Vela Leopoldina', 'bairro': 'Leopoldina' },
    { 'id': 'renaissance-sao-paulo', 'name': 'Renaissance São Paulo Hotel', 'bairro': 'Bela Vista' }
]

outDir = os.path.join(base_dir, 'espacos')
sitemapPath = os.path.join(base_dir, 'sitemap.xml')

sitemapUrls = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://unionmind.solutions/</loc>
    <lastmod>2026-03-31</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://unionmind.solutions/labs.html</loc>
    <lastmod>2026-03-31</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

def push_sitemap(vid):
    global sitemapUrls
    sitemapUrls += f"""  <url>
    <loc>https://unionmind.solutions/espacos/{vid}.html</loc>
    <lastmod>2026-03-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""

# Generate Category A
for v in venuesA:
    content = catA_HTML
    content = content.replace('Bourbon Atibaia Resort', v['name'])
    content = content.replace('Bourbon Atibaia', v['short'])
    content = content.replace(urllib.parse.quote('Bourbon Atibaia Resort'), urllib.parse.quote(v['name']))
    content = content.replace('[URL_SLUG]', v['id'])
    
    # Adjust specific sentence
    content = content.replace('Transformamos o principal resort de São Paulo', f"Transformamos o {v['short']}")

    # Point CTAs to the smart form on Home with context and pre-fill
    venue_name_enc = urllib.parse.quote(v['name'])
    content = content.replace('href="../index.html?type=resort#configurador"', f'href="../index.html?type=resort&venue={venue_name_enc}#configurador"')
    content = content.replace('href="../index.html"', 'href="../index.html"')

    with open(os.path.join(outDir, f"{v['id']}.html"), 'w', encoding='utf-8') as f:
        f.write(content)
    push_sitemap(v['id'])

# Generate Category B
for v in venuesB:
    content = catB_HTML
    content = content.replace('Expo Center Norte', v['name'])
    content = content.replace(urllib.parse.quote('Expo Center Norte'), urllib.parse.quote(v['name']))
    content = content.replace('[URL_SLUG]', v['id'])
    
    # Point CTAs to the smart form on Home with Expo context and pre-fill
    venue_name_enc = urllib.parse.quote(v['name'])
    content = content.replace('href=\"/#configurador\"', f'href=\"../index.html?type=expo&venue={venue_name_enc}#configurador\"')
    content = content.replace('href=\"/\"', 'href=\"../index.html\"')
    
    with open(os.path.join(outDir, f"{v['id']}.html"), 'w', encoding='utf-8') as f:
        f.write(content)
    push_sitemap(v['id'])

# Generate Category C (Urban Spaces SP)
for v in venuesC:
    content = catC_HTML
    content = content.replace('[VENUE_NAME]', v['name'])
    content = content.replace('[VENUE_BAIRRO]', v['bairro'])
    content = content.replace('[URL_SLUG]', v['id'])
    venue_wa = urllib.parse.quote(v['name'])
    venue_enc = urllib.parse.quote(v['name'])
    content = content.replace('[VENUE_WA]', venue_wa)
    content = content.replace('[VENUE_ENC]', venue_enc)

    with open(os.path.join(outDir, f"{v['id']}.html"), 'w', encoding='utf-8') as f:
        f.write(content)
    push_sitemap(v['id'])

sitemapUrls += "</urlset>"

with open(sitemapPath, 'w', encoding='utf-8') as f:
    f.write(sitemapUrls)

print(f"[Union Labs] Python script executado. Geradas {len(venuesA) + len(venuesB) + len(venuesC)} landing pages automaticamente! Sitemap atualizado.")
