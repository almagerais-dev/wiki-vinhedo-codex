---
name: consultar-historico-setorial
description: Consulta o histórico de setores e ruas do vinhedo da Alma Gerais. Use quando uma pergunta envolver setor, rua, quadra, talhão, área do vinhedo, manejo, ciclo da videira, fenologia, evolução temporal, comparação entre áreas, situação atual, possível relação ou padrão de campo.
---

# Consultar histórico setorial

Use este procedimento para responder perguntas de campo sobre Macaia. A ingestão diária do Granola
não usa esta skill: ela apenas registra e indexa fatos novos.

## Procedimento

1. Leia `index.md` e identifique a página canônica de cada setor citado.
2. Normalize setor e rua pelos identificadores das páginas da wiki. Não presuma que setor, quadra e
   talhão são equivalentes; use somente relações documentadas.
3. Determine o intervalo necessário pela intenção da pergunta:
   - data ou operação específica: mês correspondente;
   - intervalo explícito: todos os índices mensais abrangidos;
   - situação atual: meses recentes necessários para localizar os fatos atuais;
   - evolução, comparação, possível relação ou padrão: período solicitado e antecedentes
     tecnicamente relevantes, expandindo para o ciclo ou safras comparáveis quando necessário;
   - histórico completo: todos os índices mensais disponíveis para o setor.
4. Abra os índices em
   `wiki/historicos/setores/<setor>/AAAA-MM-<setor>.md` e filtre por setor, rua, categoria,
   variedade e estágio fenológico conforme a pergunta.
5. O histórico mensal é apenas um índice. Abra os eventos ligados em `wiki/eventos/` antes de
   afirmar detalhes, comparar ocorrências ou citar evidências.
6. Se o índice mensal esperado não existir, procure eventos cujo frontmatter cite o setor e o
   intervalo. Informe a lacuna de indexação; ausência do índice não prova ausência de eventos.
7. Consulte a página da safra quando a pergunta atravessar meses, estágios fenológicos ou ciclos.
8. Responda com links para os eventos e caminhos das fontes originais.

## Separação entre fato e interpretação

- Relate ações e observações exatamente como registradas nos eventos.
- Não transforme proximidade temporal em causalidade.
- Possíveis relações ficam em `wiki/correlacoes/`, com defasagem e confiança.
- Explicações em avaliação ficam em `wiki/hipoteses/`.
- Se faltarem setor, rua, data, ciclo ou estágio, exponha a lacuna; nunca complete por suposição.

## Eficiência

Não carregue todo o histórico por padrão. Comece pelos meses exigidos pela pergunta e amplie o
intervalo somente quando a investigação precisar. Em comparações entre setores, aplique o mesmo
intervalo e os mesmos filtros a todos eles.
