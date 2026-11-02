import os
# Gera as prévias de componentes em design/components
from build_mockups import svg, I, CHECK, HEAD, write, BASE, conflict_glyph, check

PART = '<svg viewBox="0 0 12 12" width="12" height="12"><path d="M3 6h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

def cell(label, values, inner):
    return (f'<div class="spec-cell">{inner}<div><div class="spec-k">{label}</div>'
            f'<div class="spec-v">{values}</div></div></div>')

def page(name, group, height, subtitle, body, width=960):
    write(os.path.join(BASE, name, 'preview.html'),
          f'<!-- @dsCard group="{group}" height={height} width={width} subtitle="{subtitle}" -->\n'
          + HEAD.format(t=f'{name} — Ardósia') + f'<div class="ar spec">{body}</div>\n</body></html>\n')

def grid(cols, cells):
    return f'<div class="spec-grid" style="grid-template-columns:repeat({cols},minmax(0,1fr))">{"".join(cells)}</div>'

# ---------- Button
def btns(primary):
    p = ' ar-btn--primary' if primary else ''
    label = 'Executar' if primary else 'Filtros'
    icon = svg(I['play'], 14) if primary else svg(I['filter'], 15)
    if primary:
        st = [('normal', '', 'bg accent\nborder accent\ncolor text-on-accent\nweight 600'),
              (':hover', ' is-hover', 'bg/border accent-hover'), (':pressed', ' is-pressed', 'bg/border accent-pressed'),
              (':focus', ' is-focus', 'border text-strong'), (':disabled', ' is-disabled', 'bg bg-3 · border\nborder-subtle\ncolor text-disabled')]
    else:
        st = [('normal', '', 'bg bg-3\nborder 1px border\ncolor text-primary\nradius 4 · h 28\npad 0 12'),
              (':hover', ' is-hover', 'bg bg-4\nborder border-strong'), (':pressed', ' is-pressed', 'bg bg-5\nborder border-strong'),
              (':focus', ' is-focus', 'border focus-ring'), (':disabled', ' is-disabled', 'bg bg-2\nborder border-subtle\ncolor text-disabled')]
    return grid(5, [cell(k, v, f'<span class="ar-btn{p}{c}">{icon}{label}</span>') for k, v, c in [(a, c, b) for a, b, c in st]])
page('Button', 'Controles', 340, 'QPushButton e #startButton — 5 estados',
     '<div class="spec-h">QPushButton</div>' + btns(False) + '<div style="height:26px"></div><div class="spec-h">QPushButton#startButton (primário)</div>' + btns(True))

# ---------- ToolButton
tb = [('normal', '', 'bg transparent\nborder transparent\nícone text-secondary\n36×36 · ícone 24'),
      (':hover', ' is-hover', 'bg bg-4 · border border\nícone text-strong'), (':pressed', ' is-pressed', 'bg bg-5\nborder border-strong'),
      (':checked', ' is-checked', 'bg accent-subtle\nícone accent-text'), (':disabled', ' is-disabled', 'ícone text-disabled')]
page('ToolButton', 'Controles', 190, 'QToolButton da barra de ferramentas',
     '<div class="spec-h">QToolBar QToolButton</div>' + grid(5, [cell(k, v, f'<span class="ar-tool{c}">{svg(I["install"], 24)}</span>') for k, c, v in tb])
     + '<div style="height:18px"></div><div class="spec-row">' + cell('badge (problemas)', 'bg log-warning · texto text-on-accent\n8pt bold · radius 3', f'<span class="ar-tool" style="color:var(--log-warning)">{svg(I["problems"], 24)}<span class="badge">2</span></span>') + '</div>')

# ---------- TextField
tf = [('normal', '', '<span class="ph">Filtrar mods por nome…</span>', 'bg bg-0 · border border\nplaceholder text-inactive\nradius 4 · h 28 · pad 0 8'),
      (':hover', ' is-hover', '<span class="ph">Filtrar mods por nome…</span>', 'border border-strong'),
      (':focus', ' is-focus', '<span><span class="sel">skyrim</span> 202x</span><span class="caret"></span>', 'border focus-ring (accent)\nselection-background-color\nselection · texto text-strong'),
      (':disabled', ' is-disabled', '<span class="ph">Filtrar mods por nome…</span>', 'bg bg-1 · border border-subtle\ncolor text-disabled')]
page('TextField', 'Controles', 200, 'QLineEdit — normal, hover, foco com seleção, desabilitado',
     '<div class="spec-h">QLineEdit</div>' + grid(4, [cell(k, v, f'<span class="ar-input{c}" style="width:200px"><span class="ico">{svg(I["search"], 15)}</span>{t}</span>') for k, c, t, v in tf]))

