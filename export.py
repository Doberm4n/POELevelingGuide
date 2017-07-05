# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from json import load
from json import loads
import json
import os
import sys
import time


def createGuideAndImportText(self):
    #print self.curGuide
    data = {"common":{"info":{"name":"","author":"","notes":"","version": "","date":"","time":"","URL":""}},"guide":{"tabs":[]}}
    temp = json.dumps(data)
    jsonData = loads(temp)
    dateNow = time.strftime("%d.%m.%Y")
    timeNow = time.strftime("%H:%M:%S")
    filesToImport = browseFiles()
    textInfo = ""
    guideStringCount = 0
    if filesToImport:
        #filesToImport.sort()
        for i in range (len(filesToImport)):
            with open(filesToImport[i]) as f:
                    text = f.readlines()
                    filename = os.path.splitext(os.path.basename(str(filesToImport[i])))[0]
                    if filename.startswith("_info"):
                        print "Found info"
                        textInfo = text
                        continue
                    for lines in range (len(text)):
                       text[lines] = text[lines].replace("\n", '')
            jsonData['guide']['tabs'].append({'text': [], 'name': filename.replace('_', ' '), 'isActCompleted':False})
            for j in range (len(text)):
                jsonData['guide']['tabs'][guideStringCount]['text'].append({'string': text[j], 'isCompleted':False})
            guideStringCount += 1


        guideDate = dateNow
        guideTime = timeNow
        if textInfo:
            jsonData['common']['info'].update({"name": textInfo[0], "author": textInfo[1], "notes": textInfo[2], "version": textInfo[3], "date": guideDate, "time": guideTime, "URL": textInfo[4]})
        else:
            guideName = gettext('Guide name', 'Please enter guide name:')
            guideAuthor = gettext('Guide author', 'Please enter guide author:')
            guideNotes = gettext('Guide notes', 'Please enter guide notes:')
            guideVersion = gettext('Guide version', 'Please enter guide version:')
            guideURL = gettext('Guide url', 'Please enter guide url:')
            jsonData['common']['info'].update({"name": guideName, "author": guideAuthor, "notes": guideNotes, "version": guideVersion, "date": guideDate, "time": guideTime, "URL": guideURL})
        jsonFileName = getJsonFileName()
        if jsonFileName:
            writeJson(jsonData, jsonFileName)
            writeConfigAndLoadGuide(self, jsonFileName)

def writeConfigAndLoadGuide(self, jsonFileName):
            self.curGuide = str(jsonFileName)
            guideJson = self.readJson('Configs\config.json')
            guideJson['curGuide'] = self.curGuide
            self.writeJson(guideJson, 'Configs\config.json')
            self.guideLineEdit.setText(os.path.basename(self.curGuide))
            self.loadGuide(self.curGuide)

def gettext(title, question):
      text, ok = QtGui.QInputDialog.getText(None, title, question)
      if ok:
         return str(text)

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

