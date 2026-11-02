import os, html
# Gera design/components/MainWindow e AccentVariants (mockups 1920x1080)
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'design', 'components')

def svg(body, size=24, vb=24, sw=1.6, extra=''):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {vb} {vb}" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" {extra}>{body}</svg>')

I = {
 'profile': '<circle cx="12" cy="8.5" r="3.5"/><path d="M5 19.5c1.2-3.3 3.9-5 7-5s5.8 1.7 7 5"/>',
 'install': '<path d="M4 8.5 12 4l8 4.5v7L12 20l-8-4.5z"/><path d="M12 9v7M9 13l3 3 3-3"/>',
 'nexus': '<circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c2.4 2.3 3.5 5 3.5 8s-1.1 5.7-3.5 8c-2.4-2.3-3.5-5-3.5-8S9.6 6.3 12 4z"/>',
 'exe': '<rect x="3.5" y="5" width="17" height="14" rx="2"/><path d="M7.5 10l2.5 2-2.5 2M12.5 14.5h4"/>',
 'tools': '<path d="M14.5 5.5a4 4 0 0 0-5 5L4 16l2 2 5.5-5.5a4 4 0 0 0 5-5l-2.3 2.3-2-2z"/>',
 'settings': '<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.2M12 18.3v2.2M3.5 12h2.2M18.3 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M6 18l1.6-1.6M16.4 7.6 18 6"/>',
 'problems': '<path d="M12 4.5 20.5 19h-17z"/><path d="M12 10v4M12 16.6v.1"/>',
 'update': '<path d="M19 12a7 7 0 0 1-12.2 4.7M5 12a7 7 0 0 1 12.2-4.7"/><path d="M17.5 3.8v3.6h-3.6M6.5 20.2v-3.6h3.6"/>',
 'help': '<circle cx="12" cy="12" r="8"/><path d="M9.8 9.6a2.3 2.3 0 1 1 3.2 2.1c-.7.3-1 .8-1 1.5v.4M12 16.4v.1"/>',
 'endorse': '<path d="M12 19.5s-7-4.2-7-9.2A3.8 3.8 0 0 1 12 8a3.8 3.8 0 0 1 7 2.3c0 5-7 9.2-7 9.2z"/>',
 'chev-d': '<path d="M7 10l5 5 5-5"/>',
 'chev-r': '<path d="M10 7l5 5-5 5"/>',
 'chev-u': '<path d="M7 14l5-5 5 5"/>',
 'search': '<circle cx="11" cy="11" r="6"/><path d="M15.5 15.5 20 20"/>',
 'play': '<path d="M8 5.5v13l10-6.5z" fill="currentColor"/>',
 'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 'filter': '<path d="M4.5 6h15l-6 7v5l-3 1.5V13z"/>',
 'note': '<path d="M6 4.5h9l3.5 3.5v11.5H6z"/><path d="M9 11h6M9 14.5h6"/>',
 'eyeoff': '<path d="M3 3l18 18M10.6 6.1A9 9 0 0 1 12 6c5 0 8.5 6 8.5 6a14 14 0 0 1-2.6 3.2M6.3 7.8A14 14 0 0 0 3.5 12S7 18 12 18a8 8 0 0 0 3.6-.8"/>',
 'warn': '<path d="M12 4.5 20.5 19h-17z"/><path d="M12 10v4M12 16.6v.1"/>',
 'archive': '<rect x="4" y="5" width="16" height="4" rx="1"/><path d="M5.5 9v10h13V9M10 13h4"/>',
 'feather': '<path d="M19 5c-6 0-11 4-12 12l-2 2M7 17h6c3 0 5-4 6-12"/><path d="M9.5 13.5H15"/>',
 'info': '<circle cx="12" cy="12" r="8"/><path d="M12 11v5M12 8v.1"/>',
 'sort': '<path d="M7 7h10M9 12h6M11 17h2"/>',
 'cog-s': '<circle cx="12" cy="12" r="2.6"/><path d="M12 4v2.4M12 17.6V20M4 12h2.4M17.6 12H20M6.4 6.4l1.7 1.7M15.9 15.9l1.7 1.7M6.4 17.6l1.7-1.7M15.9 8.1l1.7-1.7"/>',
 'min': '<path d="M6 12h12"/>', 'max': '<rect x="6.5" y="6.5" width="11" height="11" rx="1"/>', 'close': '<path d="M7 7l10 10M17 7 7 17"/>',
 'plus': '<path d="M12 6v12M6 12h12"/>',
 'skse': '<path d="M12 3.5 19 7.5v9L12 20.5 5 16.5v-9z"/><path d="M12 8v8M8.5 10l3.5 2 3.5-2"/>',
}
CHECK = '<svg viewBox="0 0 12 12" width="12" height="12"><path d="M2.5 6.2 5 8.6 9.6 3.6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def ic(name, size=16, sw=1.7, color=None):
    s = svg(I[name], size, sw=sw)
    return f'<span style="color:{color}">{s}</span>' if color else s

