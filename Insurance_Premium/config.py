import pymongo
import pandas as pd
import json
import numpy as np
import os,sys
from dataclasses import dataclass

@dataclass
class EnviornmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    

env_var = EnviornmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "expenses" # y
print("env_var.mongo_db_url")