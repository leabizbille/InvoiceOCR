# Projet Billing, OCR avec Azure : Laurence

Le projet vise à examiner les exigences d'une entreprise cliente pour une nouvelle application intégrant un service d'intelligence artificielle. Cela impliquait de comprendre
les besoins métier, les défis à surmonter et les attentes des utilisateurs. L'objectif était de définir avec précision les objectifs de développement en tenant compte des 
besoins identifiés et des contraintes techniques, tout en garantissant la faisabilité et la viabilité du projet. Suite à cette analyse, le client exprime le besoin d'améliorer
sa procédure de pré-traitement des factures. Il souhaite élargir les fonctionnalités de pré-traitement en y ajoutant la reconnaissance optique de caractères (OCR), permettant 
ainsi d'automatiser le reporting de sa comptabilité fournisseurs.
Pour répondre à ces exigences, les interfaces de l'application ont été développées en utilisant des outils et langages de programmation appropriés, tout en respectant 
les spécifications fonctionnelles, techniques et de gestion des données établies. Les détails des spécifications sont inclus dans ce document, décrivant en détail les
fonctionnalités requises, les interactions avec les utilisateurs et les résultats attendus.


* **Trello** :

* **La Présentation** : https://github.com/leabizbille/InvoiceOCR/blob/main/OCR%20avec%20Azure.pdf
  
*  **Le rapport** : https://github.com/leabizbille/InvoiceOCR/blob/main/OCR.pdf

* La **Base de Donnée Relationnelle**, réalisée sous _DBeaver_ et hébergée sur _Azure_ : Le fichier *SQL_CreationTables.py*
  
* **Code Python** :
  * Le fichier *requirements.txt* indique l'ensemble des packages qui seront utilisés dans ce projet.
  * Le fichier *connexion* contient les informations et la requete pour ajouter des lignes dans la base SQL.
  * Le fichier *database* contient le script python et SQL de la création de la base de données.
  * Le fichier *geolocalisateur* contient le lien avec l'API de géolocalisation et comment récupérer les informations SIG de la ville désirée.
  * Le fichier *meteo* contient le lien avec l'Api de la météo et comment récupérer les informations désirées.

-----------------------------------------------------------------------------------------------------------------------------------
  
Voici les points soutenus dans ce projet:

● Intégrer la connexion à l’API Azure Cognitives Services.
● Intégrer les appels aux fonctions de OCR,
● Intégrer la connexion à l’API des factures,
● Gestion des du texte,
● Stocker les résultats en base de données sur Azure,
● Monitorer la qualité du résultat en tenant compte de l’incertitude liée à l'OCR,
● Exposer et intégrer les résultats sous forme de graphique,
● Documenter, versionner, livrer les scripts.


Ce projet s'inscrit dans un cadre global consistant à exploiter des services d’IA externes dans le développement d’applications d’IA, avec pour missions de :

● préconiser un service d’IA en fonction du besoin et des paramètres du projet,
● intégrer dans une application existante l’API du modèle ou du service d’intelligence artificielle,
● appliquer les bonnes pratiques de sécurité et d’accessibilité dans le développement d’application web,
● développer des tests d’intégration sur le périmètre de l’API exploité,
● rédiger une documentation technique.
