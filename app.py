# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:47:51 2024

@author: tomas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:28:01 2024

@author: tomas
"""

import os
import json
import dill
import subprocess
import pandas as pd
from flask import Flask, request

with open("args.json", "r") as file:
    args = json.load(file)
df=pd.read_csv(args["dir"]+args["data"],sep = args["sep"])

app=Flask(__name__)


@app.route("/",  methods=['GET', 'POST'])
def create():
    data={
          "claim_id":request.json["claim_id"],
          "marca_vehiculo":request.json["marca_vehiculo"],
          "antiguedad_vehiculo":request.json["antiguedad_vehiculo"],
          "tipo_poliza":request.json["tipo_poliza"],
          "taller":request.json["taller"],
          "partes_a_reparar":request.json["partes_a_reparar"],
          "partes_a_reemplazar":request.json["partes_a_reemplazar"]
          }
    data=pd.DataFrame.from_dict(data, orient='index').transpose()
    ID=str(data["claim_id"].values[0])
    data = data.astype(dtype= {"claim_id":"int64","marca_vehiculo":"object","antiguedad_vehiculo":"int64", "tipo_poliza":"int64", "taller":"int64", "partes_a_reparar":"int64", "partes_a_reemplazar":"int64"})  
    data.to_csv(args["dir"]+"Dataframe_1_"+ID+".csv", index=False, sep = args["sep"])
    subprocess.Popen(['python', args["dir"]+'Pipeline_1_2.py', ID])
    data=dill.load(open(args["dir"]+"pipeline_3.pkl" , 'rb'))(data)
    data["marca_vehiculo_encoded"]=data["marca_vehiculo_encoded"].fillna(0).astype("int64")
    data.to_csv(args["dir"]+"Dataframe_3_"+ID+".csv", index=False, sep = args["sep"])
    subprocess.Popen(['python', args["dir"]+'Pipeline_4.py', ID])
    data=dill.load(open(args["dir"]+"pipeline_5.pkl" , 'rb'))(data)
    flag=True  
    while flag==True:
        if (os.path.exists(args["dir"]+"Dataframe_2_"+ID+".csv") and os.path.exists(args["dir"]+"Dataframe_3_"+ID+".csv") and os.path.exists(args["dir"]+"Dataframe_4_"+ID+".csv")):
            flag=False


    Dataframe_4=pd.read_csv(args["dir"]+"Dataframe_4_"+ID+".csv",sep = args["sep"])
    data=data.merge(Dataframe_4, how='outer')


    if data["tipo_poliza"].values[0]!=4:
        data_modelo=data[["log_total_piezas","marca_vehiculo_encoded","valor_vehiculo", "valor_por_pieza", "antiguedad_vehiculo"]]
        model=dill.load(open(args["dir"]+"linnear_regression.pkl" , 'rb'))
        results=model.predict(data_modelo)[0]
    else:
        results=-1
    data["Semanas_en_el_taller"]=results
    if os.path.exists(args["dir"]+"Log.csv"):
        data.to_csv(args["dir"]+"Log.csv", mode="a", index=False, header=False, sep="|")
    else:
        data.to_csv(args["dir"]+"Log.csv", index=False, sep = args["sep"])
    os.remove(args["dir"]+"Dataframe_1_"+ID+".csv")
    os.remove(args["dir"]+"Dataframe_2_"+ID+".csv")
    os.remove(args["dir"]+"Dataframe_3_"+ID+".csv")
    os.remove(args["dir"]+"Dataframe_4_"+ID+".csv")
    
    
    return data.to_json(orient="index")


if __name__=="__main__":
    app.run(debug=False)
    
