#-*- coding: utf-8 -*-

import requests
import json

class IOTHTTP:
    def __init__(self, url = None):
        try:
            print("HTTP initialization ... ")
            self.url = url
            print(self.url)
        except Exception as x:
            print(x)
    
    def ncaGetTextContent(self, output = None):
        try:
            r = requests.get(self.url)
            if output != None:
                fichier = open(str(output), 'w')
                fichier.write(r.text)
                fichier.close()
            else:
                print (r.text)
            return output
        except Exception as x:
            print(x)
    
    def ncaGetJsonContent(self):
        try:
            r = requests.get(self.url)
            print (r.json)
            return r.json
        except Exception as x:
            print(x)
    
    def ncaPostData(self, playload = {'some': 'data'}, headers =  {'content-type': 'application/json'}):
        try:
            print("Posting data ...")
            r = requests.post(self.url, data=json.dumps(payload))
            print(json.dumps(r))
            #return r.text
        except Exception as x:
            print(x)

http = IOTHTTP('http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?')
http.ncaGetTextContent("body.xml")

