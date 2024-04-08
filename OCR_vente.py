from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import os
from dotenv import load_dotenv
import time
from Module import Importation 
from Telechargement import liste_fichier
from ConnexionBDD import  Request_SQL_ProduitD,Request_SQL_VenteD

load_dotenv()  # Assurez-vous d'avoir appelÃ© cette fonction pour charger les variables d'environnement
'''
FONCTIONNE !
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")

def OCR_Vente(numero):
    image_url=f"https://invoiceocrp3.azurewebsites.net/invoices/{numero}"
    #print(image_url)

    # Call API with URL and raw response (allows you to get the operation location)
    read_response = computervision_client.read(image_url, raw=True)
    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]
    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)
    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        nom = None 
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                prix=0
                nombre=0
                print(line.bounding_box, line.text)
                if line.bounding_box[1] >= 195 and line.bounding_box[1]<=205:
                    if line.bounding_box[0] >= 30 and line.bounding_box[0]<=47: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix:',line.text[-11:-5])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        if nom is None:
                            if line.bounding_box[1] >= 195 and line.bounding_box[1]<=205:
                                if line.bounding_box[0] >= 30 and line.bounding_box[0]<=47: # pour differencier la ligne des produits
                                    if line.bounding_box[2] >=110: # pour differencier la ligne total
                                        print('Nom:',line.text[0:])
                                        nom=line.text[0:-1]
                        Request_SQL_VenteD(nombre,numero, nom) 
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 218 and line.bounding_box[1]<=222: 
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[-11:-5])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 238 and line.bounding_box[1]<=242:
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[-11:-5])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 258 and line.bounding_box[1]<=262:
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[-11:-5])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 278 and line.bounding_box[1]<=282:  
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[0:])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 298 and line.bounding_box[1]<=302:
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[0:])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 318 and line.bounding_box[1]<=322:
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom)
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[0:])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)      
                if line.bounding_box[1] >= 338 and line.bounding_box[1]<=342:
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[0:])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 358 and line.bounding_box[1]<=362:    
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[0:])
                        prix=line.text[-11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                if line.bounding_box[1] >= 378 and line.bounding_box[1]<=382:     
                    if line.bounding_box[0] >= 35 and line.bounding_box[0]<=45: # pour differencier la ligne des produits
                        if line.bounding_box[2] >=110: # pour differencier la ligne total
                            print('Nom:',line.text[0:])
                            nom=line.text[0:-1]
                    if line.bounding_box[0]>=505 and line.bounding_box[0]<=515:
                        print('Quantite',line.text[0:])
                        nombre=line.text[0:1]
                        Request_SQL_VenteD(nombre, numero,nom) 
                    if line.bounding_box[4]>=683 and line.bounding_box[4]<=698: # pour les lignes prix
                        print('Prix',line.text[0:])
                        prix=line.text[11:-5] # en partant de la gauche, enlever euros
                        Request_SQL_ProduitD(nom,prix)
                        
    print()
    '''
    END - Read File - remote
    '''
liste = liste_fichier()
for annee in liste:
    print(annee) # imprime l'année
    for doc in liste[annee]:
        print(doc)
        OCR_Vente(doc)
