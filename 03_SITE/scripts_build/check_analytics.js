// Fake DOM and data queue: validate destination, duplicate prevention and privacy.
// Does not load Google libraries or transmit events.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const code = fs.readFileSync(path.join(__dirname, '../scripts/analytics.js'), 'utf8');
for (const hostname of ['127.0.0.1', 'localhost', 'example.com', 'unionmind.solutions', 'www.unionmind.solutions']) {
    const inserted = [];
    const location = { hostname, origin: 'https://' + hostname, pathname: '/en/', search: '?email=private@example.com', hash: '#contact' };
    const window = { location };
    const document = { title: 'Union Mind', referrer: 'https://www.google.com/search?q=private@example.com', createElement: () => ({}), head: { appendChild: el => inserted.push(el) } };
    vm.runInNewContext(code, { window, location, document, URL, Date });
    window.UnionAnalytics.track('generate_lead', { form_id: 'config-form', service: 'general', language: 'en' });
    const production = hostname.endsWith('unionmind.solutions');
    assert.equal(inserted.length, production ? 1 : 0);
    if (!production) { assert.equal(window.dataLayer, undefined); continue; }
    const commands = window.dataLayer.map(v => Array.from(v));
    assert.equal(commands.filter(v => v[0] === 'event' && v[1] === 'page_view').length, 1);
    assert.equal(commands.filter(v => v[0] === 'event' && v[1] === 'generate_lead').length, 1);
    const config = commands.find(v => v[0] === 'config');
    assert.equal(config[1], 'G-WPW7PV9W54');
    assert.equal(config[2].send_page_view, false);
    assert.ok(!JSON.stringify(commands).includes('private@example.com'));
    assert.ok(!JSON.stringify(commands).includes('?email'));
}
console.log('PASS: GA4 production destination, single page view, local exclusion and query/referrer sanitization. No network requests sent.');
