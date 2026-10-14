---
tipo: exemplos-api
api: innovint
atualizado_em: 2026-07-14
---

# Exemplos HTTP — InnoVint / Sutter

A única vinícola em uso é `Alma Gerais`. Defina seu ID público uma vez:

```bash
export INNOVINT_WINERY_ID="wnry_V901KQJ58M316DV7NDEP64ZW"
```

Auth recomendada: Personal Access Token em `$INNOVINT_PAT`.

## Listar vinícolas acessíveis

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries"
```

## Listar lotes

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/$INNOVINT_WINERY_ID/lots?limit=50&offset=0"
```

## Ações de adição (filtro por período)

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/$INNOVINT_WINERY_ID/additionActions?effectiveAtAfter=2026-01-01T00:00:00Z&effectiveAtBefore=2026-07-01T00:00:00Z&limit=50&offset=0"
```

## Ações de análise

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/$INNOVINT_WINERY_ID/actions/analysisActions?limit=50&offset=0"
```

## Recebimento de fruta

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/$INNOVINT_WINERY_ID/actions/receiveFruitActions?limit=50&offset=0"
```

## Análises de um lote

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/$INNOVINT_WINERY_ID/lots/{lotId}/analyses"
```

Paginação: se a resposta indicar próxima página, avançar `offset` até esgotar (respeitando o
rate limit de 120 req/min).
