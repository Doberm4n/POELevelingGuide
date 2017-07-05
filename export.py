# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from json import load
from json import loads
import json
import os
import sys
import time


def createGuideAndImportText():
    data = {"common":{"info":{"name":"","author":"","notes":"","version": "","date":"","time":""}},"guide":{"tabs":[]}}
    temp = json.dumps(data)
    jsonData = loads(temp)
    dateNow = time.strftime("%d.%m.%Y")
    timeNow = time.strftime("%H:%M:%S")
    filesToImport = browseFiles()
    if filesToImport:
        filesToImport.sort()
        for i in range (len(filesToImport)):
            with open(filesToImport[i]) as f:
                    text = f.readlines()
                    for lines in range (len(text)):
                       text[lines] = text[lines].replace("\n", '')
            jsonData['guide']['tabs'].append({'text': [], 'name': os.path.splitext(os.path.basename(str(filesToImport[i])))[0].replace('_', ' '), 'isActCompleted':False})
            for j in range (len(text)):
                jsonData['guide']['tabs'][i]['text'].append({'string': text[j], 'isCompleted':False})
        jsonFileName = getJsonFileName()
        if jsonFileName:
            writeJson(jsonData, jsonFileName)

def getJsonFileName():
    newName = QtGui.QFileDialog.getSaveFileName(None, 'Text Input Dialog', directory=os.getcwd(), filter='*.json')
    return newName

def browseFiles():
    file = QtGui.QFileDialog.getOpenFileNames(None, "Select the file to add", directory=os.getcwd(), filter='*.txt')
    fileNames = list(file)
    return fileNames

def readJson(json_file):
    try:
        with open(json_file) as data_file:
            return load(data_file)
    except Exception, e:
         print "Error: " + str(e)

def writeJson(dump, json_file):
    try:
        print ""
        with open(json_file, 'w') as outfile:
                json.dump(dump, outfile)
    except Exception, e:
         print "Error: " + str(e)

