# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QEvent
from PyQt4.QtCore import QObject
#import res.res
import sys
import re
import os
from json import load
from json import loads
import json
import gc
import time
import datetime
import urllib2
import res.res
#import modules.DPSCalc as DPSCalcModule
import generated.form_main as GUIMain
import generated.form_about as GUIAbout
#import generated.about as GUIAbout
from Tkinter import Tk
import ctypes
import export


myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

form = None
formAbout = None
version = '0.9.21'
link = '<a href="https://github.com/Doberm4n/POELevelingGuide">GitHub</a>'
guideGitHubUrl = 'https://github.com/Doberm4n/POELevelingGuide/releases/download/POELevelingGuide/LevelingGuideForPoE.json'


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class POE_fast_leveling_guideApp(QtGui.QMainWindow, GUIMain.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.prepareGui()

        self.openGuidePushButton.clicked.connect(self.browseGuide)
        self.actionReset_All.triggered.connect(self.menuActionResetAll)
        self.actionComplete_All.triggered.connect(self.menuActionCompleteAll)
        self.menuActionOpen.triggered.connect(self.browseGuide)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionCreate_empty_guide_file.triggered.connect(lambda: export.createGuideAndImportText(self))
        self.actionDownload_guide_from_GitHub.triggered.connect(self.downloadAndOpenGuideFromGithub)

        self.loadConfig()

    def buttonsTextClick(self, tab, index):
        #print str(tab) + " " + str(index)
        if self.buttonsText[tab, index].isEnabled():
            self.buttonsText[tab, index].setEnabled(False)
            guideJson = self.readJson(self.curGuide)
            guideJson['guide']['tabs'][tab]['text'][index]['isCompleted'] = True
            self.writeJson(guideJson, self.curGuide)

    def buttonsCompleteClick(self, tab, index):
        #print str(tab) + " " + str(index)
        if not self.buttonsText[tab, index].isEnabled():
            self.buttonsText[tab, index].setEnabled(True)
            self.buttonsText[tab, index].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
            guideJson = self.readJson(self.curGuide)
            guideJson['guide']['tabs'][tab]['text'][index]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def menuActionResetClick(self, tab, count):
        guideJson = self.readJson(self.curGuide)
        if self.dialogYesNo('Reset', 'Reset ' + guideJson['guide']['tabs'][tab]['name'] + '\n\nAre you sure?'):
            #print str(tab) + str(count)
            for i in range (count + 1):
                if not self.buttonsText[tab, i].isEnabled():
                    self.buttonsText[tab, i].setEnabled(True)
                    self.buttonsText[tab, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
                    guideJson['guide']['tabs'][tab]['text'][i]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def menuActionResetAll(self):
        if self.dialogYesNo('Reset all', "Reset all\n\nAre you sure?"):
            guideJson = self.readJson(self.curGuide)
            for tabs in range (self.tabWidget.count()):
                    for widget in self.groupBoxes[tabs].children():
                        if isinstance(widget, QtGui.QPushButton):
                            if "guideStringPushButton_" in widget.objectName():
                                if not widget.isEnabled():
                                    widget.setEnabled(True)
                            #print "linedit: %s  - %s" %(widget.objectName(),widget.text())
                    for i in range (len(guideJson['guide']['tabs'][tabs]['text'])):
                        if guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted']:
                            guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def menuActionCompleteClick(self, tab, count):
        guideJson = self.readJson(self.curGuide)
        if self.dialogYesNo('Complete', 'Complete ' + guideJson['guide']['tabs'][tab]['name'] + '\n\nAre you sure?'):
            #print str(tab) + str(count)
            for i in range (count + 1):
                if  self.buttonsText[tab, i].isEnabled():
                    self.buttonsText[tab, i].setEnabled(False)
                    self.buttonsText[tab, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
                    guideJson['guide']['tabs'][tab]['text'][i]['isCompleted'] = True
            self.writeJson(guideJson, self.curGuide)

    def menuActionCompleteAll(self):
        if self.dialogYesNo('Complete all', "Complete all\n\nAre you sure?"):
            #print "curGuide: " + self.curGuide
            guideJson = self.readJson(self.curGuide)
            for tabs in range (self.tabWidget.count()):
                    for widget in self.groupBoxes[tabs].children():
                        if isinstance(widget, QtGui.QPushButton):
                            if "guideStringPushButton_" in widget.objectName():
                                if  widget.isEnabled():
                                    widget.setEnabled(False)
                            #print "linedit: %s  - %s" %(widget.objectName(),widget.text())
                    for i in range (len(guideJson['guide']['tabs'][tabs]['text'])):
                        if not guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted']:
                            guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'] = True
            self.writeJson(guideJson, self.curGuide)

    def dialogYesNo(self, title, question):
        result = QtGui.QMessageBox.question(self, title, question, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

    def readJson(self, json_file):
        if json_file:
            try:
                with open(json_file) as data_file:
                    return load(data_file)
            except Exception, e:
                print "Error: " + str(e)

    def writeJson(self, dump, json_file):
        if json_file:
            try:
                #print ""
                with open(json_file, 'w') as outfile:
                        json.dump(dump, outfile)
            except Exception, e:
                 print "Error: " + str(e)

    def loadConfig(self):
        try:
            guideJson = self.readJson('Configs\config.json')
            if guideJson['curGuide']:
                #print "Yes"
                self.curGuide = guideJson["curGuide"]
                curGuideFilename = os.path.basename(self.curGuide)
                self.guideLineEdit.setText(curGuideFilename)
                self.curDir = os.path.dirname(self.curGuide)
                if os.path.isfile(self.curGuide):
                    self.loadGuide(self.curGuide)
                else:
                    self.statusbar.showMessage('Guide not found (' + curGuideFilename + ')')
            else:
                self.curDir = ""
                self.curGuide = ""
                #print "No"
        except Exception, e:
             print "Error in loading config: " + str(e)

    def browseGuide(self):
        curGuide = str(QtGui.QFileDialog.getOpenFileName(self, "Select guide", filter='*.json', directory=self.curDir))
        #print self.curGuide
        if curGuide:
            self.curGuide = curGuide
            guideJson = self.readJson('Configs\config.json')
            guideJson['curGuide'] = self.curGuide
            self.writeJson(guideJson, 'Configs\config.json')
            self.guideLineEdit.setText(os.path.basename(self.curGuide))
            #self.clearGuide()
            self.loadGuide(self.curGuide)

    def prepareGui(self):

        self.tabWidget.hide()
        self.completedStylesheet = "QPushButton:!enabled {font-family: Verdana; font-size: 8pt; color: green; text-align: left;  padding: 5;}"
        self.uncompletedStylesheet = "QPushButton:enabled {font-family: Verdana; font-size: 8pt; text-align: left; border: 1px solid grey; background-color: white; padding: 5; font-weight: 1bold } QPushButton:hover {background-color: rgb(187, 255, 177);}"
        self.disabledtabsylesheet = ""
        self.actionsReset = [self.actionAct_1, self.actionAct_2, self.actionAct_3, self.actionAct_4, self.actionAct_5, self.actionAct_6, self.actionAct_7, self.actionAct_8, self.actionAct_9, self.actionAct_10, self.actionReset_All]
        self.menuActionResets = {}
        self.menuActionProgress = {}
        self.windowTitle = 'PoE Leveling Guide'
        self.tabWidget.setStyleSheet(self.disabledtabsylesheet)

    # def clearButtons(self):
    #     for tabs in range (10):
    #             for widget in self.groupBoxes_original[tabs].children():
    #                 if isinstance(widget, QtGui.QPushButton):
    #                     widget.deleteLater()

    def clearTabs(self):
        tabs_count = self.tabWidget.count()
        #print "tabs_count = " + str(tabs_count)
        for i in range (tabs_count -1, -1, -1):
            self.tabWidget.widget(i).close()
            self.tabWidget.widget(i).deleteLater()
            self.tabWidget.removeTab(i)
        gc.collect()

    def clearMenuActionReset(self):
        if self.menuActionResets:
            #print "self.menuReset_progress.widget.count()"
            for value in self.menuActionResets.values():
                self.menuReset_progress.removeAction(value)
            self.menuActionResets = {}

    def clearMenuActionProgress(self):
        if self.menuActionProgress:
            #print "self.menuReset_progress.widget.count()"
            for value in self.menuActionProgress.values():
                self.menuComplete_progress.removeAction(value)
            self.menuActionProgress = {}

    def eventFilter(self, obj, event):
        if obj and not obj.isEnabled() and event.type() == QEvent.Wheel:
            newEvent = QtGui.QWheelEvent(obj.mapToParent(event.pos()), event.globalPos(),
                                   event.delta(), event.buttons(),
                                   event.modifiers(), event.orientation())
            QtGui.QApplication.instance().postEvent(obj.parent(), newEvent)
            return True
        return QObject.eventFilter(self, obj, event)

    def loadGuide(self, guide):
        try:
            guideJson = self.readJson(guide)
            text = []
            self.setWindowTitle(self.windowTitle)
            self.clearTabs()
            self.clearMenuActionReset()
            self.clearMenuActionProgress()
            self.buttonsText = None
            self.buttonsComplete = None
            self.buttonsText = {}
            self.buttonsComplete = {}
            self.tabs = {}
            self.verticalLayouts = {}
            self.scrollAreas = {}
            self.scrollAreaWidgetContents = {}
            self.groupBoxes = {}
            self.formLayouts = {}
            self.gridLayouts = {}
            self.firstTab = False
            self.tabWidget.show()
            tabs_count = self.tabWidget.count()
            #print "tabs_count init = " + str(tabs_count)
            tabsCount = len(guideJson['guide']['tabs'])
            for tabs in range (tabsCount):
                guideActKey = 'act_' + str(tabs + 1)
                #if not guideJson['guide']['tabs'][tabs]['text']:
                    #print "tabs " + str(tabs)
                self.tabs[tabs] = QtGui.QWidget()
                self.tabs[tabs].setObjectName(_fromUtf8("tab_" + str(tabs)))
                self.verticalLayouts[tabs] = QtGui.QVBoxLayout(self.tabs[tabs])
                self.verticalLayouts[tabs].setContentsMargins(-1, -1, -1, 9)
                self.verticalLayouts[tabs].setSpacing(11)
                self.verticalLayouts[tabs].setObjectName(_fromUtf8("verticalLayout_" + str(tabs)))
                self.scrollAreas[tabs] = QtGui.QScrollArea(self.tabs[tabs])
                self.scrollAreas[tabs].setWidgetResizable(True)
                self.scrollAreas[tabs].setObjectName(_fromUtf8("scrollArea_" + str(tabs)))
                self.scrollAreaWidgetContents[tabs] = QtGui.QWidget()
                self.scrollAreaWidgetContents[tabs].setGeometry(QtCore.QRect(0, 0, 1048, 631))
                self.scrollAreaWidgetContents[tabs].setObjectName(_fromUtf8("scrollAreaWidgetContents_" + str(tabs)))
                self.formLayouts[tabs] = QtGui.QFormLayout(self.scrollAreaWidgetContents[tabs])
                self.formLayouts[tabs].setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
                self.formLayouts[tabs].setObjectName(_fromUtf8("formLayout" + str(tabs)))
                self.groupBoxes[tabs] = QtGui.QGroupBox(self.scrollAreaWidgetContents[tabs])
                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.groupBoxes[tabs].sizePolicy().hasHeightForWidth())
                self.groupBoxes[tabs].setSizePolicy(sizePolicy)
                self.groupBoxes[tabs].setObjectName(_fromUtf8("groupBox_" + str(tabs)))
                self.gridLayouts[tabs] = QtGui.QGridLayout(self.groupBoxes[tabs])
                self.gridLayouts[tabs].setVerticalSpacing(2)
                self.gridLayouts[tabs].setObjectName(_fromUtf8("gridLayout_" + str(tabs)))
                self.formLayouts[tabs].setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBoxes[tabs])
                self.scrollAreas[tabs].setWidget(self.scrollAreaWidgetContents[tabs])
                self.verticalLayouts[tabs].addWidget(self.scrollAreas[tabs])
                self.tabWidget.addTab(self.tabs[tabs], _fromUtf8(""))
                self.gridLayouts[tabs].setColumnStretch(0, 1)
                self.gridLayouts[tabs].setVerticalSpacing(2)
                textLength = len(guideJson['guide']['tabs'][tabs]['text'])
                if (not self.firstTab) and (textLength > 0):
                      self.tabWidget.setCurrentIndex(tabs)
                      self.firstTab = True
                if textLength > 0:
                    self.menuActionResets[tabs] = QtGui.QAction(self)
                    self.menuActionResets[tabs].setObjectName(_fromUtf8("actionReset_" + str(tabs)))
                    self.menuReset_progress.addAction(self.menuActionResets[tabs])
                    self.menuActionResets[tabs].setText(_translate("MainWindow", "Reset " + guideJson['guide']['tabs'][tabs]['name'], None))
                    self.menuActionProgress[tabs] = QtGui.QAction(self)
                    self.menuActionProgress[tabs].setObjectName(_fromUtf8("actionProgress_" + str(tabs)))
                    self.menuComplete_progress.addAction(self.menuActionProgress[tabs])
                    self.menuActionProgress[tabs].setText(_translate("MainWindow", "Complete " + guideJson['guide']['tabs'][tabs]['name'], None))
                i = 0
                if textLength == 0:
                    #print "Length = 0"
                    self.tabWidget.setTabEnabled(tabs, False)
                    #self.tabWidget.widget(0).hide()
                    #tabs_count = self.tabWidget.count()
                    #print "tabs_count = " + str(tabs_count)
                #print "Length " + str(tabs) + " " + str(textLength)
                for i in range (textLength):
                    self.buttonsText[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
                    self.buttonsComplete[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
                    self.buttonsText[tabs, i].setObjectName(_fromUtf8("guideStringPushButton_" + str(i)))
                    self.buttonsComplete[tabs, i].setObjectName(_fromUtf8("resetPushButton_" + str(i)))
                    self.buttonsText[tabs, i].setText(_translate("MainWindow", "guideStringPushButton", None))
                    self.buttonsComplete[tabs, i].setText(_translate("MainWindow", "resetPushButton", None))
                    self.buttonsText[tabs, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
                    self.gridLayouts[tabs].addWidget(self.buttonsText[tabs, i], i, 0, 1, 1)
                    self.gridLayouts[tabs].addWidget(self.buttonsComplete[tabs, i], i, 1, 1, 1)
                    tempString = guideJson['guide']['tabs'][tabs]['text'][i]['string']
                    if  tempString.find(u'\u25e6') >= 0:
                        tempString = "     " + tempString
                    self.buttonsText[tabs, i].setText(tempString)
                    self.buttonsText[tabs, i].setEnabled(not guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'])
                    self.buttonsText[tabs, i].installEventFilter(self)
                    self.buttonsComplete[tabs, i].setText("Reset")
                    self.buttonsText[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonsTextClick(tabs, i))
                    self.buttonsComplete[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonsCompleteClick(tabs, i))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[tabs]), _translate("MainWindow", guideJson['guide']['tabs'][tabs]['name'], None))
                if textLength > 0:
                    if self.menuActionResets[tabs].triggered:
                        self.menuActionResets[tabs].triggered.disconnect()
                    self.menuActionResets[tabs].triggered.connect(lambda clicked, tabs=tabs, i=i: self.menuActionResetClick(tabs, i))

                    if self.menuActionProgress[tabs].triggered:
                        self.menuActionProgress[tabs].triggered.disconnect()
                    self.menuActionProgress[tabs].triggered.connect(lambda clicked, tabs=tabs, i=i: self.menuActionCompleteClick(tabs, i))
            if not self.firstTab:
                self.tabWidget.hide()
            self.setWindowTitle(self.windowTitle + " - " + os.path.basename(guide) + ' (' + os.path.dirname(guide) + ')')
            guideInfo = guideJson['common']['info']
            self.guideLineEdit.setText(guideInfo['name'] + "" + guideInfo['version'] + "(" + guideInfo['date'] + " " + guideInfo['time'] + ")" + guideInfo['author'] + "" + guideInfo['notes'] + "" + guideInfo['URL'])
            self.statusbar.clearMessage()
        except Exception, e:
            self.tabWidget.hide()
            self.statusbar.showMessage("Error in loading guide: " + str(e))

    def showAbout(self):
        global formAbout
        formAbout = aboutDialog()
        formAbout.show()

    def downloadAndOpenGuideFromGithub(self):
        try:
            #self.downloading_thread = downloadingThread(url, filename)
            #self.downloading_thread.start()
            ##self.downloading_thread.downloadURL()
            # self.url = url
            # self.filename = filename
            #global form
            self.statusbar.showMessage('Downloading leveling guide json...')
            url = guideGitHubUrl
            #now = str(datetime.datetime.now()).replace(":", "_")
            now = datetime.datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
            filename =  os.getcwd() + '\\Guides\\guide_' + now + '.json'
            #print filename

            opener = urllib2.build_opener()
            #opener.addheaders = [('User-Agent', form.GetUserAgent())]
            remote_file = opener.open(url)
            #temp_filename = self.curDir + "\\" + "testfile"

            #testtest = remote_file.read()
            #print testtest

            f = open(filename, 'wb')
            # try:
            #     total_size = remote_file.info().getheader('Content-Length').strip()
            #     header = True
            # except AttributeError:
            #     header = False # a response doesn't always include the "Content-Length" header
                #form.setEnabled(True)
                #self.enableButtons()

            # if header:
            #     total_size = int(total_size)

            # bytes_so_far = 0

            while True:
                buffer = remote_file.read(8192)
                if not buffer:
                    #sys.stdout.write('\n')
                    break

                #bytes_so_far += len(buffer)
                f.write(buffer)
            f.close()
            self.statusbar.showMessage('Download complete. (' + filename + ')')
            if self.dialogYesNo('Open downloaded guide', 'Open downloaded guide?'):
                self.curGuide = filename
                guideJson = self.readJson('Configs\config.json')
                guideJson['curGuide'] = self.curGuide
                self.writeJson(guideJson, 'Configs\config.json')
                self.guideLineEdit.setText(os.path.basename(self.curGuide))
                self.loadGuide(filename)
                # if not header:
                #     total_size = bytes_so_far # unknown size

                # percent = float(bytes_so_far) / total_size
                # percent = round(percent*100, 2)
                # sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
                #form.progressBar.setValue(percent)
                # form.statusbar.showMessage("Downloading " + filename + " " + str(percent) + "%")
                # if percent == 100.00:
                #     form.statusbar.showMessage("Download " + filename + " complete")
            #self.enableButtons()
        except Exception, e:
            self.tabWidget.hide()
            self.statusbar.showMessage("Error in downloading guide from GitHub: " + str(e))

class aboutDialog(QtGui.QDialog, GUIAbout.Ui_Dialog):
    def __init__(self):
        global version
        global link
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.linkLabel.linkActivated.connect(self.openURL)
        self.versionLabel.setText("v." + version)
        self.linkLabel.setText(link)
        pic = self.picLabel
        pic.setPixmap(QtGui.QPixmap(":todo-icon32.png"))

    def openURL(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))


def main():
    app = QtGui.QApplication(sys.argv)
    appIco = QtGui.QIcon()
    appIco.addFile(':todo-icon16.png', QtCore.QSize(16,16))
    appIco.addFile(':todo-icon32.png', QtCore.QSize(32,32))
    app.setWindowIcon(appIco)
    form = POE_fast_leveling_guideApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()




