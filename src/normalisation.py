import unicodedata
import re

def nettoyer_colonne(nom):
    nom = nom.strip().lower()
    nom = unicodedata.normalize("NFKD", nom)
    nom = "".join(c for c in nom if not unicodedata.combining(c))
    nom = re.sub(r"[^a-z0-9]+", "_", nom)
    return nom.strip("_")


def renommer_colonnes(df):
    df = df.copy()

    df.columns = [nettoyer_colonne(col) for col in df.columns]

    noms = {
        "iddate": "id_date",
        "idvente": "id_vente",
        "idboutique": "id_boutique",
        "idproduit": "id_produit",
        "idpromotion": "id_promotion",
        "montant_du_retour": "montant_retour",
        "quantite_de_retour": "quantite_retour",
        "montant_des_ventes": "montant_ventes",
        "quantite_de_vente": "quantite_vente",
        "montant_de_la_remise": "montant_remise",
        "quantite_de_remise": "quantite_remise"
    }

    return df.rename(columns=noms)