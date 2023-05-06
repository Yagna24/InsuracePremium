import pymongo 
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://insurance:insurance@cluster0.abo17cz.mongodb.net/?retryWrites=true&w=majority")
DATA_FILE_PATH = r"C:\Users\HP\Desktop\yagnaa\InsuracePremium\insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ ==  "__main__" : 
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Cols:  {df.shape}")
    print('df.columns',df.columns)
    df.reset_index(drop=True, inplace = True )
    
    json_record = list(json.loads(df.T.to_json()).values())
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    