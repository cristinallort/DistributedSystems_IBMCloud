import cos_backend
import json

def main(args):
	data = args.get("data")
	config = args.get("config")
	num = args.get("num")
	cos = cos_backend.cos_backend(config)

	data = data[1:]

	diccionari={}
	for paraula in data.split(" "):
		if paraula in diccionari.keys():
			diccionari[paraula] = int(diccionari[paraula])+1
		else:
			diccionari.update({paraula:1})

	cos.put_object('cattydeposito', "fileWordCount"+str(num), json.dumps(diccionari))
	
	return diccionari
