import json, os, re

# Gera design/tokens.json (fonte da verdade) e design/tokens.css (variáveis CSS para as prévias)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'design')
TEST = ROOT

THEMES = [("ambar", "Âmbar dourado"), ("gelo", "Azul gelo"), ("esmeralda", "Verde-esmeralda")]

def same(v):
    return v

colors = [
    # ---- superfícies
    ("bg-0", "#12161b", "Fundo mais profundo (inset). QLineEdit/QComboBox editável, log (#logList), QToolTip não. Barra de título nativa no mockup."),
    ("bg-1", "#171b21", "Fundo da janela: QMainWindow, QToolBar, QMenuBar, QStatusBar, QDockWidget, abas inativas, QHeaderView::section."),
    ("bg-2", "#1c2128", "Base das views: QTreeView/QListView/QTableView `background`, QTabWidget::pane, aba selecionada."),
    ("bg-2-alt", "#20262e", "Linhas alternadas: `alternate-background-color` das views (modList, espList, downloadView…). Diferença sutil de propósito."),
    ("bg-3", "#262c35", "Controles em repouso: QPushButton, QComboBox (não editável), QSpinBox, cabeçalho em hover, QScrollBar handle não."),
    ("bg-4", "#2f3640", "Hover de controles: QPushButton:hover, QToolButton:hover, QTabBar::tab:hover, QHeaderView::section:hover."),
    ("bg-5", "#39414c", "Pressionado: QPushButton:pressed, QToolButton:pressed, QHeaderView::section:pressed."),
    ("surface-menu", "#20262e", "QMenu e QComboBox QAbstractItemView (popup). Sempre com borda `border-strong`."),
    ("surface-tooltip", "#2c333d", "QToolTip background, com borda `border-strong` e texto `text-primary`."),
    ("separator-bg", "#2a3546", "Cor de separador do MO2 (clique direito no separador › Select Color...). Opaca de propósito: separador = cabeçalho de seção."),
    # ---- bordas
    ("border-subtle", "#252b33", "Divisórias internas: linhas de grade, divisória entre seções do header (border-right), QMenu::separator."),
    ("border", "#323a45", "Borda padrão 1px: botões, campos, QTabWidget::pane, QGroupBox, moldura das views, QSplitter::handle de repouso."),
    ("border-strong", "#47515e", "Borda em hover e de overlays: QPushButton:hover, QLineEdit:hover, QMenu, QToolTip, QScrollBar::handle:hover."),
    ("border-control", "#6b7684", "Contorno do checkbox desmarcado (QAbstractItemView::indicator, QCheckBox::indicator). ≥3:1 sobre bg-0…bg-2-alt."),
    # ---- texto
    ("text-strong", "#f2f5f8", "Texto enfatizado: item em hover, aba em hover, títulos da prancha. Sobre bg-1…bg-5."),
    ("text-primary", "#d9dfe6", "Texto padrão (QWidget color): mods/plugins ativos, valores, menus. Sobre bg-0…bg-5, separator-bg e todas as cores de conflito."),
    ("text-secondary", "#97a2b0", "Rótulos e metadados: cabeçalhos de coluna, abas inativas, status bar, atalhos no menu, Versão/Categoria. Sobre bg-0…bg-3."),
    ("text-inactive", "#7b8696", "Mods e plugins DESATIVADOS (esmaecidos, mas legíveis: ≥4:1 sobre bg-2 e bg-2-alt). Também placeholder de campos."),
    ("text-disabled", "#525b67", "Controles desabilitados (:disabled) — botão, campo, item de menu. Intencionalmente abaixo de 3:1."),
    ("text-on-accent", "#14181d", "Texto/ícone SOBRE a cor de acento: botão primário (Executar), checkbox marcado (glifo do check)."),
    # ---- conflitos (configurações de cor do MO2)
    ("conflict-overwriting", {"ambar": "rgba(80, 190, 100, 0.24)", "gelo": "rgba(80, 190, 100, 0.24)", "esmeralda": "rgba(160, 200, 70, 0.24)"},
     "MO2 › Cores › 'Sobrescreve (arquivos soltos)': linha inteira dos mods que vencem o conflito com o selecionado. Translúcida para somar com a alternância. No tema Esmeralda puxa para verde-lima para não confundir com a seleção. Hex com alfa: #50BE643D (Esmeralda #A0C8463D)."),
    ("conflict-overwritten", "rgba(232, 86, 78, 0.28)",
     "MO2 › Cores › 'É sobrescrito (arquivos soltos)': linha dos mods que perdem para o selecionado. Hex com alfa: #E8564E47."),
    ("conflict-overwriting-archive", {"ambar": "rgba(80, 190, 100, 0.11)", "gelo": "rgba(80, 190, 100, 0.11)", "esmeralda": "rgba(160, 200, 70, 0.11)"},
     "MO2 › Cores › 'Sobrescreve (arquivos BSA)': metade da intensidade do conflito solto. Hex: #50BE641C (Esmeralda #A0C8461C)."),
    ("conflict-overwritten-archive", "rgba(232, 86, 78, 0.12)",
     "MO2 › Cores › 'É sobrescrito (arquivos BSA)'. Hex: #E8564E1F."),
    ("related-highlight", "rgba(150, 128, 240, 0.26)",
     "MO2 › Theme › Colors › 'Mod contains selected file' e 'Plugin is contained in selected mod'. Violeta: fora do eixo verde/vermelho e distinto dos três acentos. Hex: #9680F042."),
    ("flag-overwrite", "#6fd08a", "Referência do glifo de conflito 'sobrescreve' (coluna Conflitos). Os ícones vêm dos recursos do MO2; use para ícones próprios/legenda."),
    ("flag-overwritten", "#f27a72", "Referência do glifo 'é sobrescrito'."),
    ("flag-both", "#c9a6ff", "Referência do glifo 'sobrescreve e é sobrescrito'."),
    ("flag-redundant", "#7d8896", "Referência do glifo 'redundante' (todos os arquivos sobrescritos)."),
    # ---- log / status
    ("log-info", "#7fb8f0", "Nível INFO no log (#logList) e ícones informativos. Sobre bg-0."),
    ("log-warning", "#e5b350", "Nível AVISO no log; ícone de problemas na toolbar. Sobre bg-0/bg-1."),
    ("log-error", "#f27a72", "Nível ERRO no log. Sobre bg-0."),
    ("log-debug", "#7b8696", "Nível DEBUG no log (alias de text-inactive)."),
    # ---- acento (varia por tema)
    ("accent", {"ambar": "#e2a74a", "gelo": "#7cc6ea", "esmeralda": "#33c79b"},
     "A única cor de destaque. Preenchimento: botão primário (#startButton), checkbox marcado, indicador da aba ativa (border-top 2px), borda de foco. Texto sobre ela: text-on-accent."),
    ("accent-hover", {"ambar": "#ecb965", "gelo": "#98d3f0", "esmeralda": "#52d4ad"},
     "Hover de preenchimentos de acento: #startButton:hover, indicator:checked:hover."),
    ("accent-pressed", {"ambar": "#c48d34", "gelo": "#5daed6", "esmeralda": "#27a882"},
     "Pressionado de preenchimentos de acento: #startButton:pressed."),
    ("accent-text", {"ambar": "#e9b35e", "gelo": "#8dcdee", "esmeralda": "#4fd1aa"},
     "Acento usado como texto/glifo sobre fundos escuros: seta de ordenação, links, contador de perfil, ícone ativo. ≥7:1 sobre bg-2."),
    ("selection", {"ambar": "rgba(226, 167, 74, 0.24)", "gelo": "rgba(124, 198, 234, 0.22)", "esmeralda": "rgba(51, 199, 155, 0.26)"},
     "Seleção com foco: ::item:selected:active, QMenu::item:selected, selection-background-color de campos. Texto: text-strong. Hex: Âmbar #E2A74A3D · Gelo #7CC6EA38 · Esmeralda #33C79B42."),
    ("selection-inactive", "rgba(151, 162, 176, 0.18)",
     "Seleção sem foco: ::item:selected:!active. Neutra, para a view ativa ser óbvia. Hex: #97A2B02E."),
    ("accent-subtle", {"ambar": "rgba(226, 167, 74, 0.12)", "gelo": "rgba(124, 198, 234, 0.11)", "esmeralda": "rgba(51, 199, 155, 0.12)"},
     "Toque leve de acento: QToolButton:checked, QSplitter::handle:hover, item de download em andamento."),
    ("focus-ring", "{accent}", "Borda de foco 1px (QLineEdit:focus, QComboBox:focus, QPushButton:focus). Alias de accent; ≥3:1 sobre todas as superfícies."),
]

