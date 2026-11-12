import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Charger et garder les types où il y a des fraudes
df = pd.read_csv("data/transactions.csv")
df = df[df["type"].isin(["TRANSFER", "CASH_OUT"])]
df = df.sample(500000, random_state=1)

# 2. Colonnes utiles (sans les soldes)
df["heure"] = df["step"] % 24
df["type_num"] = (df["type"] == "TRANSFER").astype(int)
X = df[["type_num", "amount", "heure"]]
y = df["isFraud"]

# 3. Séparer 80 % / 20 %
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=1
)

# 4. Entraîner
modele = RandomForestClassifier(
    n_estimators=100, max_depth=12,
    class_weight="balanced", n_jobs=-1, random_state=1,
)
modele.fit(X_train, y_train)

# 5. Tester
print(classification_report(y_test, modele.predict(X_test)))

# 6. Sauvegarder
joblib.dump(modele, "ml/modele_fraude.joblib")

# 7. Fichiers de démo (20 fraudes + 180 normaux)
test = X_test.copy()
test["isFraud"] = y_test
demo = pd.concat([
    test[test.isFraud == 1].sample(20, random_state=1),
    test[test.isFraud == 0].sample(180, random_state=1),
]).sample(frac=1, random_state=1)
demo["type"] = demo["type_num"].map({1: "TRANSFER", 0: "CASH_OUT"})
demo[["type", "amount", "heure"]].to_csv("data/demo.csv", index=False)
demo[["isFraud"]].to_csv("data/demo_reponses.csv", index=False)
print("Modèle et démo créés")