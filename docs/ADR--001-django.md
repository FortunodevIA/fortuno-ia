# ADR 001 : Choix de Django pour le back-end et le front-end

## Contexte
Il faut une application web complète (connexion, base de données, pages)
en une journée, avec un modèle de Machine Learning en Python.

## Décision
Nous utilisons Django.

## Raisons
- Le modèle ML est en Python : pas besoin de deuxième langage ni d'API séparée.
- Django fournit déjà la connexion, les mots de passe sécurisés et les formulaires.
- Les pages sont générées côté serveur : plus rapide à construire.

## Conséquences
- Moins de souplesse qu'un front séparé (React), mais bien plus rapide à livrer.
- Pour un gros volume, il faudrait ajouter une API et un serveur de production.