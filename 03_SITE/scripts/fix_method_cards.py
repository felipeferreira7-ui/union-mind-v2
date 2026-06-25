#!/usr/bin/env python3
"""
fix_method_cards.py
Replaces the old method card titles/texts in all espacos pages
with the approved LP content.
"""

import os
import glob
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ESPACOS = os.path.join(BASE, "espacos", "*.html")

# ── Old → New replacements (title and body text) ──────────────────────────
REPLACEMENTS = [
    # Card 1 title
    (
        r'(<h3[^>]*data-i18n="method-1-h3"[^>]*>).*?(</h3>)',
        r'\g<1>01. Entramos na sua rotina\2'
    ),
    # Card 1 body
    (
        r'(<p[^>]*data-i18n="method-1-p"[^>]*>).*?(</p>)',
        r'\g<1>Mergulhamos na cultura, nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade e foco total na experiência final.\2'
    ),
    # Card 2 title
    (
        r'(<h3[^>]*data-i18n="method-2-h3"[^>]*>).*?(</h3>)',
        r'\g<1>02. Você fala direto com quem faz\2'
    ),
    # Card 2 body
    (
        r'(<p[^>]*data-i18n="method-2-p"[^>]*>).*?(</p>)',
        r'\g<1>Sem camadas, sem atendimento que repassa para criação. Você tem acesso direto ao profissional que vai estar no venue no dia do evento.\2'
    ),
    # Card 3 title
    (
        r'(<h3[^>]*data-i18n="method-3-h3"[^>]*>).*?(</h3>)',
        r'\g<1>03. Detalhe não é opcional\2'
    ),
    # Card 3 body
    (
        r'(<p[^>]*data-i18n="method-3-p"[^>]*>).*?(</p>)',
        r'\g<1>Em eventos corporativos, o detalhe que falha é o que o dono do evento lembra. Cada elemento é verificado por quem assinou o briefing.\2'
    ),
    # Also update the translation strings in the JS block ──────────────────
    # method-1-h3 PT translation
    (
        r'"method-1-h3":\s*"[^"]*"',
        '"method-1-h3": "01. Entramos na sua rotina"'
    ),
    # method-1-p PT translation
    (
        r'"method-1-p":\s*"[^"]*"',
        '"method-1-p": "Mergulhamos na cultura, nos desafios e nas dores da sua marca. Construímos soluções a quatro mãos, com proximidade e foco total na experiência final."'
    ),
    # method-2-h3 PT translation
    (
        r'"method-2-h3":\s*"[^"]*"',
        '"method-2-h3": "02. Você fala direto com quem faz"'
    ),
    # method-2-p PT translation
    (
        r'"method-2-p":\s*"[^"]*"',
        '"method-2-p": "Sem camadas, sem atendimento que repassa para criação. Você tem acesso direto ao profissional que vai estar no venue no dia do evento."'
    ),
    # method-3-h3 PT translation
    (
        r'"method-3-h3":\s*"[^"]*"',
        '"method-3-h3": "03. Detalhe não é opcional"'
    ),
    # method-3-p PT translation
    (
        r'"method-3-p":\s*"[^"]*"',
        '"method-3-p": "Em eventos corporativos, o detalhe que falha é o que o dono do evento lembra. Cada elemento é verificado por quem assinou o briefing."'
    ),
]

files = glob.glob(ESPACOS)
updated = 0

print("═" * 52)
print("  Union Mind — Method Cards Updater")
print("═" * 52)

for path in sorted(files):
    name = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    for pattern, replacement in REPLACEMENTS:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Updated: espacos/{name}")
        updated += 1
    else:
        print(f"  ⚪ Skipped (no match): espacos/{name}")

print()
print(f"  Done: {updated} files updated")
print("═" * 52)
