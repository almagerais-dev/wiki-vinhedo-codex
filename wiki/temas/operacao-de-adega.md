---
tipo: tema
titulo: Operação de adega
tags: [adega, innovint, lotes, qualidade]
fontes: [dados-vivos/gestao-vinicola.md]
atualizado_em: 2026-07-14
---

# Operação de adega

Síntese de como consultar e interpretar a operação da única vinícola ativa nesta wiki:
**Alma Gerais**, no InnoVint.

## O que cada cadastro representa

- **Origem (`vineyard`) / bloco:** procedência da uva; inclui áreas Alma Gerais e fornecedores.
  Não é uma lista automática de locais ou quadras próprias.
- **Lote de fruta:** uva recebida e ainda controlada por peso.
- **Lote a granel:** vinho em elaboração ou estágio, controlado principalmente por volume.
- **Produto acondicionado:** vinho já acondicionado; ainda não prova que seja um rótulo comercial.
- **Vaso:** recipiente físico. Sua associação a um lote muda com as operações.
- **Ação:** registro datado de recebimento, processamento, análise, adição ou movimentação.

Esta distinção evita criar páginas de quadra ou vinho a partir de homônimos operacionais sem
confirmação humana.

## Retrato factual em 2026-07-14

Consulta paginada à API:

- 16 origens e 53 blocos cadastrados; 51 blocos não arquivados;
- 145 lotes no total; 51 não arquivados;
- 209 vasos não arquivados, dos quais 91 estavam associados a lotes;
- tipos de vaso: 87 tanques, 62 barricas, 26 vasos `SUTTER`, 20 garrafões, 9 ovos, 4 barris
  pequenos (`KEG`) e 1 caixa;
- 649 ações de análise e 208 ações de adição no histórico acessível;
- as ações acessíveis começam em 2025-12-26.

As duas origens com nome Alma Gerais são:

- **Alma Gerais - Vivert:** 20 blocos e 9,988 ha declarados;
- **Alma Gerais - SGS:** 8 blocos, sem área declarada.

As outras 14 origens podem representar fornecedores. Nenhuma delas deve ser incorporada como
quadra própria de [[macaia]] sem confirmação.

## Safra 2026 no InnoVint

Até a consulta:

- 16 ações de recebimento continham 18 lançamentos e somavam **19.645,7 kg** de fruta;
- os recebimentos registrados iam de 2026-01-14 a 2026-07-14;
- havia 19 lotes ativos identificados como 2026: 13 a granel, 4 de fruta e 2 acondicionados;
- os 13 lotes a granel somavam **6.125 L** no retrato;
- os estágios dos 19 lotes eram: 8 em estágio, 3 fermentando, 2 decantando, 4 recebidos e
  2 acondicionados;
- havia 612 ações de análise em 2026, contendo 2.615 resultados válidos (não apagados e não
  pulados).

Os tipos de análise mais frequentes em 2026 e 2025, em conjunto, eram pH, acidez titulável,
densidade, temperatura, acidez volátil, Brix, peso médio de cacho, SO₂ livre, peso médio de baga e
álcool. A presença de um resultado não implica que todos os lotes tenham a mesma cobertura.

Ver o fato de recebimento consolidado em [[2026-01-14-macaia-recebimentos-uva-safra-2026]] e o hub
temporal em [[safra-2026]].

## Consultas adequadas por pergunta

- **Quanto entrou na safra?** Ações de recebimento aplicadas, excluindo apagadas, somadas por
  `effectiveAt` e unidade.
- **Em que fase está um vinho?** Lote não arquivado + vasos associados + ações recentes.
- **Como evoluiu uma análise?** Análises do lote ordenadas por `recordedAt`, mantendo unidade e
  descartando itens apagados/pulados.
- **O que foi adicionado?** Ações de adição aplicadas, ligando aditivo, lote, vaso, quantidade e
  instrução.
- **De qual área veio a fruta?** Componentes do lote e bloco/origem; nomes de lote isolados são
  insuficientes.

## Limites

- Os valores são um retrato da consulta, não estoque imutável.
- O InnoVint descreve adega e recebimento, não manejo de campo.
- Totais de processamento não devem usar campos zerados de lotes drenados sem conferir a semântica
  da ação; na consulta, várias ações preservavam o volume final, mas retornavam peso drenado zero.
- Não há interpretação causal nesta página.
