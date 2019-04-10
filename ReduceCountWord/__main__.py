import cos_backend
import json

#REDUCE COUNT WORD

def main(args):

	config = args.get("config")
	num_chunks = args.get("num_chunks")
	num_chunks = int(num_chunks)
	cos = cos_backend.cos_backend(config)
	
	diccionari = {}
	numero_paraules = 0

	for i in range(num_chunks):
		data = cos.get_object('cattydeposito', "fileCountWord"+str(i), "")
		diccionari = json.loads(data)
		numero_paraules = numero_paraules + int(diccionari["NUMERO DE PARAULES"])
		cos.delete_object('cattydeposito', "fileCountWord"+str(i))
	
	cos.put_object('cattydeposito', "ReduceCountWord", str(numero_paraules))
	
	return diccionari


