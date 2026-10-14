---
name: ingerir-gravacoes-granola
description: Ingere gravações do Granola (agrônomo e equipe) na wiki da Alma Gerais. Use quando o pedido envolver ingestão, ingerir, processar gravações, notas do Granola, registros novos de campo, atualizar o brain com o que foi gravado, ou puxar o que o agrônomo registrou.
---

# Ingerir gravações do Granola

Procedimento obrigatório de ingestão. O `AGENTS.md` define as **regras** (schema, frontmatter, fato
≠ interpretação); esta skill define a **execução**, na ordem, com as armadilhas já conhecidas.

Papel da ingestão: registrar e indexar fatos corretamente. Não é hora de propor correlações,
hipóteses ou recomendações próprias.

Rodando pela Automation diária do Cursor, o texto das instruções e a configuração recomendada estão
em `automacao-diaria.md`, nesta mesma pasta. Ao mudar o procedimento aqui, revise aquele arquivo.

## 1. Confirmar a conta do Granola

Chame `get_account_info` e informe ao usuário o e-mail e o workspace. Se a busca de gravações voltar
vazia, **avise que pode ser a conta errada** em vez de concluir que não há registros.

## 2. Definir a janela e o que já foi processado

```bash
python3 tools/granola-ingeridos.py
```

Ele informa a data da gravação mais recente já ingerida. Consulte o Granola dessa data em diante
(`list_meetings` com `time_range: custom`), colete os ids e classifique:

```bash
python3 tools/granola-ingeridos.py <id> <id> ...
```

- `NOVO` — ingerir;
- `JA INGERIDO` — não duplicar fonte, evento nem link de índice;
- `SO FONTE` — fonte existe sem página, por pendência aberta. Não recriar a fonte. Se a informação
  que faltava chegou, resolva a pendência criando os eventos;
- `NO LOG` — sem fonte, mas citada no `log.md`. Leia a entrada antes de decidir.

## 3. Ler o transcript verbatim de toda gravação a ingerir

**Nunca ingira a partir do resumo do Granola.** Chame `get_meetings` para o resumo e
`get_meeting_transcript` para o verbatim, e ingira pelo verbatim. O resumo é uma reescrita e já
introduziu erros que teriam entrado na wiki como fato:

| No resumo | No verbatim | Risco |
|---|---|---|
| "Setor 1112" tratado como setor real | "Setor 1112" (fala de 11 e 12) | Setor inexistente |
| "Data: 14 de outubro" apresentada como certa | "dia 14 de outubro" numa gravação de agosto | Data impossível |
| "2,5 L/t" | "2,5 Tert" | Unidade inventada |
| "Início do preparo: 18/08" | "no dia 18 no dia 3 do 8" (autocorreção do falante) | Data errada |
| Ethrel como "E-TREO", "Etréol", "etréu" | mesma variação | Produto duplicado |

A transcrição é automática e erra nomes próprios, unidades e números. Onde ela for ambígua, o
caminho é `pendencia`, nunca o palpite.

## 4. Gravar a fonte bruta (uma por gravação, imutável)

Um arquivo em `raw/registros-manejo/` ou `raw/registros-ciclos-videira/`, nomeado
`AAAA-MM-DD-macaia-<descricao>.md` pela **data da gravação**, com frontmatter (`granola_id`,
`granola_titulo`, `gravado_em`, `ingerido_em`, `local`), a **transcrição verbatim** e o resumo do
Granola. Uma gravação mista continua sendo uma única fonte.

Nunca edite nem apague fonte já existente. Se a gravação não gerar evento, diga isso no corpo da
fonte e aponte a pendência.

## 5. Fatiar em eventos factuais homogêneos

Datas, setores, operações ou estágios diferentes exigem eventos separados. Uma única gravação
costuma render vários eventos (ex.: preparo, poda, Dormex e fertirrigação = 4 eventos).

Quando a mesma operação, na mesma data, cobre vários setores, use **um** evento com a lista em
`setores` e nomeie o arquivo `AAAA-MM-DD-macaia-setores-<a>-<b>-<descricao>.md`. Para operação com
início e fim, preencha `data` com o início e também `data_inicio`/`data_fim`.

