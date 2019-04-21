import cos_backend
import json
import re
from collections import defaultdict

#WORD COUNT

def main(args):
	config = args.get("config")
	num = args.get("num")
	rang = args.get("rang")
	file_name = args.get("file_name")
	cos = cos_backend.cos_backend(config)

	data = cos.get_object('cattydeposito', file_name, rang).decode('latin-1')
	data = data.replace('*', '')
	data = re.sub('([.,;:_¿?!"·$%&/()\{}@#¬^<>])', '', data)
	data = re.sub(r'(\n\t)', ' ', data)
	data = re.sub(r'(\r)', '', data)
	data = data.lower()

	

	data = data.split()
	

	diccionari={}
	for word in data:
		if (diccionari.get(word))==None:
			diccionari[word]=1
		else:
			diccionari[word]=diccionari[word]+1	
	
	
	cos.put_object('cattydeposito', "fileWordCount"+str(num), json.dumps(diccionari))
	
	return {}
