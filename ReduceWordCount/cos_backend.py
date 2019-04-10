import ibm_botocore
import ibm_boto3
#import yaml

class cos_backend:
	def __init__(self, config):
		service_endpoint = config["endpoint"]
		secret_key = config["secret_key"] 
		acces_key = config["access_key"]
		client_config = ibm_botocore.client.Config(max_pool_connections=200)
		self.cos_client= ibm_boto3.client('s3',
											aws_access_key_id=acces_key,
											aws_secret_access_key=secret_key,
											config=client_config, 
											endpoint_url=service_endpoint)


	def put_object(self, bucket_name,key,data):
		try:
			res = self.cos_client.put_object(Bucket=bucket_name,Key=key,Body=data)
			status = 'OK' if res['ResponseMetadata']['HTTPStatusCode']==200 else 'Error'
		except ibm_botocore.exceptions.ClientError as e:
			raise e
				
	def get_object(self, bucket_name, key, rango, stream=False, extra_get_args={}):
		try:
			res = self.cos_client.get_object(Bucket=bucket_name,Key=key,Range=rango,**extra_get_args)
			if stream:
				data=res['Body']
			else:
				data=res['Body'].read()
			return data
		except ibm_botocore.exceptions.ClientError as e:
			raise e			


	def head_object(self, bucket_name, key):
		metadata = self.cos_client.head_object(Bucket=bucket_name, Key=key)
		return metadata['ResponseMetadata']['HTTPHeaders']['content-length']
		
				
	def delete_object(self, bucket_name, key):
		return self.cos_client.delete_object(Bucket=bucket_name,Key=key)
