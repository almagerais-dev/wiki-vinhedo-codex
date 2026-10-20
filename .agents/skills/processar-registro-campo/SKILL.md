---
name: processar-registro-campo
description: Processa fichas de atividades agrícolas aprovadas pelo agrônomo, recebidas do Assistente de Campo, em fontes imutáveis, eventos e índices da wiki-vinhedo-codex.
---

# Processar registro de campo aprovado

Trabalhe **somente** em `almagerais-dev/wiki-vinhedo-codex`. Leia `AGENTS.md` inteiro e `docs/piloto-assistente-campo/operacao-piloto.md`. Não use o repositório original do Cursor. Esta skill recebe um **pacote aprovado** do ChatGPT, sem dependência do Granola.

## 1. Validar a entrada

Exija pacote com `relato_id`, responsável identificado de maneira apropriada, origem, data do relato, estado `aprovado`, confirmação humana e fichas com `evento_id`. Conferir `relato_id` e `evento_id` já existentes em `raw/` e `wiki/`: **não criar duplicatas**. Se não houver garantia de unicidade, não publique; peça confirmação de identificador durável ao responsável.

O relato disponível, alterações do agrônomo e marca de aprovação compõem a evidência. Não afirme possuir áudio nem verbatim quando esses não foram entregues. Um pacote pode ter múltiplos eventos e **uma fonte bruta imutável**.

## 2. Separar fatos

Somente fatos executados ou observados, com data e setor confirmados, entram em `wiki/eventos/`. Planejamentos, recomendações e decisões ainda não executadas não se transformam em eventos de execução: manter a fonte e encaminhar ao tipo de página apropriado após revisão humana.

Se data, setor ou operação essencial estiver ambíguo, registrar pendência e **não criar evento com precisão inventada**. Preserve o material recebido, se autorizado, sem reescrever seu relato original.

## 3. Gerar fonte e páginas

- Criar uma fonte em `raw/registros-campo/AAAA-MM-DD-macaia-<descricao>.md` com frontmatter incluindo `tipo: fonte-registro-campo`, `origem: relato-confirmado-chatgpt`, `relato_id`, `relatado_em`, `aprovado_em`, `responsavel_relato`, `local`, `ingerido_em` e referências ao pacote; armazenar as fichas e o texto disponível com correções, explicitando indisponibilidade de áudio/verbatim.
- Criar eventos factuais em `wiki/eventos/` segundo o schema de `AGENTS.md` com `fontes` apontando para essa fonte; `granola_id: null` e `relato_id`/`evento_id` como identificadores adicionais. Respeitar `safra` e `estagio_fenologico`: se incertos, marcar pendência conforme regras da wiki, não presumir.
- Atualizar índices mensais dos setores, páginas de setor, safra, variedade/tema quando aplicável, `index.md` apenas quando houver novas entidades/índices e `log.md` de modo append-only.

**Não modificar uma fonte em `raw/` já existente.** Retificações posteriores devem produzir registro de correção vinculado, sem reescrever a evidência original.

## 4. Verificar e publicar

Execute `python3 tools/validar-wiki.py` e `python3 tools/granola-ingeridos.py`; este último verifica apenas o acervo legado Granola e **não é o validador da idempotência dos novos relatos**. Confirme separadamente a unicidade de `relato_id`/`evento_id`, links e `git diff --check`.

Apresente diff, itens pendentes e validação ao responsável. No piloto, **não faça commit, push nem merge automaticamente**. Publicação deve ser supervisionada no repositório correto. Só marque a ficha `PUBLICADO` após confirmar commit remoto e presença dos arquivos no GitHub.

## 5. Critérios de interrupção

Pare se não houver aprovação, dados essenciais estiverem ambíguos, já existir identificador processado, houver divergência com fato prévio, destino Git estiver errado, publicação indisponível ou validação com erro. Não busque Granola como substituto.
