# Gera os ícones SVG de 16px usados pelo .qss em design/icons
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'design', 'icons')
os.makedirs(OUT, exist_ok=True)
def w(n, body):
    open(os.path.join(OUT, n), 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>\n')
w('check.svg', '<path d="M3.5 8.3 6.6 11.4 12.6 4.8" stroke="#14181D" stroke-width="2.2"/>')
w('check-partial.svg', '<path d="M4 8h8" stroke="#14181D" stroke-width="2.2"/>')
w('check-disabled.svg', '<path d="M3.5 8.3 6.6 11.4 12.6 4.8" stroke="#7B8696" stroke-width="2.2"/>')
w('chevron-down.svg', '<path d="M4.5 6.5 8 10l3.5-3.5" stroke="#97A2B0" stroke-width="1.8"/>')
w('chevron-up.svg', '<path d="M4.5 9.5 8 6l3.5 3.5" stroke="#97A2B0" stroke-width="1.8"/>')
w('chevron-right.svg', '<path d="M6.5 4.5 10 8l-3.5 3.5" stroke="#97A2B0" stroke-width="1.8"/>')
w('chevron-down-disabled.svg', '<path d="M4.5 6.5 8 10l3.5-3.5" stroke="#525B67" stroke-width="1.8"/>')
for t, c in [('ambar', '#E9B35E'), ('gelo', '#8DCDEE'), ('esmeralda', '#4FD1AA')]:
    w(f'sort-up-{t}.svg', f'<path d="M4.5 9.5 8 6l3.5 3.5" stroke="{c}" stroke-width="2"/>')
    w(f'sort-down-{t}.svg', f'<path d="M4.5 6.5 8 10l3.5-3.5" stroke="{c}" stroke-width="2"/>')
    w(f'branch-closed-{t}.svg', f'<path d="M6.5 4.5 10 8l-3.5 3.5" stroke="{c}" stroke-width="2"/>')
    w(f'branch-open-{t}.svg', f'<path d="M4.5 6.5 8 10l3.5-3.5" stroke="{c}" stroke-width="2"/>')
print('ícones ok')
