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

## Registrar pelo chat

O operador relata diretamente aqui as operações e observações. Exemplo: “Hoje fizemos o
desbrote no setor 3”. O agente segue
[registrar-relatos-chat](../.agents/skills/registrar-relatos-chat/SKILL.md), esclarece dados
faltantes na conversa, preserva a mensagem literal em `raw/` e atualiza eventos, índices mensais,
setores e safra. Perguntas e operações planejadas não viram fatos realizados.
O painel `wiki/pendencias.md` reúne dúvidas abertas e resoluções; atualize-o junto com o log.
Exemplos didáticos ficam em `docs/exemplos/` e não são evidência de campo.

Cada relato tem `registro_chat_id`; eventos citam esse identificador e o caminho da fonte.
Mensagens de correção são fontes novas, ligadas ao relato anterior. Fontes existentes são
imutáveis e o log é append-only. Datas dos fatos são distintas das datas de recebimento.

## Validar localmente

```bash
python3 tools/validar-wiki.py
```

Revise `git diff` e `git status --short`, incluindo arquivos novos, e apresente alterações,
validação, avisos e pendências antes de publicar. Não há build ou servidor neste repositório.

## Encerramento do fluxo anterior

Desde 2026-10-26, não se consultam notas do Granola nem se buscam transcrições, e não há rotina
diária de coleta. Os guias de agendamento foram retirados. Nenhuma automação foi encontrada na
conta do ChatGPT durante esta mudança. Agendamentos em sistemas externos não foram verificados.
O acervo histórico mantém suas fontes e `granola_id`; `tools/granola-ingeridos.py` é apenas uma
ferramenta opcional de auditoria local desse legado, sem requisito no atendimento por chat.
