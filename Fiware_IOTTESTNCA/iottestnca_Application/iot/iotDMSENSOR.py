from iottestnca_Application.iot.iotSensorNCA import *
import ast
class IOTDMSENSOR:
    def __init__(self,sensorTuple, dmSource = "DeviceModel-NCA-6452.json"):

        self.sensorFolder = settings.BASE_DIR + settings.SENSORFOLDER
        self.file =self.sensorFolder + dmSource
        self.dmSource = json.loads(open(self.file,"r").read())
        self.dmSource = dict(self.dmSource)
        self.sensorTuple = sensorTuple

    def mapDataSensor(self, position = 1):
        try:
            print("Mapping Sensor ...")
            for tpl in self.sensorTuple:
                dm = {}
                dm["brandName"] = tpl[0]+"-S"+ str(position)
                dm["name"] = tpl[0]+"-S"+ str(position)
                dm["id"] = tpl[1]+"-S"+ str(position)
                dm["controlledProperty"] = tpl[2]

                values = ""
                for i in tpl[2]:
                    myIndex = tpl[2].index(i)
                    values = values + i + "=" +tpl[3][myIndex] +";"
                dm["value"] = values
                self.dmSource.update(dm)
                position = position +1
                jsonF = json.dumps(self.dmSource, sort_keys=True, indent=4)
                print(jsonF)
        except Exception as x:
            print(x)

tplSensor = IOTSENSORNCA()
t = tplSensor.ncaSensorProvider()
mp = IOTDMSENSOR(t)
mp.mapDataSensor()