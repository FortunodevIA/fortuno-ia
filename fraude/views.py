import joblib
import pandas as pd
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Analyse, Transaction

MODELE = joblib.load(settings.BASE_DIR / "ml" / "modele_fraude.joblib")


def decision(score):
    if score >= 0.7:
        return "bloquer"
    if score >= 0.4:
        return "vérifier"
    return "passer"


def accueil(request):
    return render(request, "accueil.html")


def inscription(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("accueil")
    return render(request, "registration/inscription.html", {"form": form})


@login_required
def analyser(request):
    erreur = None
    if request.method == "POST":
        try:
            fichier = request.FILES.get("fichier")
            if fichier:
                df = pd.read_csv(fichier).rename(columns={"amount": "montant"})
                nom = fichier.name
            else:
                df = pd.DataFrame([{
                    "type": request.POST["type"],
                    "montant": float(request.POST["montant"]),
                    "heure": int(request.POST["heure"]),
                }])
                nom = "Saisie manuelle"
            df = df[["type", "montant", "heure"]]
            if not df["type"].isin(["TRANSFER", "CASH_OUT"]).all():
                raise ValueError
            X = pd.DataFrame({
                "type_num": (df["type"] == "TRANSFER").astype(int),
                "amount": df["montant"],
                "heure": df["heure"],
            })
            scores = MODELE.predict_proba(X)[:, 1]
            analyse = Analyse.objects.create(utilisateur=request.user, nom_fichier=nom)
            Transaction.objects.bulk_create([
                Transaction(analyse=analyse, type=t, montant=m, heure=h,
                            score=s, decision=decision(s))
                for t, m, h, s in zip(df["type"], df["montant"], df["heure"], scores)
            ])
            return redirect("resultat", analyse.id)
        except (KeyError, ValueError):
            erreur = "Données invalides. Colonnes attendues : type (TRANSFER ou CASH_OUT), amount, heure."
    return render(request, "analyser.html", {"erreur": erreur})


@login_required
def resultat(request, id):
    analyse = get_object_or_404(Analyse, id=id, utilisateur=request.user)
    transactions = analyse.transactions.order_by("-score")
    return render(request, "resultat.html", {"analyse": analyse, "transactions": transactions})


@login_required
def historique(request):
    analyses = Analyse.objects.filter(utilisateur=request.user).order_by("-date")
    return render(request, "historique.html", {"analyses": analyses})