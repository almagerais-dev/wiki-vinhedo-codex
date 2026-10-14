# Automação diária da ingestão (Cursor Automations)

Texto de referência do campo **Agent Instructions** da Automation que roda a ingestão todo dia à
meia-noite. Mantido aqui para que a automação e a skill não divirjam: ao alterar o procedimento em
`SKILL.md`, revise este arquivo e cole o texto atualizado na configuração da Automation.

## Configuração da Automation

| Campo | Valor | Por quê |
|---|---|---|
| Trigger | `Every day at 00:00 GMT-3` | A janela é o dia que acabou de terminar. |
| Repositories | `almagerais-dev/wiki-vinhedo`, branch base `main` | Sem repositório, o agente não clona nem abre PR. |
| Tools | Granola (obrigatório) | É a origem das gravações. |
| Memories | desligada | O estado persistente já é o repositório (`raw/`, `log.md`). A documentação do Cursor alerta que memórias podem ser envenenadas por entrada não confiável, e transcrição automática é exatamente isso. |
| Modelo | esforço de raciocínio alto | Fatiar gravação em eventos homogêneos e decidir entre fato e pendência exige julgamento, não preenchimento de gabarito. |

A criação de Pull Request vem **ligada por padrão** em automações com repositório. Por isso as
instruções precisam dizer explicitamente quando **não** abrir PR.

## Agent Instructions (copiar a partir daqui)

```text
Rotina diária de ingestão das gravações do Granola na wiki da Alma Gerais.

Antes de qualquer ação, leia `AGENTS.md` e execute a skill
`.cursor/skills/ingerir-gravacoes-granola/SKILL.md`, que é o procedimento obrigatório, na ordem dos
seus 10 passos. Em caso de conflito, as regras do `AGENTS.md` prevalecem sobre estas instruções.

Janela: você roda à meia-noite (GMT-3), então as gravações novas são as do dia que acabou. Não
presuma a janela nem a data de hoje: obtenha a janela com `python3 tools/granola-ingeridos.py` e
consulte o Granola dessa data em diante.

Regras de decisão:
- Ingira somente os ids classificados como NOVO. Nunca duplique fonte, evento ou link de índice.
- Id `SO FONTE`: não recrie a fonte bruta. Se uma gravação nova trouxer o dado que faltava, resolva a
  pendência criando os eventos que ficaram pendentes.
- Ingira sempre pelo transcript verbatim (`get_meeting_transcript`), nunca pelo resumo do Granola: o
  resumo já produziu setor inexistente, data impossível e unidade inventada.
- Campo essencial ambíguo (setor, data, dose, estágio fenológico): não invente. Registre `pendencia`
  no `log.md` citando o prefixo de 8 caracteres do `granola_id` e, se o campo faltante impedir
  ancorar o fato, não crie o evento — preserve apenas a fonte.
- Gravação que não trata do vinhedo: não ingira e registre uma entrada `lint` no `log.md` citando o
  prefixo de 8 caracteres do id, para ela não voltar à fila amanhã.
- Não altere nem apague nada que já exista em `raw/`.

Quando abrir Pull Request:
- Abra PR apenas se houver arquivo alterado. Se nenhum id for NOVO e nenhuma pendência for resolvida,
  encerre sem commit e sem PR, informando quantas gravações foram verificadas.
- Antes de abrir o PR, `python3 tools/validar-wiki.py` precisa terminar com 0 erros.
- Não faça merge do PR nem habilite auto-merge.

Se a consulta ao Granola voltar vazia ou a autenticação falhar, não conclua que não houve registro no
dia: encerre sem PR e avise no resumo que a consulta voltou vazia e que pode ser conta ou credencial
errada.

Resumo final, em português, nesta ordem:
1. conta e workspace do Granola consultados, e a janela de datas;
2. gravações verificadas, ingeridas e descartadas;
3. eventos e históricos mensais criados;
4. pendências que precisam de resposta humana;
5. link do PR, quando houver.
```

## Primeira execução

A documentação do Cursor não afirma explicitamente que `AGENTS.md` e as skills do repositório são
carregados numa Automation — só que automações são Cloud Agents e que rules e skills de projeto valem
para os agentes do repositório. Por isso as instruções acima mandam ler os dois arquivos de forma
explícita, em vez de contar com o carregamento automático.

Confira na primeira execução se o agente citou a skill e as convenções do `AGENTS.md` (por exemplo, a
convenção de `safra` pelo ano da colheita). Se não citar, o texto acima já cobre o caso, porque manda
abrir os arquivos.
