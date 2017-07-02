# -*- coding: utf-8 -*-
from json import load
from json import loads
import json
import os

class export():


    def __init__(self):
        curDir = os.getcwd()
        # try:
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

export = export()