# AGENTS.md — Schema da wiki-vinhedo (Alma Gerais)

Este é o arquivo de configuração que transforma o agente em um **mantenedor disciplinado da wiki**,
e não em um chatbot genérico. Leia este arquivo inteiro antes de qualquer operação.

Padrão de referência: [LLM Wiki (Karpathy)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## 1. Papéis e camadas

- `raw/` — **fontes brutas, imutáveis após a entrada**. A rotina pode acrescentar uma nova fonte
  uma única vez; depois disso, o agente nunca a edita nem apaga. É a fonte da verdade.
- `raw/publicacoes/` reúne as publicações curadas pelo time, sem subdivisões temáticas. Essa coleção
  local é uma base preferencial, mas **não limita a pesquisa**: o agente tem liberdade para buscar
  conhecimento externo sempre que isso ajudar a responder, interpretar ou recomendar.
- `wiki/` — **conhecimento que você gera e mantém**. Você é o dono desta camada.
- `dados-vivos/` — **documentação de acesso** às APIs vivas (clima via WS Clima; gestão da vinícola
  via InnoVint/Sutter). Aqui ficam playbooks de consulta, IDs da Alma Gerais e exemplos HTTP
  reutilizáveis — **não** a documentação oficial completa (essa fica no link externo).
  **Não** copie dados crus das APIs para o repositório; consulte em tempo real e **arquive apenas
  as sínteses** na `wiki/`.
- `AGENTS.md` — este schema. Coevolui com o time.

Navegação: `index.md` (catálogo de conteúdo) e `log.md` (histórico cronológico da wiki).

---

## 2. Idioma e escopo

- **Todo o conteúdo em português.** Nomes de pastas, arquivos e páginas em português, sem acentos e
  em `kebab-case` (ex.: `sao-geraldo.md`, `fitossanidade.md`).
- Esta wiki é **exclusiva da Alma Gerais**. Não generalizar para "template replicável".
- **Foco atual: apenas Macaia** (`macaia`). A estrutura é **multi-local** por design (campos
  `local`/`locais`, pasta `wiki/locais/`). **São Geraldo** (`sao-geraldo`) é expansão futura: quando
  entrar, basta criar `wiki/locais/sao-geraldo.md` e incluir o slug nos frontmatters — nada mais muda.

---

## 3. Regra de ouro: FATO ≠ INTERPRETAÇÃO

Este é o princípio mais importante da wiki.

- **Fatos** (o que aconteceu, quando, onde) vivem em `wiki/eventos/`, `wiki/safras/` e nas páginas
  de entidade. Nunca embuta causa em um fato.
- **Interpretações** (por que pode ter acontecido, o que se relaciona com o quê) vivem em
  `wiki/correlacoes/` e `wiki/hipoteses/`. Toda interpretação **deve**:
  - citar os eventos/fontes datados que a sustentam;
  - explicitar a **defasagem temporal** quando houver (ex.: "~2 meses depois");
  - registrar um **nível de confiança** (`baixa` | `media` | `alta`);
  - deixar claro que **correlação não implica causalidade**.

Nunca contamine o registro factual com suposição.

---

## 4. Ancoragem temporal (obrigatória)

Para o agente conseguir ligar os pontos no tempo ("isto hoje pode ter relação com aquilo de 2 meses
atrás"), **toda página factual carrega âncoras temporais** no frontmatter:

- `data` (ou `data_inicio` + `data_fim` para períodos), no formato `AAAA-MM-DD`.
- `safra` (ano da safra).
- `estagio_fenologico` — âncora tão importante quanto a data. Valores: `dormencia`, `brotacao`,
  `floracao`, `pegamento`, `crescimento-baga`, `veraison`, `maturacao`, `colheita`, `pos-colheita`.
- `local`, `setor(es)`, `rua(s)`, `quadra(s)` e `variedade(s)` quando aplicável.

Nos registros de manejo e dos ciclos da videira, `setores` é obrigatório e `ruas` é opcional.
`data` representa quando o fato ocorreu ou foi observado; `ingerido_em` registra quando a rotina o
incorporou. Não substitua uma pela outra.

Nomes de arquivos de evento **começam pela data** para ordenarem sozinhos no tempo:
`AAAA-MM-DD-local-descricao-curta.md`.
Para eventos de campo, inclua o setor:
`AAAA-MM-DD-macaia-setor-<codigo>-descricao-curta.md`.

---

## 5. Frontmatter por tipo de página (YAML)

Sempre inicie páginas com frontmatter YAML. Campos comuns: `tipo`, `titulo`, `tags`, `fontes`
(lista de caminhos em `raw/` ou `dados-vivos/` e/ou URLs externas), `atualizado_em`.

**Evento** (`wiki/eventos/`):
```yaml
---
tipo: evento
categoria: clima        # clima | manejo | fenologia | analise | fitossanidade | qualidade | colheita | observacao
data: 2026-06-15
ingerido_em: 2026-06-16
local: macaia
setores: [setor-03]
ruas: []
quadras: [q3]
variedades: [syrah]
safra: 2026
ciclo: null
estagio_fenologico: maturacao
tags: [geada]
fontes: [raw/registros-ciclos-videira/2026-06-15-macaia.md]
granola_id: null
atualizado_em: 2026-06-16
---
```

**Setor** (`wiki/setores/`): `tipo: setor`, `codigo`, `local`, `ruas`, `variedades`, `quadras`,
`area_ha`, `fontes`.

**Quadra** (`wiki/quadras/`): `tipo: quadra`, `local`, `setores`, `variedades`, `porta_enxerto`,
`ano_plantio`, `area_ha`, `espacamento`, `sistema_conducao`.

**Variedade** (`wiki/variedades/`): `tipo: variedade`, `locais`, `setores`, `quadras`, `tags`.

**Safra** (`wiki/safras/`): `tipo: safra`, `ano`, `locais`.

**Histórico mensal de setor** (`wiki/historicos/setores/`): `tipo: historico-mensal-setor`,
`setor`, `ano`, `mes`, `data_inicio`, `data_fim`. É um índice factual regenerável, nunca a fonte
primária do evento.

**Vinho** (`wiki/vinhos/`): `tipo: vinho`, `variedades`, `safras`.

**Produto** (`wiki/produtos/`): `tipo: produto`. Sintetiza o documento em `raw/fichas-tecnicas/`.
Não é fato de campo: o que a bula diz não entra em `wiki/eventos/`.

**Tema** (`wiki/temas/`): `tipo: tema`.

**Correlação** (`wiki/correlacoes/`): `tipo: correlacao`, `defasagem`, `confianca`, `eventos: [...]`.

**Hipótese** (`wiki/hipoteses/`): `tipo: hipotese`, `status` (`aberta` | `em-teste` | `apoiada` |
`refutada`), `confianca`.

**Recomendação** (`wiki/recomendacoes/`): `tipo: recomendacao`, `origem` (`agronomica` |
`enologica` | `agente`), `status` (`questionada` | `validada` | `sugerida` | `aplicada`).

---

## 6. Ligações (grafo)

- Use wikilinks `[[nome-do-arquivo]]` (compatível com Obsidian) para conectar páginas.
- **Ligações bidirecionais**: ao criar uma correlação/hipótese, adicione um link de volta a partir
  das páginas de setor/quadra/variedade/safra/evento envolvidas.
- Todo evento de campo aponta para seu setor. O histórico mensal aponta para os eventos e para o
  setor; a página do setor aponta para seus históricos mensais.
- Entidades, gabaritos e históricos mensais novos entram no `index.md`. Eventos atômicos ficam
  catalogados nos históricos mensais e nas safras, sem inflar o índice raiz.

---

## 7. Estrutura de pastas

```
raw/            fontes brutas imutáveis (espelha as fontes do caderno)
  publicacoes/  todas as publicações, sem subdivisões temáticas
  fichas-tecnicas/
    comercial/  fichas de produtos comerciais
    biologicos/ fichas de produtos biológicos
  analises/     análises de solo, planta e outras matrizes
  qualidade-uva/    resultados físico-químicos, sanitários e sensoriais
  qualidade-vinho/  resultados de flor, prensa e outras avaliações
  consultoria/  relatórios de consultoria atualmente agronômica
  registros-manejo/ registros datados das operações de manejo
  registros-ciclos-videira/ registros datados dos ciclos e estágios fenológicos
  mapa-plantio/ mapas, fotos de drone, variedades plantadas
  assets/       imagens/anexos
wiki/
  overview.md   síntese geral
  locais/       macaia (São Geraldo = expansão futura)
  setores/      cadastro canônico dos setores do vinhedo
  quadras/      páginas por quadra/talhão
  variedades/   páginas por variedade
  safras/       hub temporal: uma página por ano
  vinhos/       páginas por produto
  produtos/     fichas de produtos comerciais e biológicos
  temas/        solo, clima, irrigacao, nutricao, fitossanidade, poda-desfolha...
  eventos/      fatos atômicos, datados e ancorados por setor quando forem de campo
  historicos/
    setores/    índices mensais por setor; um subdiretório por setor
  correlacoes/  correlações descobertas (com defasagem e confiança)
  hipoteses/    hipóteses em acompanhamento
  recomendacoes/ recomendações questionadas | validadas | sugeridas
dados-vivos/    estacao-meteorologica.md | gestao-vinicola.md | queries/
tools/          granola-ingeridos.py (idempotência) | validar-wiki.py (lint estrutural)
.cursor/skills/ ingerir-gravacoes-granola/ | consultar-historico-setorial/
```

Arquivos `_modelo-*.md` são **gabaritos**; copie-os ao criar páginas novas.

---

## 8. Operações

### Ingerir

Toda ingestão de gravações do Granola segue a skill
`.cursor/skills/ingerir-gravacoes-granola/SKILL.md`, que detalha a execução na ordem correta e as
armadilhas conhecidas da transcrição automática. O usuário não precisa pedir a skill. As regras
abaixo continuam valendo e prevalecem em caso de conflito.

0. **Antes de puxar qualquer coisa**, rode `python3 tools/granola-ingeridos.py`. Ele lê o
   repositório e informa a data da gravação mais recente já ingerida — use-a para definir a janela
   de consulta ao Granola. Com os IDs em mão, rode
   `python3 tools/granola-ingeridos.py <id> ...` para classificar cada um:
   - `NOVO` — ingerir;
   - `JA INGERIDO` — fonte e páginas já existem; não duplicar nada;
   - `SO FONTE` — a fonte existe, mas nenhuma página foi gerada (pendência aberta). Não recriar a
     fonte; se a informação que faltava chegou, resolva a pendência criando os eventos;
   - `NO LOG` — sem fonte, porém citada no `log.md` (por exemplo, gravação descartada por não
     tratar do vinhedo). Leia a entrada antes de decidir.
1. A rotina diária puxa cada gravação do Granola e salva uma única cópia imutável em
   `raw/registros-manejo/` ou `raw/registros-ciclos-videira/`, conforme o registro. Uma gravação
   mista continua sendo uma única fonte, mesmo que origine eventos de categorias diferentes.
2. Use `granola_id` como chave de idempotência. Se esse ID já tiver sido ingerido, não duplique a
   fonte, o evento nem os links dos índices. O registro de idempotência **é o próprio repositório**:
   todo arquivo em `raw/registros-*/` carrega `granola_id` no frontmatter, e cada página derivada
   repete o ID. Não existe estado fora do repo.
3. Divida a gravação em eventos factuais homogêneos. Diferenças de data, setor, operação,
   observação ou estágio fenológico exigem eventos separados.
4. Para manejo e fenologia, valide `data`, `setores`, `safra`, `estagio_fenologico`, `fontes`,
   `granola_id` e `ingerido_em`. Registre `ruas` quando informadas.
5. Não adivinhe setor, rua, data, ciclo ou estágio. Preserve a fonte e registre uma entrada
   `pendencia` em `log.md` com o campo ambíguo, sem criar um fato falsamente preciso.
6. Crie ou atualize o índice mensal de cada setor em
   `wiki/historicos/setores/<setor>/AAAA-MM-<setor>.md`, mantendo uma linha por evento, em ordem
   cronológica. Não copie a narrativa completa do evento para o histórico.
7. Atualize as páginas de setor, variedade, safra e tema afetadas. Adicione o evento à linha do
   tempo da safra e o histórico mensal ao `index.md` quando o mês surgir pela primeira vez.
8. Adicione uma entrada `ingest` em `log.md`. A rotina de ingestão não precisa carregar históricos
   anteriores nem propor relações; seu papel é registrar e indexar os fatos corretamente.
9. Cite a gravação pelo prefixo de 8 caracteres do `granola_id` nas entradas de `log.md`, inclusive
   ao descartar uma gravação. É assim que `tools/granola-ingeridos.py` reconhece o estado `NO LOG` e
   evita que a mesma nota volte à fila a cada rodada.
10. Feche a ingestão rodando `python3 tools/validar-wiki.py`. Ele confere frontmatter, wikilinks,
    âncoras temporais e existência das fontes citadas; erros devem ser resolvidos antes do commit.

### Consultar
1. Leia primeiro o `index.md` para achar páginas relevantes; depois aprofunde.
2. Para qualquer pergunta relacionada a setor, rua, evolução, comparação ou possível padrão de
   campo, use a skill `.cursor/skills/consultar-historico-setorial/SKILL.md`. Ela define quando e
   como abrir os históricos mensais e os eventos completos; o usuário não precisa pedir essa busca.
3. Para outras perguntas temporais, varra `wiki/eventos/` por data/estágio fenológico e a linha do
   tempo da(s) safra(s).
4. Consulte as APIs vivas quando precisar de números atuais (ver `dados-vivos/`).
5. Responda **com citações** (links para páginas e caminhos de fontes).
6. Arquive boas respostas de volta como páginas novas (ex.: uma correlação descoberta).

### Pesquisar conhecimento externo
- O agente pode pesquisar fontes externas sempre que julgar útil; `raw/publicacoes/` não é uma
  fronteira do conhecimento.
- Dê preferência a estudos revisados por pares, instituições técnicas e fontes primárias ligadas à
  viticultura em **clima tropical**, especialmente quando forem aplicáveis às condições de Minas
  Gerais. Referências de clima subtropical, temperado ou de outros países também podem ser usadas
  quando ajudarem a estabelecer padrões ou trouxerem conhecimento transferível.
- Registre título, autoria ou instituição, URL/DOI e data da consulta. Quando uma síntese usar fonte
  externa, inclua a URL em `fontes` e descreva no corpo da página por que ela é aplicável a Macaia.
- Conhecimento externo embasa interpretações e recomendações, mas não transforma uma generalização
  bibliográfica em fato observado na Alma Gerais. Fatos do vinhedo continuam exigindo fonte datada.

### Revisar (lint)
- Contradições entre páginas; afirmações vencidas por fontes novas; páginas órfãs; conceitos sem
  página própria; referências cruzadas faltando; lacunas que uma consulta às APIs preencheria.
- Sugira novas perguntas e fontes a buscar.

---

## 9. Dados vivos (APIs — WS Clima e InnoVint)

- Clima (WS Clima) e gestão da vinícola (InnoVint/Sutter) são consultados **em tempo real**, não
  copiados para o repo.
- O agente **não** deve reinventar a integração a cada pergunta: leia primeiro o playbook em
  `dados-vivos/` (auth, URL base, endpoints úteis, IDs Alma Gerais, exemplos). Use a documentação
  oficial só para detalhes de parâmetros/campos que o playbook não cobre.
- Credenciais vivem em variáveis de ambiente/secrets — **nunca** em arquivos do repositório.
- Ao usar dados vivos numa síntese, registre a **data da consulta**, a API e o endpoint/parâmetros
  como `fontes` (ex.: `dados-vivos/estacao-meteorologica.md` + `GET .../data/historical/...`).
- Exemplos HTTP reutilizáveis em `dados-vivos/queries/`.

---

## 10. Log

`log.md` é **append-only** e cronológico. Cada entrada começa com um prefixo consistente para ser
filtrável por ferramentas unix:

```
## [AAAA-MM-DD] ingest | <título da fonte>
## [AAAA-MM-DD] query  | <pergunta>
## [AAAA-MM-DD] lint   | <resumo>
## [AAAA-MM-DD] pendencia | <fonte e campo ambíguo>
```

`grep "^## \[" log.md | tail -5` mostra as 5 últimas entradas.

---

## Cursor Cloud specific instructions

Este repositório é uma **base de conhecimento em Markdown**, não uma aplicação com build/testes.
Não há dependências para instalar, nem serviço para subir, nem suíte de testes automatizados.

- Não existe "servidor" para rodar. Trabalhe editando os arquivos `.md` conforme as convenções acima.
- Validação = coerência do conteúdo: âncoras temporais presentes, `index.md`/`log.md` atualizados,
  wikilinks válidos e separação fato/interpretação respeitada.
- Preserve `raw/` como imutável.
