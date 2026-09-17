/* Shared language, lead context and accessible controls for PT/EN pages. */
window.UnionUI = {
    track(event, parameters) {
        if (window.UnionAnalytics) window.UnionAnalytics.track(event, parameters);
        else { window.dataLayer = window.dataLayer || []; window.dataLayer.push({ event, ...parameters }); }
    },
    services: ['eventos-corporativos', 'convencoes-de-vendas', 'ativacoes-de-marca', 'estandes-e-cenografia'],
    serviceNames: {
        pt: ['eventos corporativos', 'convenções de vendas', 'ativações de marca', 'estandes e cenografia'],
        en: ['corporate events', 'sales conventions', 'brand activations', 'exhibition booths and scenography']
    },
    service() {
        const value = new URLSearchParams(window.location.search).get('service');
        return this.services.includes(value) ? value : '';
    },
    lead(formId) {
        // Never include a person's name, email, company, message or query string.
        this.track('generate_lead', { form_id: formId,
            lead_source: 'website_form', service: this.service() || 'general',
            language: this.language() });
    },
    apply(lang, translations, metadata) {
        if (!translations[lang]) return;
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const text = translations[lang][el.getAttribute('data-i18n')];
            if (text) el.innerHTML = text;
        });
        document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
        if (metadata?.[lang]) {
            document.title = metadata[lang].title;
            document.querySelector('meta[name="description"]').content = metadata[lang].description;
        }
        this.sync(lang);
    },
    language() {
        return window.location.pathname.startsWith('/en/') ? 'en' : 'pt';
    },
    sync(lang) {
        try { sessionStorage.setItem('union-language', lang); } catch (_) { /* Storage can be disabled. */ }
        document.querySelectorAll('[data-placeholder-pt]').forEach(el => {
            el.placeholder = el.getAttribute('data-placeholder-' + lang);
        });
        document.querySelectorAll('[data-alt-pt]').forEach(el => {
            el.alt = el.getAttribute('data-alt-' + lang);
        });
        document.querySelectorAll('.lang-switcher button, .lang-switcher a').forEach(el => {
            el.classList.toggle('active', el.id === 'btn-' + lang);
            if (el.tagName === 'BUTTON') el.setAttribute('aria-pressed', String(el.id === 'btn-' + lang));
            else {
                if (el.id === 'btn-' + lang) el.setAttribute('aria-current', 'page');
                else el.removeAttribute('aria-current');
                const url = new URL(el.href);
                if (this.service()) url.searchParams.set('service', this.service());
                // Public venue context survives a language change on the contact page.
                const venue = new URLSearchParams(window.location.search).get('venue');
                if (venue && venue.length < 150) url.searchParams.set('venue', venue);
                if (location.hash && document.getElementById(location.hash.slice(1))) url.hash = location.hash;
                el.href = url.href;
            }
        });
        document.querySelectorAll('.mobile-menu-btn').forEach(el => {
            el.setAttribute('aria-label', lang === 'en' ? 'Toggle menu' : 'Abrir ou fechar menu');
        });
        document.querySelectorAll('a[href*="wa.me/"]').forEach(el => {
            if (!el.dataset.hrefPt) el.dataset.hrefPt = el.href;
            const url = new URL(el.dataset.hrefPt);
            if (lang === 'en') url.searchParams.set('text', el.dataset.waEn || 'Hello, I would like to discuss an event with Union Mind.');
            if (this.service()) {
                const name = this.serviceNames[lang][this.services.indexOf(this.service())];
                url.searchParams.set('text', lang === 'en' ? 'Hello, I would like to discuss ' + name + ' with Union.' : 'Olá, quero conversar sobre ' + name + ' com a Union.');
            }
            el.href = url.href;
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // Context is sent to the lead inbox; it does not change required form fields.
    document.querySelectorAll('form[action*="formspree.io"]').forEach(form => {
        for (const [name, value] of [['servico', UnionUI.service() || 'geral'], ['idioma', UnionUI.language()]]) {
            let input = form.querySelector('input[name="' + name + '"]');
            if (!input) { input = document.createElement('input'); input.type = 'hidden'; input.name = name; form.appendChild(input); }
            input.setAttribute('value', value);
        }
        if (UnionUI.service()) {
            const context = document.createElement('p');
            context.className = 'form-service-context';
            const language = UnionUI.language();
            const name = UnionUI.serviceNames[language][UnionUI.services.indexOf(UnionUI.service())];
            context.textContent = (language === 'en' ? 'Your project: ' : 'Seu projeto: ') + name + '.';
            form.prepend(context);
        }
    });
    document.addEventListener('click', event => {
        const link = event.target.closest?.('a[href*="wa.me/"]');
        if (!link) return;
        UnionUI.track('whatsapp_click', { language: UnionUI.language(),
            service: UnionUI.service() || UnionUI.services.find(slug => window.location.pathname.endsWith('/' + slug + '.html')) || 'general' });
    });
    document.querySelectorAll('.mobile-menu-btn').forEach(button => {
        const nav = document.querySelector('header nav');
        if (!nav) return;
        nav.id = nav.id || 'main-navigation';
        button.setAttribute('aria-controls', nav.id);
        const sync = () => button.setAttribute('aria-expanded', String(nav.classList.contains('active')));
        sync();
        new MutationObserver(sync).observe(nav, { attributes: true, attributeFilter: ['class'] });
        document.addEventListener('keydown', event => {
            if (event.key === 'Escape' && nav.classList.contains('active')) {
                nav.classList.remove('active');
                button.focus();
            }
        });
    });
});
