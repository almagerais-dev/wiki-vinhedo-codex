#!/usr/bin/env python3
"""Lint estrutural da wiki-vinhedo.

Verifica o que dá para verificar por máquina, sem julgar conteúdo:

- todo arquivo `.md` da wiki começa com frontmatter YAML parseável (`raw/` é livre por ser fonte
  bruta imutável);
- todo wikilink `[[alvo]]` aponta para um arquivo `.md` existente no repositório; placeholders de
  gabarito (`[[<setor>]]`) e os exemplos do `AGENTS.md` ficam fora da conferência;
- páginas factuais (`evento`, `historico-mensal-setor`) trazem as âncoras temporais obrigatórias;
- eventos de campo citam ao menos um setor e ao menos uma fonte;
- caminhos listados em `fontes` que apontam para `raw/` ou `dados-vivos/` existem.

Uso: `python3 tools/validar-wiki.py` na raiz do repositório. Sai com código 1 se houver erro.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTAS = ["wiki", "dados-vivos", "raw"]
ARQUIVOS_RAIZ = ["index.md", "log.md", "AGENTS.md", "README.md"]

ANCORAS_EVENTO = ["tipo", "categoria", "local", "safra", "estagio_fenologico"]
CATEGORIAS_DE_CAMPO = {"manejo", "fenologia"}
ANCORAS_HISTORICO = ["tipo", "setor", "ano", "mes", "data_inicio", "data_fim"]
ESTAGIOS = {
    "dormencia", "brotacao", "floracao", "pegamento", "crescimento-baga",
    "veraison", "maturacao", "colheita", "pos-colheita", "null", "None",
}

erros: list[str] = []
avisos: list[str] = []


def markdowns() -> list[Path]:
    achados = [RAIZ / nome for nome in ARQUIVOS_RAIZ if (RAIZ / nome).exists()]
    for pasta in PASTAS:
        achados.extend(sorted((RAIZ / pasta).rglob("*.md")))
    return achados


def frontmatter(texto: str) -> dict[str, str] | None:
    if not texto.startswith("---\n"):
        return None
    fim = texto.find("\n---", 4)
    if fim == -1:
        return None
    campos: dict[str, str] = {}
    for linha in texto[4:fim].split("\n"):
        if not linha or linha.startswith((" ", "-", "#")):
            continue
        if ":" not in linha:
            continue
        chave, _, valor = linha.partition(":")
        campos[chave.strip()] = valor.strip()
    return campos


def main() -> int:
    arquivos = markdowns()
    por_nome = {caminho.stem: caminho for caminho in arquivos}

    for caminho in arquivos:
        rel = caminho.relative_to(RAIZ)
        texto = caminho.read_text(encoding="utf-8")

        if caminho.name != "AGENTS.md":
            for alvo in re.findall(r"\[\[([^\]|#]+)", texto):
                alvo = alvo.strip()
                if "<" in alvo or "-" == alvo[:1]:
                    continue
                if alvo not in por_nome:
                    erros.append(f"{rel}: wikilink sem destino -> [[{alvo}]]")

        if caminho.name in ("log.md", "AGENTS.md", "README.md"):
            continue
        if rel.parts[0] == "raw":
            continue

        campos = frontmatter(texto)
        if campos is None:
            erros.append(f"{rel}: sem frontmatter YAML no início do arquivo")
            continue

        tipo = campos.get("tipo", "")
        gabarito = caminho.name.startswith("_modelo-")

        if tipo == "evento" and not gabarito:
            categoria = campos.get("categoria", "")
            de_campo = categoria in CATEGORIAS_DE_CAMPO

            for campo in ANCORAS_EVENTO:
                if campo not in campos:
                    erros.append(f"{rel}: evento sem a âncora obrigatória `{campo}`")

            data = campos.get("data", "")
            periodo = "data_inicio" in campos and "data_fim" in campos
            if not data and not periodo:
                erros.append(f"{rel}: evento sem `data` nem par `data_inicio`/`data_fim`")

            estagio = campos.get("estagio_fenologico", "")
            if estagio and estagio not in ESTAGIOS:
                erros.append(f"{rel}: estagio_fenologico inválido -> {estagio}")

            # `setores`, `ingerido_em` e `fontes` são obrigatórios nos registros de manejo e de
            # ciclos da videira; nas outras categorias a ausência é apenas uma lacuna a cobrir.
            faltas = [
                ("setores", campos.get("setores", "[]") == "[]", "evento sem setor"),
                ("ingerido_em", "ingerido_em" not in campos, "evento sem `ingerido_em`"),
                ("fontes", campos.get("fontes", "[]") == "[]", "evento sem fonte"),
            ]
            for _, falta, mensagem in faltas:
                if not falta:
                    continue
                (erros if de_campo else avisos).append(f"{rel}: {mensagem}")

            if not re.match(r"^\d{4}-\d{2}-\d{2}", caminho.name):
                erros.append(f"{rel}: nome de evento não começa pela data")
            inicio = data or campos.get("data_inicio", "")
            if inicio and not caminho.name.startswith(inicio):
                erros.append(f"{rel}: nome do arquivo não bate com a data do frontmatter ({inicio})")

        if tipo == "historico-mensal-setor" and not gabarito:
            for campo in ANCORAS_HISTORICO:
                if campo not in campos:
                    erros.append(f"{rel}: histórico mensal sem `{campo}`")
            setor = campos.get("setor", "")
            if setor and setor != caminho.parent.name:
                erros.append(f"{rel}: setor `{setor}` fora do diretório `{caminho.parent.name}`")

        for referencia in re.findall(r"(raw/[\w\-./]+|dados-vivos/[\w\-./]+)", texto):
            if referencia.endswith((".md", ".geojson", ".json", ".png", ".pdf")) and not (RAIZ / referencia).exists():
                erros.append(f"{rel}: fonte citada não existe -> {referencia}")

    for aviso in avisos:
        print(f"aviso: {aviso}")
    for erro in erros:
        print(f"ERRO: {erro}")

    print(f"\n{len(arquivos)} arquivos verificados; {len(erros)} erros, {len(avisos)} avisos.")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
