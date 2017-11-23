#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ftplib import FTP

class IOTFTP:
    def __init__(self, host, user, passwd, directory = None):
        try:
            print("FTP initialization ... ")
            self.host = host
            self.user = user
            self.paswd = passwd
            self.directory = directory
            self.ftp = FTP(str(host), str(user), str(self.paswd))
        except Exception as x:
            print(x)
    
    def ncaFTPRenameFolder(self, srcFolder, destFolder):
        try:
            print("Renaming Folder ...")
            self.ftp.rename(srcFolder, destFolder)
        except Exception as x:
            print(x)
    
    def ncaFTPCreateFolder(self, folder):
        try:
            print("Creating Folder ...")
            self.ftp.mkd(folder)
        except Exception as x:
            print(x)
    
    def ncaFTPCopyFile(self, f_name = "mon_fichier.txt"):
        try:
            print("Copying Files ...")
            f = open(f_name, 'rb')
            self.ftp.storbinary('STOR ' + f_name, f)
            f.close()
        except Exception as x:
            print(x)
    
    def ncaFTPDeleteFolder(self, folder):
        try:
            print("Deleting folder ... ")
            self.ftp.rmd(folder)
        except Exception as x:
            print(x)
    
    
    def ncaFTPDeleteFile(self, file):
        try:
            print("Deleting file .... ")
            self.ftp.delete(file)
        except Exception as x:
            print(x)
            
    def ncaFTPChangeDirectory(self, directory):
        try:
            print("Changing directory ...")
            #connect.sendcmd('CWD test')
            self.ftp.sendcmd('CWD '+ directory)
        except Exception as x:
            print(x)
    
    def ncaFTPViewFiles(self):
        try:
            print("Viewing files ...")
            self.ftp.dir()
        except Exception as x:
            print(x)