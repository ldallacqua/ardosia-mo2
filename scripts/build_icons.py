# Gera os ícones SVG de 16px usados pelo .qss em design/icons
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'design', 'icons')
os.makedirs(OUT, exist_ok=True)
# O MO2 não traz o plugin iconengines/qsvgicon: o Qt rasteriza o SVG no tamanho intrínseco e depois
# reescala. Por isso o tamanho intrínseco é 64px, para ficar nítido em qualquer escala de tela; o
# tamanho na tela vem do width/height no .qss.
def w(n, body, view='0 0 16 16'):
    open(os.path.join(OUT, n), 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="{view}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>\n')
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
    # ::branch ocupa o recuo de 20px da árvore: a margem no viewBox mantém o desenho em escala 1:1
    w(f'branch-closed-{t}.svg', f'<path d="M6.5 4.5 10 8l-3.5 3.5" stroke="{c}" stroke-width="2"/>', '-2 -2 20 20')
    w(f'branch-open-{t}.svg', f'<path d="M4.5 6.5 8 10l3.5-3.5" stroke="{c}" stroke-width="2"/>', '-2 -2 20 20')
# Checkbox das listas: caixa e glifo na mesma imagem. Em escala de 150%, uma lista pode cair em meio pixel, e a caixa desenhada
# pelo QSS sairia com as bordas borradas ou cortadas; a imagem o Qt alinha ao pixel. O raio é pequeno porque o Qt não pinta a cor da
# linha atrás do checkbox: nas linhas coloridas, o que sobra nos cantos aparece escuro.
GLYPH = '<path d="M3.5 8.3 6.6 11.4 12.6 4.8" stroke="{}" stroke-width="2.2" transform="scale(.875)"/>'
PARTIAL = '<path d="M4 8h8" stroke="#14181D" stroke-width="2.2" transform="scale(.875)"/>'
def lv(n, fill, line, body=''):
    w(n, f'<rect x=".5" y=".5" width="13" height="13" rx="2" fill="{fill}" stroke="{line}"/>{body}', '0 0 14 14')
lv('lv-unchecked.svg', '#12161B', '#6B7684')
lv('lv-unchecked-disabled.svg', 'none', '#323A45')
lv('lv-checked-disabled.svg', '#2F3640', '#2F3640', GLYPH.format('#7B8696'))
for t, c, h in [('ambar', '#E2A74A', '#ECB965'), ('gelo', '#7CC6EA', '#98D3F0'), ('esmeralda', '#33C79B', '#52D4AD')]:
    lv(f'lv-unchecked-hover-{t}.svg', '#12161B', c)
    lv(f'lv-checked-{t}.svg', c, c, GLYPH.format('#14181D'))
    lv(f'lv-checked-hover-{t}.svg', h, h, GLYPH.format('#14181D'))
    lv(f'lv-partial-{t}.svg', c, c, PARTIAL)
# Barra de ferramentas: mesmos desenhos de build_mockups.py (grade de 24px, traço de 1,6). A tinta é fixa porque o
# QSS não recolore ícones; Problemas usa log-warning, como no mockup.
TOOLBAR = {
 'instances': '<rect x="4" y="8" width="12" height="12" rx="2"/><path d="M8 4.5h9.5a2 2 0 0 1 2 2V16"/>',
 'install': '<path d="M4 8.5 12 4l8 4.5v7L12 20l-8-4.5z"/><path d="M12 9v7M9 13l3 3 3-3"/>',
 'nexus': '<circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c2.4 2.3 3.5 5 3.5 8s-1.1 5.7-3.5 8c-2.4-2.3-3.5-5-3.5-8S9.6 6.3 12 4z"/>',
 'profile': '<circle cx="12" cy="8.5" r="3.5"/><path d="M5 19.5c1.2-3.3 3.9-5 7-5s5.8 1.7 7 5"/>',
 'refresh': '<path d="M19 12a7 7 0 0 1-12.2 4.7M5 12a7 7 0 0 1 12.2-4.7"/><path d="M17.5 3.8v3.6h-3.6M6.5 20.2v-3.6h3.6"/>',
 'exe': '<rect x="3.5" y="5" width="17" height="14" rx="2"/><path d="M7.5 10l2.5 2-2.5 2M12.5 14.5h4"/>',
 'tools': '<path d="M14.5 5.5a4 4 0 0 0-5 5L4 16l2 2 5.5-5.5a4 4 0 0 0 5-5l-2.3 2.3-2-2z"/>',
 'settings': '<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.2M12 18.3v2.2M3.5 12h2.2M18.3 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M6 18l1.6-1.6M16.4 7.6 18 6"/>',
 'endorse': '<path d="M12 19.5s-7-4.2-7-9.2A3.8 3.8 0 0 1 12 8a3.8 3.8 0 0 1 7 2.3c0 5-7 9.2-7 9.2z"/>',
 'problems': '<path d="M12 4.5 20.5 19h-17z"/><path d="M12 10v4M12 16.6v.1"/>',
 'update': '<circle cx="12" cy="12" r="8"/><path d="M12 16V8M8.5 11.5 12 8l3.5 3.5"/>',
 'help': '<circle cx="12" cy="12" r="8"/><path d="M9.8 9.6a2.3 2.3 0 1 1 3.2 2.1c-.7.3-1 .8-1 1.5v.4M12 16.4v.1"/>',
}
for n, body in TOOLBAR.items():
    c = '#E5B350' if n == 'problems' else '#97A2B0'
    w(f'tb-{n}.svg', f'<g stroke="{c}" stroke-width="1.6">{body}</g>', '0 0 24 24')
# Botões da janela principal: grade de 24px, traço de 1,7 e tinta text-primary, como o texto dos botões
BUTTONS = {
 'options': '<circle cx="12" cy="12" r="2.6"/><path d="M12 4v2.4M12 17.6V20M4 12h2.4M17.6 12H20M6.4 6.4l1.7 1.7M15.9 15.9l1.7 1.7M6.4 17.6l1.7-1.7M15.9 8.1l1.7-1.7"/>',
 'folder': '<path d="M3.5 7.5a2 2 0 0 1 2-2h4l2 2.5h7a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2z"/>',
 'restore': '<path d="M8.5 5.5 4 10l4.5 4.5"/><path d="M4.5 10H14a5 5 0 0 1 0 10h-2.5"/>',
 'backup': '<path d="M12 4v10M8 10.5l4 4 4-4"/><path d="M4.5 15.5V18a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2v-2.5"/>',
 'sort': '<path d="M7 7h10M9 12h6M11 17h2"/>',
 'refresh': TOOLBAR['refresh'],
 'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 'clear': '<path d="M7 7l10 10M17 7 7 17"/>',
}
for n, body in BUTTONS.items():
    w(f'btn-{n}.svg', f'<g stroke="#D9DFE6" stroke-width="1.7">{body}</g>', '0 0 24 24')
# Executar fica sobre o acento: tinta text-on-accent
w('btn-run.svg', '<path d="M8 5.5v13l10-6.5z" fill="#14181D" stroke="#14181D" stroke-width="1.7"/>', '0 0 24 24')
print('ícones ok')
