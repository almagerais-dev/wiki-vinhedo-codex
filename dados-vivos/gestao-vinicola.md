---
tipo: dados-vivos
titulo: Gestão da vinícola (InnoVint / Sutter)
api: innovint
atualizado_em: 2026-07-21
---

# Gestão da vinícola — InnoVint / Sutter (dados vivos)

API da gestão da vinícola (lotes, vasos, ações de adição/análise, recebimento de fruta, blocos,
vinhedos, etc.). Consultado em tempo real; apenas sínteses vão para a wiki.

Documentação oficial (Redoc / OpenAPI):
https://sutter.innovint.us/api/v1/docs/

Schema OpenAPI (máquina): `https://sutter.innovint.us/api/v1/schema/`

> InnoVint é software de **vinícola/adega** (cellar), não um ERP de manejo de campo. Eventos de
> manejo no vinhedo (pulverização, poda, irrigação) podem não existir aqui — quando faltarem,
> buscar em `raw/registros-manejo/` e `raw/registros-ciclos-videira/`.

## Conexão

| Item | Valor |
|---|---|
| URL base | `https://sutter.innovint.us` |
| Auth (recomendado) | Header `Authorization: Access-Token $INNOVINT_PAT` |
| Auth (alternativo) | Header `Authorization: Bearer <token de login>` — evita em produção |
| Token | Variável de ambiente `INNOVINT_PAT` (Personal Access Token; nunca no repo) |
| Rate limit | 120 req/min → `429` + header `Retry-After` |
| Paginação | `limit`/`offset` (padrão até 200 por página) |

PATs são gerenciados em:
https://cellar.innovint.us/#/developer/personal-access-token

## IDs Alma Gerais

| Local / contexto | wineryId | notas |
|---|---|---|
| Alma Gerais (Macaia) | `wnry_V901KQJ58M316DV7NDEP64ZW` | Nome `Alma Gerais`; internalId `2152198`; única vinícola usada pela wiki |

O token retornou somente essa vinícola em 2026-07-14.

## Como interpretar o modelo

- **Winery** é a conta operacional da adega. Nesta wiki, só usamos `Alma Gerais`.
- **Vineyard** é uma origem cadastrada de uva. A lista inclui áreas Alma Gerais e fornecedores;
  portanto, não equivale à lista de locais próprios da wiki.
- **Block** é a subdivisão de uma origem. Só criar uma página em `wiki/quadras/` após confirmar que
  o bloco pertence a Macaia e mapear seu nome ao slug interno.
- **Fruit lot** representa uva recebida; **bulk lot**, vinho a granel; **case goods**, produto
  acondicionado. Um lote não é necessariamente um produto comercial.
- **Vessel** é um recipiente físico e pode estar vazio ou associado a um lote.
- **Action** é um fato operacional datado. Para a cronologia, usar `effectiveAt`, não `createdAt`.
- Registros `archived`, `deleted`, `skipped` ou não `applied` não devem entrar em totais ativos sem
  tratamento explícito.

### Escopo observado em 2026-07-14

A consulta completa, paginada, encontrou 16 origens, 53 blocos, 145 lotes e 209 vasos. Das origens,
duas têm nome Alma Gerais: `Alma Gerais - Vivert` (20 blocos; 9,988 ha declarados) e
`Alma Gerais - SGS` (8 blocos; sem área declarada). As outras origens não devem ser tratadas como
quadras próprias sem confirmação.

Havia 51 lotes não arquivados entre diferentes safras e 19 lotes ativos identificados como safra
2026. O retrato factual da safra está em [[safra-2026]] e o modelo operacional em
[[operacao-de-adega]].

## Endpoints que o agente usa com frequência

Preferir estes; a API tem dezenas de recursos — não explorar o catálogo inteiro a cada pergunta.

| Uso | Método e caminho |
|---|---|
| Listar vinícolas acessíveis | `GET /api/v1/wineries` |
| Lotes | `GET /api/v1/wineries/{wineryId}/lots` |
| Análises de um lote | `GET /api/v1/wineries/{wineryId}/lots/{lotId}/analyses` |
| Ações de adição | `GET /api/v1/wineries/{wineryId}/additionActions` |
| Ações de análise | `GET /api/v1/wineries/{wineryId}/actions/analysisActions` |
| Recebimento de fruta | `GET /api/v1/wineries/{wineryId}/actions/receiveFruitActions` |
| Processar fruta → volume | `GET /api/v1/wineries/{wineryId}/actions/processFruitToVolumeActions` |
| Vasos | `GET /api/v1/wineries/{wineryId}/vessels` |
| Vinhedos / blocos | `GET /api/v1/wineries/{wineryId}/vineyards` · `GET /api/v1/wineries/{wineryId}/blocks` |
| Catálogo de variedades | `GET /api/v1/varietals` |

Filtros úteis em listagens de ações (quando disponíveis): `effectiveAtAfter`, `effectiveAtBefore`,
`createdAtAfter`, `createdAtBefore`, `actionType`, `sort`, `limit`, `offset`.

## Reconciliação de recebimentos

- Calcular entrada de uva a partir de `receiveFruitActions`, não do peso atual do lote.
- Incluir somente ações com `applied: true` e `deleted: false`; usar `effectiveAt` para atribuir
  data e safra.
- Somar cada item de `fills` e ligar seu `lotId` ao cadastro de lotes. Uma ação pode preencher
  vários lotes, e um mesmo lote pode receber fruta em mais de uma ação.
- Manter as unidades explícitas. Não somar valores em unidades diferentes sem conversão documentada.
- Para variedade e procedência, o nome do lote é apenas um atalho operacional. Quando a resposta
  exigir rastreabilidade, consultar os componentes do lote e relacionar bloco, origem e variedade.
- Diferenças entre um total externo e a soma da API devem ser reconciliadas ação por ação. Não
  eliminar automaticamente lançamentos repetidos no mesmo lote: ações distintas podem representar
  recebimentos adicionais.

Caso conhecido, consultado em 2026-07-21: o lote `2026 Sauv. Blanc Vivert 1.2` tinha duas ações
aplicadas e não apagadas, de 2.100 kg em 2026-06-29 e 2.796 kg em 2026-06-30. A soma de todos os
recebimentos nomeados como Sauvignon Blanc Vivert era 13.506 kg; desconsiderar a primeira ação
produzia 11.406 kg. A API, isoladamente, não permite classificar a primeira ação como recebimento
adicional ou duplicidade operacional; confirmar com o registro de origem antes de excluir.

## Como o agente deve usar

1. Leia este playbook (e `dados-vivos/queries/exemplos-innovint.md`) antes de montar a chamada.
2. Use para reconstruir linha do tempo de adega/lote/safra e números de análise/adições.
3. Eventos **marcantes** (ex.: recebimento de fruta da colheita, análise decisiva) viram páginas em
   `wiki/eventos/`; o operacional de alta frequência fica na API e é sintetizado por safra/vinho.
4. Abra a documentação oficial só para parâmetros/campos não cobertos aqui.
5. Registrar data da consulta, endpoint e filtros como `fontes`.
6. Em `429`, esperar o `Retry-After`; não martelar a API.
7. Por padrão, **somente leitura** (GET). Não criar/alterar recursos sem pedido explícito do humano.
8. Paginar até `pagination.next` ser nulo; o primeiro lote de 200 não cobriu análises, adições ou
   vasos por completo na validação.
