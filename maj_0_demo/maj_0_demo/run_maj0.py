#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MAJ_0 — Démo brief client → Cœur ORA
Charge un brief JSON, construit un prompt et exécute ORACore.cycle().
LOCK → REM → AUTOPROMPT → AUDIT (selon config du cœur).

Usage:
  python maj_0_demo/run_maj0.py
Options:
  --brief maj_0_demo/brief_demo.json
  --iterations 2
  --no-audit
"""

from __future__ import annotations
import json
import argparse
from pathlib import Path
from typing import Any, Dict

try:
    from ora_core import ORACore  # import du cœur ORA
except Exception as e:
    raise SystemExit(
        "❌ Impossible d'importer ORACore.\n"
        "Installe d'abord le projet :\n"
        "  pip install -e .\n"
        f"Détail: {e}"
    )

ROOT = Path(__file__).resolve().parent
DEFAULT_BRIEF = ROOT / "brief_demo.json"

def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"❌ Fichier introuvable: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise SystemExit(f"❌ JSON invalide ({path}): {e}")

def build_prompt_from_brief(brief: Dict[str, Any]) -> str:
    ident = brief.get("identite", {})
    aud = brief.get("audience", {})
    voix = brief.get("voix", {})
    use_cases = brief.get("use_cases", [])
    sources = brief.get("sources", [])
    contraintes = brief.get("contraintes", {})
    kpi = brief.get("kpi", [])

    src_txt = "\n".join([f"- {s.get('type')}: {s.get('value')}" for s in sources]) or "- (aucune fournie)"
    uc_txt = "\n".join([f"- {u}" for u in use_cases]) or "- (à préciser)"
    kpi_txt = ", ".join(kpi) or "(à définir)"
    afaire = ", ".join(voix.get("a_faire", []))
    aeviter = ", ".join(voix.get("a_eviter", []))

    prompt = f"""
Tu es un architecte IA pragmatique. Tu dois proposer un **plan d'activation ORA** cohérent
à partir d'un brief client. Ta sortie doit être structurée.

=== IDENTITÉ ===
Entreprise: {ident.get('entreprise')}
Secteur: {ident.get('secteur')}
Mission: {ident.get('mission')}
Langues: {", ".join(ident.get("langues", []))}

=== AUDIENCE ===
Persona principal (rôle/objectifs/douleurs): {aud.get('persona_principal')}
Canaux: {", ".join(aud.get("canaux", []))}

=== VOIX & STYLE ===
Ton: {voix.get('ton')}
À faire: {afaire}
À éviter: {aeviter}
Langue de réponse: {voix.get('langue_reponse')}

=== CAS D'USAGE PRIORITAIRES ===
{uc_txt}

=== SOURCES DISPONIBLES ===
{src_txt}

=== CONTRAINTES / COMPLIANCE ===
Légal: {contraintes.get('legal')}
Garde-fous: {", ".join(contraintes.get("garde_fous", []))}

=== KPI CIBLÉS ===
{kpi_txt}

# OBJECTIF DE SORTIE
1) Synthèse du contexte (5 lignes max).
2) Règles **LOCK** proposées (3 à 5 règles claires).
3) Seeds de **REM** (mémoire persistante à initialiser).
4) Boucle **AUTOPROMPT** — 3 tâches initiales concrètes.
5) **AUDIT** — quels événements logger et pourquoi.
6) Mesure des KPI (comment, fréquence, seuils).
Réponds en français, sous forme de plan opérationnel.
""".strip()
    return prompt

def main():
    p = argparse.ArgumentParser(description="MAJ_0 — brief client → plan ORA")
    p.add_argument("--brief", default=str(DEFAULT_BRIEF), help="Chemin du brief JSON")
    p.add_argument("--iterations", type=int, default=1, help="Itérations AUTOPROMPT (défaut: 1)")
    p.add_argument("--no-audit", action="store_true", help="Désactiver les logs d'audit")
    args = p.parse_args()

    brief = load_json(Path(args.brief))
    prompt = build_prompt_from_brief(brief)

    core = ORACore(admin_only=False, iterations=args.iterations, audit=not args.no_audit)

    print("🚀 MAJ_0 — Brief client injecté dans le Cœur ORA")
    print("    (LOCK → REM → AUTOPROMPT → AUDIT)")
    print("-------------------------------------------------\n")
    result = core.cycle(prompt)
    print(result.strip())
    print("\n✅ Terminé.")

if __name__ == "__main__":
    main()
