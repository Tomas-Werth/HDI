
# Desafío HDI

A continuación, se explicará el funcionamiento de mi resolución al desafió de HDI.



## Archivos

app.py (código para ejecutar la api)

args.json (archivo json con los argumentos necesarios)

claim_dataset.csv (archivo con los datos del desafío)

codigo.py (código del funcionamiento del algoritmo sin api)

Desafio HDI.ipynb (Notebook con el proceso, explicacion de las deciciones tomadas y el desarrollo del desafio)

desafio-tecnico-MLE-HDI-Seguros.pdf (Pdf explicativo del desafio)

documentacio╠ün.md (documento complementario para el entendimiento del desafio)

linnear_regression.pkl (modelo predictivo suministrado por HDI)

Log.csv (archivo con los resultados de las request)

pipeline_1.pkl (pipeline_1 suministrado por HDI)

pipeline_2.pkl (pipeline_2 suministrado por HDI)

pipeline_3.pkl (pipeline_3 suministrado por HDI)

pipeline_4.pkl (pipeline_4 suministrado por HDI)

pipeline_5.pkl (pipeline_5 suministrado por HDI)

pipeline_1_2.py (codigo auxiliar para el funcionamiento de codigo.py y app.py)

pipeline_4.py (codigo auxiliar para el funcionamiento de codigo.py y app.py)

requirements.tex (archivo txt con los requerimientos para la ejecucion del codigo)

## Recomendaciones

Para el funcionamiento de la api, primero hay que generar un ambiente con las librerias del archivo requirements.txt. Antes de poder ejecutar el codigo hay que asegurarse que todos los documentos necesarios se encuentren en la misma direccion y asignar dicha direccion en el archivo args.json. Los archivos minimos y necesarios son (app.py o codigo.py, claims_dataset.csv, pipeline_1_2.py, pipeline_4.py, args.json, linnear_regression.pkl, pipeline_1.pkl, pipeline_2.pkl, pipeline_3.pkl, pipeline_4.pkl, pipeline_5.pkl). Luego se puede ejecutar el archivo app.py en cualquier visualizador de codigo y esperar a que la api este abierta. A continuacion puede utilizarse postman, insomnia o cualquier programa a eleccion para ejecutar las requests. Las requests tienen que realizarce con un archivo de tipo json, simulando la interacion de un usuario con una interfas de la api. Al momento de realizar una request se generarán archivos auxiliares del tipo csv, no se debe interactuar con estos archivos mientras se ejecute el request y dichos archivos se eliminarán automaticamente al terminar la request. En caso de querer comenzar un proceso desde 0 asegurece de eliminar o mover el achivo log.csv, en caso de existir este archivo cualquier request se asignará al final del documento, en caso de no existir, se generará automaticamente y se inicializará con los resultados del primer request. 

La dirección de la api es "http://127.0.0.1:5000/"

Los resultados se mostrarán con el siguiente formato json:

{
	"0": {
		"claim_id": value,
		"marca_vehiculo": "value",
		"antiguedad_vehiculo": value,
		"tipo_poliza": value,
		"taller": value,
		"partes_a_reparar": value,
		"partes_a_reemplazar": value,
		"marca_vehiculo_encoded": value,
		"reclamos_por_marca": value,
		"reclamos_por_taller": value,
		"total_piezas": value,
		"log_total_piezas": value,
		"valor_vehiculo": value,
		"valor_por_pieza": value,
		"Semanas_en_el_taller": value
	}
}

Donde "semanas_en_el_taller" representa el resultado de la predicioin del modelo o -1 en caso de que el "tipo_poliza" sea 4.

A continuacion se muestra un ejemplo del formato del archivo json que se necesita para la request:

{
	"claim_id": 561205,
	"marca_vehiculo": "ferd",
	"antiguedad_vehiculo": 1,
	"tipo_poliza": 1,
	"taller": 4,
	"partes_a_reparar": 3,
	"partes_a_reemplazar": 2
}