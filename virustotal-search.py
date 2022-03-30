#!/usr/bin/env python
import requests, argparse, time
import argparse
from os import path
import time
import json
from json2html import *

localTime = time.localtime()
output = "result_%04d-%02d-%02d.json" % localTime[0:3]

def VT_Request(key, hash, output):
	parameters = {"apikey": key, "resource": hash}
	url = requests.get("https://www.virustotal.com/vtapi/v2/file/report", params=parameters)
	hash_result = []
	json_response = url.json()
	response = int(json_response.get("response_code"))
	# today = "%04d-%02d-%02d" % localTime[0:3]


	if path.isfile(output) is False:
		with open(output, 'w') as json_file:
			json.dump(hash_result, json_file, indent=4, separators=(',',': '))
	else:
		with open(output) as f:
			hash_result = json.load(f)

	if response == 1 and 'Fortinet' in json_response['scans']:
		hash_result.append({
			"hash_value (MD5 or Sha256)": json_response['md5'],
			"Fortinet detection name": json_response['scans']['Fortinet']['result'],
			"Number of engines detected": json_response['positives'],
			"Scan Date": json_response['scan_date']			
		})
	elif response == 1 and 'Fortinet' not in json_response['scans']:
		hash_result.append({
			"hash_value (MD5 or Sha256)": json_response['md5'],
			"Fortinet detection name": 'not found',
			"Number of engines detected": json_response['positives'],
			"Scan Date": json_response['scan_date']			
		})
	else:
		hash_result.append({
			"hash_value (MD5 or Sha256)": hash,
			"Fortinet detection name": 'Hash is not in virustotal database',
			"Number of engines detected": 'not found',
			"Scan Date": 'not found',
		})
	with open(output, 'w') as json_file:
		json.dump(hash_result, json_file, indent=4)
	print(f"hash value: {hash} is successfully appended to the JSON file.")

def Generate_HTML():
	with open(output) as f:
		data = json.load(f)
		scanOutput = json2html.convert(json=data)
		htmlReportfile = "templates/index.html"
	with open(htmlReportfile, 'w') as htmlfile:
		htmlfile.write(str(scanOutput))
		print('Successfully generated HTML file!')

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", required=False)
	parser.add_argument("-o", "--output", required=False)
	parser.add_argument("-k", "--key", required=True)
	args = parser.parse_args()

	if args.input and args.key:
		print("Scanning report of the hashes. It takes 15 seconds on each hash.")
		with open(args.input) as f:
			for line in f.readlines():
				VT_Request(args.key, line.rstrip(), (args.output or output))
				time.sleep(15)
	Generate_HTML()


if __name__ == "__main__":
	main()