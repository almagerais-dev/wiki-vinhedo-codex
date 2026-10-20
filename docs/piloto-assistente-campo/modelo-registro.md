# Modelo de entrega — registro aprovado do Assistente de Campo

Este modelo é um **contrato de transferência manual** no piloto. Não é evidência de atividade real nem comprovante de publicação.

```yaml
schema: alma-gerais-registro-campo-v1
relato_id: "<ID durável e único, confirmado>"
origem: relato-confirmado-chatgpt
vinhedo: macaia
responsavel_relato: "<identificação aprovada pela empresa>"
relatado_em: "AAAA-MM-DDTHH:MM:SS-03:00"
aprovado_em: "AAAA-MM-DDTHH:MM:SS-03:00"
estado_captura: aprovado
aprovacao_textual: "<confirmação explícita do agrônomo>"
audio_original_disponivel: false
transcricao_literal_disponivel: false
eventos:
  - evento_id: "<relato_id>-01"
    situacao: executado # executado | em-andamento | planejado | observado | recomendado | decidido
    data: "AAAA-MM-DD"
    setor: setor-03
    ruas: [] # somente ruas confirmadas
    operacao: "<operação confirmada>"
    produtos: [] # nome, formulação, dose, unidade, base e volume quando aplicável
    observacoes: "<o que foi observado, sem inferência>"
    estagio_fenologico: null
    safra: null
    pendencias: []
```

## Evidência e conferência

**Relato disponível (texto/dicado):** <copiar exatamente o texto disponível; não chamar de verbatim se não for>

**Correções solicitadas pelo agrônomo:** <registrar alterações ou "nenhuma">

**Fotos/anexos:** <referências reais, se houver, sem inventar URL ou arquivo>

**Confirmação:** <mensagem explícita, por exemplo "Aprovo as fichas 01 e 02">

## Status da transferência

- `RASCUNHO`: sem aprovação; não transferir ao Codex como fato validado
- `APROVADO — AGUARDANDO PUBLICAÇÃO`: revisão humana concluída; aguardando curadoria
- `PENDENTE`: informação essencial precisa de esclarecimento
- `PUBLICADO`: usar somente depois de confirmar commit remoto e arquivos na wiki

Nunca preencher horários, nomes, IDs ou links que não estejam efetivamente disponíveis. Um pacote pode incluir várias fichas vinculadas ao mesmo relato.
