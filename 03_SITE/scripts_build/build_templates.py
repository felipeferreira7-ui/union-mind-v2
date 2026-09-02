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
        "nav-cta": "Fale com um Especialista →",
        'cases-section-tag': '— CASES SELECIONADOS',
        'cases-section-title': 'Experiências Corporativas de<br><em>Alto Impacto.</em>',
        'cases-natura-meta': '3.000 consultoras · Show com Jorge &amp; Mateus + Chitãozinho &amp; Xororó',
        'cases-danone-meta': '600 líderes · Show com Maiara &amp; Maraisa',
        'cases-auren-meta': '600 convidados · Show com Ferrugem',
        'cases-diase-tag': 'Evento / Branding',
        'cases-diase-name': 'Nação Diase',
        'cases-diase-meta': '150 convidados · O Crescimento Continua',
        'cases-spark-tag': 'Ativação de Marca',
        'cases-spark-name': 'Spark &amp; Live Marketing',
        'cases-spark-meta': 'Brand experience · São Paulo',
        'cases-comgas-tag': 'Treinamento Corporativo',
        'cases-comgas-name': 'Semana de Segurança Comgás',
        'cases-comgas-meta': '4.000 pessoas · 4 dias · 7 ativações tecnológicas Union Labs',
        'founder-role': 'Fundador &amp; Diretor de Operações · Union Mind',
        'config-tag': '— CONSULTORIA GRATUITA',
        'config-h2-sub': 'em 48 horas.',
        'config-reassurance': '<p><strong>Sem compromisso.</strong> A análise inicial é gratuita.<br>Em 48h você recebe um diagnóstico de escopo e faixa de investimento. Para uma proposta detalhada com cronograma e operação completa, avançamos juntos na próxima etapa.</p>',
        'config-or': 'ou',
        'config-whatsapp': 'Falar no WhatsApp agora',
        'faq-section-tag': '— DÚVIDAS FREQUENTES',
        'footer-sub': 'BOUTIQUE SOUL · AI ENGINE',
        'footer-venues-title': 'Espaços Especializados',
        'footer-cnpj': 'Union Mind Eventos e Comunicação · CNPJ 21.024.508/0001-08',

        "nav-expertise": "Expertise", "nav-cases": "Cases", "nav-methodology": "Metodologia",
        "nav-labs": "Union Labs", "nav-cta": "Fale com um Especialista →",
        "hero-h2": "10 anos entregando convenções e feiras para as maiores marcas do Brasil. Sem intermediários. Sem surpresas.",
        "expertise-h2": "Seu projeto tem um dono: o mesmo profissional que leu o briefing estará no venue no dia do evento. Sem repasses. Sem surpresas.",
        "exp-1-h3": "Eventos Corporativos & Meetings",
        "exp-1-p": "Convenções de vendas, retiros de liderança, kick-offs estratégicos e formaturas corporativas. Time sênior dedicado do briefing ao encerramento.",
        "exp-2-h3": "Eventos de Marca & Sampling",
        "exp-2-p": "Lançamentos de produto, ativações de PR, brand spaces e operações de sampling com resultado mensurável e rastreável.",
        "exp-3-h3": "Estandes & Cenografia Flex",
        "exp-3-p": "Arquitetura promocional projetada para maximizar fluxo, captura de leads e ROI nas principais feiras de São Paulo.",
        "exp-4-h3": "IA Engine — processo, não promessa",
        "exp-4-p": "Nossa engine operacional reduz o tempo de escopo de 48h para 4h. Você recebe proposta técnica com cronograma e faixa de investimento em menos de 48 horas.",
        "fairs-h2": "Feiras em SP:",
        "method-intro": "Não queremos ser a maior fábrica de eventos. Queremos ser a melhor parceira estratégica do seu negócio.",
        "method-1-h3": "Entramos na sua rotina",
        "method-1-p": "Entramos fundo nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade e foco total na experiência final.",
        "method-2-h3": "Você fala direto com quem faz",
        "method-2-p": "Sem camadas, sem atendimento que repassa para criação. Você tem acesso direto ao profissional que vai estar no venue no dia do evento.",
        "method-3-h3": "Detalhe não é opcional",
        "method-3-p": "Em eventos corporativos, o detalhe que falha é o que o dono do evento lembra. Cada elemento é verificado por quem assinou o briefing.",
        "case-1-tag": "Evento / Branding", "case-2-tag": "Convenção de Vendas",
        "case-3-tag": "Convenção da Marca", "case-4-tag": "Convenção Internacional",
        "cases-section-tag": "— CASES SELECIONADOS",
        "cases-section-title": "O que produzimos gera<br><em>Alto Impacto.</em>",
        "cases-see-all": "Cada projeto é um capítulo →",
        "case-meta-1": "Maior convenção de vendas do ano (3.000+ pax) com complexidade cenográfica e show de grande porte.",
        "case-meta-2": "Convenção de Liderança (600 pax) focada em alinhamento estratégico e reforço cultural.",
        "case-meta-3": "Integração pós-M&A com foco em endomarketing e unificação de cultura (600 pax).",
        "case-meta-4": "Convenção imersiva de alta gestão para fortalecimento de visão de futuro.",
        "case-meta-5": "Ativação de PR e relacionamento focada em geração de leads e earned media.",

        "config-h2": "Consultoria de Escopo",
        "config-p": "Você recebe o diagnóstico operacional completo em 48h, com mapeamento de logística e faixa de investimento, pronto para aprovar com sua diretoria sem dores de cabeça.",
        "config-label-1": "01. Nome da Feira / Local do Evento",
        "config-label-2": "02. Empresa",
        "config-label-3": "03. O que você precisa? (Sua Dor)",
        "config-label-4": "04. Seu E-mail Corporativo",
        "config-opt-1-1": "Impulsionar Vendas e Performance",
        "config-opt-1-2": "Branding e Posicionamento",
        "config-opt-1-3": "Engajamento e Cultura Interna",
        "config-opt-1-4": "Inovação e Lançamento",
        "config-opt-2-1": "Alta Liderança (C-Level / VIP)",
        "config-opt-2-2": "Convenção de Grande Porte (+1000 pax)",
        "config-opt-2-3": "Ativação de Marca / Público Final",
        "config-opt-2-4": "Evento Híbrido / Digital Experience",
        "config-opt-3-1": "Fast Track (menos de 30 dias)",
        "config-opt-3-2": "Standard (30 a 90 dias)",
        "config-opt-3-3": "White Glove (Produção Premium)",
        "config-submit": "Receber Proposta em 48h",
        "faq-title": "Perguntas <em>Frequentes</em>",
        "faq-q1": "O que é uma agência boutique de eventos corporativos?",
        "faq-a1": "Uma agência boutique de eventos corporativos é uma empresa com time sênior reduzido que atende poucos clientes simultaneamente, garantindo que o mesmo profissional que participa do briefing acompanhe toda a execução. A Union Mind, com 10 anos de mercado em São Paulo, opera nesse modelo: sem camadas de atendimento, sem terceirização da operação.",
        "faq-q2": "Qual a diferença entre uma agência boutique e uma agência grande?",
        "faq-a2": "Na agência grande, o briefing é feito por um diretor e a execução é delegada a equipes rotativas. Na Union Mind, o diretor de operações acompanha pessoalmente cada projeto. Isso reduz falhas de comunicação e garante accountability direta sobre o resultado.",
        "faq-q3": "Quanto custa contratar uma agência de eventos em São Paulo?",
        "faq-a3": "O investimento varia conforme o formato, número de participantes e nível de produção. A Union Mind oferece uma Consultoria de Escopo gratuita para diagnosticar tecnicamente o projeto e apresentar uma proposta personalizada em 48h.",
        "faq-q4": "Quais feiras em São Paulo a Union Mind atende em 2026?",
        "faq-a4": "A Union Mind projeta e executa estandes e ativações nas principais feiras de São Paulo em 2026, incluindo APAS Show, Automec, Expo Revestir, Feicon, Hospitalar, VTEX Day, Conarh, Intermodal, Futurecom e Equipotel, entre outras.",
        "faq-q8": "Preciso cotar um evento. Quais informações a agência precisa?",
        "faq-a8": "Para sermos rápidos (entregamos orçamentos em no mínimo 48h), precisamos de um briefing básico: objetivo do evento, data, local, estimativa de público e orçamento teto. Não sabe por onde começar? Nós fazemos uma rápida call de alinhamento.",
        "faq-q9": "A Union Mind cuida do evento de ponta a ponta?",
        "faq-a9": "Cuidamos de 100% da operação no modelo One-Stop-Shop (Turnkey) — desde o conceito criativo e montagem cenográfica até A&B e credenciamento. Se você prefere manter algum fornecedor de confiança, nós entramos na gestão técnica integrada.",
        "faq-q11": "Quem vai liderar a operação no dia do meu evento?",
        "faq-a11": "Na Union Mind, todo projeto possui um líder dedicado que acompanha sua marca desde a primeira reunião de briefing até a entrega final no local.",
        "alert-success": "Recebemos sua solicitação! Um de nossos especialistas entrará em contato em até 48h com a proposta personalizada.",
        "btn-processing": "ENVIANDO...", "btn-received": "SOLICITAÇÃO RECEBIDA",
        "hero-cta-btn": "Consultoria de Escopo Gratuita",
        "hero-tag": "AGÊNCIA BOUTIQUE DE EVENTOS CORPORATIVOS",
        "hero-h1": "<span class='accent-line'>Agência Boutique</span><span class='accent-line'>de Live Marketing.</span>",
        "hero-btn-cases": "Ver Cases ↓",
        "hero-services": "<span class='hero-pill'>Convenções</span><span class='hero-pill'>Meetings</span><span class='hero-pill'>Mini Meetings</span><span class='hero-pill'>Lançamento de Produtos</span><span class='hero-pill'>Estandes</span><span class='hero-pill'>Feiras de Negócios</span><span class='hero-pill'>Ativações</span><span class='hero-pill'>Sampling</span><span class='hero-pill'>Kick-offs</span><span class='hero-pill'>Festas de Encerramento</span>",
        "stat-1": "Anos entregando projetos no Brasil e na América Latina",
        "stat-2": "Projetos corporativos entregues para marcas líderes",
        "stat-3": "Ponto de contato — do briefing ao palco. Sempre.",
        "logo-strip-label": "Atendemos",
        "expertise-tag": "— O QUE FAZEMOS",
        "expertise-headline": "Expertise dedicada,<br>em cada detalhe.",
        "founder-label": "— FUNDADOR",
        "testimonial-quote": "A Union Mind nasceu de um princípio simples: a união de mentes em prol de um resultado. O mercado de live marketing costuma entregar uma verdadeira bagunça operacional, onde o cliente se perde em meio a intermediários. Nós escolhemos ser uma agência boutique porque acreditamos no cuidado especial, com um time sênior debruçado sobre cada detalhe.<br><br>Nosso foco é a eficiência de custos — que não significa necessariamente fazer o mais barato, mas ter a inteligência de saber exatamente onde investir a verba do cliente para gerar o maior impacto. Entregamos criatividade, mas com a segurança de quem tem o controle absoluto da execução.",
        "method-tag": "— COMO TRABALHAMOS",
        "method-headline": "Boutique<br>por escolha.",
        "method-intro-sub": "Entramos fundo na operação da sua marca para construir convenções e estandes com criatividade e foco no resultado do seu negócio.",
        "sticky-cta": "Pedir Orçamento (48h)",
        "config-tag": "— CONSULTORIA GRATUITA"},
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
        "tmpl-btn-wa": "Talk to an Expert now",,
        'cases-section-tag': '— SELECTED CASES',
        'cases-section-title': 'High-Impact Corporate<br><em>Experiences.</em>',
        'cases-natura-meta': '3,000 consultants · Major national country music show',
        'cases-danone-meta': '600 leaders · Country music concert',
        'cases-auren-meta': '600 guests · Private concert',
        'cases-diase-tag': 'Event / Branding',
        'cases-diase-name': 'Diase Nation',
        'cases-diase-meta': '150 guests · The Growth Continues',
        'cases-spark-tag': 'Brand Activation',
        'cases-spark-name': 'Spark &amp; Live Marketing',
        'cases-spark-meta': 'Brand experience · São Paulo',
        'cases-comgas-tag': 'Corporate Training',
        'cases-comgas-name': 'Comgás Safety Week',
        'cases-comgas-meta': '4,000 people · 4 days · 7 tech activations by Union Labs',
        'founder-role': 'Founder &amp; COO · Union Mind',
        'config-tag': '— FREE CONSULTATION',
        'config-h2-sub': 'in 48 hours.',
        'config-reassurance': '<p><strong>No commitment.</strong> The initial analysis is free.<br>In 48h you receive a scope diagnosis and investment range. For a detailed proposal with timeline and full operation, we move forward together to the next stage.</p>',
        'config-or': 'or',
        'config-whatsapp': 'Talk on WhatsApp now',
        'faq-section-tag': '— FREQUENTLY ASKED QUESTIONS',
        'footer-sub': 'BOUTIQUE SOUL · AI ENGINE',
        'footer-venues-title': 'Specialized Venues',
        'footer-cnpj': 'Union Mind Events &amp; Communication · CNPJ 21.024.508/0001-08',

        "nav-expertise": "Expertise", "nav-cases": "Cases", "nav-methodology": "Methodology",
        "nav-labs": "Union Labs", "nav-cta": "Talk to an Expert →",
        "hero-tag": "BOUTIQUE CORPORATE EVENTS AGENCY · DMC BRAZIL",
        "hero-h1": "<span class='accent-line'>Brazil DMC & Local</span><span class='accent-line'>Event Producer.</span>",
        "hero-h2": "English-speaking team. 10 years delivering corporate events and trade shows for Brazil's top brands. Single point of contact. No budget surprises.",
        "sticky-cta": "Get a Quote (48h)",
        "hero-btn-cases": "See Cases ↓",
        "hero-services": "<span class='hero-pill'>Conventions</span><span class='hero-pill'>Meetings</span><span class='hero-pill'>Mini Meetings</span><span class='hero-pill'>Product Launches</span><span class='hero-pill'>Trade Booths</span><span class='hero-pill'>Trade Shows</span><span class='hero-pill'>Activations</span><span class='hero-pill'>Sampling</span><span class='hero-pill'>Kick-offs</span><span class='hero-pill'>Closing Events</span>",
        "stat-1": "Years delivering projects across Brazil and Latin America",
        "stat-2": "Corporate projects delivered for market-leading brands",
        "stat-3": "Single point of contact — from briefing to stage. Always.",
        "logo-strip-label": "We serve",
        "expertise-tag": "— WHAT WE DO",
        "expertise-headline": "Dedicated expertise,<br>in every detail.",
        "expertise-h2": "Your project has one owner: the same professional who read the brief will be at the venue on event day. No hand-offs. No surprises.",
        "exp-1-h3": "Corporate Events & Meetings", "exp-1-p": "Sales conventions, leadership retreats, strategic kick-offs and corporate graduations. Senior team from briefing to closing.",
        "exp-2-h3": "Brand Events & Sampling", "exp-2-p": "Product launches, PR activations, brand spaces and sampling operations with measurable, trackable results.",
        "exp-3-h3": "Booths & Flex Scenography", "exp-3-p": "Promotional architecture designed to maximize flow, lead capture and ROI at São Paulo's major trade shows.",
        "exp-4-h3": "AI Engine — process, not promise", "exp-4-p": "Our operational engine reduces scoping time from 48h to 4h. You receive a full technical proposal with timeline and investment range in under 48 hours.",
        "fairs-h2": "Trade Shows in SP:",
        "case-1-tag": "Event / Branding", "case-2-tag": "Sales Convention", "case-3-tag": "Brand Convention", "case-4-tag": "International Convention",
        "cases-section-tag": "— SELECTED CASES",
        "cases-section-title": "What we produce generates<br><em>High Impact.</em>",
        "cases-see-all": "Every project is a chapter →",
        "case-meta-1": "Largest sales convention of the year (3,000+ pax) with complex scenography and large-scale entertainment.",
        "case-meta-2": "Leadership Convention (600 pax) focused on strategic alignment and cultural reinforcement.",
        "case-meta-3": "Post-M&A integration focused on internal marketing and cultural unification (600 pax).",
        "case-meta-4": "Immersive top-management convention to strengthen future vision.",
        "case-meta-5": "PR and relationship activation focused on lead generation and earned media.",

        "founder-label": "— FOUNDER",
        "testimonial-quote": "Union Mind was born from a simple principle: uniting minds for a result. The live marketing market often delivers true operational chaos, where the client gets lost among intermediaries. We chose to be a boutique agency because we believe in special care, with a senior team focused on every detail.<br><br>Our focus is cost efficiency — which doesn't necessarily mean doing it cheaper, but having the intelligence to know exactly where to invest the client's budget to generate the greatest impact. We deliver creativity, but with the security of those who have absolute control of execution.",
        "method-tag": "— HOW WE WORK",
        "method-headline": "Boutique<br>by choice.",
        "method-intro": "We don't want to be the biggest event factory. We want to be the best strategic partner for your business.",
        "method-intro-sub": "We embed ourselves in your brand's operation to build conventions and booths with creativity and a focus on your business results.",
        "method-1-h3": "We enter your daily routine", "method-1-p": "We embed ourselves in your brand's challenges and pain points. We co-create solutions with absolute proximity and an uncompromising focus on the final experience.",
        "method-2-h3": "You talk directly to the doer", "method-2-p": "No layers, no account manager relaying to production. You have direct access to the professional who will be at the venue on event day.",
        "method-3-h3": "Detail is not optional", "method-3-p": "In corporate events, the failing detail is the one the event owner remembers. Every element is verified by the person who signed the brief.",
        "config-tag": "— FREE CONSULTANCY",
        "config-h2": "Scoping Consultancy", "config-p": "You receive a complete operational diagnostic in 48h, with logistics mapping and investment range, ready to approve with your board without headaches.",
        "config-label-1": "01. Exhibition Name / Event Venue", 
        "config-label-2": "02. Company",
        "config-label-3": "03. Describe the event or challenge", 
        "config-label-4": "04. Corporate Email",
        "config-opt-1-1": "Boost Sales and Performance", "config-opt-1-2": "Branding and Market Positioning",
        "config-opt-1-3": "Engagement and Internal Culture", "config-opt-1-4": "Innovation and Launch",
        "config-opt-2-1": "Senior Leadership (C-Level / VIP)", "config-opt-2-2": "High-Scale Convention (+1000 pax)",
        "config-opt-2-3": "Brand Activation / Final Audience", "config-opt-2-4": "Hybrid Event / Digital Experience",
        "config-opt-3-1": "Fast Track (< 30 days)", "config-opt-3-2": "Standard (30 to 90 days)",
        "config-opt-3-3": "White Glove (Premium Production)",
        "config-submit": "Get Proposal in 48h",
        "faq-title": "Frequently Asked <em>Questions</em>",
        "faq-q1": "What is a boutique corporate events agency?", "faq-a1": "A boutique corporate events agency has a small senior team that serves few clients simultaneously, ensuring the same professional who attends the briefing oversees the entire execution. Union Mind, with 10 years in São Paulo, operates this way: no service layers, no operational outsourcing.",
        "faq-q2": "What is the difference between a boutique and a large agency?", "faq-a2": "In large agencies, the briefing director delegates execution to rotating teams. At Union Mind, the operations director personally oversees every project, reducing miscommunication and guaranteeing direct accountability.",
        "faq-q3": "How much does a corporate events agency in São Paulo cost?", "faq-a3": "Investment varies by format, number of participants and production level. As a reference: events for 50–200 people typically start from R$ 40,000 in management fee; trade show booths from R$ 15,000. Union Mind offers a free Scoping Consultancy — you receive a real investment range within 48h, no commitment required.",
        "faq-q4": "Which São Paulo trade shows does Union Mind cover in 2026?", "faq-a4": "Union Mind designs and executes booths and activations at São Paulo's main 2026 trade shows including APAS Show, Automec, Expo Revestir, Feicon, Hospitalar, VTEX Day, Conarh, Intermodal, Futurecom and Equipotel.",
        "faq-q8": "I need a quote. What information does the agency need?", "faq-a8": "To be fast (quotes in minimum 48h), we need a basic brief: event objective, date, venue, estimated attendance and budget ceiling. Don't know where to start? We do a quick alignment call.",
        "faq-q9": "Does Union Mind handle the event end-to-end?", "faq-a9": "We handle 100% of operations in a One-Stop-Shop model — from creative concept and scenic assembly to F&B and accreditation. If you prefer to keep a trusted supplier, we step in for integrated technical management.",
        "faq-q11": "Who will lead operations on my event day?", "faq-a11": "Every Union Mind project has a dedicated leader following your brand from the first briefing to final delivery on-site. This unified leadership coordinates all operational demands without miscommunication.",
        "alert-success": "Request received! One of our specialists will contact you within 48h with a personalized proposal.",
        "btn-processing": "SENDING...", "btn-received": "REQUEST RECEIVED",
        "hero-cta-btn": "Free Scoping Consultancy",
        "faq-q1": "What is a boutique corporate events agency?", "faq-a1": "A boutique corporate events agency has a small senior team that serves few clients simultaneously, ensuring the same professional who attends the briefing oversees the entire execution. Union Mind, with 10 years in São Paulo, operates this way: no service layers, no operational outsourcing.",
        "faq-q2": "What is the difference between a boutique and a large agency?", "faq-a2": "In large agencies, the briefing director delegates execution to rotating teams. At Union Mind, the operations director personally oversees every project, reducing miscommunication and guaranteeing direct accountability."}
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
    
    const venueNameMatch = document.title.split(' - ')[1];
    const venueName = venueNameMatch ? venueNameMatch.split(' |')[0] : '';
    
    document.title = (lang === 'pt') 
        ? `Agência de Eventos Corporativos - ${venueName} | Union Mind`
        : `Corporate Event Agency - ${venueName} | Union Mind DMC`;
        
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) {
        metaDesc.content = lang === 'pt'
            ? `Planejamento e produção de eventos corporativos e confraternizações premium. Especialistas em ${venueName} - São Paulo. Time bilíngue. Consultoria gratuita em 48h.`
            : `Planning and production of corporate events and premium gatherings. Experts at ${venueName} - São Paulo. English-speaking team. Free consultancy in 48h.`;
    }
    
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
        head_str = head_str.replace('href="style-v2.css"', 'href="../style-v2.css"')
        return head_str
        
    bairro_head = prepare_head(head_content, 'bairro')
    urbano_head = prepare_head(head_content, 'urbano')
    expo_head = prepare_head(head_content, 'expo')
    resort_head = prepare_head(head_content, 'resort')
    
    footer_content = footer_content.replace('href="assets/', 'href="../assets/')
    footer_content = footer_content.replace('src="assets/', 'src="../assets/')
    footer_content = footer_content.replace('href="espacos/', 'href="')
    
    # CRITICAL: Remove the index.html main script block (translations + switchLanguage + form handler)
    # from the footer content. The templates have their own I18N_SCRIPT injected below.
    footer_content = re.sub(r'<script>\s*\nconst translations = \{.*?</script>', '', footer_content, flags=re.DOTALL)
    
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

