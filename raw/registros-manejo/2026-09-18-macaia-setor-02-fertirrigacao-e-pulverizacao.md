---
tipo: registro-manejo
titulo: "Setor 2 — fertirrigação com data impossível e pulverização datada"
origem: granola
granola_id: 73ef1fb1-0f27-439d-87de-6f65edfc9d21
granola_titulo: "Fertilization and spraying plan"
gravado_em: 2026-09-18T14:32:02-03:00
ingerido_em: 2026-09-19
local: macaia
---

# Setor 2 — fertirrigação com data impossível e pulverização datada

- Gravação Granola: `73ef1fb1-0f27-439d-87de-6f65edfc9d21`
- Data/hora da gravação: 2026-09-18 14:32 (GMT-3)
- Captura: E-commerce Alma Gerais <ecommerce@almagerais.com.br>

Dois fatos na mesma gravação, com datas ditas de formas diferentes:

- **Fertirrigação** (MAP 15 g/planta + 1 L/ha de Basfoliar Black Gold): "Dia 16 de novembro de 2026
  foi feito a fértil" — data posterior à própria gravação, e o fato é relatado como já ocorrido.
  **Não gerou evento.** Ver a `pendencia` de 2026-09-19 em `log.md`.
- **Pulverização** (Cercobin 600 g + Absolut Fix 600 ml em 200 L de calda/ha): "feito no dia 16, do
  9 de 2026" — data inequívoca. **Gerou evento.**

É o quarto caso do padrão "novembro" por "nove", e o primeiro em que as duas formas aparecem na
mesma gravação para **operações diferentes** (em `75804673` a contradição era sobre o mesmo fato).
A wiki não transporta a data de uma operação para a outra: as duas gravações irmãs da mesma sessão
descrevem o mesmo par de operações no dia 16 nos setores 04 e 10, e em `004a2641` o agrônomo corrige
"novembro" para "setembro" — mas essa correção nomeia o setor 4, não o setor 2.

## Transcrição (verbatim)

> Setor 2, fértil, MAP, 15 gramas por planta, 1 litro de basfoliar Black Gold por hectare. Dia 16 de
> novembro de 2026 foi feito a fértil. Pulverização, setor 2, 600 gramas de Cercobin, 600 ml de
> Absolut Fix, num volume de 200 litros de caldo por hectare, feito no dia 16, do 9 de 2026.

## Resumo gerado pelo Granola

### Setor 2: Fertil (16 de novembro de 2026)

- Produto: MAP Fértil
  - Dose: 15 gramas por planta
  - Adjuvante: Basfoliar Black Gold, 1 litro por hectare

### Setor 2: Pulverização (16 de setembro de 2026)

- Produtos aplicados:
  - Cercobin: 600 gramas
  - Absolut Fix: 600 ml
- Volume de calda: 200 litros por hectare
