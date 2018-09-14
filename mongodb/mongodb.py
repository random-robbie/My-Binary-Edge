import sys
import json

f = open(sys.argv[1], 'r')

for line in f:
    event = json.loads(line)
    #print(event)
    if event['origin']['module'] == 'grabber':
        ip = event['target']['ip']
        try:
            if 'serverInfo' in event['result']['data']:
                  print ("[*] Mongo DB System Logged[*]")
                  text_file = open("list.txt", "a")
                  text_file.write(""+ip+"\n")
                  ext_file.close()
        except:
            continue
