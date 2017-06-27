# 
# Main execution script for the prototype demonstration of DMC 15-16-02 project
#
# Uses MBDVidia and CheckMate only for prototype
#
import boto3
import tinys3
import random
import requests
import sys
import os

def main():
	"""main function
	"""
	creo_input = r"input.prt"
	dmis_output = r"output.dmi"
	local_directory = r"C:/tmp/"

	# Get the info to login to the s3 bucket and create the connection
	login_info = get_s3_bucket_info()

	# Create our tinys3 client, used for downloading data
	tinys3_conn = tinys3.Connection(login_info['access_key'],login_info['secret_key'], login_info['bucket'])

	# Create our boto3 client, used for uploading data
	boto_s3_client = boto3.client('s3', aws_access_key_id=login_info['access_key'],aws_secret_access_key=login_info['secret_key'])
	boto_session = boto3.Session(aws_access_key_id=login_info['access_key'],aws_secret_access_key=login_info['secret_key'])
	boto_s3 = boto_session.resource('s3')

	# Download the initial input: "input.prt", a Creo model
	try:
		response = tinys3_conn.get(creo_input)
		f = open(local_directory + creo_input,'wb')
		f.write(response.content)
		f.close()
	except requests.exceptions.HTTPError as err:
		print('! Unable to download %s:\n! %s' % (creo_input, err))
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

	# Launch MBDVidia with this input file
	# TODO

	# Launch CheckMate with the results from MBDVidia
	# TODO
	
	# Upload the resulting DMIS file
	f = open(local_directory + dmis_output, 'rb')
	try:
		boto_s3.Bucket(login_info['bucket']).put_object(Key=dmis_output, Body=f)
	except requests.exceptions.HTTPError as err:
		print('! Unable to upload to %s:\n! %s' % (dmis_output, err))
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise
	f.close()

	exit()


def get_s3_bucket_info():
	"""gets the info for logging into the s3 bucket
	"""
	# Open the info file with login info
	intxt = open('s3info.txt','r')
	indata = intxt.read().split('\n')
	inputs= {}

	# parse the file
	for keyval in indata:
	   pair = keyval.split('=')
	   if len(pair) > 1:
	       inputs[pair[0].strip()] = pair[1].strip()


	ret = {
		'bucket' : inputs['bucket'],
		'access_key' : inputs['s3access'],
		'secret_key' : inputs['s3secret']
		}
	return ret


if (__name__ == "__main__"):
	"""Initial function called by interpreter at command line
	"""
	main()