def bolt(color):
    return f'<svg width="14" height="14" viewBox="0 0 14 14"><path d="M8 1 3 8h3.5L5.5 13 11 5.5H7.5z" fill="{color}"/></svg>'
def conflict_glyph(kind):
    if not kind: return ''
    if kind == 'ow': return bolt('var(--flag-overwrite)')
    if kind == 'owd': return bolt('var(--flag-overwritten)')
    if kind == 'red': return bolt('var(--flag-redundant)')
    if kind == 'both':
        return ('<svg width="14" height="14" viewBox="0 0 14 14"><path d="M8 1 3 8h3.5L5.5 13z" fill="var(--flag-overwrite)"/>'
                '<path d="M8 1 5.5 13 11 5.5H7.5z" fill="var(--flag-overwritten)"/></svg>')
    if kind == 'arc': return bolt('var(--flag-overwrite)').replace('<path', '<path opacity=".55"')
    return ''

def check(on):
    return f'<span class="ar-check{" is-checked" if on else ""}">{CHECK if on else ""}</span>'

# ------------- dados
S = 'sep'
MODS = [
 (S, 'Correções', 'collapsed', '6 mods'),
 (S, 'Interface', 'open', '5 mods'),
 ('mod', 'SkyUI', 'ow', [], 'Interface', '5.2SE', 8, True, ''),
 ('mod', 'MCM Helper', '', [], 'Recursos de modding', '1.5.0', 9, True, ''),
 ('mod', 'moreHUD SE', '', ['note'], 'Interface', '5.1.1', 10, True, ''),
 ('mod', 'A Matter of Time – HUD Clock Widget', '', [], 'Interface', '3.0', 11, False, ''),
 ('mod', 'RaceMenu', 'both', [], 'Personagem', '0.4.19.16', 12, True, ''),
 (S, 'Texturas', 'open', '6 mods'),
 ('mod', 'Skyland AIO', 'owd', [], 'Texturas', '3.2', 14, True, 'ovwn'),
 ('mod', 'Noble Skyrim – Full Pack', 'both', ['eyeoff'], 'Texturas', '4.3', 15, True, 'ovwn'),
 ('mod', 'Skyrim 202X', 'both', ['note'], 'Texturas', '10.0.1', 16, True, 'sel'),
 ('mod', 'Majestic Mountains', '', [], 'Texturas', '1.75', 17, False, ''),
 ('mod', 'Realistic Water Two', 'ow', [], 'Ambiente', '1.9', 18, True, 'ovw'),
 ('mod', 'Static Mesh Improvement Mod', 'arc', [], 'Modelos e texturas', '2.2', 19, True, 'ovwa'),
 (S, 'Gameplay', 'open', '5 mods'),
 ('mod', 'Ordinator – Perks of Skyrim', 'ow', ['note'], 'Gameplay', '9.31.0', 21, True, 'rel'),
 ('mod', 'Apocalypse – Magic of Skyrim', '', [], 'Magia', '9.45', 22, True, ''),
 ('mod', 'Immersive Citizens – AI Overhaul', 'both', [], 'NPCs', '0.4.5', 23, True, ''),
 ('mod', 'Campfire', '', [], 'Sobrevivência', '1.12.1', 24, False, ''),
 ('mod', 'Frostfall', '', ['warn'], 'Sobrevivência', '3.4.1', 25, False, ''),
 (S, 'Patches', 'open', '4 mods'),
 ('mod', "Kryptopyr's Patch Hub", 'ow', [], 'Patches', '3.0', 27, True, ''),
 ('mod', 'Immersive Citizens – USSEP Patch', 'red', [], 'Patches', '1.0', 28, True, ''),
 ('mod', 'Nemesis Output', '', ['note'], 'Gerado', '—', 29, True, ''),
 ('mod', 'Synthesis Output', 'ow', [], 'Gerado', '—', 30, True, ''),
 ('ovr', 'Overwrite', 'ow', [], '', '', '', True, ''),
]

