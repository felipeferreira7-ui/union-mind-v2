import re

def process_file(filepath, cat):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add nav items
    html = html.replace('<a href="/#expertise">Expertise</a>', '<a href="/#expertise" data-i18n="nav-expertise">Expertise</a>')
    html = html.replace('<a href="/#cases">Cases</a>', '<a href="/#cases" data-i18n="nav-cases">Cases</a>')
    
    # 2. Add language switcher to nav
    nav_repl = """                <div class="lang-switcher">
                    <button onclick="switchLanguage('pt')" id="btn-pt" class="active">PT</button>
                    <button onclick="switchLanguage('en')" id="btn-en">EN</button>
                </div>
                <a href="#contato" class="btn-cta" data-i18n="nav-cta">Fale com um Especialista</a>"""
    html = html.replace('<a href="#contato" class="btn-cta">Fale com um Especialista</a>', nav_repl)

    # 3. Add data-i18n tags
    html = html.replace('OPERAÇÃO ESPECIALIZADA', '<span data-i18n="hero-tag">OPERAÇÃO ESPECIALIZADA</span>')
    
    if cat == 'A':
        html = html.replace('<h1 class="hero-title" style="font-size: 3.5rem;">Sua Próxima Convenção no <span class="accent">Bourbon Atibaia</span>:<br>Criatividade e Operação Estratégica.</h1>', '<h1 class="hero-title" style="font-size: 3.5rem;" data-i18n="hero-h1">Sua Próxima Convenção no <span class="accent">Bourbon Atibaia</span>:<br>Criatividade e Operação Estratégica.</h1>')
        html = html.replace('<p class="hero-subtitle" style="max-width: 800px; margin: 2rem auto; font-size: 1.5rem; color: #fff;">Transformamos o principal resort de São Paulo no palco que a sua equipe de vendas merece.</p>', '<p class="hero-subtitle" style="max-width: 800px; margin: 2rem auto; font-size: 1.5rem; color: #fff;" data-i18n="hero-h2">Transformamos o principal resort de São Paulo no palco que a sua equipe de vendas merece.</p>')
        html = html.replace('<h2 class="section-title" style="text-align: left;">Segurança e Impacto para sua Convenção no <span class="accent">Bourbon Atibaia Resort</span>?</h2>', '<h2 class="section-title" style="text-align: left;" data-i18n="sect-title">Segurança e Impacto para sua Convenção no <span class="accent">Bourbon Atibaia Resort</span>?</h2>')
        html = html.replace('<p>O Bourbon Atibaia Resort é o palco das maiores convenções de vendas do Brasil. Nossa operação garante que a montagem da cenografia respeite a excelência do resort, sem imprevistos.</p>', '<p data-i18n="sect-p1">O Bourbon Atibaia Resort é o palco das maiores convenções de vendas do Brasil. Nossa operação garante que a montagem da cenografia respeite a excelência do resort, sem imprevistos.</p>')
        html = html.replace('<p>Nossa equipe conhece cada detalhe operacional deste espaço. Atuamos como seu braço direito, garantindo que o palco, as ativações e a jornada do hóspede sejam impecáveis.</p>', '<p data-i18n="sect-p2">Nossa equipe conhece cada detalhe operacional deste espaço. Atuamos como seu braço direito, garantindo que o palco, as ativações e a jornada do hóspede sejam impecáveis.</p>')
        html = html.replace('<h3>Criatividade e Produção Premium</h3>', '<h3 data-i18n="feat1-h3">Criatividade e Produção Premium</h3>')
        html = html.replace('<p>Entregamos o conceito criativo que sua marca espera, aliado a uma produção e cenografia impecáveis. Garantimos que sua convenção surpreenda a força de vendas com segurança e inovação.</p>', '<p data-i18n="feat1-p">Entregamos o conceito criativo que sua marca espera, aliado a uma produção e cenografia impecáveis. Garantimos que sua convenção surpreenda a força de vendas com segurança e inovação.</p>')
        html = html.replace('<h3>Precisão Union Labs</h3>', '<h3 data-i18n="feat2-h3">Precisão Union Labs</h3>')
        html = html.replace('<p>Implementamos gamificação e rastro digital para transformar sua convenção no Bourbon Atibaia em uma mina de inteligência comercial.</p>', '<p data-i18n="feat2-p">Implementamos gamificação e rastro digital para transformar sua convenção no Bourbon Atibaia em uma mina de inteligência comercial.</p>')
        html = html.replace('<h2 class="section-title">Prepare sua convenção no <br><span class="accent">Bourbon Atibaia Resort</span></h2>', '<h2 class="section-title" data-i18n="cta-h2">Prepare sua convenção no <br><span class="accent">Bourbon Atibaia Resort</span></h2>')
    else:
        html = html.replace('<h1 class="hero-title" style="font-size: 3.5rem;">Seu Próximo Evento no <span class="accent">Expo Center Norte</span>:<br>Criatividade e Operação Estratégica.</h1>', '<h1 class="hero-title" style="font-size: 3.5rem;" data-i18n="hero-h1">Seu Próximo Evento no <span class="accent">Expo Center Norte</span>:<br>Criatividade e Operação Estratégica.</h1>')
        html = html.replace('<p class="hero-subtitle" style="max-width: 800px; margin: 2rem auto; font-size: 1.5rem; color: #fff;">Somos a agência boutique que une cenografia High-End e IA para transformar metros quadrados em negócios reais.</p>', '<p class="hero-subtitle" style="max-width: 800px; margin: 2rem auto; font-size: 1.5rem; color: #fff;" data-i18n="hero-h2">Somos a agência boutique que une cenografia High-End e IA para transformar metros quadrados em negócios reais.</p>')
        html = html.replace('<h2 class="section-title" style="text-align: left;">Por que escolher a Union Mind para seu evento no <span class="accent">Expo Center Norte</span>?</h2>', '<h2 class="section-title" style="text-align: left;" data-i18n="sect-title">Por que escolher a Union Mind para seu evento no <span class="accent">Expo Center Norte</span>?</h2>')
        html = html.replace('<p>O Expo Center Norte exige conhecimento profundo de suas normas técnicas, logística de docas e cronogramas de montagem rígidios. Erros aqui custam caro em multas e atrasos.</p>', '<p data-i18n="sect-p1">O Expo Center Norte exige conhecimento profundo de suas normas técnicas, logística de docas e cronogramas de montagem rígidios. Erros aqui custam caro em multas e atrasos.</p>')
        html = html.replace('<p>Nossa equipe conhece cada detalhe operacional deste espaço. Atuamos como seu braço direito, resolvendo os problemas de forma silenciosa para que você foque apenas no seu convidado.</p>', '<p data-i18n="sect-p2">Nossa equipe conhece cada detalhe operacional deste espaço. Atuamos como seu braço direito, resolvendo os problemas de forma silenciosa para que você foque apenas no seu convidado.</p>')
        html = html.replace('<h3>Conceito Criativo e Segurança Operacional</h3>', '<h3 data-i18n="feat1-h3">Conceito Criativo e Segurança Operacional</h3>')
        html = html.replace('<p>Como uma verdadeira agência de eventos boutique, entregamos criatividade de ponta unida à produção rigorosa. Construímos uma experiência de marca impecável, respeitando todas as normas do pavilhão com total segurança.</p>', '<p data-i18n="feat1-p">Como uma verdadeira agência de eventos boutique, entregamos criatividade de ponta unida à produção rigorosa. Construímos uma experiência de marca impecável, respeitando todas as normas do pavilhão com total segurança.</p>')
        html = html.replace('<h3>Precisão Union Labs</h3>', '<h3 data-i18n="feat2-h3">Precisão Union Labs</h3>')
        html = html.replace('<p>Implementamos ativações de IA e rastro digital para transformar cada visitante no Expo Center Norte em um lead qualificado no seu CRM.</p>', '<p data-i18n="feat2-p">Implementamos ativações de IA e rastro digital para transformar cada visitante no Expo Center Norte em um lead qualificado no seu CRM.</p>')
        html = html.replace('<h2 class="section-title">Prepare sua operação no <br><span class="accent">Expo Center Norte</span></h2>', '<h2 class="section-title" data-i18n="cta-h2">Prepare sua operação no <br><span class="accent">Expo Center Norte</span></h2>')

    # Common fixes
    html = html.replace('<div class="method-intro" style="font-size: 2.2rem; line-height: 1.3; font-weight: 500; margin-bottom: 4rem; max-width: 900px;">', '<div class="method-intro" data-i18n="method-intro" style="font-size: 2.2rem; line-height: 1.3; font-weight: 500; margin-bottom: 4rem; max-width: 900px;">')
    html = html.replace('<h3>01. Parceiro Estratégico Real</h3>', '<h3 data-i18n="method-1-h3">01. Parceiro Estratégico Real</h3>')
    html = html.replace('<p>Mergulhamos na cultura, nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade absoluta e foco inegociável na experiência final.</p>', '<p data-i18n="method-1-p">Mergulhamos na cultura, nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade absoluta e foco inegociável na experiência final.</p>')
    html = html.replace('<h3>02. Squads High-End</h3>', '<h3 data-i18n="method-2-h3">02. Squads High-End</h3>')
    html = html.replace('<p>Sem burocracias ou camadas infinitas. Você tem acesso direto aos especialistas. Nosso formato ágil garante decisões rápidas, segurança na execução e altíssima flexibilidade.</p>', '<p data-i18n="method-2-p">Sem burocracias ou camadas infinitas. Você tem acesso direto aos especialistas. Nosso formato ágil garante decisões rápidas, segurança na execução e altíssima flexibilidade.</p>')
    html = html.replace('<h3>03. White Glove Delivery</h3>', '<h3 data-i18n="method-3-h3">03. White Glove Delivery</h3>')
    html = html.replace('<p>Cuidado extremo com os detalhes. Usamos dados, inteligência artificial e nosso feeling humano refinado para garantir que nada passe despercebido.</p>', '<p data-i18n="method-3-p">Cuidado extremo com os detalhes. Usamos dados, inteligência artificial e nosso feeling humano refinado para garantir que nada passe despercebido.</p>')
    
    html = html.replace('<p>Fale conosco e saiba como nossa IA Engine pode otimizar seu budget e garantir segurança total na entrega.</p>', '<p data-i18n="cta-p">Fale conosco e saiba como nossa IA Engine pode otimizar seu budget e garantir segurança total na entrega.</p>')
    html = html.replace('class="btn-cta" style="display: inline-block; padding: 1.2rem 3rem; margin-top: 2rem;">Falar no WhatsApp agora</a>', 'class="btn-cta" data-i18n="cta-btn" style="display: inline-block; padding: 1.2rem 3rem; margin-top: 2rem;">Falar no WhatsApp agora</a>')
    
    # footer
    disclaimer_pt = "A Union Mind é uma agência independente e não possui vínculo oficial ou afiliação direta com a administração do Expo Center Norte. As marcas mencionadas pertencem aos seus respectivos proprietários e são usadas apenas para fins de identificação logística." if cat == 'B' else "A Union Mind é uma agência independente e não possui vínculo oficial ou afiliação direta com a administração do Bourbon Atibaia Resort. As marcas mencionadas pertencem aos seus respectivos proprietários e são usadas apenas para fins de identificação logística."
    html = html.replace(disclaimer_pt, f'<span data-i18n="footer-disclaimer">{disclaimer_pt}</span>')

    # Script Injection
    js_template_a = """
    <script>
        const translations = {
            "pt": {
                "nav-expertise": "Expertise",
                "nav-cases": "Cases",
                "nav-cta": "Fale com um Especialista",
                "hero-tag": "OPERAÇÃO ESPECIALIZADA",
                "hero-h1": "Sua Próxima Convenção no <span class='accent'>Bourbon Atibaia</span>:<br>Criatividade e Operação Estratégica.",
                "hero-h2": "Transformamos o Bourbon Atibaia no palco que a sua equipe de vendas merece.",
                "sect-title": "Segurança e Impacto para sua Convenção no <span class='accent'>Bourbon Atibaia Resort</span>?",
                "sect-p1": "O Bourbon Atibaia Resort é o palco das maiores convenções de vendas do Brasil. Nossa operação garante que a montagem da cenografia respeite a excelência do resort, sem imprevistos.",
                "sect-p2": "Nossa equipe conhece cada detalhe operacional deste espaço. Atuamos como seu braço direito, garantindo que o palco, as ativações e a jornada do hóspede sejam impecáveis.",
                "feat1-h3": "Criatividade e Produção Premium",
                "feat1-p": "Entregamos o conceito criativo que sua marca espera, aliado a uma produção e cenografia impecáveis. Garantimos que sua convenção surpreenda a força de vendas com segurança e inovação.",
                "feat2-h3": "Precisão Union Labs",
                "feat2-p": "Implementamos gamificação e rastro digital para transformar sua convenção no Bourbon Atibaia em uma mina de inteligência comercial.",
                "method-intro": "Somos uma <span class='accent'>agência boutique</span> por escolha. Não queremos ser a maior fábrica de eventos; queremos ser a melhor parceira estratégica do seu negócio.",
                "method-1-h3": "01. Parceiro Estratégico Real",
                "method-1-p": "Mergulhamos na cultura, nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade absoluta e foco inegociável na experiência final.",
                "method-2-h3": "02. Squads High-End",
                "method-2-p": "Sem burocracias ou camadas infinitas. Você tem acesso direto aos especialistas. Nosso formato ágil garante decisões rápidas, segurança na execução e altíssima flexibilidade.",
                "method-3-h3": "03. White Glove Delivery",
                "method-3-p": "Cuidado extremo com os detalhes. Usamos dados, inteligência artificial e nosso feeling humano refinado para garantir que nada passe despercebido.",
                "cta-h2": "Prepare sua convenção no <br><span class='accent'>Bourbon Atibaia Resort</span>",
                "cta-p": "Fale conosco e saiba como nossa IA Engine pode otimizar seu budget e garantir segurança total na entrega.",
                "cta-btn": "Falar no WhatsApp agora",
                "footer-disclaimer": "A Union Mind é uma agência independente e não possui vínculo oficial ou afiliação direta com a administração do Bourbon Atibaia Resort. As marcas mencionadas pertencem aos seus respectivos proprietários e são usadas apenas para fins de identificação logística."
            },
            "en": {
                "nav-expertise": "Expertise",
                "nav-cases": "Cases",
                "nav-cta": "Talk to an Expert",
                "hero-tag": "SPECIALIZED OPERATION",
                "hero-h1": "Your Next Convention at <span class='accent'>Bourbon Atibaia</span>:<br>Creativity and Strategic Operations.",
                "hero-h2": "We transform the Bourbon Atibaia into the stage your sales team deserves.",
                "sect-title": "Security and Impact for your Convention at <span class='accent'>Bourbon Atibaia Resort</span>?",
                "sect-p1": "Bourbon Atibaia Resort hosts some of the biggest sales conventions. Our operation ensures that the scenography assembly matches the resort's excellence, without any surprises.",
                "sect-p2": "Our team knows every operational detail of this venue. We act as your right arm, ensuring the stage, activations, and guest journey are flawless.",
                "feat1-h3": "Premium Creativity and Production",
                "feat1-p": "We deliver the creative concept your brand expects, combined with impeccable execution and scenography. We ensure your convention amazes the sales force with safety and innovation.",
                "feat2-h3": "Union Labs Precision",
                "feat2-p": "We deploy gamification and digital tracking to turn your convention at Bourbon Atibaia into a goldmine of commercial intelligence.",
                "method-intro": "We are a <span class='accent'>boutique agency</span> by choice. We don't want to be the biggest event factory; we want to be the best strategic partner for your business.",
                "method-1-h3": "01. True Strategic Partner",
                "method-1-p": "We dive deep into your brand's culture, challenges, and pain points. We build solutions together, with absolute proximity and an uncompromising focus on the final experience.",
                "method-2-h3": "02. High-End Squads",
                "method-2-p": "No endless bureaucracy or layers. You get direct access to experts. Our agile format ensures fast decisions, flawless execution, and supreme flexibility.",
                "method-3-h3": "03. White Glove Delivery",
                "method-3-p": "Extreme attention to detail. We use data, AI, and our refined human feeling to ensure nothing falls through the cracks.",
                "cta-h2": "Plan your convention at <br><span class='accent'>Bourbon Atibaia Resort</span>",
                "cta-p": "Talk to us and discover how our AI Engine can optimize your budget and ensure total security in delivery.",
                "cta-btn": "Talk on WhatsApp now",
                "footer-disclaimer": "Union Mind is an independent agency and has no official affiliation with the management of Bourbon Atibaia Resort. Mentioned brands belong to their respective owners and are used here entirely for logistical identification purposes."
            }
        };

        function switchLanguage(lang) {
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    el.innerHTML = translations[lang][key];
                }
            });
            document.getElementById('btn-pt').classList.remove('active');
            document.getElementById('btn-en').classList.remove('active');
            document.getElementById('btn-' + lang).classList.add('active');
            document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
        }
    </script>
</body>"""

    js_template_b = """
    <script>
        const translations = {
            "pt": {
                "nav-expertise": "Expertise",
                "nav-cases": "Cases",
                "nav-cta": "Fale com um Especialista",
                "hero-tag": "OPERAÇÃO ESPECIALIZADA",
                "hero-h1": "Seu Próximo Evento no <span class='accent'>Expo Center Norte</span>:<br>Criatividade e Operação Estratégica.",
                "hero-h2": "Somos a agência boutique que une cenografia High-End e IA para transformar metros quadrados em negócios reais.",
                "sect-title": "Por que escolher a Union Mind para seu evento no <span class='accent'>Expo Center Norte</span>?",
                "sect-p1": "O Expo Center Norte exige conhecimento profundo de suas normas técnicas, logística de docas e cronogramas de montagem rígidios. Erros aqui custam caro em multas e atrasos.",
                "sect-p2": "Nossa equipe conhece cada detalhe operacional deste espaço. Atuamos como seu braço direito, resolvendo os problemas de forma silenciosa para que você foque apenas no seu convidado.",
                "feat1-h3": "Conceito Criativo e Segurança Operacional",
                "feat1-p": "Como uma verdadeira agência de eventos boutique, entregamos criatividade de ponta unida à produção rigorosa. Construímos uma experiência de marca impecável, respeitando todas as normas do pavilhão com total segurança.",
                "feat2-h3": "Precisão Union Labs",
                "feat2-p": "Implementamos ativações de IA e rastro digital para transformar cada visitante no Expo Center Norte em um lead qualificado no seu CRM.",
                "method-intro": "Somos uma <span class='accent'>agência boutique</span> por escolha. Não queremos ser a maior fábrica de eventos; queremos ser a melhor parceira estratégica do seu negócio.",
                "method-1-h3": "01. Parceiro Estratégico Real",
                "method-1-p": "Mergulhamos na cultura, nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade absoluta e foco inegociável na experiência final.",
                "method-2-h3": "02. Squads High-End",
                "method-2-p": "Sem burocracias ou camadas infinitas. Você tem acesso direto aos especialistas. Nosso formato ágil garante decisões rápidas, segurança na execução e altíssima flexibilidade.",
                "method-3-h3": "03. White Glove Delivery",
                "method-3-p": "Cuidado extremo com os detalhes. Usamos dados, inteligência artificial e nosso feeling humano refinado para garantir que nada passe despercebido.",
                "cta-h2": "Prepare sua operação no <br><span class='accent'>Expo Center Norte</span>",
                "cta-p": "Fale conosco e saiba como nossa IA Engine pode otimizar seu budget e garantir segurança total na entrega.",
                "cta-btn": "Falar no WhatsApp agora",
                "footer-disclaimer": "A Union Mind é uma agência independente e não possui vínculo oficial ou afiliação direta com a administração do Expo Center Norte. As marcas mencionadas pertencem aos seus respectivos proprietários e são usadas apenas para fins de identificação logística."
            },
            "en": {
                "nav-expertise": "Expertise",
                "nav-cases": "Cases",
                "nav-cta": "Talk to an Expert",
                "hero-tag": "SPECIALIZED OPERATION",
                "hero-h1": "Your Next Event at <span class='accent'>Expo Center Norte</span>:<br>Creativity and Strategic Operations.",
                "hero-h2": "We are the boutique agency that merges High-End scenography and AI to turn square meters into real business.",
                "sect-title": "Why choose Union Mind for your event at <span class='accent'>Expo Center Norte</span>?",
                "sect-p1": "Expo Center Norte requires deep knowledge of its technical norms, dock logistics, and strict assembly schedules. Mistakes here cost dearly in fines and delays.",
                "sect-p2": "Our team knows every operational detail of this venue. We act as your right arm, silently solving problems so you can focus entirely on your guests.",
                "feat1-h3": "Creative Concept and Operational Security",
                "feat1-p": "As a true boutique event agency, we deliver cutting-edge creativity coupled with rigorous production. We build flawless brand experiences, respecting all pavilion rules with total security.",
                "feat2-h3": "Union Labs Precision",
                "feat2-p": "We implement AI activations and digital tracking to convert every visitor at Expo Center Norte into a qualified lead in your CRM.",
                "method-intro": "We are a <span class='accent'>boutique agency</span> by choice. We don't want to be the biggest event factory; we want to be the best strategic partner for your business.",
                "method-1-h3": "01. True Strategic Partner",
                "method-1-p": "We dive deep into your brand's culture, challenges, and pain points. We build solutions together, with absolute proximity and an uncompromising focus on the final experience.",
                "method-2-h3": "02. High-End Squads",
                "method-2-p": "No endless bureaucracy or layers. You get direct access to experts. Our agile format ensures fast decisions, flawless execution, and supreme flexibility.",
                "method-3-h3": "03. White Glove Delivery",
                "method-3-p": "Extreme attention to detail. We use data, AI, and our refined human feeling to ensure nothing falls through the cracks.",
                "cta-h2": "Plan your operation at <br><span class='accent'>Expo Center Norte</span>",
                "cta-p": "Talk to us and discover how our AI Engine can optimize your budget and ensure total security in delivery.",
                "cta-btn": "Talk on WhatsApp now",
                "footer-disclaimer": "Union Mind is an independent agency and has no official affiliation with the management of Expo Center Norte. Mentioned brands belong to their respective owners and are used here entirely for logistical identification purposes."
            }
        };

        function switchLanguage(lang) {
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    el.innerHTML = translations[lang][key];
                }
            });
            document.getElementById('btn-pt').classList.remove('active');
            document.getElementById('btn-en').classList.remove('active');
            document.getElementById('btn-' + lang).classList.add('active');
            document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
        }
    </script>
</body>"""

    if cat == 'A':
        html = html.replace('</body>', js_template_a)
    else:
        html = html.replace('</body>', js_template_b)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

process_file('espacos/bourbon-atibaia-resort.html', 'A')
process_file('espacos/expo-center-norte.html', 'B')
