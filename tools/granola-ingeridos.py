#!/usr/bin/env python3
"""Registro de idempotência da ingestão do Granola.

Responde a duas perguntas antes de qualquer nova ingestão:

1. quais `granola_id` já entraram na wiki e em que estado;
2. de que data em diante vale consultar o Granola.

A fonte da verdade é o próprio repositório: cada gravação ingerida deixa um arquivo em
`raw/registros-manejo/` ou `raw/registros-ciclos-videira/` com `granola_id` no frontmatter. Uma
gravação pode estar registrada como fonte sem ter gerado evento — é o caso das que ficaram em
`pendencia` por falta de setor, data ou dose. Essas **não** devem ser reingeridas como fonte nova,
mas continuam esperando eventos quando a informação faltante chegar.

Uso:

    python3 tools/granola-ingeridos.py                 # relatório completo
    python3 tools/granola-ingeridos.py <id> [<id> ...] # classifica ids vindos do Granola
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTAS_FONTE = ["raw/registros-manejo", "raw/registros-ciclos-videira"]
PASTAS_WIKI = ["wiki"]


def campo(texto: str, nome: str) -> str | None:
    achado = re.search(rf"^{nome}:\s*(.+)$", texto, re.MULTILINE)
    if not achado:
        return None
    valor = achado.group(1).strip().strip("\"'").replace('\\"', '"')
    return None if valor in ("", "null", "~") else valor


def fontes_ingeridas() -> dict[str, dict[str, str]]:
    registro: dict[str, dict[str, str]] = {}
    for pasta in PASTAS_FONTE:
        for caminho in sorted((RAIZ / pasta).glob("*.md")):
            texto = caminho.read_text(encoding="utf-8")
            gid = campo(texto, "granola_id")
            if not gid:
                continue
            registro[gid] = {
                "fonte": str(caminho.relative_to(RAIZ)),
                "titulo": campo(texto, "titulo") or "",
                "gravado_em": campo(texto, "gravado_em") or "",
                "ingerido_em": campo(texto, "ingerido_em") or "",
            }
    return registro


def paginas_por_id() -> dict[str, list[str]]:
    mapa: dict[str, list[str]] = {}
    for pasta in PASTAS_WIKI:
        for caminho in sorted((RAIZ / pasta).rglob("*.md")):
            gid = campo(caminho.read_text(encoding="utf-8"), "granola_id")
            if gid:
                mapa.setdefault(gid, []).append(str(caminho.relative_to(RAIZ)))
    return mapa


def citados_no_log() -> dict[str, str]:
    """Ids citados no `log.md`, inclusive os descartados por não tratarem do vinhedo.

    As entradas do log referenciam a gravação pelo prefixo de 8 caracteres do `granola_id`.
    """
    citados: dict[str, str] = {}
    for linha in (RAIZ / "log.md").read_text(encoding="utf-8").splitlines():
        if not linha.startswith("## ["):
            continue
        for prefixo in re.findall(r"\b([0-9a-f]{8})\b", linha):
            citados.setdefault(prefixo, linha.strip())
    return citados


def ultima_ingestao() -> str:
    log = (RAIZ / "log.md").read_text(encoding="utf-8")
    datas = re.findall(r"^## \[(\d{4}-\d{2}-\d{2})\] ingest \|", log, re.MULTILINE)
    return max(datas) if datas else "—"


def main(argv: list[str]) -> int:
    registro = fontes_ingeridas()
    paginas = paginas_por_id()

    if argv:
        citados = citados_no_log()
        for gid in argv:
            dados = registro.get(gid)
            if not dados:
                nota = citados.get(gid[:8])
                if nota:
                    print(f"NO LOG      {gid} — sem fonte, mas citada no log.md; não reingerir "
                          f"sem ler a entrada:\n            {nota}")
                else:
                    print(f"NOVO        {gid} — nenhuma fonte no repositório; ingerir")
                continue
            quantas = len(paginas.get(gid, []))
            estado = "JA INGERIDO" if quantas else "SO FONTE   "
            extra = "" if quantas else " — sem página na wiki; conferir a pendência no log.md"
            print(f"{estado} {gid} -> {dados['fonte']} ({quantas} página(s)){extra}")
        return 0

    gravacoes = sorted(registro.items(), key=lambda item: item[1]["gravado_em"])
    print(f"Última entrada `ingest` no log.md: {ultima_ingestao()}")
    if gravacoes:
        print(f"Gravação mais recente já ingerida: {gravacoes[-1][1]['gravado_em']}")
        print("Consultar o Granola dessa data em diante e classificar cada id pelo modo com "
              "argumentos.\n")
    print(f"{len(registro)} gravação(ões) ingerida(s):\n")

    for gid, dados in gravacoes:
        vinculadas = paginas.get(gid, [])
        estado = f"{len(vinculadas)} página(s)" if vinculadas else "SÓ FONTE"
        print(f"  {gid}  {estado:<12} {dados['fonte']}")

    orfas = [gid for gid in registro if not paginas.get(gid)]
    if orfas:
        print("\nFontes registradas sem página na wiki (não reingerir como fonte; aguardam a "
              "resolução da pendência em log.md):")
        for gid in orfas:
            print(f"  {gid} — {registro[gid]['titulo']}")

    sem_fonte = [gid for gid in paginas if gid not in registro]
    if sem_fonte:
        print("\nERRO: páginas citam granola_id sem fonte bruta correspondente:")
        for gid in sem_fonte:
            print(f"  {gid} -> {', '.join(paginas[gid])}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
