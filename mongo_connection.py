# python -m pip install "pymongo[srv]"==3.11
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv(override=True) # haetaan ensisijaisesti .env -tiedostosta, sitten vasta ympäristömuuttujista

def connect():
    try:                        
        client = MongoClient("mongodb+srv://oilikalm:mongokokeilu@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") ### LISÄÄ CONNECTION STRINGISI,
                                                         ### HAE SALASANASI .env -TIEDOSTOSTA)
        print("connected to mongo")
        return client
    except:
        print("connection error")
# connect()

def fetch_new_id(coll):
    ### FUNKTION TULEE PALAUTTAA UUSI id, JOTA KANNASSA EI VIELÄ OLE.
    ### MIKÄLI KANNASSA EI OLE YHTÄÄN DOKUMENTTIA, PALAUTETAAN 0.
    max_id_doc = coll.find_one(sort=[("id", -1)]) # descending, oletus ascending
    max_id = max_id_doc["id"]
    if max_id is not None:
        new_id = int(max_id) +1
        return new_id
    else:
        return 0
    
def fetch_task_by_id(coll,task_id):
    ### FUNKTION TULEE HAKEA task_id -MUUTTUJAN PERUSTEELLA TIETOKANNASTA TASK, JONKA id ON task_id
    ### JA PALAUTTAA LÖYTYNYT TASK
    # coll.insert_one({"id": new_id}, {"task": task})
    pass #placeholder, (poista)