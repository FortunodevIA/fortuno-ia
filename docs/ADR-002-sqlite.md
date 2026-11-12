# ADR 002 : Choix de SQLite pour la base de données

## Contexte
L'application garde les utilisateurs, les analyses et les transactions.

## Décision
Nous utilisons SQLite, la base fournie par défaut avec Django.

## Raisons
- Aucune installation : un seul fichier, idéal pour le MVP et la démo.
- Suffisant pour quelques milliers de lignes.
- Le code ne change presque pas si on passe à PostgreSQL plus tard.

## Conséquences
- Pas adapté à beaucoup d'utilisateurs en même temps.
- En production, on migrerait vers PostgreSQL.