# raw/ — Fontes brutas (imutáveis após a entrada)

Fonte da verdade. Humanos ou rotinas de ingestão podem **acrescentar** uma fonte uma única vez; o
agente nunca altera nem apaga um arquivo já registrado. Coloque cada fonte na pasta correspondente.
As pastas espelham as fontes de dados do projeto:

| Pasta | Conteúdo |
|---|---|
| `publicacoes/` | Todas as publicações que embasam a produção, sem subdivisões temáticas |
| `fichas-tecnicas/comercial/` | Fichas técnicas de produtos comerciais |
| `fichas-tecnicas/biologicos/` | Fichas técnicas de produtos biológicos |
| `analises/` | Resultados de análises de solo, planta e outras matrizes |
| `qualidade-uva/` | Resultados físico-químicos, sanitários e sensoriais da uva |
| `qualidade-vinho/` | Resultados de flor, prensa e outras avaliações do vinho |
| `consultoria/` | Relatórios de consultoria, atualmente agronômica |
| `registros-manejo/` | Registros datados das operações de manejo |
| `registros-ciclos-videira/` | Registros datados dos ciclos e estágios fenológicos da videira |
| `mapa-plantio/` | Mapas de plantio, fotos de drone, variedades plantadas |
| `assets/` | Imagens e anexos |

Dica: nomeie arquivos datados começando pela data (`AAAA-MM-DD-...`) para ordenarem no tempo.
As publicações curadas nesta pasta não restringem a pesquisa do agente: ele pode consultar fontes
externas, priorizando estudos sobre viticultura em clima tropical e usando referências
internacionais quando forem relevantes. A síntese na `wiki/` deve citar a URL/DOI e a data da
consulta, sem confundir conhecimento geral com fato observado na Alma Gerais.
Estação meteorológica e software de gestão da vinícola **não** ficam aqui — são APIs vivas
(ver `dados-vivos/`).
