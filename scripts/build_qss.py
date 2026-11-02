# Compila stylesheets/*.qss a partir de design/qss-reference.md + copia os ícones
import re, os, shutil
REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(REPO)
ref = open('design/qss-reference.md', encoding='utf-8').read()
sections = re.findall(r'^## (.+?)\n.*?```css\n(.*?)```', ref, re.S | re.M)
assert len(sections) == 9
body = '\n'.join(f'/* ==================== {t} ==================== */\n{c}' for t, c in sections)
body += '''
/* ==================== Ajustes de herança ==================== */
/* QWidget pinta bg-1; páginas de aba e rótulos precisam herdar o fundo do painel */
QTabWidget > QStackedWidget { background: transparent; }
QTabWidget > QStackedWidget > QWidget { background: #1C2128; }
QLabel, QCheckBox, QRadioButton { background: transparent; }
QAbstractScrollArea > QWidget { background: transparent; }
QAbstractItemView > QWidget { background: transparent; }
QToolTip { opacity: 255; }
'''
amber = {
 '#E2A74A': ['#7CC6EA', '#33C79B'], '#ECB965': ['#98D3F0', '#52D4AD'], '#C48D34': ['#5DAED6', '#27A882'],
 '#E9B35E': ['#8DCDEE', '#4FD1AA'],
 'rgba(226, 167, 74, 0.24)': ['rgba(124, 198, 234, 0.22)', 'rgba(51, 199, 155, 0.26)'],
 'rgba(226, 167, 74, 0.12)': ['rgba(124, 198, 234, 0.11)', 'rgba(51, 199, 155, 0.12)'],
 '-ambar.svg': ['-gelo.svg', '-esmeralda.svg'],
}
out = 'stylesheets'
shutil.rmtree(out, ignore_errors=True); os.makedirs(out + '/ardosia')
for f in os.listdir('design/icons'): shutil.copy('design/icons/' + f, out + '/ardosia/' + f)
conf = {'Âmbar': ('#50BE643D', '#50BE641C'), 'Gelo': ('#50BE643D', '#50BE641C'), 'Esmeralda': ('#A0C8463D', '#A0C8461C')}
for i, (name, fname) in enumerate([('Âmbar', 'Ardosia Ambar'), ('Gelo', 'Ardosia Gelo'), ('Esmeralda', 'Ardosia Esmeralda')]):
    s = body
    if i:
        for k, v in amber.items(): s = s.replace(k, v[i-1])
    ow, owa = conf[name]
    head = f'''/*
 * Ardósia — {name}
 * Tema escuro para Mod Organizer 2 (Qt Style Sheet)
 *
 * Instalação: copie este arquivo e a pasta "ardosia" para <MO2>/stylesheets/
 * e escolha "{fname}" em Settings > Theme > Style.
 *
 * Cores que NÃO ficam no .qss — defina em Settings > Theme > Colors:
 *   Is overwriting (loose files) ......... {ow}
 *   Is overwritten (loose files) ......... #E8564E47
 *   Is overwriting (archives) ............ {owa}
 *   Is overwritten (archives) ............ #E8564E1F
 *   Mod contains selected file ........... #9680F042
 *   Plugin is contained in selected mod .. #9680F042
 *   (#RRGGBBAA — no seletor de cor do MO2, ajuste o canal Alfa)
 *
 * Separadores: clique direito no separador > Select Color... > #2A3546
 *
 * Regra do tema: nenhum background em ::item / ::item:hover, para não
 * cobrir as cores de conflito e de separador que o MO2 pinta nas linhas.
 */

'''
    open(f'{out}/{fname}.qss', 'w', encoding='utf-8').write(head + s)
for f in sorted(os.listdir(out)):
    if not f.endswith('.qss'): continue
    s = open(f'{out}/{f}', encoding='utf-8').read()
    nc = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    assert nc.count('{') == nc.count('}'), f
    leftovers = [k for k in amber if k in s] if 'Ambar' not in f else []
    icons = set(re.findall(r'url\(\./ardosia/([^)]+)\)', s))
    missing = [x for x in icons if not os.path.exists(f'{out}/ardosia/{x}')]
    blocks = re.findall(r'\{([^}]*)\}', nc)
    bad = [b for b in blocks if b.strip() and not b.strip().endswith(';')]
    print(f, 'regras', len(blocks), 'ícones', len(icons), 'faltando', missing, 'resíduo âmbar', leftovers, 'sem ;', bad[:2])
