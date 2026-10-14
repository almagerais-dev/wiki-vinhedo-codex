---
tipo: evento
categoria: colheita
data_inicio: 2026-01-14
data_fim: 2026-07-14
local: macaia
quadras: []
variedades: [merlot, pinot-noir, chardonnay, syrah, sauvignon-blanc]
safra: 2026
estagio_fenologico: colheita
tags: [recebimento-uva, adega, innovint]
fontes: [dados-vivos/gestao-vinicola.md]
atualizado_em: 2026-07-14
---

# 2026-01-14 a 2026-07-14 — recebimentos de uva da safra 2026

## O que aconteceu (fato)

Em consulta ao InnoVint em 2026-07-14, a vinícola Alma Gerais tinha **16 ações aplicadas de
recebimento**, com **18 lançamentos** de entrada e **19.645,7 kg** de fruta da safra 2026. Não havia
ações apagadas ou não aplicadas nesse conjunto.

Os registros iam de 2026-01-14 a 2026-07-14. Pelos nomes dos lotes de fruta, havia entradas
identificadas como Merlot, Pinot Noir, Chardonnay, Syrah e Sauvignon Blanc, além de um lote chamado
`Rosé Margot`, cuja variedade não foi inferida.

Consulta: `GET /api/v1/wineries/{wineryId}/actions/receiveFruitActions`, com paginação completa;
totais agrupados por `effectiveAt` e apenas quantidades em quilogramas.

## Contexto

- **Safra:** [[safra-2026]]
- **Local de operação nesta wiki:** [[macaia]]
- **Operação:** [[operacao-de-adega]]
- **Quadras / origens:** não mapeadas automaticamente; o InnoVint inclui áreas próprias e
  fornecedores.
- **Estágio fenológico:** colheita.

## Limites do registro

- O total é válido até o instante da consulta e pode aumentar com novos recebimentos.
- O cadastro operacional não basta para atribuir cada entrada a uma quadra própria de Macaia.
- Nomes de lotes foram usados apenas como identificação factual, não como prova de composição.

## Interpretações relacionadas

Nenhuma. Este registro não atribui causas nem avalia qualidade.