PLUGINS = [
 ('Skyrim.esm', [], 0, '00', True, ''), ('Update.esm', [], 1, '01', True, ''), ('Dawnguard.esm', [], 2, '02', True, ''),
 ('HearthFires.esm', [], 3, '03', True, ''), ('Dragonborn.esm', [], 4, '04', True, ''), ('ccBGSSSE001-Fish.esm', ['archive'], 5, '05', True, ''),
 ('ccQDRSSE001-SurvivalMode.esl', ['feather', 'archive'], 6, 'FE:000', True, ''), ('ccBGSSSE037-Curios.esl', ['feather', 'archive'], 7, 'FE:001', True, ''),
 ('ccBGSSSE025-AdvDSGS.esm', ['archive'], 8, '06', True, ''), ('Campfire.esm', [], 9, '', False, ''),
 ('Unofficial Skyrim Special Edition Patch.esp', ['archive', 'info'], 10, '07', True, ''), ('SkyUI_SE.esp', ['archive'], 11, '08', True, ''),
 ('MCMHelper.esp', ['feather'], 12, 'FE:002', True, ''), ('RaceMenu.esp', [], 13, '09', True, ''), ('RaceMenuPlugin.esp', [], 14, '0A', True, ''),
 ('RealisticWaterTwo.esp', ['archive'], 15, '0B', True, ''), ('Ordinator - Perks of Skyrim.esp', ['info'], 16, '0C', True, 'seli'),
 ('Apocalypse - Magic of Skyrim.esp', ['archive'], 17, '0D', True, ''), ('Immersive Citizens - AI Overhaul.esp', ['archive'], 18, '0E', True, ''),
 ('Frostfall.esp', ['warn'], 19, '', False, ''), ('Immersive Citizens - USSEP Patch.esp', [], 20, '0F', True, ''),
 ('Synthesis.esp', [], 21, '10', True, ''),
]

FLAG_COLOR = {'warn': 'var(--log-warning)', 'info': 'var(--log-info)'}
def flags(lst, off=False):
    out = []
    for f in lst:
        col = FLAG_COLOR.get(f)
        out.append(f'<span class="ico" style="{f"color:{col}" if col and not off else ""}">{svg(I[f], 15, sw=1.7)}</span>')
    return ''.join(out)

MODCOLS = [('Nome do mod', 452, ''), ('Conflitos', 86, ''), ('Flags', 82, ''), ('Categoria', 186, ''), ('Versão', 110, ''), ('Prioridade', 96, 'num')]

def mod_list():
    h = ['<div class="ar-head">']
    for i, (t, w, cls) in enumerate(MODCOLS):
        sorted_ = t == 'Prioridade'
        arrow = f'<span class="arrow">{svg(I["chev-u"], 12, sw=2.2)}</span>' if sorted_ else ''
        h.append(f'<div class="ar-hcell {cls}{" is-sorted" if sorted_ else ""}" style="width:{w}px">{t}{arrow}</div>')
    h.append('<div class="ar-hcell" style="flex:1"></div></div>')
    rows = []
    vis = 0
    for m in MODS:
        alt = ' alt' if vis % 2 else ''
        vis += 1
        if m[0] == S:
            _, name, state, cnt = m
            br = svg(I['chev-r' if state == 'collapsed' else 'chev-d'], 12, sw=2.2)
            rows.append(f'<div class="ar-row sep"><div class="c" style="width:{MODCOLS[0][1]}px"><span class="branch">{br}</span>{html.escape(name)}'
                        f'<span class="meta">{cnt}</span></div></div>')
            continue
        kind, name, conf, fl, cat, ver, prio, on, cls = m
        classes = ['ar-row']
        if alt: classes.append('alt')
        if not on: classes.append('off')
        if cls == 'sel': classes.append('is-selected')
        elif cls: classes.append(cls)
        if kind == 'ovr':
            classes.append('overwrite-row')
            first = f'<span class="indent" style="width:12px"></span><span class="ico">{svg(I["archive"], 15)}</span>{name}'
        else:
            first = f'<span class="indent"></span>{check(on)}<span style="overflow:hidden;text-overflow:ellipsis">{html.escape(name)}</span>'
        rows.append(f'<div class="{" ".join(classes)}">'
                    f'<div class="c" style="width:{MODCOLS[0][1]}px">{first}</div>'
                    f'<div class="c" style="width:{MODCOLS[1][1]}px">{conflict_glyph(conf)}</div>'
                    f'<div class="c" style="width:{MODCOLS[2][1]}px">{flags(fl, not on)}</div>'
                    f'<div class="c meta" style="width:{MODCOLS[3][1]}px">{cat}</div>'
                    f'<div class="c meta" style="width:{MODCOLS[4][1]}px">{ver}</div>'
                    f'<div class="c num meta" style="width:{MODCOLS[5][1]}px">{prio}</div></div>')
    sb = '<div class="ar-vscroll"><div class="h" style="top:2px;height:62%"></div></div>'
    return ''.join(h) + f'<div class="ar-body"><div style="padding-right:12px">{"".join(rows)}</div>{sb}</div>'

