const fs = require('fs');
const path = require('path');

const catA_HTML = fs.readFileSync(path.join(__dirname, 'espacos/bourbon-atibaia-resort.html'), 'utf8');
const catB_HTML = fs.readFileSync(path.join(__dirname, 'espacos/expo-center-norte.html'), 'utf8');

const venuesA = [
    { id: 'almenat-tapestry', name: 'Almenat Tapestry Collection', short: 'Almenat' },
    { id: 'hotel-vila-rossa', name: 'Hotel Vila Rossa', short: 'Vila Rossa' },
    { id: 'clara-resorts', name: 'Clara Resorts', short: 'Clara Resorts' },
    { id: 'windsor-copacabana', name: 'Windsor Copacabana', short: 'Windsor Copacabana' },
    { id: 'royal-palm-plaza', name: 'Royal Palm Plaza Resort', short: 'Royal Palm Plaza' },
    { id: 'taua-atibaia', name: 'Tauá Hotel & Convention', short: 'Tauá Atibaia' },
    { id: 'hotel-fazenda-dona-carolina', name: 'Hotel Fazenda Dona Carolina', short: 'Dona Carolina' },
    { id: 'beach-hotel-maresias', name: 'Beach Hotel Maresias', short: 'Beach Hotel Maresias' },
    { id: 'costao-do-santinho', name: 'Costão do Santinho Resort', short: 'Costão do Santinho' },
    { id: 'lk-design-hotel', name: 'LK Design Hotel', short: 'LK Design Hotel' },
    { id: 'bourbon-cataratas', name: 'Bourbon Cataratas do Iguaçu', short: 'Bourbon Cataratas' },
    { id: 'rafain-palace', name: 'Rafain Palace Hotel & Convention', short: 'Rafain Palace' },
    { id: 'wish-foz', name: 'Wish Foz do Iguaçu', short: 'Wish Foz do Iguaçu' },
    { id: 'iberostar-praia-do-forte', name: 'Iberostar Praia do Forte', short: 'Iberostar Praia do Forte' },
    { id: 'costa-do-sauipe', name: 'Costa do Sauípe Resorts', short: 'Costa do Sauípe' },
    { id: 'tivoli-ecoresort', name: 'Tivoli Ecoresort Praia do Forte', short: 'Tivoli Ecoresort' },
    { id: 'fiesta-bahia-hotel', name: 'Fiesta Bahia Hotel', short: 'Fiesta Bahia Hotel' },
    { id: 'windsor-barra', name: 'Windsor Barra Convention Center', short: 'Windsor Barra' },
    { id: 'fairmont-copacabana', name: 'Fairmont Rio de Janeiro', short: 'Fairmont Copacabana' },
    { id: 'grand-hyatt-rj', name: 'Grand Hyatt Rio de Janeiro', short: 'Grand Hyatt RJ' }
];

const venuesB = [
    { id: 'sao-paulo-expo', name: 'São Paulo Expo' },
    { id: 'transamerica-expo', name: 'Transamerica Expo Center' },
    { id: 'distrito-anhembi', name: 'Distrito Anhembi' },
    { id: 'pro-magno', name: 'Pro Magno Centro de Eventos' },
    { id: 'riocentro', name: 'Riocentro' },
    { id: 'centro-convencoes-salvador', name: 'Centro de Convenções Salvador' },
    { id: 'expo-unimed-curitiba', name: 'Expo Unimed Curitiba' },
    { id: 'expo-d-pedro', name: 'Expo D. Pedro' }
];

const outDir = path.join(__dirname, 'espacos');
const sitemapPath = path.join(__dirname, 'sitemap.xml');
let sitemapUrls = `<?xml version="1.0" encoding="UTF-8"?>
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
`;

function pushSitemap(id) {
    sitemapUrls += `  <url>
    <loc>https://unionmind.solutions/espacos/${id}.html</loc>
    <lastmod>2026-03-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n`;
}

// Generate Category A
venuesA.forEach(v => {
    let content = catA_HTML;
    content = content.replace(/Bourbon Atibaia Resort/g, v.name);
    content = content.replace(/Bourbon Atibaia/g, v.short);
    content = content.replace(/Bourbon%20Atibaia%20Resort/g, encodeURIComponent(v.name));
    
    // adjust specific sentence
    content = content.replace('Transformamos o principal resort de São Paulo', 'Transformamos o espaço');

    fs.writeFileSync(path.join(outDir, `${v.id}.html`), content);
    pushSitemap(v.id);
});
pushSitemap('bourbon-atibaia-resort');

// Generate Category B
venuesB.forEach(v => {
    let content = catB_HTML;
    content = content.replace(/Expo Center Norte/g, v.name);
    content = content.replace(/Expo%20Center%20Norte/g, encodeURIComponent(v.name));
    
    fs.writeFileSync(path.join(outDir, `${v.id}.html`), content);
    pushSitemap(v.id);
});
pushSitemap('expo-center-norte');

sitemapUrls += `</urlset>`;
fs.writeFileSync(sitemapPath, sitemapUrls);

console.log(`[Union Labs] Geradas ${venuesA.length + venuesB.length} landing pages automaticamente! Sitemap atualizado.`);
