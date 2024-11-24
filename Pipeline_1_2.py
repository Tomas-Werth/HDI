# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:54:19 2024

@author: tomas
"""

import sys
import dill
import json
import pandas as pd
import numpy as np

with open("args.json", "r") as file:
    args = json.load(file)
    
ID=sys.argv[1]
#ID="561205"

data=pd.read_csv(args["dir"]+"Dataframe_1_"+ID+".csv",sep = args["sep"])


if pd.isna(data["antiguedad_vehiculo"].values):
    data["antiguedad_vehiculo"]=1
if pd.isna(data["tipo_poliza"].values):
    data["tipo_poliza"]=1
if pd.isna(data["taller"].values):
    data["taller"]=1
if pd.isna(data["partes_a_reparar"].values):
    data["partes_a_reparar"]=3
if pd.isna(data["partes_a_reemplazar"].values):
    data["partes_a_reemplazar"]=1


data=dill.load(open(args["dir"]+"pipeline_1.pkl" , 'rb'))(data)
data=dill.load(open(args["dir"]+"pipeline_2.pkl" , 'rb'))(data)
data["log_total_piezas"]=data["log_total_piezas"].fillna(1.4545)



    
    
print(ID)

data.to_csv(args["dir"]+"Dataframe_2_"+ID+".csv",sep = args["sep"], index=False)