---
tipo: exemplos-api
api: wsclima
atualizado_em: 2026-07-14
---

# Exemplos HTTP — WS Clima

Estação em uso: Macaia, ID `966`. O `User-Agent` é obrigatório no ambiente validado.

## Listar estações

```bash
curl -sS -H "Authorization: Bearer $WSCLIMA_API_TOKEN" \
  -H "User-Agent: Alma-Gerais-Wiki/1.0" \
  "https://api.wsclima.com.br/integrations/stations/list"
```

## Leitura atual

```bash
curl -sS -H "Authorization: Bearer $WSCLIMA_API_TOKEN" \
  -H "User-Agent: Alma-Gerais-Wiki/1.0" \
  "https://api.wsclima.com.br/integrations/stations/966/data/current"
```

## Histórico (ex.: 7 dias brutos)

Datas no path: `YYYYMMDD`.

```bash
curl -sS -H "Authorization: Bearer $WSCLIMA_API_TOKEN" \
  -H "User-Agent: Alma-Gerais-Wiki/1.0" \
  "https://api.wsclima.com.br/integrations/stations/966/data/historical/20260701/20260707"
```

## Histórico mensal (agregação diária automática se > 31 dias)

```bash
curl -sS -H "Authorization: Bearer $WSCLIMA_API_TOKEN" \
  -H "User-Agent: Alma-Gerais-Wiki/1.0" \
  "https://api.wsclima.com.br/integrations/stations/966/data/historical/20260501/20260630"
```

Campos úteis no modo agrupado: `temp_min`/`temp_avg`/`temp_max`, `precip_total`,
`humidity_avg`, `wind_gust_max`, `period`.
