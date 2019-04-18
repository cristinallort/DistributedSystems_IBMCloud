import cos_backend
import json
from collections import Counter

#REDUCER WORD COUNT

def main(args):

	config = args.get("config")
	num_chunks = args.get("num_chunks")
	num_chunks = int(num_chunks)
	cos = cos_backend.cos_backend(config)

	diccionari = {}

	for i in range(num_chunks):
		data = cos.get_object('cattydeposito', "fileWordCount"+str(i), "")
		diccionariWorker = json.loads(data)
		diccionari = Counter(diccionari)+Counter(diccionariWorker)
		cos.delete_object('cattydeposito', "fileWordCount"+str(i))
	
	cos.put_object('cattydeposito', "ReduceWordCount", json.dumps(diccionari))

	return {}