color_tokens = []
for name, val, usage in colors:
    if isinstance(val, dict):
        v = val
    else:
        v = val
    color_tokens.append({"name": name, "value": v, "usage": usage})

tokens = {
    "name": "Ardósia",
    "version": 1,
    "color": {"themes": [{"id": i, "name": n} for i, n in THEMES], "tokens": color_tokens},
    "type": {
        "fonts": [],
        "families": {
            "sans": "\"Segoe UI Variable Text\", \"Segoe UI\", Inter, system-ui, sans-serif",
            "mono": "\"Cascadia Mono\", \"JetBrains Mono\", Consolas, monospace",
        },
        "groups": [
            {"name": "Interface", "family": "sans", "styles": [
                {"name": "body", "fontSize": "13px", "lineHeight": "18px", "fontWeight": 400, "sample": "Unofficial Skyrim Special Edition Patch",
                 "usage": "10pt. Texto base de TODO widget (QWidget font-size: 10pt): itens de lista, campos, botões, menus."},
                {"name": "body-strong", "fontSize": "13px", "lineHeight": "18px", "fontWeight": 600, "sample": "Texturas",
                 "usage": "10pt semibold. Aba selecionada, nome de separador (quando o MO2 permitir), botão primário."},
                {"name": "label", "fontSize": "12px", "lineHeight": "16px", "fontWeight": 400, "sample": "Ativos 21 de 25 · API Nexus 2.384/2.500",
                 "usage": "9pt. Status bar, contadores, rótulos de campo, atalhos de menu, dicas."},
                {"name": "header", "fontSize": "12px", "lineHeight": "16px", "fontWeight": 600, "sample": "Prioridade",
                 "usage": "9pt semibold em text-secondary. QHeaderView::section."},
                {"name": "caption", "fontSize": "11px", "lineHeight": "14px", "fontWeight": 600, "sample": "2",
                 "usage": "8pt. Badges (contador de problemas), legendas da prancha."},
            ]},
            {"name": "Log", "family": "mono", "styles": [
                {"name": "mono", "fontSize": "12px", "lineHeight": "18px", "fontWeight": 400, "sample": "16:08:12.441  I  Perfil \"Principal\" carregado",
                 "usage": "9pt monoespaçada. #logList e qualquer saída técnica. Alinhamento de timestamps."},
            ]},
        ],
    },
    "spacing": {"tokens": [
        {"name": "space-2xs", "value": "2px", "usage": "Margem do handle na scrollbar; respiro entre ícone e badge."},
        {"name": "space-xs", "value": "4px", "usage": "Padding vertical do ::item (gera linha de 26px); gap entre ícones de flag; spacing de QToolBar."},
        {"name": "space-sm", "value": "6px", "usage": "Padding vertical de botões/campos (5–6px); gap entre controles na mesma barra."},
        {"name": "space-md", "value": "8px", "usage": "Padding horizontal de campos e ::item; margens internas de painéis; padding do QToolTip (6px 8px)."},
        {"name": "space-lg", "value": "12px", "usage": "Padding horizontal de botões e seções do header (0 8px já basta no header); padding de QMenu::item (6px 24px 6px 12px)."},
        {"name": "space-xl", "value": "16px", "usage": "Padding horizontal das abas (6px 16px); margem entre grupos de botões na toolbar."},
        {"name": "space-2xl", "value": "24px", "usage": "Recuo de nível da árvore (QTreeView indentation: 20–24px); padding-right de QMenu::item para o atalho."},
    ]},
    "radius": {"tokens": [
        {"name": "radius-sm", "value": "3px", "usage": "Checkbox (::indicator), badges."},
        {"name": "radius-md", "value": "4px", "usage": "Botões, QToolButton, campos, QComboBox, handle da scrollbar, QMenu::item."},
        {"name": "radius-lg", "value": "6px", "usage": "Abas (só cantos de cima), QTabWidget::pane, QMenu, QToolTip, QGroupBox, moldura das views."},
    ]},
    "size": {"tokens": [
        {"name": "row-height", "value": "26px", "usage": "Altura de linha das views = 18px de texto + 2×4px de padding no ::item (o padrão do Qt é ~20px)."},
        {"name": "header-height", "value": "26px", "usage": "QHeaderView::section (padding 4px 8px + min-height)."},
        {"name": "control-height", "value": "28px", "usage": "Botões, campos e combos: min-height 16px + padding 5px + borda 1px."},
        {"name": "tab-height", "value": "30px", "usage": "QTabBar::tab: padding 6px 16px, com border-top 2px."},
        {"name": "toolbar-icon", "value": "24px", "usage": "QToolBar icon-size (qproperty-iconSize: 24px 24px)."},
        {"name": "toolbar-button", "value": "36px", "usage": "QToolButton na toolbar: ícone 24px + padding 5px + borda 1px."},
        {"name": "checkbox-size", "value": "16px", "usage": "::indicator width/height — maior que o padrão (13px) para clicar fácil."},
        {"name": "scrollbar-size", "value": "12px", "usage": "QScrollBar:vertical width / :horizontal height. Handle de 8px com margem de 2px."},
        {"name": "scroll-handle-min", "value": "32px", "usage": "QScrollBar::handle min-height/min-width."},
        {"name": "splitter-size", "value": "6px", "usage": "QSplitter::handle width/height e QMainWindow::separator."},
        {"name": "border-width", "value": "1px", "usage": "Toda borda do tema. Única exceção: indicador da aba ativa (2px)."},
        {"name": "tab-indicator", "value": "2px", "usage": "border-top da aba selecionada, em accent."},
    ]},
}

