import cos_backend
import json

#REDUCE COUNT WORD

def main(args):

	config = args.get("config")
	num_chunks = args.get("num_chunks")
	num_chunk = int(num_chunks)
	bucket_name = args.get("bucket_name")
	cos = cos_backend.cos_backend(config)
	
	diccionari = {}
	numero_paraules = 0

	numero_fitxers = 0
	while(numero_fitxers!=(num_chunks)):
		diccionari_bucket=cos.list_object(bucket_name, 'fileCountWord')
		numero_fitxers=diccionari_bucket['KeyCount']

	for i in range(num_chunk):
		data = cos.get_object(bucket_name , "fileCountWord"+str(i), "")
		diccionari = json.loads(data)
		numero_paraules = numero_paraules + int(diccionari["NUMERO DE PARAULES"])			
		cos.delete_object(bucket_name, "fileCountWord"+str(i))
		
	cos.put_object(bucket_name, "ReduceCountWord", str(numero_paraules))
	
	return {}

