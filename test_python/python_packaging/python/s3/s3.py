

import boto3


def get_response()->dict:
	s3 = boto3.client('s3')
	response = s3.list_buckets()
	return response

def print_buckets(res:dict)->None:
	print("s3 response keys:", res.keys())
	if "Buckets" in res.keys():
		print(res["Buckets"])
		name = list(map(lambda x:x['Name'],res["Buckets"]))
		return name

def print_response():
	print(boto3.client('s3').list_buckets())
