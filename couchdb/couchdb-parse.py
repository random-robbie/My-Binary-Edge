import sys
import json

f = open(sys.argv[1], 'r')

for line in f:
    event = json.loads(line)
    #print(event)
    if event['origin']['module'] == 'grabber':
        ip = event['target']['ip']
        try:
            if 'response' in event['result']['data']:
                if 'etag' in event['result']['data']['response']['body']:
                   print ("[*] Docker System Logged[*]")
                   text_file = open("./cfg/"+ip+".json", "a")
                   js = json.loads(event['result']['data']['response']['body'])
                   text_file.write(json.dumps(js, indent=4))
                   text_file.close()
        except:
            continue
