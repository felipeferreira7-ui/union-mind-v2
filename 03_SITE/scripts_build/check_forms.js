// Exercise submission handlers with a fake network; no request leaves this process.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');

(async () => {
    let cases = 0;
    for (const file of ['index.html', 'labs.html']) {
        const html = fs.readFileSync(path.join(__dirname, '..', file), 'utf8');
        const script = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)]
            .map(match => match[1]).find(code => code.includes("addEventListener('submit'"));
        assert.ok(script, `Missing form handler in ${file}`);
        for (const language of ['pt', 'en']) for (const outcome of ['success', 'http-error', 'offline']) {
            let handler, reset = false, calls = 0;
            const leadEvents = [];
            const alerts = [];
            const span = { innerText: '', textContent: '', removeAttribute() {} };
            const button = { disabled: false, style: {}, querySelector: () => span };
            const form = {
                action: 'https://example.invalid/test-only',
                addEventListener: (_, callback) => { handler = callback; },
                querySelector: () => button,
                reset: () => { reset = true; }
            };
            const context = vm.createContext({
                document: { documentElement: { lang: language === 'pt' ? 'pt-BR' : 'en' }, getElementById: () => form, addEventListener() {} },
                FormData: class {},
                UnionUI: { lead: id => leadEvents.push(id) },
                alert: text => alerts.push(text),
                fetch: async () => {
                    calls++;
                    if (outcome === 'offline') throw new Error('Offline');
                    return { ok: outcome === 'success' };
                }
            });
            vm.runInContext(script, context);
            if (file === 'index.html') vm.runInContext(`currentLang = '${language}'`, context);
            await handler.call(form, { preventDefault() {} });
            // The home uses a promise chain; flush it without making a network request.
            await new Promise(resolve => setImmediate(resolve));
            assert.equal(calls, 1);
            assert.equal(reset, outcome === 'success');
            assert.equal(leadEvents.length, outcome === 'success' ? 1 : 0, 'Only accepted submissions count as leads');
            if (outcome === 'success') assert.equal(leadEvents[0], file === 'index.html' ? 'config-form' : 'labs-form');
            assert.equal(button.disabled, outcome === 'success');
            const visibleText = span.innerText || span.textContent;
            assert.ok(visibleText.length > 0 && !visibleText.includes('<span'));
            if (outcome !== 'success') {
                assert.equal(alerts.length, 1);
                assert.ok(alerts[0].includes(language === 'en' ? 'We could not send' : 'Não foi possível enviar'));
                assert.ok(!/SENDING|Enviando|Sending/.test(visibleText));
            }
            cases++;
        }
    }
    console.log(`PASS: ${cases} simulated form scenarios (PT/EN, success, HTTP failure, offline). No network requests sent.`);
})().catch(error => { console.error(error); process.exitCode = 1; });
