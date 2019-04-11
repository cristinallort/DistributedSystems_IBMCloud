import cos_backend
import json

#COUNT WORD

def main(args):
	data = args.get("data")
	config = args.get("config")
	num = args.get("num")
	cos = cos_backend.cos_backend(config)
	
	num_paraules = len(data.split())	
	diccionari = {"NUMERO DE PARAULES":num_paraules}

	cos.put_object('cattydeposito', "fileCountWord"+str(num), json.dumps(diccionari))
	
	return diccionari

