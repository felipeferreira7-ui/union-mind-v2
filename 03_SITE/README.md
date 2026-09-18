# Union Mind — manual do site

Atualizado em 18/09/2026. Site estático publicado no GitHub Pages em [unionmind.solutions](https://unionmind.solutions/). A fonte de verdade é esta pasta; o repositório público contém somente `03_SITE` e o workflow de publicação.

## Estado publicado

- 124 páginas públicas: português e inglês em URLs próprias, incluindo serviços, insights, espaços, dois cases anônimos e a página de captura.
- Captação: `/checklist-convencao.html` entrega o PDF `assets/downloads/checklist-convencao-corporativa-union-mind.pdf` após formulário aceito pelo Formspree `xzdawggb`.
- GA4 `G-WPW7PV9W54`: `generate_lead` só é enviado após aceite do Formspree e está marcado como evento principal. `whatsapp_click` mede somente a intenção de abrir conversa.
- O último teste real autorizado chegou ao Formspree e ao Outlook. As validações posteriores usam rede simulada; não repetir envio técnico sem necessidade.
- A auditoria final de 18/09 confirmou 124/124 URLs publicadas com HTTP 200, título, descrição e canônico corretos. A página de captura foi conferida visualmente em produção com rótulos, placeholders e contraste legíveis.

SEO técnico, GEO e medição estão implementados. Isso não garante indexação, posição ou novos contratos: acompanhar Search Console, consultas sem marca, leads aceitos e conversas qualificadas.

## Onde editar

- `index.html`: home em português. `index-v2.html` é uma cópia local com `noindex`, gerada para revisão.
- `labs.html`, `insights/*.html` e `servicos/*.html`: fontes em português com dicionários PT/EN. Não editar a cópia em `en/` diretamente.
- `checklist-convencao.html` e os dois cases de convenção possuem versão inglesa revisada manualmente em `en/`; preservar a equivalência das duas páginas ao editar.
- `templates/template_*.html`: fontes das páginas de espaços. Gerar novamente depois de qualquer alteração nelas.
- `scripts_build/space_directory.html`: fonte do diretório de espaços.
- `scripts/site-ui.js`: interação, idioma, contexto dos serviços, formulário e WhatsApp.
- `scripts/analytics.js`: implementação GA4. Não adicionar GTM ou outra tag GA4 em paralelo.
- `assets/`: apenas mídia usada pelo site. Manuais de marca, apresentações e documentos comerciais ficam fora desta pasta.

## Geração e verificação

Na pasta `03_SITE`, usar os runtimes configurados no workspace e executar:

```sh
python3 scripts_build/generate_seo.py
python3 scripts_build/build_languages.py
python3 scripts_build/check_site.py
node scripts_build/check_forms.js
node scripts_build/check_analytics.js
python3 scripts_build/prepare_public.py --output /tmp/union-public-review
```

`generate_seo.py` gera espaços e sitemap de base. `build_languages.py` gera os pares PT/EN, hreflang, canônicos, sitemap completo e quatro redirecionamentos estáticos. `prepare_public.py` exige um destino inexistente, evitando resíduos de builds antigos.

O pacote público inclui mídia de `assets/` e somente o PDF de `assets/downloads/`. Modelos, prévias, documentação, apresentações e manuais de marcas são excluídos. Nunca incluir OneDrive, propostas, credenciais ou a base interna de conhecimento.

## Idiomas, contato e dados

O idioma segue a URL e os controles navegam para o endereço equivalente. Todas as páginas indexáveis têm canônico próprio e `hreflang` recíproco. A 404 tem `noindex`.

Os formulários usam honeypot `_gotcha`. Em erro ou ausência de rede, os dados permanecem no formulário e nenhum evento de lead é enviado. O Analytics não envia nome, e-mail, empresa, mensagem, query string ou fragmento de URL. Google Signals e personalização de anúncios permanecem desativados.

Formspree não substitui CRM: registrar contatos respondidos, origem, adequação, proposta e fechamento em sistema comercial próprio. UTM e campanhas pagas exigem um plano de atribuição antes de investimento.

## Publicação

1. Rodar toda a geração e os verificadores acima.
2. Conferir `git diff`, principalmente ativos removidos ou alterações em páginas geradas.
3. Gerar o pacote em um diretório temporário e conferir que não há material interno.
4. Enviar ao repositório e aguardar o workflow GitHub Pages concluir.
5. Conferir URLs, formulário sem novo envio técnico, Analytics e Search Console conforme necessário.

Os quatro endereços legados (`/sobre-nos`, `/portfolio` e dois serviços antigos) usam meta refresh estático e canônico do destino; não são HTTP 301. Nove URLs antigas de cases seguem pendentes de decisão editorial e não devem ser redirecionadas para projetos não equivalentes.

## Limites e pendências conscientes

- Os cases não citam clientes, marcas, métricas ou resultados sem aprovação.
- As páginas de espaços são úteis como diretório, mas parte delas compartilha modelos; ampliar conteúdo específico só com pesquisa confirmada.
- Search Console pode levar tempo para reprocessar sitemap e indexar páginas. Acompanhar, não prometer ranking.
- Para reverter uma publicação, usar o histórico Git documentado em `05_KNOWLEDGE_BASE/migracao/CONTEXTO_ATUAL_20260917.md`.
