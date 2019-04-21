import ibm_cf_connector
import sys
import yaml
import cos_backend 
import re
import os
from time import time

inici = time()

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
	diccionari["file_name"] = file_name

	chunk_size = int(size_file/num_chunks)
	llistaRang = []
	
	tempsWordCount=0
	tempsCountWord=0
	
	#Creem les particions
	for i in range(num_chunks):
		rang = ""
		if(i == num_chunks-1):
			inici = i*chunk_size
			final = size_file
		else:
			inici = i*chunk_size
			final = ((i+1)*chunk_size)-1
		
		rang = "bytes="+str(inici)+"-"+str(final)
		llistaRang.append(rang)

		diccionari["rang"]=rang
		diccionari["num"]=i

		
		cf.invoke("WordCount", diccionari)
		fiWordCount = time()
		cf.invoke("CountWord", diccionari)
		fiCountWord = time()

		tempsWordCount = tempsWordCount+fiWordCount-inici
		tempsCountWord = tempsCountWord+fiCountWord-fiWordCount

	inici = time()
	#cf.invoke("ReduceWordCount", diccionari)
	fiWordCount = time()
	cf.invoke("ReduceCountWord", diccionari)
	fiCountWord = time()

	tempsWordCount = tempsWordCount+fiWordCount-inici
	tempsCountWord = tempsCountWord+fiCountWord-fiWordCount

	print ("Temps Count Word: "+str(tempsCountWord)+"s\nTemps Word Count: "+str(tempsWordCount)+"s\n")

else:
	print("Nombre de parametres incorrecte.")


