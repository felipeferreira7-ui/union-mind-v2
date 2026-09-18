import os
import re
import html
from pathlib import Path
import urllib.parse
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
current_date = datetime.now().strftime('%Y-%m-%d')
catA_path = os.path.join(base_dir, 'templates/template_resort.html')
catB_path = os.path.join(base_dir, 'templates/template_expo.html')

with open(catA_path, 'r', encoding='utf-8') as f:
    catA_HTML = f.read()

with open(catB_path, 'r', encoding='utf-8') as f:
    catB_HTML = f.read()

catC_path = os.path.join(base_dir, 'templates/template_urbano.html')
with open(catC_path, 'r', encoding='utf-8') as f:
    catC_HTML = f.read()

catD_path = os.path.join(base_dir, 'templates/template_bairro.html')
with open(catD_path, 'r', encoding='utf-8') as f:
    catD_HTML = f.read()

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
    { 'id': 'jk-iguatemi-eventos', 'name': 'JK Iguatemi Espaços', 'bairro': 'Vila Olímpia' },
    { 'id': 'palacio-tangara', 'name': 'Palácio Tangará', 'bairro': 'Morumbi' },
    { 'id': 'arca-eventos-pinheiros', 'name': 'Arca Eventos Pinheiros', 'bairro': 'Pinheiros' },
    { 'id': 'grand-hyatt-sao-paulo', 'name': 'Grand Hyatt São Paulo', 'bairro': 'Brooklin' },
    { 'id': 'blue-tree-faria-lima', 'name': 'Blue Tree Premium Faria Lima', 'bairro': 'Pinheiros' },
    { 'id': 'infinito-na-vela-leopoldina', 'name': 'Espaço Infinitto — Vila Leopoldina', 'bairro': 'Leopoldina' },
    { 'id': 'renaissance-sao-paulo', 'name': 'Renaissance São Paulo Hotel', 'bairro': 'Jardins' }
]

# Categoria D: Polos Corporativos (Bairros)
venuesD = [
    { 'id': 'faria-lima', 'name': 'Faria Lima', 'lat': '-23.5855', 'lng': '-46.6852' },
    { 'id': 'berrini', 'name': 'Berrini', 'lat': '-23.6068', 'lng': '-46.6946' },
    { 'id': 'alphaville', 'name': 'Alphaville', 'lat': '-23.4938', 'lng': '-46.8488' },
    { 'id': 'paulista', 'name': 'Avenida Paulista', 'lat': '-23.5615', 'lng': '-46.6560' },
    { 'id': 'vila-olimpia', 'name': 'Vila Olímpia', 'lat': '-23.5976', 'lng': '-46.6853' },
    { 'id': 'chacara-santo-antonio', 'name': 'Chácara Santo Antônio', 'lat': '-23.6318', 'lng': '-46.7088' }
]

# Templates are the source of truth. Legacy generators must not overwrite them.
base = Path(base_dir)
out_dir = base / 'espacos'
all_venues = venuesA + venuesB + venuesC + venuesD
for template, venues in [(catA_HTML, venuesA), (catB_HTML, venuesB), (catC_HTML, venuesC), (catD_HTML, venuesD)]:
    for venue in venues:
        content = template
        values = {
            '[VENUE_NAME]': venue['name'], '[BAIRRO_NOME]': venue['name'],
            '[URL_SLUG]': venue['id'], '[VENUE_BAIRRO]': venue.get('bairro', ''),
            '[VENUE_WA]': urllib.parse.quote(venue['name']), '[VENUE_ENC]': urllib.parse.quote(venue['name']),
            '[GEO_LAT]': venue.get('lat', ''), '[GEO_LNG]': venue.get('lng', '')
        }
        for key, value in values.items(): content = content.replace(key, value)
        content = content.replace('<meta name="robots" content="noindex, follow">', '<meta name="robots" content="index, follow">')
        if re.search(r'\[(?:VENUE|BAIRRO|URL_SLUG|GEO_)[A-Z_]*\]', content):
            raise ValueError('Unresolved template token: ' + venue['id'])
        (out_dir / (venue['id'] + '.html')).write_text(content, encoding='utf-8')

# A navigable directory gives every space an internal link, not just a sitemap entry.
sections = []
for i, (title, venues) in enumerate([('Hotéis e resorts', venuesA), ('Pavilhões e centros de convenções', venuesB), ('Espaços urbanos', venuesC), ('Regiões corporativas', venuesD)]):
    links = ''.join('<li><a href="' + v['id'] + '.html">' + html.escape(v['name']) + '</a></li>' for v in venues)
    sections.append('<section><h2 data-i18n="category-' + str(i) + '">' + title + '</h2><ul>' + links + '</ul></section>')
directory = (base / 'scripts_build/space_directory.html').read_text(encoding='utf-8').replace('[DIRECTORY_SECTIONS]', ''.join(sections))
(out_dir / 'index.html').write_text(directory, encoding='utf-8')
paths = ['/', '/labs.html', '/checklist-convencao.html', '/espacos/', '/insights/']
paths += ['/espacos/' + v['id'] + '.html' for v in all_venues]
paths += ['/insights/' + p.name for p in sorted((base / 'insights').glob('*.html')) if p.name != 'index.html']
# No artificial modification dates: update lastmod only with verified editorial history.
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += ''.join('  <url><loc>https://unionmind.solutions' + path + '</loc></url>\n' for path in paths)
sitemap += '</urlset>\n'
(base / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
print(f'Generated {len(all_venues)} venue pages, directory and sitemap with {len(paths)} URLs.')
