
# Framework GrenaPrompt (FGP)

Le **Framework GrenaPrompt** (FGP) fournit un ensemble de règles et de mécanismes de gouvernance
pour le Cœur d'ORA. Il garantit la cohérence, la sécurité et la traçabilité des actions de l'IA.

## Principes clés

- **Verrouillage (LOCK)** : les paramètres principaux du Cœur d'ORA sont verrouillés pour 24 heures
  afin d'assurer une stabilité dans la personnalité et les réponses.
- **Checkpoints** : des points de contrôle toutes les 12 heures permettent d'auditer les interactions
  et de réinjecter des instructions si nécessaire.
- **Autoprompts** : l'IA génère régulièrement ses propres prompts de vérification afin de détecter
  d'éventuelles dérives et de maintenir l'alignement avec les valeurs définies.
- **Journalisation et empreintes digitales** : chaque interaction est enregistrée avec un hachage
  unique pour garantir l'intégrité et l'auditabilité des conversations.

## Langage GrenaPrompt

Le GrenaPrompt est un **langage hybride** qui combine :

- des structures **JSON** pour définir des modules, des paramètres et des règles de fonctionnement ;
- des instructions en **français ou anglais** pour contextualiser et personnaliser les tâches de l'IA.

Ce mélange offre un contrôle granulaire tout en laissant la place à la créativité et à l'interprétation. Les
instructions peuvent notamment préciser : la tonalité, le niveau de créativité, les leviers de persuasion
(SONCAS), ou encore les contraintes de temps (par exemple la marge d'erreur de 7 %).

## Sécurité et éthique

Le FGP vise également à assurer que l'IA reste conforme à des principes éthiques :

- **Confidentialité** : les données sensibles des utilisateurs ne sont jamais stockées sans protection.
- **Transparence** : les règles et décisions de l'IA sont documentées et peuvent être auditées.
- **Adaptabilité contrôlée** : bien que la mémoire soit adaptative, elle reste encadrée par le FGP pour
  empêcher toute dérive ou manipulation involontaire.

Les paramètres du FGP peuvent être adaptés selon les besoins des clients, mais les principes fondamentaux
restent immuables pour préserver la confiance et la cohérence du système.

