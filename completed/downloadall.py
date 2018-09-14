import json
import requests
import os

session = requests.Session()


headers = {"Accept":"*/*","X-Token","YOURTOKEN","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded"}
response = session.get("https://api.binaryedge.io/v1/tasks", headers=headers)


y = json.loads(response.content)

for x in y:
  if x["status"] == "Success":
  	if os.path.exists(x["job_id"]) == False:
  		os.makedirs(x["job_id"])
  		job_id = x["job_id"]
  		print ("[*] Downloading Job ID: "+job_id+" [*]")
  		os.system('curl -l https://stream.api.binaryedge.io/v1/replay/'+job_id+' -H "X-Token:YOURTOKEN" '+job_id+'/'+job_id+'.json')
  		print ("[*] Downloaded Job ID: "+job_id+" [*]")