with open(os.path.join(ROOT, 'tokens.json'), 'w', encoding='utf-8') as f:
    json.dump(tokens, f, ensure_ascii=False, indent=1)

# ---------- test tokens.css (local only, mimics the page's compiled form)
first = THEMES[0][0]
def cval(t, th):
    v = t['value']
    if isinstance(v, dict):
        v = v.get(th, v[first])
    m = re.fullmatch(r'\{(.+)\}', v)
    return f'var(--{m.group(1)})' if m else v

css = [f':root, [data-theme="{first}"] {{']
for t in color_tokens:
    css.append(f'  --{t["name"]}: {cval(t, first)};')
css.append('}')
for th, _ in THEMES[1:]:
    css.append(f'[data-theme="{th}"] {{')
    for t in color_tokens:
        css.append(f'  --{t["name"]}: {cval(t, th)};')
    css.append('}')
css.append(':root {')
for fam in ('spacing', 'radius', 'size'):
    for t in tokens[fam]['tokens']:
        css.append(f'  --{t["name"]}: {t["value"]};')
for k, v in tokens['type']['families'].items():
    css.append(f'  --font-{k}: {v};')
css.append('}')
with open(os.path.join(TEST, 'tokens.css'), 'w', encoding='utf-8') as f:
    f.write('/* Ardósia — gerado de tokens.json por scripts/build_tokens.py */\n' + '\n'.join(css) + '\n')

