import cos_backend
import json
from collections import Counter

#REDUCER WORD COUNT

def main(args):

	config = args.get("config")
	num_chunks = args.get("num_chunks")
	num_chunks = int(num_chunks)
	bucket_name = args.get("bucket_name")
	cos = cos_backend.cos_backend(config)

	diccionari = {}

	numero_fitxers = 0
	while(numero_fitxers!=(num_chunks)):
		diccionari_bucket=cos.list_object(bucket_name, 'fileWordCount')
		numero_fitxers=diccionari_bucket['KeyCount']


	for i in range(num_chunks):
		data = cos.get_object(bucket_name, "fileWordCount"+str(i), "")
		diccionariWorker = json.loads(data)
		diccionari = Counter(diccionari)+Counter(diccionariWorker)
		cos.delete_object(bucket_name, "fileWordCount"+str(i))
	
	cos.put_object(bucket_name, "ReduceWordCount", json.dumps(diccionari))

	return {}