# ---------- ComboBox
dd = f'<span class="dd">{svg(I["chev-d"], 14, sw=2)}</span>'
cb = [('normal', '', 'bg bg-3 · border border\nradius 4 · h 28\n::drop-down 22px\nborder-left border-subtle'), (':hover', ' is-hover', 'bg bg-4\nborder border-strong'),
      (':focus', ' is-focus', 'border focus-ring'), (':disabled', ' is-disabled', 'bg bg-2 · border border-subtle\ncolor text-disabled')]
popup = ('<div style="display:flex;flex-direction:column;width:220px"><span class="ar-combo is-open" style="width:220px"><span class="val">SKSE</span>' + dd + '</span>'
         '<div class="ar-menu" style="min-width:0;width:220px;border-top-left-radius:0;border-top-right-radius:0;border-top:none">'
         + ''.join(f'<div class="ar-mi{" is-hover" if i == 1 else ""}"><span class="ic">{svg(I["skse" if i == 0 else "exe"], 15)}</span>{t}</div>' for i, t in enumerate(['SKSE', 'Skyrim Special Edition', 'LOOT', 'xEdit', 'Bodyslide']))
         + '</div></div>')
page('ComboBox', 'Controles', 400, 'QComboBox — seletor de perfil e de executável',
     '<div class="spec-h">QComboBox</div>' + grid(4, [cell(k, v, f'<span class="ar-combo{c}" style="width:200px"><span class="val">Principal</span>{dd}</span>') for k, c, v in cb])
     + '<div style="height:24px"></div><div class="spec-row">' + cell('aberto · QAbstractItemView', 'popup surface-menu\nborder border-strong\nitem :selected selection', popup) + '</div>')

# ---------- Checkbox
ck = [('desmarcado', '', '', 'bg bg-0\nborder 1px border-control\n16×16 · radius 3'), (':unchecked:hover', ' is-hover', '', 'border accent'),
      (':checked', ' is-checked', CHECK, 'bg/border accent\nimage check.svg\n(glifo text-on-accent)'), (':checked:hover', ' is-checked is-hover', CHECK, 'bg/border accent-hover'),
      (':indeterminate', ' is-partial', PART, 'bg/border accent\nimage check-partial.svg'), (':disabled', ' is-disabled', '', 'bg transparent\nborder border'),
      (':checked:disabled', ' is-checked is-disabled', CHECK, 'bg/border bg-4\nimage check-disabled.svg')]
big = ''.join(f'<span class="ar-check{c}" style="zoom:3">{g}</span>' for _, c, g, _ in ck[:5:2])
page('Checkbox', 'Controles', 400, '::indicator — 16px, acento quando marcado',
     '<div class="spec-h">QTreeView::indicator · QCheckBox::indicator</div>' + grid(4, [cell(k, v, f'<span class="ar-check{c}">{g}</span>') for k, c, g, v in ck])
     + f'<div style="height:24px"></div><div class="spec-h">Ampliado 3×</div><div style="display:flex;gap:28px;align-items:center">{big}</div>')

# ---------- Tabs
tabs = (f'<div class="ar-tabs"><span class="ar-tab is-active">Plugins<span class="count">20/22</span></span><span class="ar-tab">Arquivos (BSA)</span>'
        f'<span class="ar-tab is-hover">Data</span><span class="ar-tab">Saves</span><span class="ar-tab is-disabled">Downloads</span></div>'
        f'<div class="ar-pane" style="height:70px;width:640px"></div>')
labels = grid(4, [cell('::tab:selected', 'bg bg-2 (= pane) · text-strong 600\nborder 1px border, sem base\nborder-top 2px accent\ntopo reto · pad 6 16', ''),
                  cell('::tab (normal)', 'bg transparent\ncolor text-secondary', ''), cell('::tab:hover', 'bg bg-3\ncolor text-strong', ''),
                  cell('::tab:disabled', 'color text-disabled', '')])
page('Tabs', 'Controles', 300, 'QTabBar e QTabWidget::pane', '<div class="spec-h">QTabWidget</div>' + tabs + '<div style="height:20px"></div>' + labels)

# ---------- ColumnHeader
def hd(label, cls, arrow=None, w=150):
    a = f'<span class="arrow">{svg(I["chev-u" if arrow == "up" else "chev-d"], 12, sw=2.2)}</span>' if arrow else ''
    return f'<div class="ar-view" style="width:{w}px;border-radius:4px"><div class="ar-head" style="border-bottom:none"><div class="ar-hcell {cls}" style="width:100%">{label}{a}</div></div></div>'
