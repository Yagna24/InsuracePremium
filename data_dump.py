import pymongo 
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://yagna:wow@cluster0.abo17cz.mongodb.net/?retryWrites=true&w=majority")
db = client.InsurancePremium


