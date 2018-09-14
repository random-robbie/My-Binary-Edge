import sys
import json

f = open(sys.argv[1], 'r')

for line in f:
    event = json.loads(line)
    #print(event)
    if event['origin']['module'] == 'grabber':
        ip = event['target']['ip']
        try:
            
            if 'OK' in event['result']['data']['response']['statusMessage']:
               print ("[*] CouchDB System Logged[*]")
               URL = event['result']['data']['request']['url']
               text_file = open("found.txt", "a")
               text_file.write(""+URL+"\n")
               text_file.close()
        except:
            continue