O nome do arquivo deve começar pela data do frontmatter — o lint confere.

## 6. Normalizar sem inventar

- **Produtos:** normalize a grafia (Ethrel, Dormex, MAP, Basfoliar) e registre no corpo do evento
  como a fonte grafou. Nomes comerciais distintos (Basfoliar Black Gold e Black Evoluto) **não** são
  unificados.
- **Setores:** só use equivalência já documentada. "T3" → `setor-03` vale porque a numeração
  operacional dos setores é a de `raw/mapa-plantio/2026-08-29-mapa-rotulado-setores.png`; diga isso
  no evento. Sem relação documentada, é pendência. **Nunca** derive setor da ordem das partes do
  MultiPolygon em `2026-08-29-plantio-vivert.geojson`: ela não acompanha a numeração dos setores
  (ver a tabela em [[macaia]]).
- **Ruas e variedades:** preencha somente se a gravação disser. Não herde variedade do cadastro do
  setor: vários setores têm mais de uma, e isso seria interpretação dentro de página factual.
- **Safra:** as gravações não a nomeiam. A convenção vigente é o ano da colheita do ciclo (poda de
  agosto de 2026 → `safra: 2027`), ainda pendente de confirmação da equipe. Se mudar, corrija em
  bloco.
- **Estágio fenológico:** se a fonte não declarar, use `dormencia` apenas quando a operação o
  define (preparo de poda, poda, Dormex) e explique isso no corpo. Quando houver dúvida real
  (fertirrigação depois da poda pode ser dormência ou brotação), deixe `null` e registre pendência.

## 7. Registrar pendências em vez de fatos falsos

Não adivinhe setor, rua, data, ciclo, dose ou estágio. Se o campo essencial faltar, **não crie o
evento**: preserve a fonte e registre `pendencia` no `log.md` citando o prefixo de 8 caracteres do
`granola_id` e o campo ambíguo. Se só um detalhe secundário faltar (ex.: unidade da dose), crie o
evento com o dado marcado como pendente e registre a pendência.

## 8. Indexar

1. Índice mensal de cada setor em `wiki/historicos/setores/<setor>/AAAA-MM-<setor>.md`: uma linha
   por evento, em ordem cronológica, com a seção de pendências de indexação. Não copie a narrativa.
2. Ligação de volta na página de cada setor envolvido (seção `Históricos mensais`).
3. Linha do tempo da safra, mais páginas de variedade e tema afetadas.
4. `index.md`: entidades, temas, históricos mensais novos e recomendações. Eventos atômicos **não**
   entram no índice raiz.
5. `log.md` (append-only): uma entrada `ingest` com o total de fontes, eventos e índices, mais uma
   `pendencia` por ambiguidade e uma `lint` para gravações descartadas.

## 9. Fechar

```bash
python3 tools/validar-wiki.py        # precisa terminar com 0 erros
python3 tools/granola-ingeridos.py   # confere estado final e ids órfãos
```

Commits separados por camada (fontes brutas, eventos e históricos, entidades, índices), push e PR.
Antes do resumo final, confira: nº de fontes = nº de gravações ingeridas; todo `granola_id` de página
tem fonte; nenhuma fonte de `raw/` foi modificada (`git diff --name-only HEAD -- raw/` vazio).

## 10. O que relatar ao usuário

- conta e workspace do Granola consultados, e a janela de datas;
- quantas gravações entraram, quantos eventos e índices nasceram, e quais gravações **não** geraram
  evento e por quê;
- as pendências que precisam de resposta humana, de forma direta;
- fatos que só apareceram ao cruzar as gravações e merecem o olhar da equipe (ex.: dose de Dormex
  subindo ao longo da campanha), sempre sem virar causa.

## Quando parar e perguntar

Pare e pergunte, em vez de decidir sozinho, quando: a convenção de safra ou de estágio afetar muitos
eventos de uma vez; uma gravação contradisser fato já registrado na wiki; ou uma gravação parecer
tratar de local/setor fora do cadastro atual.
