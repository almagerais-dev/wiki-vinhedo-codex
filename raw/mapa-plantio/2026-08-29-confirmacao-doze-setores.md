# Confirmação dos doze setores e da geometria vigente

- Data da confirmação: 2026-08-29
- Origem: confirmação explícita do usuário ao atualizar o mapa de plantio, com a
  FeatureCollection `Plantio Vivert` gravada em
  `raw/mapa-plantio/2026-08-29-plantio-vivert.geojson`.

> hoje no nosso brain diz que temos 10, mas na verdade temos 12.

A coleção recebida tem uma única feição MultiPolygon, sem rótulo por talhão. A
normalização cadastral usa a ordem das 12 partes:

| Parte (1-based) | Setor wiki | Relação com a fonte de 2026-08-25 |
|---|---|---|
| 1 a 10 | `setor-01` a `setor-10` | Vértices coincidem com `Talhao 1` a `Talhao 10` (diferença só de precisão decimal). |
| 11 | `setor-11` | Polígono novo; a fonte não traz nome de talhão. |
| 12 | `setor-12` | Polígono novo; a fonte não traz nome de talhão. |

A fonte de 2026-08-25 permanece no repositório e não foi alterada. A geometria
vigente passa a ser a coleção de 2026-08-29.