# ---------- contrast report
def hex2rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def parse(v):
    if v.startswith('#'): return hex2rgb(v) + (1.0,)
    m = re.match(r'rgba\(([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\)', v)
    return (float(m[1]), float(m[2]), float(m[3]), float(m[4]))
def over(fg, bg):
    a = fg[3]; return tuple(fg[i]*a + bg[i]*(1-a) for i in range(3))
def lum(c):
    def ch(x):
        x /= 255; return x/12.92 if x <= 0.03928 else ((x+0.055)/1.055)**2.4
    r, g, b = c[:3]; return 0.2126*ch(r)+0.7152*ch(g)+0.0722*ch(b)
def cr(a, b):
    la, lb = lum(a), lum(b); return (max(la, lb)+0.05)/(min(la, lb)+0.05)

def get(name, th):
    for t in color_tokens:
        if t['name'] == name:
            v = cval(t, th)
            if v.startswith('var('): return get(v[6:-1], th)
            return parse(v)

for th, _ in THEMES:
    print('==', th)
    bgs = ['bg-0', 'bg-1', 'bg-2', 'bg-2-alt', 'bg-3', 'bg-4', 'separator-bg', 'surface-menu', 'surface-tooltip']
    for fg in ['text-primary', 'text-secondary', 'text-inactive', 'text-disabled', 'accent-text', 'border-control', 'accent']:
        print(f'  {fg:15}', ' '.join(f'{b}:{cr(get(fg, th), get(b, th)):.1f}' for b in bgs))
    base = get('bg-2', th); alt = get('bg-2-alt', th)
    for ov in ['conflict-overwriting', 'conflict-overwritten', 'related-highlight', 'selection', 'selection-inactive']:
        c = over(get(ov, th), base); c2 = over(get(ov, th), alt)
        print(f'  {ov:22} text-primary {cr(get("text-primary", th), c):.1f}/{cr(get("text-primary", th), c2):.1f}  inactive {cr(get("text-inactive", th), c):.1f}  strong {cr(get("text-strong", th), c):.1f}  vs bg-2 {cr(c, base):.2f}')
    print('  on-accent', f'{cr(get("text-on-accent", th), get("accent", th)):.1f}', 'hover', f'{cr(get("text-on-accent", th), get("accent-hover", th)):.1f}', 'pressed', f'{cr(get("text-on-accent", th), get("accent-pressed", th)):.1f}')
    for o in ['flag-overwrite', 'flag-overwritten', 'flag-both', 'log-info', 'log-warning', 'log-error']:
        print(f'  {o:16} bg-2 {cr(get(o, th), get("bg-2", th)):.1f} bg-0 {cr(get(o, th), get("bg-0", th)):.1f}')
