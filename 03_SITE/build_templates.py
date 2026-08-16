import os
import re

def create_templates():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    main_start = -1
    footer_start = -1
    
    for i, line in enumerate(lines):
        if '<main>' in line:
            main_start = i
        if '<!-- ============ FOOTER ============ -->' in line:
            footer_start = i
            
    head_content = "".join(lines[:main_start+1])
    footer_content = "".join(lines[footer_start:])
    
    # Bairro Template HTML
    bairro_main = """
        <section style="position: relative; padding: 14rem 0 7rem; text-align: center; color: #fff; overflow: hidden;">
            <div style="position: absolute; inset: 0; background-image: url('../assets/hero-urbano-bg.jpg'); background-size: cover; background-position: center; z-index: 0;"></div>
            <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.65); z-index: 1;"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <span class="label-tag" style="color: var(--blue-bright); margin-bottom: 1rem; display: block;" data-i18n="tmpl-expo-tag">AGÊNCIA DE EVENTOS SP</span>
                <h1 style="font-size: clamp(3rem, 5vw, 4.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; letter-spacing:-0.03em;" data-i18n="tmpl-bairro-h1">Seu Evento Corporativo na <span style="color: var(--blue-bright);">[BAIRRO_NOME]</span></h1>
                <p style="max-width: 800px; margin: 0 auto; font-size: 1.25rem; color: rgba(255,255,255,0.8);" data-i18n="tmpl-bairro-p1">Sua marca precisa de um parceiro estratégico perto do QG em [BAIRRO_NOME]. Nós entregamos a execução impecável para que você foque em relacionamento e gerar negócios.</p>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream); color: var(--charcoal);">
            <div class="container">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                    <div>
                        <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 2rem; line-height: 1.1; letter-spacing:-0.02em;" data-i18n="tmpl-bairro-h2">O Polo Corporativo exige Eventos de Alto Padrão</h2>
                        <div style="border-left: 4px solid var(--blue); padding-left: 1.5rem; margin-bottom: 2rem;">
                            <p style="font-size: 1.1rem; color: var(--gray-text);" data-i18n="tmpl-bairro-p2">A região de [BAIRRO_NOME] é o coração financeiro e corporativo de São Paulo. Seus diretores e convidados estão acostumados ao mais alto nível de exigência. Nós estruturamos eventos premium na sua região.</p>
                        </div>
                        <p style="font-size: 1.1rem; color: var(--gray-text);" data-i18n="tmpl-bairro-p3">Você precisa realizar um C-Level Meeting amanhã? Com 10 anos de mercado, somos a agência boutique que tem agilidade e entrega White Glove para os líderes da sua empresa.</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 2rem;">
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-bairro-h3-1">Time Sênior. Sem Intermediários.</h3>
                            <p style="color: var(--gray-text);" data-i18n="tmpl-bairro-p4">Você negocia e planeja diretamente com quem decide. Sabemos que em [BAIRRO_NOME] o tempo é escasso. Otimizamos aprovações e resolvemos a operação sem burocracia.</p>
                        </div>
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-bairro-h3-2">Inteligência Logística</h3>
                            <p style="color: var(--gray-text);" data-i18n="tmpl-bairro-p5">Montar eventos nos principais prédios e hotéis da região de [BAIRRO_NOME] requer know-how de regras prediais e horários rígidos. Nós já conhecemos o terreno.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section style="padding: 6rem 0; background-color: var(--charcoal-mid); color: var(--cream);">
            <div class="container">
                <div style="font-size: 2.2rem; line-height: 1.3; font-weight: 500; margin-bottom: 4rem; max-width: 900px;">
                    <span data-i18n="tmpl-bairro-footer">Somos uma <span style="color: var(--blue-bright);">agência boutique</span> por escolha. 10 anos no mercado de live marketing corporativo com quem faz — não quem delega.</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
                    <div>
                        <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 1rem; color: var(--blue-bright);">01. Parceiro Estratégico Real</h3>
                        <p style="color: rgba(255,255,255,0.7); font-size: 0.95rem;">Construímos soluções a quatro mãos, com proximidade absoluta e foco inegociável na experiência final.</p>
                    </div>
                    <div>
                        <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 1rem; color: var(--blue-bright);">02. Squads High-End</h3>
                        <p style="color: rgba(255,255,255,0.7); font-size: 0.95rem;">Você tem acesso direto aos especialistas. Nosso formato ágil garante decisões rápidas e execução segura.</p>
                    </div>
                    <div>
                        <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 1rem; color: var(--blue-bright);">03. White Glove Delivery</h3>
                        <p style="color: rgba(255,255,255,0.7); font-size: 0.95rem;">Cuidado extremo com os detalhes. Usamos dados e feeling humano para garantir que nada passe despercebido.</p>
                    </div>
                </div>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream-dark); text-align: center; color: var(--charcoal);">
            <div class="container" style="max-width: 700px;">
                <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing:-0.02em;">Planeje seu evento corporativo hoje</h2>
                <p style="font-size: 1.1rem; color: var(--gray-text); margin-bottom: 2rem;">Consultoria de Escopo Gratuita: nossa equipe sênior analisa seu briefing e entrega um diagnóstico técnico em 48h.</p>
                <a href="https://wa.me/5511947684604?text=Ol%C3%A1%2C%20quero%20falar%20sobre%20um%20evento%20corporativo%20na%20regi%C3%A3o%20de%20[VENUE_WA]!" target="_blank" style="display: inline-block; padding: 1.2rem 3rem; background: var(--blue); color: #fff; font-weight: 700; border-radius: 50px; font-size: 1.1rem; text-decoration:none;">Falar no WhatsApp agora</a>
                <p style="margin-top: 1.5rem;"><a href="../index.html#configurador" style="color: var(--blue); font-weight: 600; text-decoration:none;">→ Ou solicite uma Consultoria de Escopo via Site</a></p>
            </div>
        </section>
    </main>
"""

    urbano_main = """
        <section style="position: relative; padding: 14rem 0 7rem; text-align: center; color: #fff; overflow: hidden;">
            <div style="position: absolute; inset: 0; background-image: url('../assets/hero-urbano-bg.jpg'); background-size: cover; background-position: center; z-index: 0;"></div>
            <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.65); z-index: 1;"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <span class="label-tag" style="color: var(--blue-bright); margin-bottom: 1rem; display: block;" data-i18n="tmpl-expo-tag">AGÊNCIA DE EVENTOS SP</span>
                <h1 style="font-size: clamp(3rem, 5vw, 4.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; letter-spacing:-0.03em;" data-i18n="tmpl-urbano-h1">Seu Evento Corporativo no <span style="color: var(--blue-bright);">[VENUE_NAME]</span></h1>
                <p style="max-width: 800px; margin: 0 auto; font-size: 1.25rem; color: rgba(255,255,255,0.8);" data-i18n="tmpl-urbano-p1">Você decidiu que será no [VENUE_NAME]. Nós garantimos que a execução seja impecável, unindo nossa excelência operacional à logística do local.</p>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream); color: var(--charcoal);">
            <div class="container">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                    <div>
                        <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 2rem; line-height: 1.1; letter-spacing:-0.02em;" data-i18n="tmpl-urbano-h2">Especialistas no <span style="color: var(--blue);">[VENUE_NAME]</span></h2>
                        <div style="border-left: 4px solid var(--blue); padding-left: 1.5rem; margin-bottom: 2rem;">
                            <p style="font-size: 1.1rem; color: var(--gray-text);">O [VENUE_NAME] é um dos espaços mais disputados para eventos em [VENUE_BAIRRO]. Mas um bom espaço só brilha com uma operação impecável. Nós somos especialistas na logística e cenografia deste local.</p>
                        </div>
                        <p style="font-size: 1.1rem; color: var(--gray-text);">Não somos apenas uma agência de montagem. Somos uma consultoria completa que planeja a arquitetura promocional, a tecnologia (Union Labs) e o A&B focado na experiência do seu cliente (C-Level).</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 2rem;">
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-resort-h3-1">White Glove Delivery</h3>
                            <p style="color: var(--gray-text);">Da recepção VIP à coordenação do palco, entregamos uma operação silenciosa e assertiva no [VENUE_NAME].</p>
                        </div>
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-bairro-h3-2">Inteligência Logística</h3>
                            <p style="color: var(--gray-text);">Cada pavilhão e hotel possui regras de montagem rigorosas (horários, CA, NR-12). Nós tiramos essa dor de cabeça da sua equipe.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream-dark); text-align: center; color: var(--charcoal);">
            <div class="container" style="max-width: 700px;">
                <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing:-0.02em;">Leve seu evento no [VENUE_NAME] para o próximo nível</h2>
                <p style="font-size: 1.1rem; color: var(--gray-text); margin-bottom: 2rem;">Fale diretamente com quem decide. Nossa equipe sênior responde sua cotação em 48 horas.</p>
                <a href="https://wa.me/5511947684604?text=Ol%C3%A1%2C%20quero%20falar%20sobre%20um%20evento%20no%20[VENUE_WA]!" target="_blank" style="display: inline-block; padding: 1.2rem 3rem; background: var(--blue); color: #fff; font-weight: 700; border-radius: 50px; font-size: 1.1rem; text-decoration:none;">Falar com Especialista agora</a>
                <p style="margin-top: 1.5rem;"><a href="../index.html" style="color: var(--blue); font-weight: 600; text-decoration:none;" data-i18n="tmpl-btn-back">→ Voltar para a Página Inicial</a></p>
            </div>
        </section>
        
        <div style="padding: 1.5rem 0; background: #000; text-align: center; font-size: 0.75rem; color: rgba(255,255,255,0.4);">
            A Union Mind é uma agência de live marketing independente. Não possuímos vínculo comercial direto ou exclusividade com a administração do [VENUE_NAME], atuando como agência contratada por marcas expositoras.
        </div>
    </main>
"""

    expo_main = """
        <section style="position: relative; padding: 14rem 0 7rem; text-align: center; color: #fff; overflow: hidden;">
            <div style="position: absolute; inset: 0; background-image: url('../assets/hero-expo-bg.jpg'); background-size: cover; background-position: center; z-index: 0;"></div>
            <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.72); z-index: 1;"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <span class="label-tag" style="color: var(--blue-bright); margin-bottom: 1rem; display: block;" data-i18n="tmpl-expo-tag">AGÊNCIA DE EVENTOS SP</span>
                <h1 style="font-size: clamp(3rem, 5vw, 4.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; letter-spacing:-0.03em;" data-i18n="tmpl-expo-h1">Seu Estande no <span style="color: var(--blue-bright);">[VENUE_NAME]</span></h1>
                <p style="max-width: 800px; margin: 0 auto; font-size: 1.25rem; color: rgba(255,255,255,0.8);" data-i18n="tmpl-expo-p1">Sua marca vai expor no [VENUE_NAME]? Construímos estandes focados em relacionamento corporativo e captura de leads.</p>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream); color: var(--charcoal);">
            <div class="container">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                    <div>
                        <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 2rem; line-height: 1.1; letter-spacing:-0.02em;" data-i18n="tmpl-expo-h2">Destaque-se no <span style="color: var(--blue);">[VENUE_NAME]</span></h2>
                        <div style="border-left: 4px solid var(--blue); padding-left: 1.5rem; margin-bottom: 2rem;">
                            <p style="font-size: 1.1rem; color: var(--gray-text);" data-i18n="tmpl-expo-p2">Participar de uma feira ou exposição no [VENUE_NAME] é um alto investimento. Seu estande não pode ser apenas uma estrutura padrão, ele precisa gerar ROI.</p>
                        </div>
                        <p style="font-size: 1.1rem; color: var(--gray-text);" data-i18n="tmpl-expo-p3">Projetamos arquitetura promocional e ativações (EventTech) que atraem leads, enquanto nossa equipe cuida de toda a logística e liberação junto à promotora da feira.</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 2rem;">
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-expo-h3-1">Cenografia de Impacto</h3>
                            <p style="color: var(--gray-text);" data-i18n="tmpl-expo-p4">Estandes cenográficos, painéis de LED curvos, salas VIP de negócios e design de impacto visual para atrair os principais decisores do seu mercado.</p>
                        </div>
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-expo-h3-2">Gestão Burocrática</h3>
                            <p style="color: var(--gray-text);" data-i18n="tmpl-expo-p5">Nós lidamos com taxas, alvarás, RRTs e negociação com a operação local do [VENUE_NAME]. Você só chega para receber os clientes.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream-dark); text-align: center; color: var(--charcoal);">
            <div class="container" style="max-width: 700px;">
                <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing:-0.02em;" data-i18n="tmpl-expo-h2-2">Planeje seu Estande no [VENUE_NAME]</h2>
                <p style="font-size: 1.1rem; color: var(--gray-text); margin-bottom: 2rem;" data-i18n="tmpl-expo-p6">Entre em contato conosco hoje mesmo e receba um diagnóstico 3D preliminar ou orçamento técnico em 48h.</p>
                <a href="https://wa.me/5511947684604?text=Ol%C3%A1%2C%20quero%20falar%20sobre%20um%20estande%20no%20[VENUE_WA]!" target="_blank" style="display: inline-block; padding: 1.2rem 3rem; background: var(--blue); color: #fff; font-weight: 700; border-radius: 50px; font-size: 1.1rem; text-decoration:none;">Falar com Especialista agora</a>
                <p style="margin-top: 1.5rem;"><a href="../index.html" style="color: var(--blue); font-weight: 600; text-decoration:none;" data-i18n="tmpl-btn-back">→ Voltar para a Página Inicial</a></p>
            </div>
        </section>
        
        <div style="padding: 1.5rem 0; background: #000; text-align: center; font-size: 0.75rem; color: rgba(255,255,255,0.4);">
            <span data-i18n="tmpl-expo-footer">A Union Mind atua como montadora e agência contratada por marcas expositoras. Não somos a promotora da feira nem a administração oficial do [VENUE_NAME].</span>
        </div>
    </main>
"""

    resort_main = """
        <section style="position: relative; padding: 14rem 0 7rem; text-align: center; color: #fff; overflow: hidden;">
            <div style="position: absolute; inset: 0; background-image: url('../assets/hero-urbano-bg.jpg'); background-size: cover; background-position: center; z-index: 0;"></div>
            <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.65); z-index: 1;"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <span class="label-tag" style="color: var(--blue-bright); margin-bottom: 1rem; display: block;" data-i18n="tmpl-expo-tag">AGÊNCIA DE EVENTOS SP</span>
                <h1 style="font-size: clamp(3rem, 5vw, 4.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; letter-spacing:-0.03em;" data-i18n="tmpl-resort-h1">Sua Convenção no <span style="color: var(--blue-bright);">[VENUE_NAME]</span></h1>
                <p style="max-width: 800px; margin: 0 auto; font-size: 1.25rem; color: rgba(255,255,255,0.8);" data-i18n="tmpl-resort-p1">Você decidiu realizar sua convenção de líderes ou vendas no [VENUE_NAME]. Nós garantimos uma experiência C-Level para sua equipe — da plenária principal ao encerramento.</p>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream); color: var(--charcoal);">
            <div class="container">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                    <div>
                        <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 2rem; line-height: 1.1; letter-spacing:-0.02em;" data-i18n="tmpl-resort-h2">Especialistas em Convenções no <span style="color: var(--blue);">[VENUE_NAME]</span></h2>
                        <div style="border-left: 4px solid var(--blue); padding-left: 1.5rem; margin-bottom: 2rem;">
                            <p style="font-size: 1.1rem; color: var(--gray-text);" data-i18n="tmpl-resort-p2">O [VENUE_NAME] oferece uma infraestrutura excelente para eventos, mas a operação do seu evento exige controle minucioso de voos, hospedagem e plenárias simultâneas.</p>
                        </div>
                        <p style="font-size: 1.1rem; color: var(--gray-text);" data-i18n="tmpl-resort-p3">Nós gerenciamos toda a jornada do participante. Da cenografia da plenária principal até festas de encerramento, garantimos que a cultura da sua empresa brilhe enquanto nós cuidamos da logística complexa.</p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 2rem;">
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-resort-h3-1">White Glove Delivery</h3>
                            <p style="color: var(--gray-text);" data-i18n="tmpl-resort-p4">Recepção nos aeroportos, RSVP ativo, controle de rooming list e kits de boas-vindas personalizados em cada quarto do resort.</p>
                        </div>
                        <div>
                            <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--blue);" data-i18n="tmpl-resort-h3-2">Gestão de Plenária (A/V)</h3>
                            <p style="color: var(--gray-text);" data-i18n="tmpl-resort-p5">Coordenação de direção técnica, painéis de LED, áudio cristalino e cronograma rigoroso para o conteúdo (Run of Show).</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section style="padding: 6rem 0; background: var(--cream-dark); text-align: center; color: var(--charcoal);">
            <div class="container" style="max-width: 700px;">
                <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing:-0.02em;" data-i18n="tmpl-resort-h2-2">Planeje sua Convenção no [VENUE_NAME]</h2>
                <p style="font-size: 1.1rem; color: var(--gray-text); margin-bottom: 2rem;" data-i18n="tmpl-resort-p6">Entre em contato e descubra como otimizar seu orçamento. Entregamos propostas técnicas em 48 horas.</p>
                <a href="https://wa.me/5511947684604?text=Ol%C3%A1%2C%20quero%20falar%20sobre%20uma%20conven%C3%A7%C3%A3o%20no%20[VENUE_WA]!" target="_blank" style="display: inline-block; padding: 1.2rem 3rem; background: var(--blue); color: #fff; font-weight: 700; border-radius: 50px; font-size: 1.1rem; text-decoration:none;">Falar com Especialista agora</a>
                <p style="margin-top: 1.5rem;"><a href="../index.html" style="color: var(--blue); font-weight: 600; text-decoration:none;" data-i18n="tmpl-btn-back">→ Voltar para a Página Inicial</a></p>
            </div>
        </section>
        
        <div style="padding: 1.5rem 0; background: #000; text-align: center; font-size: 0.75rem; color: rgba(255,255,255,0.4);">
            <span data-i18n="tmpl-resort-footer">A Union Mind atua como agência de produção corporativa independente e não possui vínculo com a administração direta do [VENUE_NAME].</span>
        </div>
    </main>
"""

    # ==========================================
    # SHARED BLOCKS — used by all 4 templates
    # ==========================================

    LOGO_STRIP = """
        <!-- MINI LOGO STRIP -->
        <section style="padding: 2.5rem 0; background: var(--cream); border-bottom: 1px solid var(--cream-dark);">
            <div class="container">
                <div style="display: flex; align-items: center; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
                    <span style="font-family: var(--font-mono); font-size: 0.65rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--gray-light); white-space: nowrap; margin-right: 1rem;">Já atendemos</span>
                    <div style="display: flex; align-items: center; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
                        <img src="../assets/logos/natura-clean.png" alt="Natura" style="height: 30px; opacity: 0.65; filter: grayscale(1);">
                        <img src="../assets/logos/danone-nutricia.png" alt="Danone" style="height: 30px; opacity: 0.65; filter: grayscale(1);">
                        <img src="../assets/logos/pepsico.svg" alt="PepsiCo" style="height: 30px; opacity: 0.65; filter: grayscale(1);">
                        <img src="../assets/logos/toyota.svg" alt="Toyota" style="height: 30px; opacity: 0.65; filter: grayscale(1);">
                        <img src="../assets/logos/auren.svg" alt="Auren Energia" style="height: 30px; opacity: 0.65; filter: grayscale(1);">
                    </div>
                </div>
            </div>
        </section>
    """

    CASES_SECTION = """
        <!-- CASES SECTION -->
        <section style="padding: 6rem 0; background: var(--cream-dark); color: var(--charcoal);">
            <div class="container">
                <div style="margin-bottom: 3rem;">
                    <span style="font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--blue); display: block; margin-bottom: 0.8rem;">— CASES SELECIONADOS</span>
                    <h2 style="font-size: 2rem; font-weight: 800; letter-spacing: -0.02em;">Marcas que já confiaram em nós</h2>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;">
                    <div style="position: relative; border-radius: 8px; overflow: hidden; aspect-ratio: 4/3;">
                        <img src="../assets/cases/case-natura-new.jpg" alt="Natura — INFINITY INTERNACIONAL" loading="lazy" style="width:100%; height:100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 1.2rem; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%); color: #fff;">
                            <span style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; color: var(--blue-bright);">Convenção Internacional</span>
                            <p style="font-weight: 700; font-size: 0.95rem; margin-top: 0.25rem;">INFINITY INTERNACIONAL · Natura</p>
                            <p style="font-size: 0.8rem; opacity: 0.7;">3.000 consultoras</p>
                        </div>
                    </div>
                    <div style="position: relative; border-radius: 8px; overflow: hidden; aspect-ratio: 4/3;">
                        <img src="../assets/cases/case-danone.jpg" alt="DNA Danone" loading="lazy" style="width:100%; height:100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 1.2rem; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%); color: #fff;">
                            <span style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; color: var(--blue-bright);">Convenção de Vendas</span>
                            <p style="font-weight: 700; font-size: 0.95rem; margin-top: 0.25rem;">DNA Danone</p>
                            <p style="font-size: 0.8rem; opacity: 0.7;">600 líderes</p>
                        </div>
                    </div>
                    <div style="position: relative; border-radius: 8px; overflow: hidden; aspect-ratio: 4/3;">
                        <img src="../assets/cases/case-auren-new.jpg" alt="#SomosAuren 2025" loading="lazy" style="width:100%; height:100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 1.2rem; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%); color: #fff;">
                            <span style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; color: var(--blue-bright);">Convenção da Marca</span>
                            <p style="font-weight: 700; font-size: 0.95rem; margin-top: 0.25rem;">#SomosAuren 2025</p>
                            <p style="font-size: 0.8rem; opacity: 0.7;">600 convidados</p>
                        </div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 2.5rem;">
                    <a href="../index.html#cases" style="color: var(--blue); font-weight: 600; font-size: 0.95rem; text-decoration: none;">Ver todos os cases →</a>
                </div>
            </div>
        </section>
    """

    def make_faq(q1, a1, q2, a2, q3, a3, name_pt):
        return f"""
        <!-- FAQ LOCAL -->
        <section style="padding: 5rem 0; background: var(--cream); color: var(--charcoal);" id="faq">
            <div class="container" style="max-width: 800px;">
                <div style="margin-bottom: 2.5rem;">
                    <span style="font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--blue); display: block; margin-bottom: 0.8rem;">— DÚVIDAS FREQUENTES</span>
                    <h2 style="font-size: 2rem; font-weight: 800; letter-spacing: -0.02em;">Perguntas sobre eventos em {name_pt}</h2>
                </div>
                <details style="border-bottom: 1px solid var(--cream-dark); padding: 1.2rem 0; cursor: pointer;">
                    <summary style="font-weight: 600; font-size: 1.05rem;">{q1}</summary>
                    <p style="margin-top: 0.8rem; color: var(--gray-text); line-height: 1.7;">{a1}</p>
                </details>
                <details style="border-bottom: 1px solid var(--cream-dark); padding: 1.2rem 0; cursor: pointer;">
                    <summary style="font-weight: 600; font-size: 1.05rem;">{q2}</summary>
                    <p style="margin-top: 0.8rem; color: var(--gray-text); line-height: 1.7;">{a2}</p>
                </details>
                <details style="border-bottom: 1px solid var(--cream-dark); padding: 1.2rem 0; cursor: pointer;">
                    <summary style="font-weight: 600; font-size: 1.05rem;">{q3}</summary>
                    <p style="margin-top: 0.8rem; color: var(--gray-text); line-height: 1.7;">{a3}</p>
                </details>
            </div>
        </section>
    """

    # FAQs by type
    faq_bairro = make_faq(
        "Vocês organizam C-Level Meetings na região de [BAIRRO_NOME]?",
        "Sim. Eventos executivos, reuniões de conselho e retiros de liderança na [BAIRRO_NOME] são uma especialidade da Union Mind. Operamos com agilidade para prazos curtos e entregamos toda a coordenação logística e A&B.",
        "Quanto custa um evento corporativo na [BAIRRO_NOME]?",
        "Eventos de 50 a 200 pessoas geralmente partem de R$ 40 mil em fee de gestão, já incluindo coordenação operacional, cenografia e A&B. A Consultoria de Escopo Gratuita entrega uma faixa real em 48h, sem compromisso.",
        "Qual o prazo mínimo para contratar a Union Mind?",
        "Atendemos projetos com prazos curtos. Para eventos na [BAIRRO_NOME] com menos de 30 dias, operamos no modelo Fast Track — priorizamos fornecedores com disponibilidade imediata e entregamos o planejamento em até 4 horas.",
        "[BAIRRO_NOME]"
    )

    faq_urbano = make_faq(
        "Vocês já realizaram eventos no [VENUE_NAME]?",
        "A Union Mind tem experiência em eventos nos principais espaços premium de São Paulo, incluindo hotéis e centros de eventos de alto padrão como o [VENUE_NAME]. Conhecemos os regulamentos de montagem, horários de acesso e restrições de cada venue.",
        "<span data-i18n='faq-q-urbano-1'>Quanto custa um evento corporativo no [VENUE_NAME]?</span>",
        "O investimento varia conforme formato e número de convidados. Eventos de 50 a 300 pessoas geralmente partem de R$ 40 mil em fee de gestão. A Consultoria de Escopo Gratuita entrega uma faixa real em 48h.",
        "A Union Mind cuida de toda a operação no [VENUE_NAME]?",
        "Sim. Gerenciamos 100% da operação — desde a negociação do espaço e cenografia até A&B, credenciamento e direção técnica (áudio e vídeo). Você recebe um único ponto de contato do briefing ao encerramento.",
        "[VENUE_NAME]"
    )

    faq_expo = make_faq(
        "<span data-i18n='faq-q-expo-1'>Quanto custa um estande no [VENUE_NAME]?</span>",
        "<span data-i18n='faq-a-expo-1'>O valor de um estande varia conforme a metragem quadrada e a complexidade do projeto. Estandes menores (até 36m²) tendem a ter um custo por m² maior, pois certos custos operacionais de montagem existem independente do tamanho. Estandes maiores diluem esses custos e costumam ter um custo por m² mais eficiente. Nossa Consultoria de Escopo Gratuita entrega um orçamento técnico preciso em 48h — sem compromisso.</span>",
        "<span data-i18n='faq-q-expo-2'>Quem cuida do CA (Certificado de Aprovação) e do credenciamento no [VENUE_NAME]?</span>",
        "<span data-i18n='faq-a-expo-2'>A Union Mind assume toda a burocracia: aprovação do projeto com a promotora da feira, emissão do RRT, licenças e credenciamento da equipe. Você chega para receber os clientes.</span>",
        "<span data-i18n='faq-q-expo-3'>É possível montar um estande no [VENUE_NAME] com menos de 30 dias de prazo?</span>",
        "<span data-i18n='faq-a-expo-3'>Sim. Temos parceiros de montagem com disponibilidade imediata e operamos no modelo Fast Track para projetos urgentes. Entre em contato o quanto antes — projetos com menos de 2 semanas de prazo exigem escopo simplificado.</span>",
        "[VENUE_NAME]"
    )

    faq_resort = make_faq(
        "<span data-i18n='faq-q-resort-1'>Quanto custa uma convenção no [VENUE_NAME]?</span>",
        "<span data-i18n='faq-a-resort-1'>O investimento varia conforme o número de participantes, a quantidade de dias de operação e o nível de complexidade da produção (cenografia, A/V, palestrantes). A Consultoria de Escopo Gratuita analisa suas necessidades e entrega uma faixa de investimento real e personalizada em 48h.</span>",
        "<span data-i18n='faq-q-resort-2'>A Union Mind cuida do transfer e da logística de hospedagem no [VENUE_NAME]?</span>",
        "<span data-i18n='faq-a-resort-2'>Sim. Gerenciamos toda a jornada do participante: voos, transfer, rooming list, check-in e kits de boas-vindas nos quartos. Você delega a operação completa e foca no conteúdo do evento.</span>",
        "<span data-i18n='faq-q-resort-3'>A Union Mind faz a direção técnica da plenária no [VENUE_NAME]?</span>",
        "Sim. Direção de palco, A/V, painéis de LED, run of show e coordenação de palestrantes são serviços integrados. Trabalhamos com um único cronograma minuto a minuto, da abertura ao encerramento.",
        "[VENUE_NAME]"
    )

    # i18n script for venue pages
    I18N_SCRIPT = """
<script>
const localTranslations = {
    pt: {
        "local-hero-tag": "AGÊNCIA DE EVENTOS SP",
        "local-clients": "Já atendemos",
        "local-cases-tag": "— CASES SELECIONADOS",
        "local-cases-title": "Marcas que já confiaram em nós",
        "local-faq-tag": "— DÚVIDAS FREQUENTES",
        "local-cta-btn": "Falar no WhatsApp agora",
        "local-cta-btn2": "Solicitar Consultoria via Site",
        "nav-cta": "Fale com um Especialista →"
    },
    en: {
        "local-hero-tag": "CORPORATE EVENTS AGENCY · SÃO PAULO · DMC BRAZIL",
        "local-clients": "Trusted by",
        "local-cases-tag": "— SELECTED CASES",
        "local-cases-title": "Brands that trusted us",
        "local-faq-tag": "— FREQUENTLY ASKED QUESTIONS",
        "local-cta-btn": "Talk on WhatsApp now",
        "local-cta-btn2": "Request Consultancy via Website",
        "nav-cta": "Talk to an Expert →",

        "tmpl-bairro-h1": "Your Corporate Event in <span style='color: var(--blue-bright);'>[BAIRRO_NOME]</span>",
        "tmpl-bairro-p1": "Your brand needs a strategic partner near your HQ in [BAIRRO_NOME]. We deliver impeccable execution so you can focus on relationships and generating business.",
        "tmpl-bairro-h2": "The Corporate Hub demands High-Standard Events",
        "tmpl-bairro-p2": "The [BAIRRO_NOME] region is the financial and corporate heart of São Paulo. Your directors and guests are accustomed to the highest level of excellence. We structure premium events in your area.",
        "tmpl-bairro-p3": "Do you need to hold a C-Level Meeting tomorrow? With 10 years in the market, we are the boutique agency with the agility and White Glove delivery for your company's leaders.",
        "tmpl-bairro-h3-1": "Senior Team. No Intermediaries.",
        "tmpl-bairro-p4": "You negotiate and plan directly with decision-makers. We know time is scarce in [BAIRRO_NOME]. We optimize approvals and handle operations without bureaucracy.",
        "tmpl-bairro-h3-2": "Logistical Intelligence",
        "tmpl-bairro-p5": "Building events in the main buildings and hotels of [BAIRRO_NOME] requires know-how of building rules and strict schedules. We already know the terrain.",
        "tmpl-bairro-footer": "We are a <span style='color: var(--blue-bright);'>boutique agency</span> by choice. 10 years in corporate live marketing with those who do the work — not those who delegate.",
        
        "tmpl-urbano-h1": "Your Corporate Event at <span style='color: var(--blue-bright);'>[VENUE_NAME]</span>",
        "tmpl-urbano-p1": "You decided it will be at [VENUE_NAME]. We guarantee impeccable execution, uniting our operational excellence with the venue's logistics.",
        "tmpl-urbano-h2": "Experts at <span style='color: var(--blue);'>[VENUE_NAME]</span>",
        "tmpl-urbano-p2": "[VENUE_NAME] is a highly sought-after venue that requires millimeter-precise logistical operation. Our team knows the local rules and manages everything end-to-end.",
        "tmpl-urbano-p3": "Whether it's a product launch, year-end party, or award ceremony, we deliver premium scenography and flawless production so you can focus on your guests.",
        "tmpl-urbano-p6": "Avoid surprises with uncoordinated suppliers. We deliver the project 100% resolved. Request a scope and quote in 48 hours.",
        "tmpl-urbano-footer": "Union Mind acts as an independent corporate agency and has no exclusivity or affiliation with the management of [VENUE_NAME].",
        
        "faq-q-urbano-1": "How much does a corporate event at [VENUE_NAME] cost?",
        "faq-a-urbano-1": "Events for 150 to 500 people in São Paulo typically start at R$ 150,000 (depending on F&B, scenography, and entertainment). Our Scoping Consultancy analyzes your idea and delivers precise financial feasibility in 48h.",
        "faq-q-urbano-2": "Does Union Mind negotiate directly with [VENUE_NAME]?",
        "faq-a-urbano-2": "Yes. Besides renting the space, we manage the venue's approved suppliers (security, cleaning, F&B) and all assembly logistics to secure the best negotiation.",
        "faq-q-urbano-3": "How does the agency's Boutique model work?",
        "faq-a-urbano-3": "In the boutique model, the same Senior Director who takes your brief will be responsible for the operation on the event day at [VENUE_NAME]. No hand-offs to juniors, ensuring total quality.",

        "tmpl-expo-tag": "CORPORATE EVENTS AGENCY SP",
        "tmpl-expo-h1": "Your Booth at <span style='color: var(--blue-bright);'>[VENUE_NAME]</span>",
        "tmpl-expo-p1": "Exhibiting at [VENUE_NAME]? We build booths focused on corporate networking and lead capture.",
        "tmpl-expo-h2": "Stand out at <span style='color: var(--blue);'>[VENUE_NAME]</span>",
        "tmpl-expo-p2": "Participating in a trade show at [VENUE_NAME] is a high investment. Your booth cannot be just a standard structure, it needs to generate ROI.",
        "tmpl-expo-p3": "We design promotional architecture and activations (EventTech) that attract leads, while our team handles all logistics and clearance with the show promoter.",
        "tmpl-expo-h3-1": "High-Impact Scenography",
        "tmpl-expo-p4": "Scenic booths, curved LED walls, VIP business rooms, and high-impact visual design to attract top decision-makers in your market.",
        "tmpl-expo-h3-2": "Bureaucracy Management",
        "tmpl-expo-p5": "We handle fees, permits, RRTs, and negotiation with [VENUE_NAME]'s local operations. You just arrive to welcome clients.",
        "tmpl-expo-h2-2": "Plan your Booth at [VENUE_NAME]",
        "tmpl-expo-p6": "Contact us today and receive a preliminary 3D diagnosis or technical quote in 48h.",
        "tmpl-expo-footer": "Union Mind acts as a builder and agency hired by exhibiting brands. We are not the show promoter nor the official administration of [VENUE_NAME].",
        
        "tmpl-resort-h1": "Your Convention at <span style='color: var(--blue-bright);'>[VENUE_NAME]</span>",
        "tmpl-resort-p1": "You decided to hold your leadership or sales convention at [VENUE_NAME]. We guarantee a C-Level experience for your team — from the main plenary to closing.",
        "tmpl-resort-h2": "Convention Experts at <span style='color: var(--blue);'>[VENUE_NAME]</span>",
        "tmpl-resort-p2": "[VENUE_NAME] offers excellent infrastructure for events, but operating your event requires meticulous control of flights, lodging, and simultaneous plenaries.",
        "tmpl-resort-p3": "We manage the entire attendee journey. From the main plenary's scenography to closing parties, we ensure your company's culture shines while we handle complex logistics.",
        "tmpl-resort-h3-1": "White Glove Delivery",
        "tmpl-resort-p4": "Airport reception, active RSVP, rooming list control, and custom welcome kits in every resort room.",
        "tmpl-resort-h3-2": "Plenary Management (A/V)",
        "tmpl-resort-p5": "Technical direction coordination, LED panels, crystal-clear audio, and rigorous content timeline (Run of Show).",
        "tmpl-resort-h2-2": "Plan your Convention at [VENUE_NAME]",
        "tmpl-resort-p6": "Contact us and discover how to optimize your budget. We deliver technical proposals in 48 hours.",
        "tmpl-resort-footer": "Union Mind acts as an independent corporate production agency and has no direct affiliation with the administration of [VENUE_NAME].",
        
        "faq-q-expo-1": "How much does a booth at [VENUE_NAME] cost?",
        "faq-a-expo-1": "The value of a booth varies according to square footage and project complexity. Smaller booths (up to 36m²) tend to have a higher cost per m², as certain operational assembly costs exist regardless of size. Larger booths dilute these costs and usually have a more efficient cost per m². Our Free Scoping Consultancy delivers an accurate technical quote in 48h — no commitment.",
        "faq-q-expo-2": "Who handles the CA (Approval Certificate) and credentials at [VENUE_NAME]?",
        "faq-a-expo-2": "Union Mind assumes all bureaucracy: project approval with the show promoter, RRT issuance, licenses, and team credentials. You just arrive to welcome clients.",
        "faq-q-expo-3": "Is it possible to build a booth at [VENUE_NAME] with less than 30 days notice?",
        "faq-a-expo-3": "Yes. We have assembly partners with immediate availability and operate on a Fast Track model for urgent projects. Contact us as soon as possible — projects with less than 2 weeks notice require a simplified scope.",
        
        "faq-q-resort-1": "How much does a convention at [VENUE_NAME] cost?",
        "faq-a-resort-1": "Investment varies according to the number of attendees, operation days, and production complexity (scenography, A/V, speakers). The Free Scoping Consultancy analyzes your needs and delivers a real, personalized investment range in 48h.",
        "faq-q-resort-2": "Does Union Mind handle transfers and lodging logistics at [VENUE_NAME]?",
        "faq-a-resort-2": "Yes. We manage the entire attendee journey: flights, transfers, rooming list, check-in, and welcome kits in rooms. You delegate the full operation and focus on the event content.",
        "faq-q-resort-3": "Does Union Mind provide technical direction for the plenary at [VENUE_NAME]?",
        "faq-a-resort-3": "Yes. We deliver everything from the sound and light technical rider to creating LED panels (KVs, animated PPTs) and full Stage Management (Run of Show).",
        
        "tmpl-btn-back": "→ Back to Home Page",
        "tmpl-btn-wa": "Talk to an Expert now",
    }
};
let localLang = 'pt';
function switchLanguage(lang) {
    localLang = lang;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (localTranslations[lang] && localTranslations[lang][key]) el.innerHTML = localTranslations[lang][key];
    });
    document.getElementById('btn-pt').classList.toggle('active', lang === 'pt');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');
    document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
}
document.addEventListener('DOMContentLoaded', () => switchLanguage('pt'));
</script>
"""

    def prepare_head(head_str, type_str):
        name_placeholder = '[BAIRRO_NOME]' if type_str == 'bairro' else '[VENUE_NAME]'
        
        head_str = re.sub(r'<title>.*?</title>', f'<title>Agência de Eventos Corporativos - {name_placeholder} | Union Mind</title>', head_str)
        head_str = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Planejamento e produção de eventos corporativos e confraternizações premium. Especialistas em {name_placeholder} - São Paulo. Time bilíngue. Consultoria gratuita em 48h.">', head_str)
        
        head_str = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head_str, flags=re.DOTALL)
        
        json_ld = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": ["ProfessionalService", "LocalBusiness"],
      "name": "Union Mind - Eventos em {name_placeholder}",
      "description": "Corporate events, conventions and trade show booths in {name_placeholder}, São Paulo. English-speaking team. Free scoping consultancy in 48h.",
      "url": "https://unionmind.solutions/espacos/[URL_SLUG].html",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "São Paulo",
        "addressRegion": "SP",
        "addressCountry": "BR"
      }},
      "sameAs": ["https://www.linkedin.com/company/unionmindsolutions"],
      "mainEntityOfPage": {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Quanto custa um evento em {name_placeholder}?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Eventos de 50 a 200 pessoas partem de R$ 40 mil em fee de gestão. A Union Mind oferece Consultoria de Escopo Gratuita com faixa de investimento em 48h."}}
          }},
          {{
            "@type": "Question",
            "name": "A Union Mind é uma agência bilíngue?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Sim. A Union Mind conta com equipe bilíngue (PT/EN) e atende empresas internacionais como Corporate DMC em São Paulo."}}
          }}
        ]
      }}
    }}
    </script>
        """
        head_str = head_str.replace('</head>', json_ld + '\n</head>')
        head_str = head_str.replace('href="assets/', 'href="../assets/')
        head_str = head_str.replace('src="assets/', 'src="../assets/')
        return head_str
        
    bairro_head = prepare_head(head_content, 'bairro')
    urbano_head = prepare_head(head_content, 'urbano')
    expo_head = prepare_head(head_content, 'expo')
    resort_head = prepare_head(head_content, 'resort')
    
    footer_content = footer_content.replace('href="assets/', 'href="../assets/')
    footer_content = footer_content.replace('src="assets/', 'src="../assets/')
    footer_content = footer_content.replace('href="espacos/', 'href="')
    # Append i18n script before </body>
    # Remove sticky CTA completely from generated landing pages
    footer_content = footer_content.replace(
        '<a href="#configurador" class="sticky-mobile-cta" id="sticky-cta-btn" data-i18n="sticky-cta">Pedir Or\u00e7amento (48h)</a>',
        ''
    )
    footer_content = footer_content.replace(
        '<a href="https://wa.me/5511947684604?text=Ol%C3%A1%2C%20vim%20pelo%20site%20da%20Union%20Mind%20e%20quero%20falar%20sobre%20um%20evento!" target="_blank" class="sticky-mobile-cta" id="sticky-cta-btn" data-i18n="sticky-cta">Falar com Especialista agora</a>',
        ''
    )
    footer_content = footer_content.replace('</body>', I18N_SCRIPT + '\n</body>')

    templates_dir = os.path.join(base_dir, 'templates')
    with open(os.path.join(templates_dir, 'template_bairro.html'), 'w', encoding='utf-8') as f:
        f.write(bairro_head + bairro_main + LOGO_STRIP + CASES_SECTION + faq_bairro + footer_content)
        
    with open(os.path.join(templates_dir, 'template_urbano.html'), 'w', encoding='utf-8') as f:
        f.write(urbano_head + urbano_main + LOGO_STRIP + CASES_SECTION + faq_urbano + footer_content)

    with open(os.path.join(templates_dir, 'template_expo.html'), 'w', encoding='utf-8') as f:
        f.write(expo_head + expo_main + LOGO_STRIP + CASES_SECTION + faq_expo + footer_content)

    with open(os.path.join(templates_dir, 'template_resort.html'), 'w', encoding='utf-8') as f:
        f.write(resort_head + resort_main + LOGO_STRIP + CASES_SECTION + faq_resort + footer_content)
        
    print("Todos os 4 templates V3 atualizados com Logo Strip, Cases, FAQ e i18n PT/EN.")

if __name__ == '__main__':
    create_templates()

