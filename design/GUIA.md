Ardósia é um tema escuro para o Mod Organizer 2, feito para sessões longas de modding. A base é cinza-azulada (nunca preto puro) e há **uma** cor de destaque, em três versões: Âmbar dourado (padrão), Azul gelo e Verde-esmeralda. Tudo aqui pode ser escrito em Qt Style Sheet (.qss): cores sólidas ou rgba, bordas de 1px, raios de 3–6px, padding e ícones SVG. Não há sombra, blur, gradiente nem animação.

As três versões de acento são os **temas** deste sistema. Troque o tema na página e todos os mockups e componentes mudam junto. Só os tokens `accent*`, `selection`, `accent-subtle` e as duas cores de conflito "sobrescreve" mudam entre eles. O resto é idêntico.

## Princípios

1. **As cores do MO2 têm prioridade.** O MO2 pinta o fundo da linha inteira para indicar conflitos, plugins relacionados e separadores. O tema nunca define `background` em `::item` (nem em `:hover`). Fundo só na view (`background`, `alternate-background-color`) e na seleção.
2. **Estrutura legível de relance.** Os separadores ficam em `separator-bg`, um tom opaco claramente acima das linhas, com texto `text-strong` e seta de ramo na cor de acento.
3. **Ativo × desativado.** Mods e plugins ativos ficam em `text-primary`. Os desativados ficam em `text-inactive`, esmaecidos mas ainda legíveis (4,4:1).
4. **Acento com moderação.** `accent` aparece só em: botão Executar, checkbox marcado, indicador da aba ativa, borda de foco, seta de ordenação e seta dos separadores. Nunca em grandes áreas.
5. **Estados sempre visíveis.** Todo controle tem hover (fundo um nível acima e borda `border-strong`), pressionado (mais um nível), foco (borda `accent`) e desabilitado (`text-disabled`).

## Cor

Superfícies, do fundo mais profundo ao mais elevado:

| Token | Hex | Onde |
|---|---|---|
| `bg-0` | `#12161B` | Campos de texto (inset), log, barra de título |
| `bg-1` | `#171B21` | Janela, toolbar, menubar, status bar, cabeçalhos de coluna |
| `bg-2` | `#1C2128` | Base das listas, painel das abas, aba ativa |
| `bg-2-alt` | `#20262E` | Linhas alternadas |
| `bg-3` | `#262C35` | Botões, combos, aba em hover |
| `bg-4` | `#2F3640` | Hover de controles |
| `bg-5` | `#39414C` | Pressionado; handle da scrollbar |
| `surface-menu` | `#20262E` | QMenu, popup de combo |
| `surface-tooltip` | `#2C333D` | QToolTip |
| `separator-bg` | `#2A3546` | Separadores de mods (configuração do MO2) |

Bordas: `border-subtle` `#252B33` (divisórias internas), `border` `#323A45` (padrão), `border-strong` `#47515E` (hover e overlays), `border-control` `#6B7684` (checkbox desmarcado, ≥3:1).

Texto (contraste sobre `bg-2`): `text-strong` `#F2F5F8` · `text-primary` `#D9DFE6` (12,1:1) · `text-secondary` `#97A2B0` (6,3:1) · `text-inactive` `#7B8696` (4,4:1) · `text-disabled` `#525B67` (só controles desabilitados) · `text-on-accent` `#14181D`.

Acento por tema:

| Token | Âmbar | Gelo | Esmeralda |
|---|---|---|---|
| `accent` | `#E2A74A` | `#7CC6EA` | `#33C79B` |
| `accent-hover` | `#ECB965` | `#98D3F0` | `#52D4AD` |
| `accent-pressed` | `#C48D34` | `#5DAED6` | `#27A882` |
| `accent-text` | `#E9B35E` | `#8DCDEE` | `#4FD1AA` |
| `selection` | `rgba(226,167,74,.24)` | `rgba(124,198,234,.22)` | `rgba(51,199,155,.26)` |
| `accent-subtle` | `rgba(226,167,74,.12)` | `rgba(124,198,234,.11)` | `rgba(51,199,155,.12)` |

`text-on-accent` sobre `accent` fica entre 8,3:1 e 9,4:1 nos três temas. A seleção sem foco é sempre neutra: `selection-inactive` `rgba(151,162,176,.18)`.

### Cores de conflito (Settings do MO2 › aba Theme › Colors)

Essas cores **não** vão no .qss. Elas são definidas na janela de configurações do MO2, que aceita alfa. Por serem translúcidas, somam com a alternância de linhas em vez de esconder a lista.

