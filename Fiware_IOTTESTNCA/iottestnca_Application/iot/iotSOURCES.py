#-*- coding: utf-8 -*-
import errno
#import lxml
import xmltodict
import json
import os
from Fiware_IOTTESTNCA import settings
#from Fiware_IOTTESTNCA. import *

class IOTSOURCE:

    def __init__(self):
    
        try:
            self.sourceFolder = settings.BASE_DIR+settings.SOURCES_FOLDER
            print(self.sourceFolder)
        except Exception as x:
            print(x)

    
    def clean (self, convertedFile = "None"):
        try:
            print("Cleaning ...")
        except Exception as x:
            print(x)

    
    def ncaCreateFolder(self, folder):
        try:
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
        except IOError:
            print("Impossible de créer le dossier "+ str(folder))
        except Exception as x:
            print(x)

    def ncaGetListFiles(self, directory = None, extension = "json"):
        try:
            if directory == None:
                directory = self.sourceFolder
            root = os.path.dirname(directory)
            listFiles = []
            dirs = os.listdir(root)
            for file in dirs:
                propertiesFiles = {}
                propertiesFiles['racine'] = root
                propertiesFiles['xmlSrc'] = file
                propertiesFiles['jsonFilename'] = str(os.path.basename(file)).split(".")[0]
                listFiles.append(propertiesFiles)
            print(listFiles)
            return listFiles
        except Exception as x:
            print(x)

    """
        
    """
    def ncaConvertListOfFiles(self, listOfFiles, xml_attribs=True):
        try:
            self.ncaCreateFolder(settings.DEST_FOLDER)
            for elt in listOfFiles:
                xmlFile = elt.get('xmlSrc')
                racine = elt.get('racine')
                jsonFilename = elt.get('jsonFilename')
                try:
                    with open(str(racine + "/"+xmlFile), "rb") as f:
                        d = xmltodict.parse(f, xml_attribs=xml_attribs)
                        fjson = settings.DEST_FOLDER + "/"+jsonFilename +".json"
                        fh = open(fjson, 'w')
                        fh.writelines(json.dumps(d, indent=4))
                        fh.close()
                    print("Entity - " + str(jsonFilename).upper().split('_')[1])
                except Exception as x:
                    print(x)
        except Exception as x:
            print(x)

    """
        Function to show all files of specific folder
    """
    def ncaShowFiles(self,  outputFolder = "convertedSource/", xml_attribs=True,  output = None):
        try:
            print("Viewing contents ...")
            racine = os.path.dirname(self.sourceFolder)
            print(os.path.dirname(self.sourceFolder))
            dirs = os.listdir(os.path.dirname(self.sourceFolder))
            for file in dirs:
                #print(file)
                print(os.path.basename(file)) #Just the filename
                name = str(os.path.basename(file)).split(".")[0]+".json"
                manifest = str(os.path.dirname(self.sourceFolder)) + "/"+ str(file)
                if outputFolder == None:
                    self.ncaCreateFolder(racine)
                    jsonFile = str(racine + "/"+ name)
                else:
                    self.ncaCreateFolder(racine + "/"+ outputFolder)
                    jsonFile = str(racine + "/"+ outputFolder+ name)
                print(manifest)
                print(jsonFile)
                try:
                    with open(str(manifest), "rb") as f:
                        d = xmltodict.parse(f, xml_attribs=xml_attribs)
                        # print(f)
                        # f= json.dumps(d, indent=4)
                        fh = open(manifest, 'w')
                        fh.writelines(json.dumps(d, indent=4))
                        fh.close()
                    contenu = ""
                    with open(str(manifest), "rb") as fh:  # notice the "rb" mode
                        for ligne in fh:
                            contenu += str(ligne).replace("@", "")
                        fh.close()
                        #self.creatingFolder(self.folderDest)
                        output = settings.DEST_FOLDER +"/entry.json"
                        #print(os.path.dirname(output))
                        #self.creatingFolder(self.folderDest)
                        fichier = open(str(jsonFile), 'w')
                        fichier.write(contenu)
                        fichier.close()
                    #print("Manifest Converti : \n" + manifest)
                    #return manifest
                except Exception as x:
                    print(x)
        except Exception as x:
            print(x)