hs = [('normal', hd('Categoria', ''), 'bg bg-1 · h 26\ntexto text-secondary\n9pt 600 · pad 0 8\nborder-right border-subtle\nborder-bottom border'),
      (':hover', hd('Categoria', 'is-hover'), 'bg bg-4\ncolor text-strong'), (':pressed', hd('Categoria', 'is-pressed'), 'bg bg-5'),
      ('ordenado ↑', hd('Prioridade', 'is-sorted', 'up'), '::up-arrow sort-up-*.svg\n(accent-text) 12px\ntexto text-primary'),
      ('ordenado ↓', hd('Prioridade', 'is-sorted', 'down'), '::down-arrow\nsort-down-*.svg')]
page('ColumnHeader', 'Listas', 210, 'QHeaderView::section e indicador de ordenação',
     '<div class="spec-h">QHeaderView::section</div>' + grid(5, [cell(k, v, h) for k, h, v in hs]))

# ---------- ModListRow
def row(name, cls, note, conf='', on=True, cat='Texturas', ver='4.3', prio=15):
    c = 'ar-row ' + cls + ('' if on else ' off')
    return (f'<div style="display:flex;align-items:center;gap:20px"><div style="width:560px;flex:none;border:1px solid var(--border-subtle)"><div class="{c}">'
            f'<div class="c" style="width:250px"><span class="indent" style="width:8px"></span>{check(on)}<span>{name}</span></div>'
            f'<div class="c" style="width:56px">{conflict_glyph(conf)}</div><div class="c meta" style="width:120px">{cat}</div>'
            f'<div class="c meta" style="width:66px">{ver}</div><div class="c num meta" style="width:70px">{prio}</div></div></div>'
            f'<div><div class="spec-k">{note[0]}</div><div class="spec-v" style="white-space:normal">{note[1]}</div></div></div>')
rows = [
 row('Noble Skyrim – Full Pack', '', ('::item (ativo)', 'bg herdado da view: bg-2 · texto text-primary · meta text-secondary')),
 row('Noble Skyrim – Full Pack', 'alt', ('alternada', 'alternate-background-color: bg-2-alt')),
 row('Noble Skyrim – Full Pack', 'is-hover', ('::item:hover', 'SÓ color: text-strong — sem background (preserva cores de conflito)')),
 row('Majestic Mountains', '', ('mod desativado', 'texto text-inactive (#7B8696, 4.4:1) — aplicado pelo MO2'), on=False),
 row('Skyrim 202X', 'is-selected', ('::item:selected:active', 'bg selection · color text-strong'), 'both'),
 row('Skyrim 202X', 'is-selected-inactive', ('::item:selected:!active', 'bg selection-inactive · color text-strong'), 'both'),
 row('Realistic Water Two', 'ovw', ('sobrescreve (solto)', 'MO2 › Cores: conflict-overwriting'), 'ow', cat='Ambiente'),
 row('Skyland AIO', 'ovwn', ('é sobrescrito (solto)', 'MO2 › Cores: conflict-overwritten'), 'owd'),
 row('Static Mesh Improvement Mod', 'ovwa', ('sobrescreve (BSA)', 'conflict-overwriting-archive'), 'arc', cat='Modelos'),
 row('Skyland AIO', 'ovwna alt', ('é sobrescrito (BSA)', 'conflict-overwritten-archive (sobre bg-2-alt)'), 'owd'),
 row('Ordinator – Perks of Skyrim', 'rel', ('relacionado', 'related-highlight — mod contém o plugin selecionado'), 'ow', cat='Gameplay'),
]
page('ModListRow', 'Listas', 470, 'Linha de mod: estados, seleção e cores de conflito do MO2',
     '<div class="spec-h">QTreeView#modList::item — linha 26px (padding 4px 8px)</div><div style="display:flex;flex-direction:column;gap:6px">' + ''.join(rows) + '</div>')

# ---------- Separator
def sep(name, cnt, open_):
    return (f'<div class="ar-row sep"><div class="c" style="width:400px"><span class="branch">{svg(I["chev-d" if open_ else "chev-r"], 12, sw=2.2)}</span>{name}<span class="meta">{cnt}</span></div></div>')
def child(name, alt, on=True, cls=''):
    return (f'<div class="ar-row{" alt" if alt else ""}{"" if on else " off"} {cls}"><div class="c" style="width:400px"><span class="indent"></span>{check(on)}{name}</div>'
            f'<div class="c meta" style="width:140px">Interface</div></div>')
lst = (sep('Correções', '6 mods', False) + sep('Interface', '5 mods', True) + child('SkyUI', 0) + child('MCM Helper', 1) + child('A Matter of Time', 0, False)
       + sep('Texturas', '6 mods', True) + child('Skyland AIO', 0, cls='ovwn') + child('Skyrim 202X', 1))
