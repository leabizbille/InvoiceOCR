
"""
Connects to a SQL database using pyodbc
"""

import os  # Importation du module os pour accéder aux variables d'environnement
import pyodbc

# Paramètres de connexion Azure SQL
server = os.getenv("server")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("password")
driver = '{ODBC Driver 18 for SQL Server}'  # Assurez-vous d'avoir installé ce pilote

# Chaîne de connexion
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connexion à la base de données
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Script SQL pour créer la table Ventes -------------------------
script_sql = """
CREATE TABLE Ventes (
    nombre NUMERIC(38,0) NULL,
    NumFacture NUMERIC(38,0) NULL,
    IdProduit NUMERIC(38,0) NULL,
    IdVente NUMERIC(38,0) NOT NULL,
    CONSTRAINT Vente_PK PRIMARY KEY (IdVente),
    CONSTRAINT Vente_Facturation_FK FOREIGN KEY (NumFacture) REFERENCES Facturations(NumFacture) ON DELETE CASCADE ON UPDATE CASCADE
);
"""
# Exécution du script SQL
cursor.execute(script_sql)
conn.commit()

# Script SQL pour créer la table Produits ----------------------------
script_sql = """
CREATE TABLE Produits (
	IdProduit numeric(38,0) NOT NULL,
	nom varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	prix numeric(38,0) NULL,
	NumFacture numeric(38,0) NULL,
	CONSTRAINT Produit_Facturation_FK FOREIGN KEY (NumFacture) REFERENCES BDDLaurence.dbo.Facturations(NumFacture) ON DELETE CASCADE ON UPDATE CASCADE
);
"""
# Exécution du script SQL
cursor.execute(script_sql)
conn.commit()

# Script SQL pour créer la table Facturations ----------------------------
script_sql = """
CREATE TABLE Facturations (
	NumFacture numeric(38,0) NOT NULL,
	[Date] date NULL,
	Heure varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	NumClient numeric(38,0) NULL,
	CONSTRAINT Facturation_Clientele_FK FOREIGN KEY (NumClient) REFERENCES BDDLaurence.dbo.Clienteles(NumClient) ON DELETE CASCADE ON UPDATE CASCADE
);
"""
# Exécution du script SQL
cursor.execute(script_sql)
conn.commit()

# Script SQL pour créer la table Clientèles ----------------------------
script_sql = """
CREATE TABLE Clienteles (
	NumClient numeric(38,0) NOT NULL,
	Nom varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Prenom varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Adresse varchar(200) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	[timestamp] varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	CONSTRAINT Clientele_PK PRIMARY KEY (NumClient)
);

"""
# Exécution du script SQL
cursor.execute(script_sql)
conn.commit()

# Fermeture de la connexion
cursor.close()
conn.close()
#-------------------------------------------------------------------------------------
