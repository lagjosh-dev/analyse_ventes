import pandas as pd

colonnes_monetaires = [
    "montant_retour",
    "montant_ventes",
    "cout_total",
    "cout_unitaire",
    "prix_unitaire",
    "montant_remise"
]

def convertir_montants(df):
    df = df.copy()

    for col in colonnes_monetaires:
        df[col] = (
            df[col]
            .astype("string")
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )

        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df