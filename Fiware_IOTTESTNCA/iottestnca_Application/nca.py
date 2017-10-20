#!/usr/bin/python
# -*- coding: utf-8 -*-
#from Fiware_IOTTESTNCA.iottestnca.iot.iotSOURCES import *
from iottestnca_Application.iot.iotSOURCES import *
if __name__ == "__main__":
    map =  IOTSOURCE()
    liste = map.ncaGetListFiles()
    map.ncaConvertListOfFiles(liste)