PCOLS = [('Nome', 400, ''), ('Flags', 92, ''), ('Prioridade', 96, 'num'), ('Índice do mod', 112, 'num')]
def plugin_list():
    h = ['<div class="ar-head">']
    for t, w, cls in PCOLS:
        sorted_ = t == 'Prioridade'
        arrow = f'<span class="arrow">{svg(I["chev-u"], 12, sw=2.2)}</span>' if sorted_ else ''
        h.append(f'<div class="ar-hcell {cls}{" is-sorted" if sorted_ else ""}" style="width:{w}px">{t}{arrow}</div>')
    h.append('<div class="ar-hcell" style="flex:1"></div></div>')
    rows = []
    for i, (n, fl, prio, idx, on, cls) in enumerate(PLUGINS):
        c = ['ar-row']
        if i % 2: c.append('alt')
        if not on: c.append('off')
        if cls == 'seli': c.append('is-selected-inactive')
        rows.append(f'<div class="{" ".join(c)}"><div class="c" style="width:400px">{check(on)}<span>{html.escape(n)}</span></div>'
                    f'<div class="c" style="width:92px">{flags(fl, not on)}</div>'
                    f'<div class="c num meta" style="width:96px">{prio}</div>'
                    f'<div class="c num meta" style="width:112px;font-family:var(--font-mono);font-size:12px">{idx or "—"}</div></div>')
    return ''.join(h) + f'<div class="ar-body">{"".join(rows)}</div>'

LOG = [
 ('16:08:12.441', 'I', 'log-info', 'Perfil "Principal" carregado — 25 de 30 mods ativos, 20 de 22 plugins'),
 ('16:08:12.503', 'D', 'log-debug', 'estrutura virtual montada: 1.284.112 arquivos, 412 conflitos de arquivo solto, 37 de BSA'),
 ('16:08:13.017', 'W', 'log-warning', '"Frostfall.esp" tem master ausente: Campfire.esm (o mod "Campfire" está desativado)'),
 ('16:08:14.220', 'I', 'log-info', 'Download concluído: Skyrim 202X 10.0.1 – Architecture PART 1 (2,1 GB)'),
 ('16:08:15.902', 'E', 'log-error', 'Falha ao consultar a API do Nexus para "Majestic Mountains": tempo esgotado (tentativa 1 de 3)'),
]

def toolbar():
    L = [('profile', 'Perfis'), ('install', 'Instalar mod', 'hover'), ('nexus', 'Nexus'), None, ('exe', 'Executáveis'), ('tools', 'Ferramentas'), ('settings', 'Configurações')]
    R = [('endorse', 'Endossar MO2'), ('problems', 'Problemas', 'badge'), ('update', 'Atualizar'), ('help', 'Ajuda')]
    def btn(t):
        if t is None: return '<span style="width:1px;height:24px;background:var(--border);margin:0 8px"></span>'
        cls = ' is-hover' if len(t) > 2 and t[2] == 'hover' else ''
        badge = '<span class="badge">2</span>' if len(t) > 2 and t[2] == 'badge' else ''
        col = 'style="color:var(--log-warning)"' if t[0] == 'problems' else ''
        return f'<span class="ar-tool{cls}" {col}>{svg(I[t[0]], 24)}{badge}</span>'
    return (f'<div style="height:48px;display:flex;align-items:center;gap:4px;padding:0 10px;background:var(--bg-1);border-bottom:1px solid var(--border)">'
            + ''.join(btn(t) for t in L) + '<span style="flex:1"></span>' + ''.join(btn(t) for t in R) + '</div>')

