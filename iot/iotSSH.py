#!/usr/bin/env python
#-*- coding: utf-8 -*-

from fabric.api import *

class IOTSSH:
    def __init__(self, host, user, passwd, directory = None):
        try:
            print("SSH initialization ... ")
            self.host = host
            self.user = user
            self.paswd = passwd
            self.directory = directory
             
            self.env.host_string =  host
            self.env.user = user
            self.env.password = passwd
        except Exception as x:
            print(x)
        
    def ncaSSHGetFile(self, remotePath = "/backup/2014.sql.gz", localPath):
        try:
            print("Getting Folder ...")
            get(remote_path= remotePath, local_path= localPath)
        except Exception as x:
            print(x)
    
    def ncaSSHSendFile(self, remoteFile = "/backup/2014.sql.gz", localFile):
        try:
            print("Sending File ...")
            put(localFile, remoteFile)
        except Exception as x:
            print(x)
    