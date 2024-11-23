# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:06:47 2024

@author: tomas
"""

import sys
import dill
import json
import pandas as pd

with open("args.json", "r") as file:
    args = json.load(file)
    
ID=sys.argv[1]

data=pd.read_csv(args["dir"]+"Dataframe_1_"+ID+".csv",sep = args["sep"])


data=dill.load(open(args["dir"]+"pipeline_3.pkl" , 'rb'))(data)
data["marca_vehiculo_encoded"]=data["marca_vehiculo_encoded"].fillna(0).astype("int64")
data=dill.load(open(args["dir"]+"pipeline_5.pkl" , 'rb'))(data)

data.to_csv(args["dir"]+"Dataframe_3_"+ID+".csv",sep = args["sep"], index=False)