def window(tooltip=True):
    title = ('<div style="height:32px;display:flex;align-items:center;padding-left:12px;background:var(--bg-0);color:var(--text-secondary);font-size:12px;gap:10px">'
             f'<span style="color:var(--accent-text)">{svg(I["skse"], 16)}</span>Mod Organizer v2.5.2 — Skyrim Special Edition — Principal'
             '<span style="flex:1"></span>' + ''.join(f'<span style="width:46px;height:32px;display:flex;align-items:center;justify-content:center">{svg(I[k], 16, sw=1.4)}</span>' for k in ('min', 'max', 'close')) + '</div>')
    menubar = ('<div style="height:26px;display:flex;align-items:center;padding:0 6px;background:var(--bg-1);font-size:13px">'
               + ''.join(f'<span style="padding:3px 10px;border-radius:4px{";background:var(--bg-4);color:var(--text-strong)" if i == 99 else ""}">{t}</span>' for i, t in enumerate(['Arquivo', 'Exibir', 'Ferramentas', 'Ajuda'])) + '</div>')
    left = f'''
<div style="position:absolute;left:10px;top:10px;width:1124px;bottom:0;display:flex;flex-direction:column;gap:8px">
  <div style="display:flex;align-items:center;gap:8px;height:28px">
    <span style="color:var(--text-secondary);font-size:12px">Perfil</span>
    <span class="ar-combo" style="width:280px"><span class="val"><span style="color:var(--accent-text)">{svg(I["profile"], 16)}</span>Principal</span><span class="dd">{svg(I["chev-d"], 14, sw=2)}</span></span>
    <span class="ar-btn" style="padding:0 8px" title="Configurações do perfil">{svg(I["cog-s"], 16)}</span>
    <span style="flex:1"></span>
    <span style="color:var(--text-secondary);font-size:12px">Ativos <b style="color:var(--text-primary);font-weight:600">25</b> de 30 · Plugins <b style="color:var(--text-primary);font-weight:600">20</b> de 22</span>
  </div>
  <div class="ar-view" style="flex:1">{mod_list()}</div>
  <div style="display:flex;align-items:center;gap:8px;height:28px">
    <span class="ar-input" style="flex:1"><span class="ico">{svg(I["search"], 15)}</span><span class="ph">Filtrar mods por nome…</span></span>
    <span class="ar-combo" style="width:190px"><span class="val">Sem agrupamento</span><span class="dd">{svg(I["chev-d"], 14, sw=2)}</span></span>
    <span class="ar-btn">{svg(I["filter"], 15)}Filtros</span>
  </div>
</div>'''
    tabs = [('Plugins', True, '20/22'), ('Arquivos (BSA)', False, ''), ('Data', False, ''), ('Saves', False, ''), ('Downloads', False, '3')]
    tabhtml = ''.join(f'<span class="ar-tab{" is-active" if a else ""}{" is-hover" if t == "Saves" else ""}">{t}{f"<span class=count>{c}</span>" if c else ""}</span>' for t, a, c in tabs)
    right = f'''
<div style="position:absolute;left:1146px;right:10px;top:10px;bottom:0;display:flex;flex-direction:column">
  <div style="display:flex;align-items:center;gap:8px;height:28px;margin-bottom:10px">
    <span class="ar-combo" style="flex:1"><span class="val"><span style="color:var(--accent-text)">{svg(I["skse"], 16)}</span>SKSE</span><span class="dd">{svg(I["chev-d"], 14, sw=2)}</span></span>
    <span class="ar-btn ar-btn--primary" style="width:132px;justify-content:center">{svg(I["play"], 14)}Executar</span>
    <span class="ar-btn">{svg(I["link"], 15)}Atalho</span>
  </div>
  <div class="ar-tabs">{tabhtml}</div>
  <div class="ar-pane" style="flex:1;display:flex;flex-direction:column;padding:8px;gap:8px;min-height:0">
    <div style="display:flex;align-items:center;gap:8px;height:28px">
      <span class="ar-btn">{svg(I["sort"], 15)}Ordenar (LOOT)</span>
      <span class="ar-btn is-disabled">Restaurar backup</span>
      <span style="flex:1"></span>
      <span style="color:var(--text-secondary);font-size:12px">Ativos <b style="color:var(--text-primary);font-weight:600">20</b> de 22</span>
    </div>
    <div class="ar-view" style="flex:1;border-radius:4px">{plugin_list()}</div>
    <span class="ar-input is-focus" style="height:28px"><span class="ico">{svg(I["search"], 15)}</span><span class="ph">Filtrar plugins…</span></span>
  </div>
</div>'''
    loglines = ''.join(f'<div style="display:flex;gap:14px;height:20px;align-items:center;padding:0 10px;{"background:var(--bg-2-alt)" if i % 2 else ""}">'
                       f'<span style="color:var(--text-inactive)">{t}</span><span style="color:var(--{c});font-weight:700;width:10px">{lv}</span>'
                       f'<span style="color:{"var(--text-primary)" if lv != "D" else "var(--text-inactive)"}">{html.escape(msg)}</span></div>' for i, (t, lv, c, msg) in enumerate(LOG))
    log = f'''
<div style="height:150px;background:var(--bg-1);border-top:1px solid var(--border);display:flex;flex-direction:column">
  <div style="height:28px;display:flex;align-items:center;padding:0 12px;gap:8px;color:var(--text-secondary);font-size:12px;font-weight:600">Log
    <span style="flex:1"></span><span style="font-weight:400">Nível: Info</span>{svg(I["chev-d"], 12, sw=2)}</div>
  <div style="flex:1;margin:0 10px 8px;background:var(--bg-0);border:1px solid var(--border);border-radius:4px;font-family:var(--font-mono);font-size:12px;line-height:18px;overflow:hidden;padding-top:3px">{loglines}</div>
</div>'''
    status = ('<div class="ar-statusbar"><span style="color:var(--text-primary)">Pronto</span><span>Skyrim Special Edition 1.6.1170 · SKSE 2.2.6</span><span style="flex:1"></span>'
              '<span>API Nexus 2.384 / 2.500</span><span style="color:var(--log-warning)">2 problemas</span><span>v2.5.2</span></div>')
    tip = ''
    if tooltip:
        tip = ('<div class="ar-tooltip" style="position:absolute;left:66px;top:114px;z-index:5"><b>Instalar mod</b><br>Instalar um mod a partir de um arquivo (.7z, .zip, .rar)</div>')
    main_h = 1080 - 32 - 26 - 48 - 150 - 24
    return (f'<div class="ar mo2" style="position:relative;width:1920px;height:1080px;background:var(--bg-1);overflow:hidden;display:flex;flex-direction:column">'
            f'{title}{menubar}{toolbar()}<div style="position:relative;height:{main_h}px;padding-bottom:10px">'
            f'<div class="ar-splitter" style="position:absolute;left:1136px;top:10px;bottom:0;width:6px;display:flex;align-items:center;justify-content:center"><span style="width:2px;height:28px;border-radius:1px;background:var(--border-strong)"></span></div>'
            f'{left}{right}</div>{log}{status}{tip}</div>')

