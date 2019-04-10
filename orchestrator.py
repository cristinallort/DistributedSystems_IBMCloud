import ibm_cf_connector
import sys
import yaml
import cos_backend 
import re

with open("ibm_cloud_config.yaml", "r") as config_file: 
	res = yaml.safe_load(config_file)


if(len(sys.argv) == 3):

	cos = cos_backend.cos_backend(res['ibm_cos'])
	cf = ibm_cf_connector.CloudFunctions(res['ibm_cf'])

	file_name = sys.argv[1]
	num_chunks = int(sys.argv[2])
	size_file = int(cos.head_object('cattydeposito',file_name))
	
	diccionari = {}	
	diccionari["config"] = res['ibm_cos']
	diccionari["num_chunks"] = num_chunks
	diccionari["size_file"] = size_file

	chunk_size = int(size_file/num_chunks)

	#Creem les particions
	for i in range(num_chunks):
		rang = ""
		if(i == num_chunks-1):
			inici = i*chunk_size
			final = size_file
		else:
			inici = i*chunk_size
			final = ((i+1)*chunk_size)
		
		rang = "bytes="+str(inici)+"-"+str(final)
		data = str(cos.get_object('cattydeposito', file_name, rang))
		diccionari["num"]=i

		data = data.lower()
		data = re.sub('[.,;:_¿?!"·$%&/()\{}@#¬^<>]', '', data).replace('-', '').replace("\\n", " ").replace("\\r", "").replace("\\t", " ").replace("*", "").replace("'", "").replace("  "," ")
		
		diccionari["data"]=data
		
		#Invoquem mapwordcount i mapcountword
		cf.invoke("WordCount", diccionari)
		cf.invoke("CountWord", diccionari)

	#Invoquem reducewordcount i reducecountword
	cf.invoke("ReduceWordCount", diccionari)
	cf.invoke("ReduceCountWord", diccionari)
else:
	print("Nombre de parametres incorrecte.")


