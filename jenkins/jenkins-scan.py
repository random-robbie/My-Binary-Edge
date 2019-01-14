import requests
import sys
import json
import os

session = requests.Session()

fname = "list.txt"
YOURTOKEN = "APIKEY"

def issue_scan (YOURTOKEN,TARGET):

	rawBody = '''{
	"type": "scan",
	"description": "Jenkins",
	"options": [
		{
		"targets": ["'''+TARGET+'''"],
		"ports": [
			{
			"port": 8080,
			"config": {
				"http_path": "/view/all/builds"
			},
			"modules": [
				"http"
			]
			}
		]
		}
	]
	}'''





	headers = {"User-Agent":"curl/7.55.1","Accept":"*/*","X-Token":YOURTOKEN,"Content-Type":"application/x-www-form-urlencoded"}
	response = session.post("https://api.binaryedge.io/v1/tasks", data=rawBody, headers=headers)

	print("Status code:   %i" % response.status_code)
	print("Response body: %s" % response.content)
	text_file = open("jobs.txt", "a")
	js = json.loads(response.text)
	j = json.dumps(js['job_id'])
	vg = str(""+j+"\n")
	fds = vg.replace('"','')
	text_file.write(fds)
	text_file.close()

	

try:
	os.remove("jobs.txt")
	with open(fname) as f:
		for line in f:
			TARGET = line.replace("\n","")
			issue_scan (YOURTOKEN,TARGET)
		
except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
				
except Exception as e:
		print('Error: %s' % e)
		sys.exit(1)