| Configuração do MO2 | Token | Valor (#RRGGBBAA) |
|---|---|---|
| Is overwriting (loose files) | `conflict-overwriting` | `#50BE643D` (Esmeralda: `#A0C8463D`) |
| Is overwritten (loose files) | `conflict-overwritten` | `#E8564E47` |
| Is overwriting (archives) | `conflict-overwriting-archive` | `#50BE641C` (Esmeralda: `#A0C8461C`) |
| Is overwritten (archives) | `conflict-overwritten-archive` | `#E8564E1F` |
| Mod contains selected file / Plugin is contained in selected mod | `related-highlight` | `#9680F042` |

A cor de separador não fica nessa tabela: é definida por separador, com clique direito › Select Color... (token `separator-bg`, `#2A3546`).

`text-primary` mantém ≥6,8:1 sobre todas essas camadas. No tema Esmeralda, o verde de "sobrescreve" puxa para o lima, para não ser confundido com a seleção. Vermelho e verde também diferem pelo glifo de raio na coluna Conflitos, então a informação não depende só da cor.

Log: `log-info` `#7FB8F0`, `log-warning` `#E5B350`, `log-error` `#F27A72` e `log-debug` (= `text-inactive`), todos sobre `bg-0`.

## Tipografia

Família: `"Segoe UI Variable Text", "Segoe UI"` no Windows (Inter fica de fallback nas prévias). Monoespaçada: `"Cascadia Mono", Consolas`. Em QSS use pt. Equivalência a 96 dpi: 10pt ≈ 13px e 9pt = 12px.

| Estilo | QSS | Uso |
|---|---|---|
| `body` | 10pt, 400 | Base de todo widget, listas, campos, menus |
| `body-strong` | 10pt, 600 | Aba selecionada, botão primário |
| `label` | 9pt, 400 | Status bar, contadores, atalhos de menu, tooltip |
| `header` | 9pt, 600, `text-secondary` | Cabeçalhos de coluna |
| `caption` | 8pt, 600 | Badges |
| `mono` | 9pt, Cascadia Mono | Log |

## Espaçamento, dimensões e raios

- Linha de lista: **26px** (texto de 18px + `padding: 4px 8px` no `::item`). Cabeçalho: 26px. Controles: 28px. Abas: 30px. Toolbar: botões de 36px com ícone de 24px.
- Escala de espaçamento: 2 · 4 · 6 · 8 · 12 · 16 · 24px. Painéis com 8–10px de margem; controles na mesma barra com 8px de gap.
- Raios: `radius-sm` 3px (checkbox), `radius-md` 4px (botões, campos, handle, item de menu), `radius-lg` 6px (abas no topo, painel, menus, tooltip, molduras).
- Todas as bordas têm 1px. A única exceção é o indicador da aba ativa: `border-top: 2px` em `accent`.
- Checkbox de 16px (o padrão do Qt é 13px). Scrollbar de 12px, com handle de 8px e sem setas.

## Iconografia

O tema traz 19 SVGs de 16px no grupo de assets **QSS**: check (escuro, para ir sobre o acento), parcial, desabilitado, chevrons neutros e, para cada acento, setas de ordenação e de ramo da árvore. Referencie-os no .qss com caminho relativo à pasta do tema, por exemplo `url(./ardosia/check.svg)`. Os ícones da toolbar e os glifos das colunas Conflitos/Flags vêm do próprio MO2 e não mudam com o .qss. Nos mockups eles aparecem em `text-secondary` como referência.

## Limites do QSS (o que depende do MO2)

- **Destaque dos separadores.** Uma regra QSS não consegue selecionar só as linhas de separador. O fundo vem da cor de separador do MO2 (use `separator-bg`). A seta de acento vem de `::branch`, e o peso do texto depende da versão do MO2. Não dá para dar altura extra a uma única linha: a altura é uniforme.
- **Mods desativados esmaecidos.** O próprio MO2 pinta esse texto. `text-inactive` é a referência visual, e nas listas de plugins o comportamento é o mesmo.
- **Hover nas listas.** Se você definir `::item:hover { background }`, a cor de conflito some sob o cursor. Por isso o tema muda só `color`.
- **Barra de título.** É nativa do Windows e fica fora do QSS.
- **Placeholder dos campos.** A cor vem da paleta do Qt (PlaceholderText), não de uma propriedade do QSS. O valor de referência é `text-inactive`.

A referência seletor por seletor, com todos os valores prontos para o .qss, está na seção **Referência QSS**.