HEAD = '''<!doctype html>
<html><head><meta charset="utf-8"><title>{t}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:var(--bg-0)}}</style>
</head><body>
'''

def write(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(s)

def main():
    # MainWindow
    write(os.path.join(BASE, 'MainWindow', 'preview.html'),
          '<!-- @dsCard group="Mockups" width=1920 height=1080 subtitle="Janela principal 1920×1080 no tema atual" -->\n'
          + HEAD.format(t='Janela principal — Ardósia') + window() + '\n</body></html>\n')

    # AccentVariants
    blocks = []
    for tid, tname, hexv in [('ambar', 'Âmbar dourado', '#E2A74A'), ('gelo', 'Azul gelo', '#7CC6EA'), ('esmeralda', 'Verde-esmeralda', '#33C79B')]:
        blocks.append(f'<section data-theme="{tid}" style="background:var(--bg-0);padding:0 0 28px">'
                      f'<div class="ar" style="height:72px;display:flex;align-items:center;gap:14px;padding:0 4px">'
                      f'<span style="width:28px;height:28px;border-radius:6px;background:var(--accent)"></span>'
                      f'<span style="font-size:26px;line-height:30px;font-weight:600;color:var(--text-strong)">{tname}</span>'
                      f'<span style="font-family:var(--font-mono);font-size:15px;color:var(--accent-text)">accent {hexv}</span></div>'
                      f'{window(tooltip=False)}</section>')
    write(os.path.join(BASE, 'AccentVariants', 'preview.html'),
          '<!-- @dsCard group="Mockups" width=1920 height=3540 subtitle="A mesma janela com cada uma das 3 cores de acento" -->\n'
          + HEAD.format(t='Variações de acento — Ardósia') + '<div style="padding:12px 0 0">' + ''.join(blocks) + '</div>\n</body></html>\n')

if __name__ == '__main__':
    main()
    print('mockups ok')
