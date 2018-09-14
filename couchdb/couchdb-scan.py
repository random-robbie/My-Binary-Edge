import requests

session = requests.Session()

YOURTOKEN = ""



rawBody = '{
  "type": "scan",
  "description": "couchdb",
  "options": [
    {
      "targets": [
        "192.0.0.0/8"
      ],
      "ports": [
        {
          "port": 5984,
          "config": {
            "http_path": "/_all_dbs"
          },
          "modules": [
            "http"
          ]
        }
      ]
    }
  ]
}'





headers = {"User-Agent":"curl/7.55.1","Accept":"*/*","X-Token":YOURTOKEN,"Content-Type":"application/x-www-form-urlencoded"}
response = session.post("https://api.binaryedge.io/v1/tasks", data=rawBody, headers=headers)

print("Status code:   %i" % response.status_code)
print("Response body: %s" % response.content)

