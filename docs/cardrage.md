# Note de cadrage : Fortuno IA

## 1. Le besoin
Les sociétés de paiement mobile perdent de l'argent à cause des fraudes.
Les équipes de contrôle vérifient les paiements à la main : c'est lent,
et beaucoup de fraudes passent sans être vues.

## 2. La cible
Les équipes de contrôle et de sécurité des sociétés de paiement mobile
.

## 3. La solution
Fortuno IA donne un score de risque à chaque paiement grâce à un modèle de
Machine Learning. L'utilisateur envoie un paiement ou un fichier CSV, et
l'application répond pour chaque paiement : passer, vérifier ou bloquer.

## 4. Fonctionnalités du MVP
1. Créer un compte et se connecter
2. Saisir un seul paiement (type, montant, heure) et voir son score
3. Envoyer un fichier CSV (une journée, une semaine) et voir un tableau
   avec un score par ligne, en couleurs (vert, orange, rouge)
4. Consulter l'historique de ses analyses
5. Page d'accueil qui explique l'utilisation en 3 étapes


## 7. Les données
Dataset PaySim (Kaggle) : paiements de mobile money simulés, avec la
réponse « fraude » ou « normal ». Les colonnes de soldes sont retirées,
car elles révèlent la réponse (fuite de données, signalée par Kaggle).
Le modèle utilise 3 colonnes : type, montant, heure.

## 8. Résultat sur la démo
Sur 200 paiements de test contenant 20 vraies fraudes :
- 12 fraudes sur 20 signalées (7 bloquées, 5 à vérifier)
- 8 fraudes ratées
- environ 10 % de paiements normaux signalés à tort

## 9. Risques et limites
- Le modèle ne voit que 3 informations : il rate une partie des fraudes
  et fait des fausses alertes.
- Il est entraîné sur des données simulées : pour une vraie entreprise,
  il faudrait le réentraîner avec ses propres données.
- La démo contient 10 % de fraudes. En vrai, elles sont bien plus rares
  (environ 1 pour 300), donc il y aurait plus de fausses alertes.
- SQLite et le serveur de développement ne conviennent pas à beaucoup
  d'utilisateurs en même temps.

## 10. Critères de réussite
- L'application marche de bout en bout (compte, analyse, historique)
- Un fichier CSV de 200 paiements est analysé en quelques secondes
- Le dépôt GitHub est propre et le README permet de tout relancer