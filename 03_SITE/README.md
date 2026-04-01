# Union Mind — Engenharia de Front-End

Este diretório contém a interface pública da Union Mind, otimizada para performance, SEO e conversão multi-idioma.

## 🏗️ Estrutura de Ativos (Assets)

> [!IMPORTANT]
> **Política de Assets:** Todos os arquivos de mídia (imagens, logotipos, favicons e backgrounds) devem estar localizados obrigatoriamente dentro de `03_SITE/assets/`. O uso de symlinks ou caminhos externos quebrará o deploy automático no GitHub Pages.

- `assets/cases/`: Imagens do portfólio (Danone, Natura, Auren, Diase).
- `assets/logos/`: Logotipos de clientes e favicon.
- `assets/hero/`: Backgrounds de alta resolução (incluindo o `hero-bg.webp` do Mac).

## 🚀 SEO Programático (pSEO)

Utilizamos um motor híbrido para gerar páginas de aterrizagem específicas para locais de eventos em escala:

1. **`generate_seo.py`**: Script Python que usa os arquivos `espacos/bourbon-atibaia-resort.html` (Categoria A - Resort) e `espacos/expo-center-norte.html` (Categoria B - Pavilhões) como templates mestres para gerar as 30 landing pages geográficas.
2. **`sitemap.xml`**: Gerado automaticamente pelo script de SEO para garantir que o Google indexe todas as variações de locais.

### Como gerar novas páginas:
1. Adicione o novo local no dicionário `venuesA` ou `venuesB` dentro do `generate_seo.py`.
2. Execute: `python3 generate_seo.py`.
3. Verifique a nova página na pasta `espacos/`.

## 🌍 Internacionalização (i18n)

O site é bilingue (PT/EN) sem necessidade de múltiplas pastas de idioma:
- **`generate_seo.js`**: Gerencia a troca de textos em tempo real usando o atributo `data-i18n` no HTML.
- **Dicionário:** Os conteúdos de tradução estão embarcados no final de cada arquivo HTML para garantir carregamento instantâneo.

## 🛠️ Manutenção
- **Favicon:** Definido como `assets/logos/favicon.png` em todas as páginas via tag `<link rel="icon">`.
- **Formulários:** Conectados via Formspree API.
- **Analytics:** Google Tag Manager integrado no `<head>`.
