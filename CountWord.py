import cos_backend
import json


def main(args):
	data = args.get("data")
	config = args.get("config")
	num = args.get("num")
	cos = cos_backend.cos_backend(config)

	#num_paraules = len(data.split())
	num_paraules = 23
	diccionariCountWord = {"Numero_paraules":num_paraules}

	#cos.put_object('cattydeposito', "fileCountWord"+str(num), json.dumps(diccionariCountWord))
	cos.put_object('cattydeposito', "fileCountWord"+str(num)+".txt", "sdfdffs")
	return diccionariCountWord
       
