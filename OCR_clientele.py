from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import os
from dotenv import load_dotenv
import time
from Module import Importation 
from Telechargement import liste_fichier
from ConnexionBDD import Request_SQL_ClienteleD, Request_SQL_FacturationD


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

def OCR_Clientele(numero):
    image_url=f"https://invoiceocrp3.azurewebsites.net/invoices/{numero}"
    print(image_url)
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
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.bounding_box, line.text)
                if line.bounding_box[1]>=77 and line.bounding_box[1]<=81:
                    print('CUSTUMER :', line.text[8:])
                    Custumer=line.text[8:]
                if line.bounding_box[1]>=117 and line.bounding_box[1]<=120:
                    print('Adress:', line.text[8:])
                    Adresse = line.text[8:]
                if line.bounding_box[1] >= 131 and line.bounding_box[1]<=134:
                    Etat = line.text[0:]
                    print('Etat:', line.text[0:])
                if line.bounding_box[1] >= 48 and line.bounding_box[1]<=51:
                    print('Issue date:', line.text[11:21])
                    Date = line.text[11:21]
                if line.bounding_box[1] >= 48 and line.bounding_box[1]<=51:
                    print('Heure:', line.text[21:])
                    Heure = line.text[21:]
                if line.bounding_box[0] >= 33 and line.bounding_box[0]<=42:
                    if line.bounding_box[2]>=100 and line.bounding_box[2] <=113:
                        index = text_result.lines.index(line)
                        #print(index)
                        Total = text_result.lines[index + 1].text[0:-5]
                        #print(Total)
                        print('Total:', Total)
            Request_SQL_ClienteleD(0, Custumer,Adresse, Etat)
            Request_SQL_FacturationD(numero, Date, Heure,"NumClient",Total, image_url)           
    print()
    '''
    END - Read File - remote
    '''
liste = liste_fichier()

for annee in liste:
    #print(annee) # imprime l'année
    for doc in liste[annee]:
        print(doc)
        OCR_Clientele(doc)

