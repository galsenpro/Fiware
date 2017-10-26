#!/usr/bin/python
# -*- coding: utf-8 -*-
#from Fiware_IOTTESTNCA.iottestnca.iot.iotSOURCES import *
from iottestnca_Application.iot.iotSOURCES import *
from iottestnca_Application.iot.iotDMSENSOR import *
if __name__ == "__main__":
    """ SOURCE IOT """
    #map =  IOTSOURCE()
    #liste = map.ncaGetListFiles()
    #map.ncaConvertListOfFiles(liste)
    """ SENSOR """
    tplSensor = IOTSENSORNCA()
    t = tplSensor.ncaSensorProvider()
    mp = IOTDMSENSOR(t)
    mp.mapDataSensor()