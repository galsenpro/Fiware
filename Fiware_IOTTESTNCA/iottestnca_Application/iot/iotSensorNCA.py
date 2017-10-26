#-*- coding: utf-8 -*-
import json
from Fiware_IOTTESTNCA import settings
"""
    Create Device datamodel for each lines of Sensibel source
"""
class IOTSENSORNCA:

    def __init__(self, fileName = "Sensibel.json"):
        try:
            print("Sensor NCA ...")
            self.sensorFolder = settings.BASE_DIR + settings.SENSORFOLDER
            self.file =self.sensorFolder + fileName
            #print(json.dumps(open(self.config).read()))
            self.config = json.loads(open(self.file).read())
            #print(self.config)
        except Exception as x:
            print(x)


    def ncaGetSourceSensor(self, *params):
        try:
            src = self.config["source"]
            #print(src)
            return src
        except Exception as x:
            print(x)

    def ncaGetIdentificationSensor(self, *params):
        try:
            id = self.config["identification"]
            #print(id)
            return id
        except Exception as x:
            print(x)

    def ncaGetDataSensor(self, *params):
        try:
            data = self.config["data"]
            #print(data)
            #print(type(data))
            return data
        except Exception as x:
            print(x)

    def ncaSensorProvider(self, *params):
        try:
            data = self.ncaGetDataSensor()
            listSensor =  []
            for k in data:
                listAttrs = []
                listValues = []
                #del k['t']
                #print(k)
                for key, value in k.items():
                    listAttrs.append(str(key))
                    listValues.append(str(value))
                del listAttrs[0]
                #del listValues[0]
                sensorTuple = str(self.ncaGetSourceSensor()), str(self.ncaGetIdentificationSensor()),listAttrs, listValues
                #print(listAttrs, listValues)
                #print(sensorTuple)
                listSensor.append(sensorTuple)
            #print(listSensor)
            return listSensor
                #return listAttrs, listValues
        except Exception as x:
            print(x)

    def ncaMapAttribute(self, attribute):
        try:
            print("Mapping ...")

        except Exception as x:
            print(x)

testsensor = IOTSENSORNCA()
#testsensor.ncaGetSourceSensor()
#testsensor.ncaGetIdentificationSensor()
#data = testsensor.ncaGetDataSensor()
#testsensor.ncaGetListAttrsDataSensor()
#testsensor.getValuesDataSensor(data)
testsensor.ncaSensorProvider()