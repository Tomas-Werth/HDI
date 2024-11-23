# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:16:13 2024

@author: tomas
"""

import os
import sys
import dill
import json
import pandas as pd

with open("args.json", "r") as file:
    args = json.load(file)
    
ID=sys.argv[1]

flag=True  
while flag==True:
    if os.path.exists(args["dir"]+"Dataframe_2_"+ID+".csv") and os.path.exists(args["dir"]+"Dataframe_3_"+ID+".csv"):
        flag=False

Dataframe_2=pd.read_csv(args["dir"]+"Dataframe_2_"+ID+".csv",sep = args["sep"])
Dataframe_3=pd.read_csv(args["dir"]+"Dataframe_3_"+ID+".csv",sep = args["sep"])
data=Dataframe_2.merge(Dataframe_3, how='outer')
data=dill.load(open(args["dir"]+"pipeline_4.pkl" , 'rb'))(data)
data["valor_vehiculo"]=data["valor_vehiculo"].fillna(3560).astype("int64")
data["valor_por_pieza"]=data["valor_por_pieza"].fillna(150)


data.to_csv(args["dir"]+"Dataframe_4_"+ID+".csv",sep = args["sep"], index=False)