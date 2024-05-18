

import boto3

def bucket_response()->dict:
	s3 = boto3.client('s3')
	return response

def print_buckets(res:dict)->None:
	print("s3 response keys:", res.keys())
	if "Buckets" in res.keys():
		print(res["Buckets"])

