# Fortuno IA

Application web qui donne un score de risque de fraude aux paiements mobiles.
L'utilisateur saisit un paiement ou envoie un fichier CSV, et voit pour chaque
paiement une décision : passer, vérifier ou bloquer.

## Installation
git clone https://github.com/presidentfortuno-star/fortuno-ia.git
cd fortuno-ia
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser

## Entraîner le modèle
1. Télécharger PaySim : https://www.kaggle.com/datasets/ealaxi/paysim1
2. Renommer le fichier en `data/transactions.csv`
3. Lancer : python ml/train.py
(crée `ml/modele_fraude.joblib` et les fichiers de démo `data/demo.csv`)

## Lancer l'application
python manage.py runserver
Ouvrir http://127.0.0.1:8000

## Structure
- config/ : réglages Django
- fraude/ : application (modèles, vues)
- templates/ : pages HTML
- ml/ : entraînement du modèle
- data/ : données (non envoyées sur GitHub)
- docs/ : cadrage, ADR, maquettes

## Limites
Le modèle utilise 3 colonnes (type, montant, heure). Les colonnes de soldes
sont retirées pour éviter une fuite de données (recommandation du dataset).
Il trouve environ la moitié des fraudes et fait des fausses alertes.