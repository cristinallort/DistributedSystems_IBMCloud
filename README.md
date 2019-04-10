# Distributed Systems: MapReduce 
Communication models and Middleware: Playing out with MapReduce in IBM Cloud.

## Authors
Catalina Vilsan and Cristina Llort.

## How it works?
MapReduce is a programming model and implementation to enable the parallel processing of huge amounts of data. In a nutshell, it breaks a large dataset into smaller chunks to be processed separately on different worker nodes and automatically gathers the results across the multiple nodes to return a single result. 
As it name suggests, it allows for distributed processing of the map() and reduce() functional operations, which carry out most of the programming logic. Indeed, it consists of three majors steps, which are the following ones: 
1. "Map" step: Each worker node applies the "map()" function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of redundant input data is processed.
2. "Shuffle" step: Worker nodes redistribute data based on the output keys (produced by the "map()" function), such that all data belonging to one key is located on the same worker node.
3. "Reduce" step: Worker nodes now process each group of output data, per key, in parallel.
Because each mapping operation is independent of the others, all maps can be performed in parallel. The same occurs to the reducers, given that all outputs of the map operation with the same key are handed to the same reducer. 

## How to execute it?
1. Create an IBM Cloud account -> then create a bucket and upload a text file.
2. Modify ibm_cloud_config.txt -> include your credentials and change the format to yaml format.
3. Change "cattydeposito" to your bucket name in all the files.
4. Login to IBM Cloud in your console (Linux): ibmcloud login -a cloud.ibm.com
5. Execute the makefile (Linux).
6. Execute orchestrator.py:
python3 orchestrator.py "file_name" "number_of_partitions"


## Architecture and implementation
We need to have our IBM Cloud Credentials in ibm_cloud_config.yaml and have ibm_cf_connector.py to enable the connection to the cloud.
We need to implement the following python files and zips:
1. orchestrator.py -> it contains the structure of the program and does the partitionings and the invokes
2. WordCount.zip -> it contains the code that implements the mapping of the word count function
3. CountWord.zip -> it contains the code that implements the mapping of the count word function
4. ReduceWordCount.zip -> it contains the code that implements the reducing of the count word function
5. ReduceCountword.zip -> it contains the code that implements the reducing of the count word function
6. cos_backend.py -> it contains all the functions that enable working with IBM Cloud (get, pull or delete files, for example)

All the zips contain the cos_backend.py.

## Validation
To test our code we use the following texts:
1. Sherlock Holmes  (6.5M) (English): https://norvig.com/big.txt
2. El Quijote (2.2M) (Spanish): http://www.gutenberg.org/cache/epub/2000/pg2000.txt
3. The Bible (4.5M) (English): http://www.gutenberg.org/cache/epub/10/pg10.txt

We also use larger text files that were created by concatenating books from Project Gutenberg:
http://cloudlab.urv.cat/josep/distributed_systems/

## Analysis using the speed-up
We are going to analyze the improvements that we get partitionating the text in more chunks to do the mapreduce using the speed-up methods.


