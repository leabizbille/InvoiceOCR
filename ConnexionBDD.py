
"""
Connects to a SQL database using pyodbc
"""
#Environnement
import dotenv
import os
import pyodbc #Requetes SQL
from unidecode import unidecode  # Importez la fonction unidecode depuis la bibliothèque unidecode

load_dotenv()
server = os.getenv("server")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("password")
driver= '{ODBC Driver 18 for SQL Server}'  # Assurez-vous d'avoir installé ce pilote

# Chaîne de connexion
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
#conn = pyodbc.connect(connection_string) a tester
conn = pyodbc.connect(connection_string, driver=driver)# Connexion à la base de données

# #-----------------Vente----------------------------------------------------------------------------------------

def Request_SQL_VenteD( nombre, NumFacture,nom):
    try:
        cursor = conn.cursor() # Création d'un curseur
        # Exécution d'une requête SQL
        SQL_STATEMENT = """
        MERGE INTO BDDLaurence.dbo.Vente AS target
        USING (VALUES (?, ?,?)) AS source ( nombre, NumFacture ,nom)
        ON target.NumFacture = source.NumFacture AND target.nom = source.nom
        WHEN NOT MATCHED BY TARGET THEN
            INSERT ( nombre, NumFacture ,nom)
            VALUES (source.nombre, source.NumFacture,source.nom);
        """
        cursor.execute(
            SQL_STATEMENT, (nombre, NumFacture ,nom))
        conn.commit()
        print("La requête a été exécutée avec succès.")
        # Fermeture du curseur et de la connexion
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
    finally:
        cursor.close()
    return    

#-------------------------------------------------------------------------------------------

def Request_SQL_ProduitD(nom, prix):
    try:
        cursor = conn.cursor()  # Création d'un curseur
        # Exécution d'une requête SQL
        SQL_STATEMENT = """
        MERGE INTO BDDLaurence.dbo.Produit AS target
        USING (VALUES (?, ?)) AS source (nom, prix)
        ON target.nom = source.nom AND REPLACE(REPLACE(target.nom, 'x', ''), ' ', '') = REPLACE(REPLACE(source.nom, 'x', ''), ' ', '')
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (nom, prix)
            VALUES (source.nom, source.prix);
        """
        cursor.execute(SQL_STATEMENT, (nom, prix))
        conn.commit()
        print("La requête a été exécutée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
    finally:
        cursor.close()  # Fermeture du curseur
    return
#-----------------------------------Facturation sans doublons------------------------------------------------------
def Request_SQL_FacturationD(NumFacture, Date, Heure, NumClient,Total,image_url):
    try:
        cursor = conn.cursor()  # Création d'un curseur
        # Exécution d'une requête SQL
        SQL_STATEMENT = """
        MERGE INTO BDDLaurence.dbo.Facturation AS target
        USING (VALUES (?, ?, ?, ?,?,?)) AS source (NumFacture, Date, Heure, NumClient,Total,Image_url)
        ON target.NumFacture = source.NumFacture
        WHEN MATCHED THEN
            UPDATE SET 
                Date = source.Date,
                Heure = source.Heure,
                NumClient = source.NumClient,
                Total = source.Total,
                Image_url = source.Image_url
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (NumFacture, Date, Heure, NumClient,Total,image_url)
            VALUES (source.NumFacture, source.Date, source.Heure, source.NumClient,source.Total, source.Image_url);
        """
        cursor.execute(SQL_STATEMENT, (NumFacture, Date, Heure, NumClient, Total, image_url))
        conn.commit()
        print("La requête a été exécutée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
    finally:
        cursor.close()  # Fermeture du curseur
    return
#----------------------------------Clientèle sans doublons-------------------------
def Request_SQL_ClienteleD(NumClient, Nom,Adresse, Etat): 
    try:
        cursor = conn.cursor() # Création d'un curseur
        SQL_STATEMENT = """
        MERGE INTO BDDLaurence.dbo.Clientele AS target
        USING (VALUES (?, ?, ?, ?)) AS source  (NumClient, Nom,  Adresse, Etat)
        ON target.Nom = source.Nom
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (NumClient, Nom,  Adresse, timestamp, Etat)
            VALUES (source.NumClient, source.Nom, source.Adresse,CURRENT_TIMESTAMP, source.Etat);
        """
        nom_sans_accents = unidecode(Nom)  # Translittérer le nom pour enlever les accents
        cursor.execute(SQL_STATEMENT, NumClient, nom_sans_accents,Adresse, Etat)
        conn.commit()
        print("La requête a été exécutée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
    finally:
        cursor.close()
    return







# def Request_SQL_Clientele(NumClient, Nom,Adresse, Etat): 
#     try:
#         cursor = conn.cursor() # Création d'un curseur
#         # Exécution d'une requête SQL
#         SQL_STATEMENT = """
#         INSERT into BDDLaurence.dbo.Clientele (NumClient, Nom,  Adresse, timestamp, Etat)
#         VALUES (?, ?,?, CURRENT_TIMESTAMP,?)
#         """
#         cursor.execute(SQL_STATEMENT, NumClient, Nom,Adresse, Etat)
#         conn.commit()
#         print("La requête a été exécutée avec succès.")
#     except Exception as e:
#         print(f"Erreur lors de la connexion à la base de données : {e}")
#         cursor.close()
#     return
# #Request_SQL_Clientele(1,"Laurence","11 bld")
# #-----------------Facturation ----------------------------------------------------------------------------------------

# def Request_SQL_Facturation(NumFacture, Date, Heure,NumClient):
#     try:
#         cursor = conn.cursor() # Création d'un curseur
#         SQL_STATEMENT = """
#         INSERT into BDDLaurence.dbo.Facturation(NumFacture, Date, Heure,NumClient )
#         VALUES (?, ?,?, ?)
#         """
#         cursor.execute(SQL_STATEMENT, NumFacture, Date, Heure,NumClient)     
#         conn.commit()
#         print("La requête a été exécutée avec succès.")
#         # Fermeture du curseur et de la connexion
#     except Exception as e:
#         print(f"Erreur lors de la connexion à la base de données : {e}")
#         cursor.close()
#     return
# # #-----------------Produit----------------------------------------------------------------------------------------

# def Request_SQL_Produit(nom, prix,NumFacture):
#     try:
#         cursor = conn.cursor() # Création d'un curseur
#         # Exécution d'une requête SQL
#         SQL_STATEMENT = """
#         INSERT into BDDLaurence.dbo.Produit(nom, prix ,NumFacture )
#         VALUES ( ?,?, ?)
#         """
#         cursor.execute(
#             SQL_STATEMENT, nom, prix ,NumFacture )
#         conn.commit()
#         print("La requête a été exécutée avec succès.")
#         # Fermeture du curseur et de la connexion
#     except Exception as e:
#         print(f"Erreur lors de la connexion à la base de données : {e}")
#         cursor.close()
#     return