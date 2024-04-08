from dotenv import load_dotenv  # Import de la fonction pour charger les variables d'environnement
import requests  # Import du module requests pour effectuer des requêtes HTTP
import os  # Import du module os pour interagir avec le système d'exploitation

load_dotenv()  # Chargement des variables d'environnement à partir du fichier .env

# Définition de la fonction pour remplacer le nom si vide


def liste_fichier():
    """Fonction pour récupérer une liste de fichiers à partir d'une API pour plusieurs années"""
    annee = 2024  # Année initiale
    liste_dico_fichier = {}  # Dictionnaire pour stocker les listes de fichiers par année
    while True:
        liste = []  # Liste temporaire pour stocker les fichiers d'une année
        header = {'Accept': 'application/json'}
        url = os.getenv('URL')  # Récupération de l'URL de l'API à partir des variables d'environnement
        #print(url)
        response = requests.get(url+f"?start_date={annee}-04-01", headers=header) #
        status = response.status_code  # Statut de la réponse de la requête
        if status == 200:
            documents = response.json()
            for doc in documents["invoices"]:
                liste.append(doc["no"])
            if not liste:  # Si la liste est vide, arrête la boucle
                break
            else:
                liste_dico_fichier[annee] = liste
                annee += 1  # Passage à l'année suivante
            #print(documents)
    return liste_dico_fichier
#liste_fichier()
