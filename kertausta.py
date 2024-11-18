from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import os
from mongo_connection import connect

def connect():
    try:
        # 
        # client = MongoClient("MONGO")
        global client 
        client = MongoClient("mongodb+srv://oilikalm:mongokokeilu@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        # client = MongoClient(f"mongodb+srv://oilikalm:{('MONGOPASS')}@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print("connected")
        return client
    except:
        print("no connection")

client = connect()

db=client["taskDB"]
coll=db["task_colletion"]

document = ({
    "task": "pölyt"})


