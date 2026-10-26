---
name: registrar-relatos-chat
description: Registra na wiki da Alma Gerais operações e observações relatadas pelo operador diretamente no chat, incluindo esclarecimentos e correções. Use ao receber registros novos de campo; perguntas e planos não são fatos realizados.
---

# Registrar relatos pelo chat

Leia `AGENTS.md` inteiro. Trabalhe no checkout de `almagerais-dev/wiki-vinhedo-codex`.
O operador conversa diretamente com o agente; não há conector Granola, transcrição ou coleta diária
como pré-requisito. O relato deve ser registrado durante o atendimento.

## 1. Entender e esclarecer

Distinga fato ocorrido de intenção, pergunta ou recomendação. Extraia data do fato, local,
setores, operação/observação, produtos, doses, unidades e estágio quando declarados. Pergunte
pelos campos essenciais ausentes no próprio chat, sem exigir que o operador preencha um formulário.
Resolva “hoje” e “ontem” pela data da mensagem em `America/Sao_Paulo`, preservando a expressão
original e explicitando a data usada. Se a data da mensagem não for conhecida, pergunte.
Não deduza variedades do cadastro, setores da ordem de polígonos, produtos de relatos vizinhos
ou estágio apenas pela proximidade com a poda. A convenção vigente de safra é o ano da colheita
(poda de agosto de 2026 → safra 2027), ainda pendente de confirmação; sinalize essa convenção.
Estágio incerto fica `null`, com pendência. Contradições exigem esclarecimento do operador.

## 2. Preservar a fonte e evitar duplicações

Antes de criar arquivos, confira `raw/registros-*/`, eventos e `log.md` para identificar relatos
já registrados, repetições e pendências. O mesmo fato repetido não gera outro evento; uma nova
mensagem que o confirme pode ser preservada como fonte adicional.

Salve as mensagens relevantes literalmente, sem substituir pelo resumo do agente, em uma fonte
nova em `raw/registros-manejo/` ou `raw/registros-ciclos-videira/`. Uma mensagem mista tem uma
única fonte. Nome: `AAAA-MM-DD-macaia-relato-chat-<identificador>.md`, pela data de recebimento.
Use `origem: chat`, `registro_chat_id`, `recebido_em`, `ingerido_em`, `local` e `operador` quando
conhecido. Preserve IDs/links da conversa e das mensagens se disponíveis; na ausência deles,
gere um UUID local uma única vez (`python3 -c 'import uuid; print(uuid.uuid4())'`) e identifique-o
como ID local, sem inventar link ou ID da plataforma. Não exija `granola_id`.

Fontes existentes nunca são editadas nem apagadas. Esclarecimentos viram outra fonte com seu
próprio ID e referência à anterior. Relacione ambas em `fontes` no evento e registre a resolução
no log, preservando a pendência antiga. Fonte sem dado essencial pode ficar sem evento.

## 3. Criar eventos e indexar

Copie `wiki/eventos/_modelo-evento.md`; repita o `registro_chat_id` da fonte primária e cite todas
as fontes usadas. Separe fatos por data, operação e estágio. Uma operação idêntica na mesma data
em vários setores pode ter um único evento com `setores` e nome
`AAAA-MM-DD-macaia-setores-<a>-<b>-<descricao>.md`. Períodos têm `data` inicial e `data_inicio`/`data_fim`.
Não altere silenciosamente fatos contraditos: esclareça e documente a correção e suas fontes.

Atualize histórico mensal de cada setor (uma linha por evento), links de volta dos setores,
linha do tempo da safra, temas e variedades afetados. Inclua históricos novos no `index.md`;
eventos atômicos não entram no índice raiz. Acrescente `ingest` no `log.md` com ID/caminho da fonte,
eventos e índices afetados; registre `pendencia` para ambiguidades e a resolução quando respondida.
Atualize também `wiki/pendencias.md` ao abrir ou resolver dúvidas, citando a evidência da resolução.
Não proponha relações causais durante o registro factual.

## 4. Validar e responder

Rode `python3 tools/validar-wiki.py` e revise `git diff` e arquivos novos.
Confira que nenhuma fonte preexistente de `raw/` foi alterada ou apagada e que cada evento cita
sua fonte. O utilitário legado `tools/granola-ingeridos.py` não é necessário para registros de chat.
Responda com os fatos registrados, datas e setores, links das páginas e perguntas pendentes.
Apresente validação e alterações antes de publicar; não faça merge sem autorização explícita.
