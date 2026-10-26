---
tipo: tema
titulo: Clima
tags: [meteorologia]
fontes: [dados-vivos/estacao-meteorologica.md]
atualizado_em: 2026-10-26
---

# Clima

Síntese do clima de [[macaia]]. Dados quantitativos vêm da estação `966` na API WS Clima (ver
`dados-vivos/estacao-meteorologica.md`).

## Resumo operacional

Em 2026-07-14, a estação estava online e a leitura atual funcionava. A API informou coordenadas
`-21.123929, -44.909792`, elevação de 827 m e fuso `America/Sao_Paulo`.

O histórico retornou zero linhas em todos os intervalos testados, inclusive no próprio dia, nos
últimos 7 e 31 dias e de 2026-01-01 a 2026-07-14. Esse resultado, limitado à consulta de 2026-07-14, não sustentava
calcular resumo climático da safra, chuva acumulada, extremos, geadas, veranicos ou graus-dia.
Ausência de linhas não significa ausência desses fenômenos.

## O que sabemos (das fontes)

- Fonte de consulta: WS Clima, estação `966`; disponibilidade atual não verificada nesta revisão.
- Campos disponíveis na leitura atual: temperatura, índice de calor, ponto de orvalho, sensação
  térmica, vento, pressão, taxa e acumulado de precipitação, umidade e radiação solar.
- O acervo já contém registros de manejo e fenologia; ver [[safra-2027]]. Eles não substituem
  medições meteorológicas nem comprovam cobertura histórica da estação.
- Nova avaliação climática requer consulta datada à API; a revisão de 2026-10-26 foi documental.

## Como se manifesta no nosso vinhedo

- Resumos por safra: [[safra-2026]].
- Eventos climáticos factuais devem entrar em `wiki/eventos/` somente quando houver medição ou
  observação datada.
