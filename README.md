# Coeur ORA — GrenaPrompt (PoC mini)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Alpha-orange.svg)]()

---

## 🚀 Présentation

**Coeur ORA** est un framework **open-source** (sous licence Apache 2.0) basé sur le langage hybride **GrenaPrompt**.  
Il permet de créer des IA **modulaires, adaptatives et personnalisées** autour de 4 briques principales :  

- 🔒 **LOCK** : règles et contrôle d’accès  
- 🧠 **REM** : mémoire adaptative (cycle 24h)  
- 🤖 **AUTOPROMPT** : génération et amélioration continue de prompts  
- 📊 **AUDIT** : traçabilité et logs  

---

## 📦 Installation

```bash
pip install -e .

ora "Explique en une phrase ce qu’est le Coeur ORA."
"Un framework open-source modulaire qui combine LOCK, REM, AUTOPROMPT et AUDIT pour créer des IA adaptatives."

---

## 🤝 Contribuer

Les contributions sont les bienvenues !  
- Ouvrez une **issue** pour signaler un bug ou proposer une idée  
- Faites une **pull request** pour améliorer le code  

---

## 🧩 MAJ_0 — Brief client

Le dossier `maj_0_demo/` fournit :
- `brief_template.md` : le formulaire client (à remplir)
- `brief_demo.json` : un exemple **déjà rempli**
- `run_maj0.py` : injecte le brief dans le **Cœur d’ORA** et génère un **plan d’activation ORA** (LOCK/REM/AUTOPROMPT/AUDIT)

### Lancer la démo
```bash
pip install -e .
python maj_0_demo/run_maj0.py
# ou avec votre propre brief :
python maj_0_demo/run_maj0.py --brief mon_brief.json --iterations 2

Licence : **Apache 2.0**

