#!/usr/bin/env python3
"""
Converte blocos de grid-table restantes (sem células mescladas) em GFM pipe tables.

Uso: python3 scripts/convert-grid-tables-to-gfm.py

Contexto: etapa 1 da migração Gatsby -> Docusaurus. Após a conversão das tabelas
com células mescladas (scripts/convert-merged-tables-to-html.py), restam tabelas
simples (1 linha por célula, sem merge). GFM pipe tables lidam perfeitamente
com elas, e eliminam a dependência em remark-grid-tables.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')

GRID_FENCE_RE = re.compile(r'^\+[-=+]+\+\s*$')
HEADER_FENCE_RE = re.compile(r'^\+[=+]+\+\s*$')


def find_grid_blocks(lines):
    """Return list of (start, end) inclusive line indices of grid-table blocks."""
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


def fence_positions(fence_line):
    """Return list of column positions from a `+---+---+` fence line."""
    return [i for i, ch in enumerate(fence_line) if ch == '+']


def split_cells(row_line, positions):
    """Slice a |...|...| row into cells using fence-derived column positions."""
    cells = []
    for i in range(len(positions) - 1):
        start = positions[i] + 1  # skip the '|'
        end = positions[i + 1]
        # If the row is shorter than the fence (trailing whitespace stripped),
        # pad with empty.
        cell = row_line[start:end] if start < len(row_line) else ''
        cells.append(cell.strip())
    return cells


def escape_cell(text):
    """Escape pipe-table-hostile characters inside a cell."""
    # Pipes inside cells must be escaped as \|.
    text = text.replace('|', r'\|')
    # Replace &ndash; / &mdash; named entities with literal characters so the
    # resulting markdown matches how Gatsby rendered them.
    text = text.replace('&ndash;', '–').replace('&mdash;', '—')
    return text


def parse_grid_block(lines):
    """Parse grid-table lines into (header_row, body_rows)."""
    # The first fence line is authoritative for column positions; subsequent
    # fence lines in the same block re-use the same column layout.
    positions = None
    for line in lines:
        if GRID_FENCE_RE.match(line):
            positions = fence_positions(line)
            break
    if positions is None or len(positions) < 2:
        return None, []

    rows = []  # list of cell-list
    header_idx = None  # index of the row that ends with a +===+ separator
    for line in lines:
        if HEADER_FENCE_RE.match(line):
            header_idx = len(rows) - 1
        elif GRID_FENCE_RE.match(line):
            pass
        elif line.startswith('|'):
            rows.append(split_cells(line, positions))

    if not rows:
        return None, []

    if header_idx is None:
        # No +===+ separator: promote the first row to header (matches the
        # visual intent in every such table in this corpus).
        header = rows[0]
        body = rows[1:]
    else:
        header = rows[header_idx]
        body = rows[header_idx + 1:]
    return header, body


def emit_pipe_table(header, body, indent=''):
    """Emit a GFM pipe table as a list of lines."""
    ncols = max(len(header), max((len(r) for r in body), default=0))
    # Pad rows to ncols
    header = header + [''] * (ncols - len(header))
    body = [r + [''] * (ncols - len(r)) for r in body]

    # Compute column widths (plain char count). Good enough for ASCII
    # alignment; double-width CJK is not in scope.
    def cell_repr(c):
        return escape_cell(c)

    widths = [max(len(cell_repr(header[c])),
                  max((len(cell_repr(r[c])) for r in body), default=0),
                  3)  # minimum 3 for '---'
              for c in range(ncols)]

    def fmt_row(cells):
        parts = []
        for c in range(ncols):
            txt = cell_repr(cells[c])
            parts.append(' ' + txt + ' ' * (widths[c] - len(txt)) + ' ')
        return indent + '|' + '|'.join(parts) + '|'

    sep_parts = []
    for c in range(ncols):
        sep_parts.append(' ' + '-' * widths[c] + ' ')
    sep_line = indent + '|' + '|'.join(sep_parts) + '|'

    out = [fmt_row(header), sep_line]
    out.extend(fmt_row(r) for r in body)
    return out


def convert_file(src_path):
    text = open(src_path, encoding='utf-8').read()
    original = text
    lines = text.splitlines()
    blocks = find_grid_blocks(lines)
    if not blocks:
        return 0

    replaced = 0
    # Walk in reverse so line indices stay valid.
    for (start, end) in reversed(blocks):
        block_lines = lines[start:end + 1]
        header, body = parse_grid_block(block_lines)
        if header is None:
            print(f'  SKIP empty block: {src_path}:{start+1}', file=sys.stderr)
            continue
        pipe_lines = emit_pipe_table(header, body)
        lines[start:end + 1] = pipe_lines
        replaced += 1

    if replaced:
        new_text = '\n'.join(lines)
        if original.endswith('\n') and not new_text.endswith('\n'):
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
                print(f'  {rel}: converted {count} table(s)')
    print(f'\nDone. {total_tables} tables converted across {total_files} files.')


if __name__ == '__main__':
    main()
