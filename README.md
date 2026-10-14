# wiki-vinhedo — Memória de IA da Alma Gerais

Base de conhecimento viva da vinícola **Alma Gerais** (sul de Minas Gerais), mantida por
agentes de IA e inspirada no padrão [LLM Wiki do Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

O objetivo é dar aos nossos agentes uma **memória persistente e interligada** sobre tudo o que
acontece no cultivo das uvas e na produção dos vinhos — para que eles consigam *ligar os pontos*
ao longo do tempo e apoiar as decisões do time de campo, do enólogo e dos consultores.

## Locais de cultivo

- **Macaia** (foco atual)
- _São Geraldo — expansão futura. A estrutura já é multi-local; basta adicionar a página em `wiki/locais/` quando entrar._

## A ideia central

Não é um RAG que redescobre tudo a cada pergunta. É uma **wiki que o agente constrói e mantém**:
ele lê as fontes, extrai o essencial, cria/atualiza páginas, cruza referências e sinaliza
contradições. Você cura as fontes e faz as perguntas; o agente faz todo o fichamento.

## As camadas

| Camada | Pasta | Quem escreve | O que é |
|---|---|---|---|
| Fontes brutas | `raw/` | Humanos + rotinas | Fonte local, imutável após a entrada. Novas fontes são acrescentadas; as existentes nunca são alteradas. |
| Wiki | `wiki/` | Agente | Conhecimento gerado: entidades, temas, eventos, correlações, hipóteses. |
| Dados vivos | `dados-vivos/` | Humanos + agente | *Como acessar* as APIs (WS Clima e InnoVint). Não guarda dados crus. |
| Schema | `AGENTS.md` | Humanos + agente | As regras e workflows que o agente segue. |

Navegação: `index.md` (catálogo de páginas) e `log.md` (histórico cronológico).

## Como usar (resumo)

- **Ingerir**: coloque uma fonte em `raw/` e peça ao agente para processá-la.
- **Pesquisar**: o agente pode buscar conhecimento externo, priorizando estudos de viticultura em
  clima tropical sem excluir referências internacionais relevantes.
- **Consultar setores**: o agente usa históricos mensais para localizar os eventos pertinentes, sem
  carregar todo o histórico quando a pergunta não exige.
- **Perguntar**: faça perguntas; boas respostas viram páginas novas na `wiki/`.
- **Revisar**: peça periodicamente uma revisão (contradições, dados vencidos, lacunas).

As convenções detalhadas estão em `AGENTS.md`.
