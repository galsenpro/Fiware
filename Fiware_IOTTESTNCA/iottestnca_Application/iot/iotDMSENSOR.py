from iottestnca_Application.iot.iotSensorNCA import *
import ast
class IOTDMSENSOR:
    def __init__(self,sensorTuple, dmSource = "DeviceModel-NCA-6452.json"):

        self.sensorFolder = settings.BASE_DIR + settings.SENSORFOLDER
        self.file =self.sensorFolder + dmSource
        self.dmSource = json.loads(open(self.file,"r").read())
        self.dmSource = dict(self.dmSource)
        self.sensorTuple = sensorTuple

    def mapDataSensor(self, nameModel = "DeviceModel-Sensibel-NCA-"):
        try:
            print("Mapping Sensor ...")
            for tpl in self.sensorTuple:
                dm = {}
                dm["controlledProperty"] = tpl[2]
                dateT = tpl[3][0]
                import datetime
                dm["dateLastValueReported"] = datetime.datetime.utcfromtimestamp(int(dateT)).strftime('%Y-%m-%dT%H:%M:%SZ')
                dm["id"] = tpl[1]+ "-"+ str(dateT)
                dm["brandName"] = tpl[0]+"-"+ str(dateT)
                dm["name"] = tpl[0]+"-"+ str(dateT)
                values = ""
                for i in tpl[2]:
                    myIndex = tpl[2].index(i)
                    values = values + str(i).split('-')[1] + "=" +tpl[3][myIndex] +";"
                dm["value"] = values
                print(dateT)
                self.dmSource.update(dm)
                jsonF = json.dumps(self.dmSource, sort_keys=True, indent=4)
                print(jsonF)
                fichier = open("schema/"+nameModel+str(dm["id"]+".json"), "w") #a
                fichier.write(jsonF)
                fichier.close()
        except Exception as x:
            print(x)

tplSensor = IOTSENSORNCA()
t = tplSensor.ncaSensorProvider()
mp = IOTDMSENSOR(t)
mp.mapDataSensor()
