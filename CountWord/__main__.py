import cos_backend
import json

#COUNT WORD

def main(args):
	config = args.get("config")
	num = args.get("num")
	rang = args.get("rang")
	file_name = args.get("file_name")
	cos = cos_backend.cos_backend(config)

	data = cos.get_object('cattydeposito', file_name, rang).decode('latin-1')
	
	num_paraules = len(data.split())	
	diccionari = {"NUMERO DE PARAULES":num_paraules}

	cos.put_object('cattydeposito', "fileCountWord"+str(num), json.dumps(diccionari))
	

	return {}

