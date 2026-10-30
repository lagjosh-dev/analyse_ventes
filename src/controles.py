def verifier_ventes(df):
    df = df.copy()

    # Calculer les ventes théoriques
    df["ventes_calculees"] = (
        df["quantite_vente"] * df["prix_unitaire"]
        - df["montant_remise"]
    )

    # Calculer et arrondir les écarts
    df["ecart_ventes"] = (
        df["montant_ventes"] - df["ventes_calculees"]
    ).round(2)

    # Identifier les écarts supérieurs à 0,01 $
    anomalies = df[df["ecart_ventes"].abs() > 0.01]

    return anomalies



def verifier_couts(df):
    df = df.copy()

    # Calcul du coût théorique
    df["cout_calcule"] = (
        df["quantite_vente"] * df["cout_unitaire"]
    )

    # Calcul des écarts
    df["ecart_cout"] = (
        df["cout_total"] - df["cout_calcule"]
    ).round(2)

    # Sélection des écarts supérieurs à 0,01 $
    anomalies = df[df["ecart_cout"].abs() > 0.01]

    return anomalies