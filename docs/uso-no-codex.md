# Uso da wiki no Codex

Esta é a cópia independente `almagerais-dev/wiki-vinhedo-codex` da memória da Alma Gerais.
Use seu checkout existente e leia [AGENTS.md](../AGENTS.md) inteiro. Não sincronize alterações
com `almagerais-dev/wiki-vinhedo` nem crie worktrees por padrão.

## Consultar

Peça, por exemplo: “Compare o manejo dos setores 2 e 4 em setembro de 2026”. O Codex deve ler
[consultar-historico-setorial](../.agents/skills/consultar-historico-setorial/SKILL.md), localizar
os índices mensais e abrir os eventos antes de responder com citações. Ausência de índice não
significa ausência de evento; relações exigem defasagem, confiança e distinção entre correlação
e causalidade. Uma consulta pode usar apenas as fontes locais.

## Ingerir gravações, quando autorizado

Peça a ingestão de uma janela definida e disponibilize o conector Granola autorizado. O Codex
segue [ingerir-gravacoes-granola](../.agents/skills/ingerir-gravacoes-granola/SKILL.md): confirma
conta/workspace, obtém a janela pelo registro local, classifica IDs e usa a transcrição literal.
Sem conector ou verbatim, a ingestão fica bloqueada; o resumo não substitui a evidência.

`granola_id` garante idempotência. Fontes existentes em `raw/` são imutáveis; ambiguidades vão
para `log.md`, que é append-only. Eventos novos precisam de fontes e âncoras temporais e entram
nos índices mensais e na safra pertinente, preservando a rastreabilidade.

## Validar localmente

Na raiz do checkout:

```bash
python3 tools/validar-wiki.py
python3 tools/granola-ingeridos.py
```

Os comandos leem arquivos locais e não consultam APIs. O primeiro verifica estrutura e links;
o segundo confere ingestões e páginas sem fonte. Ambos devem terminar com código 0. Relate os
avisos e pendências separadamente. Não há build, servidor, dependências adicionais nem suíte de
testes automatizados neste repositório. Revise `git diff` e `git status --short`, incluindo os
arquivos novos, e apresente as alterações e a validação antes de publicar.

## Automação diária

O [guia diário](../.agents/skills/ingerir-gravacoes-granola/automacao-diaria.md) contém a frequência
sugerida, os pré-requisitos e as instruções para uma futura tarefa. A automação permanece inativa;
sua ativação exige pedido explícito. As skills em `.cursor/skills/` continuam preservadas.

Nesta adaptação operacional, não se executam ingestões, agendamentos nem APIs externas, e os
conteúdos de `raw/`, `wiki/` e `dados-vivos/` permanecem integralmente preservados.
