import joblib
import pandas as pd

modele = joblib.load("ml/modele_fraude.joblib")
demo = pd.read_csv("data/demo.csv")
vrai = pd.read_csv("data/demo_reponses.csv")["isFraud"]

X = pd.DataFrame({
    "type_num": (demo["type"] == "TRANSFER").astype(int),
    "amount": demo["amount"],
    "heure": demo["heure"],
})
score = modele.predict_proba(X)[:, 1]
demo["decision"] = pd.cut(score, [-1, 0.4, 0.7, 2], labels=["passer", "vérifier", "bloquer"])
demo["fraude"] = vrai

print(pd.crosstab(demo["decision"], demo["fraude"]))