page('Separator', 'Listas', 330, 'Separador de mods como cabeçalho de seção',
     '<div class="spec-h">Separador do MO2 (mod *_separator)</div><div style="display:flex;gap:28px;align-items:flex-start">'
     f'<div class="ar-view" style="width:560px;border-radius:4px"><div class="ar-body">{lst}</div></div>'
     '<div style="display:flex;flex-direction:column;gap:14px">'
     + cell('fundo', 'separator-bg #2A3546 (opaco)\nMO2 › Cores › Separador', '')
     + cell('texto', 'text-strong · 10pt 600*\n* peso depende do MO2', '')
     + cell('seta de ramo', '::branch:closed/open\nchevron-*-accent.svg (accent-text)', '')
     + cell('contador', 'text-secondary 9pt', '') + '</div></div>')

# ---------- Scrollbar
def vs(cls, top, h):
    return f'<div style="position:relative;width:12px;height:150px;border:1px solid var(--border-subtle);border-radius:2px;overflow:hidden"><div class="ar-vscroll" style="border-left:none"><div class="h {cls}" style="top:{top}px;height:{h}px"></div></div></div>'
hs_ = (f'<div style="position:relative;width:260px;height:12px;background:var(--bg-2);border:1px solid var(--border-subtle);border-radius:2px">'
       f'<div style="position:absolute;top:2px;bottom:2px;left:40px;width:110px;border-radius:4px;background:var(--bg-5)"></div></div>')
page('Scrollbar', 'Listas', 290, 'QScrollBar vertical e horizontal — sem setas',
     '<div class="spec-h">QScrollBar</div>' + grid(4, [cell('normal', 'track bg-2 · 12px\nhandle bg-5 · margem 2\nradius 4 · min 32px\n::add/sub-line 0px', vs('', 20, 60)),
                                                   cell(':hover', 'handle border-strong', vs('is-hover', 50, 60)), cell(':pressed', 'handle text-inactive', vs('is-pressed', 80, 60)),
                                                   cell(':horizontal', 'height 12px · mesmas cores', hs_)]))

# ---------- Tooltip
page('Tooltip', 'Overlays', 170, 'QToolTip',
     '<div class="spec-h">QToolTip</div><div class="spec-row">'
     + cell('padrão', 'bg surface-tooltip · border border-strong\nradius 6 · pad 6 8 · 9pt text-primary\ntítulo text-strong 600', '<span class="ar-tooltip"><b>Instalar mod</b><br>Instalar um mod a partir de um arquivo (.7z, .zip, .rar)</span>')
     + cell('curto', '', '<span class="ar-tooltip">Prioridade 16 · 2.381 arquivos</span>') + '</div>')

# ---------- ContextMenu
def mi(t, ic=None, sc='', cls='', sub=False):
    i = f'<span class="ic">{svg(I[ic], 15) if ic else ""}</span>'
    s = f'<span class="sc">{sc}</span>' if sc else ''
    if sub: s = f'<span class="sub">{svg(I["chev-r"], 14, sw=2)}</span>'
    return f'<div class="ar-mi {cls}">{i}{t}{s}</div>'
menu = ('<div class="ar-menu">' + mi('Abrir no Explorer', 'archive') + mi('Informações…', 'info', 'Enter', 'is-hover') + mi('Renomear mod…', None, 'F2')
        + mi('Reinstalar mod') + mi('Restaurar backup', None, '', 'is-disabled') + '<div class="ar-msep"></div>'
        + mi('Definir categoria', None, sub=True) + mi('Enviar para separador', None, sub=True) + '<div class="ar-msep"></div>'
        + mi('Visitar no Nexus', 'nexus') + mi('Remover mod…', None, 'Del') + '</div>')
page('ContextMenu', 'Overlays', 400, 'QMenu — menu de contexto da lista de mods',
     '<div class="spec-h">QMenu</div><div style="display:flex;gap:32px;align-items:flex-start">' + menu + '<div style="display:flex;flex-direction:column;gap:14px">'
     + cell('QMenu', 'bg surface-menu · border border-strong\nradius 6 · padding 4', '')
     + cell('::item', 'h 28 · pad 0 12 0 8 · radius 4\ncolor text-primary · atalho text-secondary 9pt', '')
     + cell('::item:selected', 'bg selection · color text-strong', '')
     + cell('::item:disabled', 'color text-disabled', '')
     + cell('::separator', '1px border · margem 4 6', '')
     + cell('::right-arrow', 'chevron-right.svg (text-secondary)', '') + '</div></div>')
print('componentes ok')
