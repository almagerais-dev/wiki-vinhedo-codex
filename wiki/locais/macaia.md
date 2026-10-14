---
tipo: local
titulo: Macaia
slug: macaia
fontes:
  - dados-vivos/estacao-meteorologica.md
  - dados-vivos/gestao-vinicola.md
  - raw/mapa-plantio/2026-08-29-mapa-de-plantio-alma-gerais-vivert.json
  - raw/mapa-plantio/2026-08-29-plantio-vivert.geojson
  - raw/mapa-plantio/2026-08-29-confirmacao-doze-setores.md
  - raw/mapa-plantio/2026-08-29-mapa-rotulado-setores.png
atualizado_em: 2026-08-29
---

# Macaia

Local de cultivo da Alma Gerais.

## Ficha

- **Município / região na estação:** Bom Sucesso, MG
- **Elevação informada pela estação:** 827 m
- **Estação meteorológica:** WS Clima `966` (única usada pela wiki)
- **Gestão da vinícola:** InnoVint / Sutter, vinícola `Alma Gerais` (única usada pela wiki)
- **Área total dos setores mapeados:** 10,7374 ha
- **Plantas no mapa de plantio:** 35.921
- **Produção anual esperada no mapa de plantio:** 63.479,8 kg

As doze áreas são geodésicas WGS84, calculadas sobre as partes do MultiPolygon de 2026-08-29 e
atribuídas a cada setor pela correspondência da imagem rotulada.

As plantas e a produção esperada vêm da linha `TOTAL VIVERT` do mapa de plantio de 2026-08-29 e
coincidem com a soma dos 18 trechos plantados. O objeto `totais` do mesmo JSON duplica esses
números (71.842 plantas e 126.959,6 kg); a wiki não usa esses totais duplicados.

## Quadras

_A fonte de plantio não relaciona quadras. Links para `wiki/quadras/` quando houver confirmação._

## Setores

A coleção vigente identifica doze polígonos, confirmados como os doze setores operacionais de
Macaia:

- [[setor-01]], [[setor-02]], [[setor-03]], [[setor-04]] e [[setor-05]]
- [[setor-06]], [[setor-07]], [[setor-08]], [[setor-09]] e [[setor-10]]
- [[setor-11]] e [[setor-12]]

As geometrias vigentes estão em `raw/mapa-plantio/2026-08-29-plantio-vivert.geojson`. O arquivo tem
uma única feição, um MultiPolygon com doze partes, e **nenhuma parte carrega atributo** — a feição
inteira só tem a propriedade `name: Plantio Vivert`. O mapa de plantio de 2026-08-29 é o oposto:
numera os setores 1 a 12 com ruas e variedades, mas não tem coordenada alguma. A ligação entre
geometria e cadastro, portanto, não está em nenhum dos dois arquivos.

Quem fecha essa ligação é `raw/mapa-plantio/2026-08-29-mapa-rotulado-setores.png`, a imagem de
satélite com os doze contornos e os números operacionais desenhados pelo time. **A ordem das partes
no GeoJSON não acompanha a numeração dos setores**, e nove dos doze diferem:

| Setor | Parte do MultiPolygon | Área (ha) |
|---|---:|---:|
| [[setor-01]] | 5 | 1,0585 |
| [[setor-02]] | 4 | 1,0769 |
| [[setor-03]] | 3 | 1,2055 |
| [[setor-04]] | 6 | 1,0730 |
| [[setor-05]] | 7 | 0,9042 |
| [[setor-06]] | 2 | 1,2883 |
| [[setor-07]] | 1 | 0,4657 |
| [[setor-08]] | 9 | 1,0829 |
| [[setor-09]] | 10 | 1,3431 |
| [[setor-10]] | 8 | 0,2704 |
| [[setor-11]] | 11 | 0,3498 |
| [[setor-12]] | 12 | 0,6191 |

Só os setores 03, 11 e 12 têm parte de mesmo número. Qualquer consulta que recorte a geometria por
setor precisa passar por esta tabela; usar a ordem do arquivo troca as áreas de nove setores.

No JSON de plantio, cada item de `talhoes` é um **trecho de ruas** dentro de um setor, não o
polígono georreferenciado nem uma quadra.

| Setor | Ruas | Variedades | Plantas |
|---|---|---|---:|
| [[setor-01]] | 1 a 47 | [[sauvignon-blanc]] | 4.232 |
| [[setor-02]] | 1 a 39 | [[syrah]] | 3.877 |
| [[setor-03]] | 1 a 36 | [[syrah]] | 4.994 |
| [[setor-04]] | 1 a 38 | [[sauvignon-blanc]] | 4.038 |
| [[setor-05]] | 1 a 42 | [[cabernet-franc]] | 3.803 |
| [[setor-06]] | 1 a 8; 9 a 38 | [[cabernet-franc]]; [[cabernet-sauvignon]] | 3.829 |
| [[setor-07]] | 1 a 24 | [[cabernet-franc]] | 1.825 |
| [[setor-08]] | 1 a 18; 19 a 42 sem plantio | [[cabernet-sauvignon]] | 2.268 |
| [[setor-09]] | 1 a 9; 10 a 41 sem plantio; 42 a 71 | [[piwis]]; [[cabernet-franc]] | 2.250 |
| [[setor-10]] | 1 a 5; 6 a 8; 9 a 10 | [[sauvignon-blanc]]; [[cabernet-franc]]; [[syrah]] | 1.200 |
| [[setor-11]] | 1 a 7; 8 a 23; 24 a 46 | [[margoth]]; [[cabernet-franc]]; [[marselan]] | 1.322 |
| [[setor-12]] | 1 a 47 | [[marselan]] | 2.283 |

## Variedades plantadas

- [[sauvignon-blanc]] — 8.870 plantas
- [[syrah]] — 9.111 plantas
- [[cabernet-franc]] — 8.536 plantas
- [[cabernet-sauvignon]] — 5.689 plantas
- [[marselan]] — 2.965 plantas
- [[piwis]] — 500 plantas (rótulo `PIWI´S` na fonte; cultivar não informado)
- [[margoth]] — 250 plantas

## Notas

- A estação `966` estava online em 2026-07-14. A leitura atual funcionava, mas o histórico retornava
  zero registros; ver [[clima]].
- O InnoVint reúne operação de adega e origens de fruta próprias e de terceiros; uma origem
  cadastrada não é automaticamente uma quadra de Macaia. Ver [[operacao-de-adega]].
- Eventos ligados: [[2026-01-14-macaia-recebimentos-uva-safra-2026]].
- A campanha de poda de agosto de 2026 é o primeiro manejo de campo ingerido: ver [[safra-2027]],
  [[poda-desfolha]] e [[irrigacao]]. Doze setores têm histórico mensal de 2026-08.
