from iottestnca_Application.iot.iotSensorNCA import *
import ast
class IOTDMSENSOR:
    def __init__(self,sensorTuple, dmSource = "Device-NCA-6452.json"):
        self.dm = {}
        #self.dmSource = json.loads(open(dmSource).read())
        self.sensorFolder = settings.BASE_DIR + settings.SENSORFOLDER
        self.file =self.sensorFolder + dmSource
        #print(json.dumps(open(self.config).read()))
        self.dmSource = json.loads(open(self.file,"r").read())
        #print(self.dmSource)
        self.sensorTuple = sensorTuple

    def mapDataSensor(self, position = "PS"):
        try:
            print("Mapping Sensor ...")
            for tpl in self.sensorTuple:
                self.dm["idS"] = tpl[1]+"-"+ str(position)
                self.dm["controlledProperty"] = tpl[2]
                values = " "
                for i in tpl[2]:
                    myIndex = tpl[2].index(i)
                    values = values + i + "=" +tpl[3][myIndex] +";"
                self.dm["valueS"] = values
                #print(tpl)
                #self.dmSource = json.loads(self.dmSource)
                #self.dm.update(ast.literal_eval(json.dumps(self.dmSource)))

                #print(self.dmSource)
                #self.dm = json.loads(self.dm)
                #self.dmSource = self.dmSource
                jsonF = json.dumps(self.dm)
                print(jsonF)

                #print(json.loads(jsonF))
        except Exception as x:
            print(x)

tplSensor = IOTSENSORNCA()
t = tplSensor.ncaSensorProvider()
mp = IOTDMSENSOR(t)
mp.mapDataSensor()