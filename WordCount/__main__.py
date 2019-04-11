import cos_backend
import json
import re

#WORD COUNT

def main(args):
	data = args.get("data")
	data = re.sub('([.,;:_¿?!"·$%&/()\{}@#¬^<>])', '', data)
	data = re.sub(r'(\n)', ' ', data)
	data = re.sub(r'(\r)', '', data)

	config = args.get("config")
	num = args.get("num")
	cos = cos_backend.cos_backend(config)

	diccionari={}
	for paraula in data.split(" "):
		if paraula in diccionari.keys():
			diccionari[paraula] = int(diccionari[paraula])+1
		else:
			diccionari.update({paraula:1})

	cos.put_object('cattydeposito', "fileWordCount"+str(num), json.dumps(diccionari))
	
	return diccionari
