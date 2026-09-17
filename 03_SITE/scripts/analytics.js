/* GA4 destination verified in the Union account on 17 September 2026.
   One owner for page views and contact events; local previews send no GA4 data. */
(() => {
    const production = ['unionmind.solutions', 'www.unionmind.solutions'].includes(location.hostname);
    const measurementId = 'G-WPW7PV9W54';
    window.UnionAnalytics = {
        track(event, parameters) {
            if (!production) return;
            window.gtag('event', event, { ...parameters, send_to: measurementId });
        }
    };
    if (!production) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    let referrer = '';
    try { referrer = document.referrer ? new URL(document.referrer).origin : ''; } catch (_) { /* Invalid referrer. */ }
    // Contact/venue query strings and fragments are excluded from Analytics.
    window.gtag('set', {
        page_location: location.origin + location.pathname,
        page_referrer: referrer,
        page_title: document.title
    });
    window.gtag('config', measurementId, {
        send_page_view: false,
        allow_google_signals: false,
        allow_ad_personalization_signals: false
    });
    window.gtag('event', 'page_view', { send_to: measurementId });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + measurementId;
    document.head.appendChild(script);
})();
