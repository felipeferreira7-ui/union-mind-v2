# Union Mind — site

Site estático no GitHub Pages, a partir de `main`. Alterações locais não mudam o site público até o envio e a execução do deploy. A preparação de 17/09/2026 ainda não foi publicada.

## Fontes e geração

- `index.html`: home. `index-v2.html` e `index-v2-preview.html` são cópias de revisão, sincronizadas pelo gerador, com `noindex` e excluídas do pacote.
- `labs.html`, `insights/*.html`, `servicos/*.html`: fontes editoriais portuguesas com dicionários PT/EN. Os quatro serviços são eventos corporativos, convenções de vendas, ativações de marca e estandes/cenografia.
- `templates/template_*.html`: fontes das quatro categorias de espaços. Editar antes de regenerar as 46 páginas.
- `scripts_build/space_directory.html`: fonte do diretório. Preservar `category-0` a `category-3`, usadas nas seções inseridas.
- `scripts_build/generate_seo.py`: gera espaços, diretório e o sitemap português de base.
- `scripts_build/build_languages.py`: gera inglês estático, canônicos/hreflang recíprocos, sitemap completo de 118 URLs, quatro encaminhamentos antigos e sincroniza as prévias.
- `scripts/site-ui.js`: idioma por URL, campos, contexto do serviço, eventos de contato, WhatsApp e acessibilidade.
- `scripts/analytics.js`: GA4 `G-WPW7PV9W54`, conferido no painel da Union. Carrega apenas no domínio público. Eventos não incluem nomes, e-mails, empresas, mensagens ou parâmetros completos da URL.
- `generate_seo.js`: compatibilidade com o gerador Python. Para preparar publicação, executar também o gerador de idiomas.
- `build_templates.py` e `generate_lang_templates.py`: bootstrap histórico desativado para evitar sobrescritas.

Da pasta `03_SITE`, executar nesta ordem:

```sh
python3 scripts_build/generate_seo.py
python3 scripts_build/build_languages.py
python3 scripts_build/check_site.py
node scripts_build/check_forms.js
node scripts_build/check_analytics.js
python3 scripts_build/prepare_public.py --output /tmp/union-public-review
```

Python 3 e Node.js são suficientes, sem pacotes adicionais. `UNION_NODE` define o executável Node para o verificador; `UNION_PYTHON` define o Python da entrada JavaScript.

## Idiomas

São 59 páginas portuguesas e 59 inglesas em `/en/`. Conteúdo, título e descrição já estão no HTML de cada idioma; cada página tem canônico próprio e hreflang recíproco. Alterar os dois dicionários juntos nas fontes portuguesas e gerar novamente. Não editar cópias inglesas diretamente.

O idioma segue a URL, e os controles navegam para a página equivalente. Não depende da preferência de uma sessão anterior. A 404 mantém tradução dinâmica e `noindex`.

## Contatos e medição

Home e Labs usam o Formspree `xzdawggb`, com contexto de serviço e idioma. Há campo `_gotcha` invisível para filtragem adicional de spam. Sucesso só aparece após resposta aceita; falha conserva os dados e permite tentar novamente.

`generate_lead` só ocorre após envio aceito. `whatsapp_click` mede intenção de contato, sem representar conversa realizada, lead qualificado ou venda. O GA4 usa uma única implementação direta, substituindo o contêiner legado GTM que não estava acessível na conta auditada. Não instalar outra tag GA4 no GTM em paralelo: isso pode duplicar eventos. Clarity foi preservado.

A implementação exclui prévias locais do GA4 e remove consulta/fragmento do endereço e consulta do referenciador. Personalização de anúncios e Google Signals ficam desativados. A coleta real, classificação de eventos e origem dos contatos precisam ser conferidas no painel após publicação. Campanhas pagas exigem definição e validação próprias de atribuição; não estão configuradas nesta etapa.

## Pacote e publicação

O workflow gera páginas e idiomas, verifica site/formulários/Analytics com rede simulada, monta `_site_public` e publica somente esse pacote. Exclui modelos, prévias, manutenção, apresentações e documentos internos. Em `assets`, inclui apenas extensões de mídia; PDFs de manuais de marca ficam fora. O destino deve ser inexistente para impedir resíduos de builds anteriores.

Nunca incluir OneDrive, propostas, credenciais ou a base interna de conhecimento no repositório/pacote público. Confirmar acesso de escrita antes do envio ao GitHub.

Quatro endereços antigos possuem destino equivalente: `/sobre-nos`, `/portfolio`, `/servicos/organizacao-de-eventos` e `/servicos/cenografia-e-estandes`. O encaminhamento usa meta refresh imediato, alternativa estática do GitHub Pages; fontes ficam fora do sitemap. Se houver infraestrutura com regras HTTP, preferir 301/308. Endereços de cases antigos dependem de revisão editorial; não foram direcionados para projetos diferentes.

## Validação de 17/09/2026

- 118 URLs: links/âncoras locais, ativos HTML, canônicos, hreflang recíproco, JSON-LD e sintaxe JavaScript verificados.
- Build completo repetido produziu os mesmos arquivos; HTML inicial corresponde ao dicionário de cada idioma.
- 118 páginas em celular de 390 px: sem excesso de largura, imagens quebradas ou títulos principais ausentes.
- Doze cenários de formulário: PT/EN × sucesso/falha HTTP/offline, incluindo evento de lead somente no sucesso, com rede simulada.
- Analytics verificado com DOM/rede simulados: destino, uma visualização por página, exclusão local e remoção de parâmetros privados.
- Nenhum formulário real enviado nesta preparação. Recebimento da versão nova e coleta em produção ainda precisam de validação.

O editorial prioriza serviços, liderança próxima e fotos do portfólio. Cases continuam resumidos, por decisão de Felipe. O retrato preto e branco foi editado com IA a partir da foto original preservada; não é uma nova sessão fotográfica. Tipografia Barlow com destaques Instrument Serif.

SEO de aquisição exige acompanhamento: as 46 páginas de espaços ainda compartilham quatro modelos e precisam de conteúdo específico verificado. Links corretos não garantem indexação, ranking ou clientes. Papel/resultados detalhados dos cases e fotos com melhor procedência permanecem para revisão futura.
