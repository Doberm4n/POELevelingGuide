# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from json import load
from json import loads
import json
import os
import sys
import time
#import export_test as GUIMain

class export():


    def __init__(self):
        #super(self.__class__, self).__init__()
        self.curDir = os.getcwd()
    #     # try:
        self.createGuideAndImportText()

    def test(self):
        data = {"common": {  "info": {} }, "guide": {  "tabs": [] }}
        temp = json.dumps(data)
        # jsonData['common'] = "{}"
        jsonData = loads(temp)
        dateNow = time.strftime("%d.%m.%Y")
        timeNow = time.strftime("%H:%M:%S")
        #self.writeJson(jsonData, self.getJsonFileName())
        #print  jsonData['guide']['tabs'][0]
        #jsonData = None
        #jsonData = self.readJson(self.browseFiles())
        #print jsonData['guide']['tabs']
        #del jsonData['guide']['tabs']
        filesToImport = self.browseFiles()
        #print filesToImport[0]
        #print os.path.splitext(os.path.basename(str(filesToImport[0])))[0]
        if filesToImport:
            for i in range (len(filesToImport)):
                with open(filesToImport[i]) as f:
                        self.text = f.readlines()
                        #print text_filename
                        #print str(len(self.text))
                        for lines in range (len(self.text)):
                            self.text[lines] = self.text[lines].replace("\n", '')
                jsonData['guide']['tabs'].append({'text': [], 'name': os.path.splitext(os.path.basename(str(filesToImport[i])))[0], 'isActCompleted':False})
                for j in range (len(self.text)):

                    jsonData['guide']['tabs'][i]['text'].append({'string': self.text[j], 'isCompleted':False})
            #jsonData['guide']['tabs'].append()
            jsonFileName = self.getJsonFileName()
            if jsonFileName:
                self.writeJson(jsonData, jsonFileName)
        #del jsonData['guide']['tabs']
        #json1 = load(jsonData)
        #jsonData = json.dumps(jsonData)
        #print jsonData
        #return newName

    def createGuideAndImportText(self):
        data = {"common":{"info":{"name":"","author":"","notes":"","version": "","date":"","time":""}},"guide":{"tabs":[]}}
        temp = json.dumps(data)
        # jsonData['common'] = "{}"
        jsonData = loads(temp)
        dateNow = time.strftime("%d.%m.%Y")
        timeNow = time.strftime("%H:%M:%S")
        #self.writeJson(jsonData, self.getJsonFileName())
        #print  jsonData['guide']['tabs'][0]
        #jsonData = None
        #jsonData = self.readJson(self.browseFiles())
        #print jsonData['guide']['tabs']
        #del jsonData['guide']['tabs']
        filesToImport = self.browseFiles()
        #print filesToImport[0]
        #print os.path.splitext(os.path.basename(str(filesToImport[0])))[0]
        if filesToImport:
            filesToImport.sort()
            for i in range (len(filesToImport)):
                with open(filesToImport[i]) as f:
                        self.text = f.readlines()
                        #print text_filename
                        #print str(len(self.text))
                        for lines in range (len(self.text)):
                            self.text[lines] = self.text[lines].replace("\n", '')
                jsonData['guide']['tabs'].append({'text': [], 'name': os.path.splitext(os.path.basename(str(filesToImport[i])))[0].replace('_', ' '), 'isActCompleted':False})
                for j in range (len(self.text)):

                    jsonData['guide']['tabs'][i]['text'].append({'string': self.text[j], 'isCompleted':False})
            #jsonData['guide']['tabs'].append()
            jsonFileName = self.getJsonFileName()
            if jsonFileName:
                self.writeJson(jsonData, jsonFileName)
        #del jsonData['guide']['tabs']
        #json1 = load(jsonData)
        #jsonData = json.dumps(jsonData)
        #print jsonData
        #return newName

    def getJsonFileName(self):
        newName = QtGui.QFileDialog.getSaveFileName(None, 'Text Input Dialog', directory=self.curDir, filter='*.json')
        # if ok and newName:
        #     print "ok"
        return newName

    def browseFiles(self):
        file = QtGui.QFileDialog.getOpenFileNames(None, "Select the file to add", directory=self.curDir, filter='*.txt')
        fileNames = list(file)
        return fileNames


    def readJson(self, json_file):
        try:
            with open(json_file) as data_file:
                return load(data_file)
        except Exception, e:
             print "Error: " + str(e)

    def writeJson(self, dump, json_file):
        try:
            print ""
            with open(json_file, 'w') as outfile:
                    json.dump(dump, outfile)
        except Exception, e:
             print "Error: " + str(e)

    def start(self):
        f = None

        for text_files in range (10):
            self.text = []
            text_filename = 'Act_' + str(text_files + 1) + '.txt'
            if os.path.isfile(os.path.join(curDir, text_filename)):
                print "Exists " + text_filename
                with open(text_filename) as f:
                    self.text = f.readlines()
                    print text_filename
                    print str(len(self.text))
                    for i in range (len(self.text)):
                        self.text[i] = self.text[i].replace("\n", '')

                    #self.text = f
                    print self.text
                    self.writeTextToJson(self.text, text_files + 1)
        # except Exception, e:
        #     print "Error: " + str(e)


    def writeTextToJson(self, text, act_number):
            with open('guide.json') as data_file:
                guideJson = load(data_file)
                # configCommon = configJson['common']
                # configTags = configJson['tags']
                # self.curDir = configCommon['curDir']
                # if self.curDir and os.path.isdir(self.curDir):
                #     self.curDirEdit.setText(self.curDir)
                #     self.populateLists(self.curDir)
                # for i in range(len(configTags['genre'])):
                #     self.genrelist.addItem(configTags['genre'][i])
                #print guideJson['guide']['act_1']['text'][0]
                #var = 'wrkwjel'
                #guideJson['guide']['act_1']['text'].append({'f':'wqewqewqewq'})

                #for i in range (10):
                    #print guideJson['guide']['act_1']['text'][0]
                    #print guideJson['guide']['act_1']['text'][1]
                act_dict = 'act_' + str(act_number)
                # delete dictionary
                del guideJson['guide'][act_dict]['text']
                del guideJson['guide'][act_dict]['isActCompleted']
                # add dictionary 'text'
                guideJson['guide'][act_dict].update({'text':[]})
                guideJson['guide'][act_dict].update({'isActCompleted': False})

                # add text to dictionary
                # guideJson['guide'][act_dict]['text'].append('ewqewqeqw')
                # guideJson['guide'][act_dict]['text'].append('ewqewqeqw2')
                print str(len(text))
                for j in range (len(text)):
                     guideJson['guide'][act_dict]['text'].append({'string': text[j], 'isCompleted': False})


                    # #





                    #guideJson['guide']['act_1']['text'][0] = 'test2'
                temp = guideJson
                with open('guide.json', 'w') as outfile:
                    json.dump(temp, outfile)
                print 'dump'
                    #return guideJson
            #print guideJson['guide']['act_2']['text'][4]



                # for i in range(len(configTags['quality'])):
                #     self.qualitylist.addItem(configTags['quality'][i])

    def writeConfig(self):
            with open('config.json') as data_file:
                configJson = load(data_file)
            #temp = configCommon['curDir']
            configJson['common']['curDir'] = self.curDir
            with open("config.json", "w") as data_file:
                json.dump(configJson, data_file)
                self.statusbar.showMessage("Config saved")

    def browseDir(self):
            self.curDir = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
            if self.curDir:
                self.curDirEdit.setText(self.curDir)
                self.clearLists()
                self.populateLists(self.curDir)

    def refresh(self):
            if self.curDir and os.path.isdir(self.curDir):
                self.curDirEdit.setText(self.curDir)
                self.clearLists()
                self.populateLists(self.curDir)

def main():
    app = QtGui.QApplication(sys.argv)
    # appIco = QtGui.QIcon()
    # appIco.addFile(':todo-icon16.png', QtCore.QSize(16,16))
    # appIco.addFile(':todo-icon32.png', QtCore.QSize(32,32))
    # app.setWindowIcon(appIco)
    form = export()
    #form.setWindowFlags(QtCore.Qt.WindowTitleHint)
    #form.show()
    app.exec_()
    #export.test()


if __name__ == '__main__':
    main()