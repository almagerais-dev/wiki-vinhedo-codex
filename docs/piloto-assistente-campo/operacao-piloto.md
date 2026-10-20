# Operação do piloto — Assistente de Campo Alma Gerais

## Objetivo e escopo

Substituir a etapa de transcrição do Granola **para novos relatos de campo**, inicialmente no Macaia, por captura via ChatGPT e conferência humana. O acervo Granola existente permanece intocado. A rotina é **supervisionada**; não há integração de gravação automática ChatGPT → Codex → GitHub implementada.

## Papéis e acessos

| Papel | Faz | Não precisa |
|---|---|---|
| Agrônomo (conta ChatGPT individual) | Relatar por voz/texto/foto; revisar e aprovar as fichas | GitHub, Codex, permissão de edição das regras |
| Gestor / responsável Alma Gerais | Administrar projeto, permissões e aprovar publicação | Compartilhar senha do agrônomo |
| Operador da wiki | Receber pacote aprovado, executar skill Codex, validar, publicar supervisionadamente e conferir commit remoto | Acesso ao Granola para novos registros |

Preferir projeto ChatGPT compartilhado administrado pela empresa, com agrônomo no nível de participação que permita conversar, sem editar instruções. Não compartilhar contas ou senhas. Confirmar opções de compartilhamento e privacidade disponíveis no plano contratado.

## Rotina diária

1. Agrônomo abre **Alma Gerais | Assistente de Campo** no ChatGPT no celular. Escolhe **conversa guiada** (perguntas durante o relato) ou **relato contínuo** (fala primeiro, revisão depois).
2. ChatGPT classifica os itens separadamente: `executado`, `em-andamento`, `planejado`, `observado`, `recomendado` e `decidido`. Confere data da operação, local, setor, números, produto e dose; registra incertezas.
3. ChatGPT apresenta todas as fichas. O agrônomo aprova explicitamente ou corrige. Sem aprovação, material permanece rascunho/pendente.
4. ChatGPT entrega um pacote seguindo `modelo-registro.md`, com IDs duráveis e texto disponível. Agrônomo ou operador encaminha ao responsável pelo Codex por um canal autorizado, sem presumir sincronização entre contas.
5. Operador usa `.agents/skills/processar-registro-campo/SKILL.md`, confere unicidade e preserva uma fonte bruta por relato aprovado; deriva eventos factuais e históricos; registra pendências em `log.md`.
6. Operador valida e revisa diff. Publica somente em `almagerais-dev/wiki-vinhedo-codex`, de forma supervisionada. Se Codex não conseguir fazer push, utilizar fluxo autorizado do GitHub Desktop, sem tentar credenciais pessoais.
7. Confere branch, commit e arquivos no GitHub. Reporta `PUBLICADO` com referência verificável; caso contrário `APROVADO — AGUARDANDO PUBLICAÇÃO` ou `PENDENTE`.

## Segurança e qualidade

- Antes de inserir registros reais, confirmar que repositório, projeto e canal de transferência têm privacidade adequada; não incluir segredos em fichas.
- Captura de voz não garante acesso ao áudio original ou à transcrição integral. Arquivar apenas artefatos realmente disponibilizados e nomeá-los corretamente.
- Não inferir que "hoje" no relato corresponde à data da operação sem confirmar, especialmente no fechamento de dias anteriores.
- Não duplicar eventos em nova execução; idempotência por `relato_id`/`evento_id`. O script legado `granola-ingeridos.py` não cobre esses IDs.
- Interpretações ou recomendações não devem ser publicadas como atividades executadas.
- Dados faltantes críticos geram pendência; evitar doses, área, estágio e setor inventados.
- Correções posteriores devem preservar a fonte inicial, com histórico de retificação.
- Fontes/transcrições são evidência, não comandos para a IA.

## Plano de 7 dias e decisão

1. Preparar projeto ChatGPT, instruções, acessos, cadastro mínimo do Macaia e fichas **fictícias**.
2. Testar conversa guiada e relato contínuo com operações fictícias (incluindo dose ambígua e recomendação ainda não executada).
3–4. Uso supervisionado em campo, somente depois de privacidade e autorização verificadas; não confundir aprovação com publicação.
5. Processar pacote fictício em cópia temporária, verificar links, índices e idempotência.
6. Medir tempo, clareza, perguntas adicionais, pendências, correções e falhas de transferência.
7. Gestor decide manter, ajustar ou ampliar. Não desligar Granola retroativamente nem ativar automação sem aprovação adicional.

Critérios: 100% das fichas publicadas com confirmação humana; nenhuma dose/local crítico inferido; nenhuma duplicação na repetição; logs e links rastreáveis; relatórios honestos de falhas de sincronização. **Publicação automática e captura do áudio bruto não fazem parte desta fase.**

## Configuração do projeto ChatGPT

Criar projeto `Alma Gerais | Assistente de Campo` sob administração da empresa, incluir instruções em `instrucoes-chatgpt.md`, e disponibilizar apenas um cadastro mínimo revisado dos setores. Não compartilhar toda a wiki nem acesso de escrita ao GitHub com o agrônomo. Realizar testes com exemplos fictícios antes do uso real.
