#!/usr/bin/python
# -*- coding: utf-8 -*

import os, sys
class IOTTRAITMENT:
    
    def __init__(self, sourceFolder="source", destFolder="destination"):
        try:
            print("Traitment ...")
        except Exception as x:
            print(x)
    
    """ 
        Renvoie une liste des fichiers d'un répertoire donné 
    """
    def ncaCheckFolder(self):
        try:
            print("Checking Source Folder ...")
        except Exception as x:
            print(x)
    
    """ 
        Convert
    """
    def ncaShowFiles(self, path = None):
        try:
            print("Converting files ...")
            # Open a file
            #path = "/var/www/html/"
            dirs = os.listdir( path )
            for file in dirs:
                print(file)
        except Exception as x:
            print(x)
            
iotttmt = IOTTRAITMENT("sorties")
iotttmt.ncaShowFiles("../datamodels/Fiware/OTC")