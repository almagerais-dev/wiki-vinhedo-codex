---
tipo: tema
titulo: Fenologia
tags: [fenologia, brotacao, estagio-fenologico]
fontes:
  - raw/registros-ciclos-videira/2026-09-15-macaia-setor-01-inicio-brotacao.md
  - raw/registros-ciclos-videira/2026-09-15-macaia-setores-11-12-inicio-brotacao.md
  - raw/registros-ciclos-videira/2026-09-15-macaia-setor-03-inicio-brotacao.md
  - raw/registros-ciclos-videira/2026-09-15-macaia-setor-09-inicio-brotacao.md
  - raw/registros-ciclos-videira/2026-09-15-macaia-setores-05-08-inicio-brotacao-data-impossivel.md
atualizado_em: 2026-09-16
---

# Fenologia

Página aberta com a primeira rodada de registros de estágio fenológico da wiki, gravada em
2026-09-15. Até então nenhuma gravação declarava estágio: as operações de preparo, poda e Dormex
foram ancoradas em `dormencia` pela natureza da operação, as fertirrigações posteriores à poda
ficaram com o campo nulo e a única palavra de estágio que aparecera nas fontes — "gema algodão",
nas pulverizações de 2026-09-02 — está fora do vocabulário controlado do `AGENTS.md`.

## Início da brotação (safra 2027)

| Setor(es) | Início da brotação | Poda | Dias entre poda e brotação | Evento |
|---|---|---|---:|---|
| [[setor-01]] | 2026-09-08 | sem registro | — | [[2026-09-08-macaia-setor-01-inicio-brotacao]] |
| [[setor-11]], [[setor-12]] | 2026-09-11 | 2026-08-26 | 16 | [[2026-09-11-macaia-setores-11-12-inicio-brotacao]] |
| [[setor-03]] | 2026-09-14 | 2026-08-27 | 18 | [[2026-09-14-macaia-setor-03-inicio-brotacao]] |
| [[setor-09]] | 2026-09-14 | 2026-08-27 | 18 | [[2026-09-14-macaia-setor-09-inicio-brotacao]] |

Traço (—) significa ausência de registro nas gravações ingeridas, não ausência da operação. O
intervalo entre poda e brotação é o que as datas mostram; a wiki não atribui causa a ele nem o
transforma em previsão para os setores que ainda não brotaram.

## Cobertura e lacunas

- Sem brotação registrada: setores [[setor-02]], [[setor-04]], [[setor-06]], [[setor-07]] e
  [[setor-10]].
- Setores [[setor-05]] e [[setor-08]]: a brotação foi gravada em `c90294f7`, mas datada em "11 de
  novembro de 2026", posterior à própria gravação. Sem data ancorável não há evento; ver a
  `pendencia` de 2026-09-16 em `log.md`.
- Nenhum estágio posterior à brotação foi registrado — floração, pegamento, véraison, maturação e
  colheita seguem vazios em [[safra-2027]].
- As gravações não informam a fração de gemas brotadas nem a rua ou o trecho observado, então a data
  marca o que o agrônomo chamou de início, sem critério quantitativo declarado.

## Vocabulário e transcrição

O `AGENTS.md` fixa a lista de estágios (`dormencia`, `brotacao`, `floracao`, `pegamento`,
`crescimento-baga`, `veraison`, `maturacao`, `colheita`, `pos-colheita`). Duas dificuldades aparecem
ao ligar as fontes a essa lista:

- "Gema algodão", usado nas pulverizações de 2026-09-02, não consta da lista e continua sem
  correspondência confirmada pela equipe; ver [[fitossanidade]].
- A transcrição automática grafou "brotação" como "votação" na gravação dos setores 11 e 12
  (`9394b85e`) e o título automático a verteu para "Voting update". A classificação seguiu a
  estrutura idêntica das quatro gravações irmãs da mesma sequência.

## Interpretações relacionadas

_Nenhuma correlação ou hipótese registrada._ As datas de brotação por setor e as de poda, Dormex e
fertirrigação ([[poda-desfolha]], [[irrigacao]]) já permitem comparações entre setores; enquanto
nenhuma for examinada e registrada com defasagem e confiança, esta página fica sendo só o índice
factual do estágio.
