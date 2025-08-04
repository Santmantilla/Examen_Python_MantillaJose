import json
import os
from typing import List,Dict

def readJson(filename:str)->List[Dict]:
    try:
        with open(filename,"r",encoding="utf-8") as file:
            datos = json.load(file)
            return datos
    except Exception as e:
        return []
    
def writeJson(filename:str, datos:List[Dict]):
    with open(filename,"w",encoding="utf-8") as file:
        json.dump(datos,file,indent=4)