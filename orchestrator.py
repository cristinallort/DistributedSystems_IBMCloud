import ibm_cf_connector
import sys
import yaml
import cos_backend 
import re
import os
from time import time

with open("ibm_cloud_config.yaml", "r") as config_file: 
	res = yaml.safe_load(config_file)


if(len(sys.argv) == 3):

	cos = cos_backend.cos_backend(res['ibm_cos'])
	cf = ibm_cf_connector.CloudFunctions(res['ibm_cf'])
	print("Nombre del bucket: ")
	bucket_name = input()

	file_name = sys.argv[1]
	num_chunks = int(sys.argv[2])
	size_file = int(cos.head_object(bucket_name,file_name))
	
	diccionari = {}	
	diccionari["config"] = res['ibm_cos']
	diccionari["num_chunks"] = num_chunks
	diccionari["file_name"] = file_name
	diccionari["bucket_name"] = bucket_name


	chunk_size = int(size_file/num_chunks)
	llistaRang = []
	
	inicitemps = time()
	
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

		
		#MAP WORD COUNT
		cf.invoke("WordCount", diccionari)
	
		#MAP COUNT WORD
		cf.invoke("CountWord", diccionari)

	

	#REDUCE WORD COUNT
	iniciWordCount = time()
	cf.invoke("ReduceWordCount", diccionari)
	i = 0
	while(i == 0):
		d = cos.list_object(bucket_name, 'ReduceWordCount')
		i = d['KeyCount']
		timeOut = time()
		if((timeOut-iniciWordCount)>180): i=2
	fiWordCount = time()
	
	
	#REDUCE COUNT WORD
	cf.invoke("ReduceCountWord", diccionari)
	i = 0
	while(i == 0):
		d = cos.list_object(bucket_name, 'ReduceCountWord')
		i = d['KeyCount']
		timeOut = time()
		if((timeOut-fiWordCount)>180): i=2
	fiCountWord = time()


	
	#TEMPS
	if(i==1):
		tempsWordCount = fiWordCount-inicitemps
		tempsCountWord = fiCountWord-inicitemps-(fiWordCount-iniciWordCount)
		print ("Temps Count Word: "+str(tempsCountWord)+"s\nTemps Word Count: "+str(tempsWordCount)+"s\n")
	else:
		print("Time out!")

else:
	print("Nombre de parametres incorrecte.")


