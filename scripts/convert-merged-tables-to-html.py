#!/usr/bin/env python3
"""
Converte blocos de tabela com células mescladas (grid tables do remark-grid-tables)
em HTML <table> simples, usando o output de build em public/ como fonte da verdade.

Uso: python3 scripts/convert-merged-tables-to-html.py

Contexto: etapa 1 da migração Gatsby -> Docusaurus. Docusaurus/MDX v3 não possui
substituto mantido para remark-grid-tables. Tabelas sem mesclagem ficarão para
uma conversão posterior para pipe tables GFM.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
PUBLIC = os.path.join(ROOT, 'public')

EDITOR_COMMENT = """<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->"""

GRID_FENCE_RE = re.compile(r'^\+[-=+]+\+\s*$')
TABLE_RE = re.compile(r'<table[^>]*>.*?</table>', re.DOTALL)
MERGE_RE = re.compile(r'(?:colspan|rowspan)="(?:[2-9]|[1-9][0-9]+)"')


def src_to_public(src_path: str) -> str:
    rel = os.path.relpath(src_path, CONTENT)
    assert rel.endswith('.md'), rel
    rel = rel[:-3]
    if rel == 'index':
        return os.path.join(PUBLIC, 'index.html')
    return os.path.join(PUBLIC, rel, 'index.html')


def find_grid_blocks(lines):
    """Return list of (start, end) line indices (inclusive) of grid-table blocks."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        if GRID_FENCE_RE.match(lines[i]):
            start = i
            i += 1
            while i < n and (lines[i].startswith('+') or lines[i].startswith('|')):
                i += 1
            blocks.append((start, i - 1))
        else:
            i += 1
    return blocks


def has_real_merge(table_html: str) -> bool:
    return bool(MERGE_RE.search(table_html))


def clean_table(table_html: str) -> str:
    """Clean Gatsby-rendered <table> into a compact, hand-editable HTML block."""
    t = table_html

    # Drop no-op span attributes.
    t = re.sub(r'\s+colspan="1"', '', t)
    t = re.sub(r'\s+rowspan="1"', '', t)

    # Walk each cell (td/th) individually. The body pattern is non-recursive:
    # it explicitly refuses to cross <td>/<th> boundaries, so nothing can leak
    # from one cell into the next (a mistake an unanchored non-greedy regex
    # would make when a cell body contains trailing content after a wrapped
    # paragraph, e.g. `<p class="paragraph">x</p><br/>y`).
    cell_re = re.compile(
        r'<(td|th)([^>]*)>'
        r'((?:(?!</?(?:td|th)\b).)*?)'
        r'</\1>',
        re.DOTALL,
    )
    wrapper_re = re.compile(
        r'\A\s*<p class="paragraph">(.*)</p>\s*\Z',
        re.DOTALL,
    )

    def process_cell(match):
        tag = match.group(1)
        attrs = match.group(2)
        body = match.group(3)
        # Unwrap only when the paragraph wrapper is the entire cell body.
        wrap = wrapper_re.match(body)
        if wrap:
            body = wrap.group(1).strip()
        # For cells where additional content follows (e.g. `<br/>more text`),
        # drop only the class attribute so the <p> survives as neutral markup.
        body = body.replace(' class="paragraph"', '')
        return f'<{tag}{attrs}>{body}</{tag}>'

    t = cell_re.sub(process_cell, t)

    # MDX v1 artifact: literal "<!-- -->" comments injected to break character
    # fusion (e.g. "*<!-- --> "). Drop them; MDX v3 doesn't need them.
    t = t.replace('<!-- -->', '')

    # Collapse any in-cell newlines into single spaces so the final pretty-print
    # can insert its own newlines deterministically.
    t = re.sub(r'\s*\n\s*', ' ', t)

    # Pretty-print: one element per line. We insert newlines around block-level
    # table tags only.
    t = re.sub(r'<(table|thead|tbody|tfoot)(\s[^>]*)?>', lambda m: '\n' + m.group(0) + '\n', t)
    t = re.sub(r'</(table|thead|tbody|tfoot)>', lambda m: '\n' + m.group(0) + '\n', t)
    t = re.sub(r'<tr(\s[^>]*)?>', lambda m: '\n' + m.group(0) + '\n', t)
    t = re.sub(r'</tr>', '\n</tr>', t)
    t = re.sub(r'<(td|th)(\s[^>]*)?>', lambda m: '\n' + m.group(0), t)

    # Tidy: collapse 3+ newlines to 2, strip trailing spaces, trim.
    t = re.sub(r'\n{2,}', '\n', t)
    t = '\n'.join(line.rstrip() for line in t.splitlines() if line.strip())
    return t.strip()


def convert_file(src_path: str):
    text = open(src_path, encoding='utf-8').read()
    lines = text.splitlines()
    blocks = find_grid_blocks(lines)
    if not blocks:
        return 0

    pub_path = src_to_public(src_path)
    if not os.path.exists(pub_path):
        print(f'  SKIP (no build output): {src_path}', file=sys.stderr)
        return 0

    html = open(pub_path, encoding='utf-8').read()
    rendered = TABLE_RE.findall(html)
    if len(rendered) != len(blocks):
        print(
            f'  WARN mismatched table counts: {src_path} '
            f'(source={len(blocks)} rendered={len(rendered)})',
            file=sys.stderr,
        )
        return 0

    replaced = 0
    # Walk blocks in reverse so line indices stay valid across replacements.
    for (start, end), table_html in reversed(list(zip(blocks, rendered))):
        if not has_real_merge(table_html):
            continue
        cleaned = clean_table(table_html)
        replacement = EDITOR_COMMENT + '\n' + cleaned
        lines[start:end + 1] = replacement.splitlines()
        replaced += 1

    if replaced:
        new_text = '\n'.join(lines)
        if text.endswith('\n') and not new_text.endswith('\n'):
            new_text += '\n'
        open(src_path, 'w', encoding='utf-8').write(new_text)
    return replaced


def main():
    total_files = 0
    total_tables = 0
    for dirpath, _, filenames in os.walk(CONTENT):
        for f in filenames:
            if not f.endswith('.md'):
                continue
            path = os.path.join(dirpath, f)
            count = convert_file(path)
            if count:
                total_files += 1
                total_tables += count
                rel = os.path.relpath(path, ROOT)
                print(f'  {rel}: replaced {count} table(s)')
    print(f'\nDone. {total_tables} tables converted across {total_files} files.')


if __name__ == '__main__':
    main()
