rm countWord.zip
rm reduceCountWord.zip
rm wordCount.zip
rm reduceWordCount.zip
ibmcloud fn action delete CountWord
ibmcloud fn action delete ReduceCountWord
ibmcloud fn action delete WordCount
ibmcloud fn action delete ReduceWordCount


cd CountWord
rm countWord.zip
zip -r countWord.zip __main__.py cos_backend.py 
cp countWord.zip ../
ibmcloud fn action create CountWord -t 180000 -m 2048 --kind python:3.6 countWord.zip



cd ..

cd ReduceCountWord
rm reduceCountWord.zip
zip -r reduceCountWord.zip __main__.py cos_backend.py
cp reduceCountWord.zip ../
ibmcloud fn action create ReduceCountWord -t 180000 -m 2048 --kind python:3.6 reduceCountWord.zip


cd ..

cd WordCount
rm wordCount.zip
zip -r wordCount.zip __main__.py cos_backend.py
cp wordCount.zip ../
ibmcloud fn action create WordCount -t 180000 -m 2048 --kind python:3.6 wordCount.zip

cd ..

cd ReduceWordCount
rm reduceWordCount.zip
zip -r reduceWordCount.zip __main__.py cos_backend.py
cp reduceWordCount.zip ../
ibmcloud fn action create ReduceWordCount -t 180000 -m 2048 --kind python:3.6 reduceWordCount.zip
