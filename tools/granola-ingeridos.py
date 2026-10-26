#!/usr/bin/env python3
"""Auditoria local do acervo histórico do Granola (fluxo encerrado em 2026-10-26).

Lê fontes, páginas e log; não acessa APIs nem recomenda coleta ou ingestão nova.
Fontes sem página podem ser pendências, correções ou evidência complementar;
verifique `wiki/pendencias.md`, `fontes` dos eventos e o log antes de classificá-las.
O registro pelo chat usa `registro_chat_id` e não depende deste utilitário.

Uso: python3 tools/granola-ingeridos.py [<id> ...]
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
                    print(f"SEM FONTE   {gid} — ID não localizado no acervo legado; nenhuma ingestão é executada")
                continue
            quantas = len(paginas.get(gid, []))
            estado = "JA INGERIDO" if quantas else "SO FONTE   "
            extra = "" if quantas else " — sem página com este ID primário; conferir fontes dos eventos, painel e log"
            print(f"{estado} {gid} -> {dados['fonte']} ({quantas} página(s)){extra}")
        return 0

    gravacoes = sorted(registro.items(), key=lambda item: item[1]["gravado_em"])
    print(f"Última entrada `ingest` no log.md: {ultima_ingestao()}")
    if gravacoes:
        print(f"Gravação mais recente já ingerida: {gravacoes[-1][1]['gravado_em']}")
        print("Acervo legado: não consultar o Granola nem buscar transcrições.\n")
    print(f"{len(registro)} gravação(ões) ingerida(s):\n")

    for gid, dados in gravacoes:
        vinculadas = paginas.get(gid, [])
        estado = f"{len(vinculadas)} página(s)" if vinculadas else "SÓ FONTE"
        print(f"  {gid}  {estado:<12} {dados['fonte']}")

    orfas = [gid for gid in registro if not paginas.get(gid)]
    if orfas:
        print("\nFontes sem página com seu ID primário (podem ser correções ou pendências; "
              "verificar fontes dos eventos, wiki/pendencias.md e log.md):")
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
