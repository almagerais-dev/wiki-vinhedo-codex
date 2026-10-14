---
tipo: dados-vivos
titulo: Estação meteorológica (WS Clima)
api: wsclima
atualizado_em: 2026-07-14
---

# Estação meteorológica — WS Clima (dados vivos)

Cada local tem estação própria (hoje só **Macaia**; São Geraldo é expansão futura). Os dados
**não** são copiados para o repo: o agente consulta a API em tempo real e arquiva apenas
**sínteses** na wiki (ex.: resumo climático em `wiki/safras/`).

Documentação oficial (detalhe de campos/erros):
https://wsclima.com.br/integrations/documentation

## Conexão

| Item | Valor |
|---|---|
| URL base | `https://api.wsclima.com.br/integrations` |
| Auth | Header `Authorization: Bearer $WSCLIMA_API_TOKEN` |
| Token | Variável de ambiente `WSCLIMA_API_TOKEN` (nunca no repo) |
| Identificação do cliente | Header `User-Agent: Alma-Gerais-Wiki/1.0` |

## IDs Alma Gerais

| Local | station_id | nome na API | notas |
|---|---|---|---|
| macaia | `966` | Bom Sucesso Vinícola Alma Gerais - MG | Única estação usada pela wiki neste momento |

O token também enxerga a estação `990` (São Gonçalo do Sapucaí), mas ela fica **fora do escopo**
até decisão humana em contrário.

### Metadados confirmados da estação 966

Consulta em 2026-07-14: `GET /stations/966/details`.

- coordenadas: `-21.123929, -44.909792`;
- elevação informada pela API: `827 m`;
- fuso: `America/Sao_Paulo`;
- provedor: Wunderground, identificador `IBOMSU8`;
- a estação estava online;
- o campo `data_since` veio nulo.

O `966` é o ID público usado no caminho. A resposta de detalhes e o campo `station_id` das leituras
retornaram o ID interno `4`; não substituir `966` por `4` nas URLs.

## Endpoints que o agente usa

Preferir estes; não varrer a doc oficial a cada pergunta.

| Uso | Método e caminho |
|---|---|
| Listar estações da chave | `GET /stations/list` |
| Detalhes / lat-long / data_since | `GET /stations/{id}/details` |
| Leitura atual | `GET /stations/{id}/data/current` |
| Histórico | `GET /stations/{id}/data/historical/{start}/{end}` |

Datas do histórico no formato `YYYYMMDD`. Intervalo máximo: **366 dias**.

Agrupamento automático da API:

- até 7 dias → leituras brutas (`grouping: raw`)
- 8–31 dias → a cada 4 h (`min`/`avg`/`max`)
- > 31 dias → diário (`min`/`avg`/`max`)

### Cobertura observada

Em 2026-07-14, a leitura atual funcionou e trouxe temperatura, sensação térmica, ponto de orvalho,
vento, pressão, precipitação, umidade e radiação solar. Na mesma consulta, o histórico da estação
`966` retornou `count: 0` para todos os períodos testados: 2026-07-14, 2026-07-13 a 2026-07-14,
2026-07-08 a 2026-07-14, 2026-06-14 a 2026-07-14 e 2026-01-01 a 2026-07-14.

Consequência: até o histórico começar a retornar dados, a API sustenta **estado atual**, mas não
resumos de chuva, extremos, geadas, veranicos ou graus-dia. Não interpretar ausência de linhas como
ausência de fenômeno climático.

## Como o agente deve usar

1. Leia este playbook (e `dados-vivos/queries/exemplos-wsclima.md`) antes de montar a chamada.
2. Consulte para números atuais/históricos (temperatura, chuva, geada, veranico, graus-dia).
3. Abra a documentação oficial só se faltar um parâmetro/campo não coberto aqui.
4. Ao usar numa síntese, registre a **data da consulta**, o endpoint e o período como `fontes`.
5. Em `429`, respeitar o limite; não martelar a API.
6. Sempre enviar o `User-Agent`: sem ele, a infraestrutura respondeu `403` durante a validação.

## Erros comuns

| Código | Significado |
|---|---|
| `400` | Parâmetros inválidos (data, intervalo) |
| `401` | Token ausente/inválido/expirado |
| `403` | Cliente sem `User-Agent` ou acesso recusado |
| `404` | Estação inexistente ou sem permissão |
| `429` | Rate limit |
