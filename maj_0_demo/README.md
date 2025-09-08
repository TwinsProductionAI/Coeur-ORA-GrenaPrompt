# 🚀 MAJ_0 — Starter pack du Cœur d’ORA

Ce dossier fournit une **démonstration clé en main** du framework :  
- 📝 un questionnaire client (brief)  
- ⚙️ un script d’exécution (`run_maj0.py`)  
- 📂 un jeu de données d’exemple (`brief_demo.json`)  

Objectif : montrer le fonctionnement de **LOCK → REM → AUTOPROMPT → AUDIT** immédiatement, sans configuration complexe.

---

## ▶️ Lancer la démo

```bash
# Installation locale
pip install -e .

# Exécution avec le jeu de données fourni
python maj_0_demo/run_maj0.py --input maj_0_demo/brief_demo.json


---

[LOCK] Sécurisation du contexte en cours...
[REM] Mémoire initialisée avec le brief utilisateur
[AUTOPROMPT] Génération de prompts à partir des données...
[AUDIT] Vérification des réponses → OK ✅

Demo terminée avec succès (client : "Optimiser la relation client").


📋 Questionnaire client (MAJ_0)

Voici un extrait du questionnaire de démo :

Quel est votre principal objectif avec l’IA ?

Exemple : "Optimiser la relation client"

Quel niveau de personnalisation attendez-vous ?

Options : Basique / Avancé / Complet
Exemple : "Avancé"

Quelle contrainte prioritaire doit être respectée ?

Exemple : "Respect RGPD", "Budget limité", "Sécurité forte"

👉 Vous pouvez personnaliser vos propres briefs en partant du fichier :
brief_template.md

📂 Structure du dossier

brief_demo.json → Données fictives prêtes à l’emploi

brief_template.md → Modèle pour créer votre propre questionnaire

run_maj0.py → Script qui exécute la démonstration

🔮 Prochaines étapes

Ajout de nouveaux jeux de données clients

Intégration avec API externes (CRM, analytics, etc.)

Génération automatique de rapports après chaque exécution

📜 Licence

Ce projet est publié sous licence Apache 2.0
.
Framework principal disponible dans le README du repo
.
