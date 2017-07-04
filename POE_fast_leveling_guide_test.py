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
import res.res
#import modules.DPSCalc as DPSCalcModule
import generated.form_main_test as GUIMain
import generated.form_about as GUIAbout
#import generated.about as GUIAbout
from Tkinter import Tk
import ctypes


myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

form = None
formAbout = None
version = '0.9.0'
link = '<a href="https://github.com/Doberm4n/POELevelingGuide">Github</a>'


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
        # self.pasteButton.clicked.connect(self.pasteFromClipboard)
        # self.actionAbout.triggered.connect(self.showAbout)
        # tab1 = QtGui.QScrollArea()
        # tab1.setWidget(QtGui.QWidget())
        # self.scrollArea.setWidget(QtGui.QWidget())
        # self.verticalLayout = QtGui.QVBoxLayout(tab1.widget())
        #global j

        self.openGuidePushButton.clicked.connect(self.browseGuide)
        self.actionReset_All.triggered.connect(self.menuActionResetAll)

        self.menuActionOpen.triggered.connect(self.browseGuide)

        self.actionAbout.triggered.connect(self.showAbout)




        self.loadConfig()


    def buttonsTextClick(self, tab, index):
        print str(tab) + " " + str(index)
        if self.buttonsText[tab, index].isEnabled():
            self.buttonsText[tab, index].setEnabled(False)
            #self.buttonsText[tab, index].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
            #with open(self.curGuide) as data_file:
            guideJson = self.readJson(self.curGuide) #load(data_file)
            guideActKey = 'act_' + str(tab + 1)
            guideJson['guide'][guideActKey]['text'][index]['isCompleted'] = True

            #temp = guideJson
            # with open(self.curGuide, 'w') as outfile:
            #     json.dump(temp, outfile)
            self.writeJson(guideJson, self.curGuide)
        #     print 'dump'

    def buttonsCompleteClick(self, tab, index):
        print str(tab) + " " + str(index)
        if not self.buttonsText[tab, index].isEnabled():
            self.buttonsText[tab, index].setEnabled(True)
            self.buttonsText[tab, index].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)

            #with open(self.curGuide) as data_file:
            guideJson = self.readJson(self.curGuide) #load(data_file)
            guideActKey = 'act_' + str(tab + 1)
            guideJson['guide'][guideActKey]['text'][index]['isCompleted'] = False

            #temp = guideJson
            # with open(self.curGuide, 'w') as outfile:
            #     json.dump(temp, outfile)
            self.writeJson(guideJson, self.curGuide)

    def menuActionResetClick(self, tab, count):
        #print "resetClick"
        if self.dialogYesNo('Reset', 'Reset act ' + str(tab + 1) + ' progress  \n\nAre you sure?'):
            print str(tab) + str(count)
            guideJson = self.readJson(self.curGuide) #load(data_file)
            guideActKey = 'act_' + str(tab + 1)
            for i in range (count + 1):
                if not self.buttonsText[tab, i].isEnabled():
                    self.buttonsText[tab, i].setEnabled(True)
                    self.buttonsText[tab, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)

                    #with open(self.curGuide) as data_file:


                    guideJson['guide'][guideActKey]['text'][i]['isCompleted'] = False

                    #temp = guideJson
                    # with open(self.curGuide, 'w') as outfile:
                    #     json.dump(temp, outfile)
            #print "i= " + str(i)
            self.writeJson(guideJson, self.curGuide)

    def menuActionResetAll(self):
        if self.dialogYesNo('Reset all', "Reset all progress\n\nAre you sure?"):
            guideJson = self.readJson(self.curGuide) #load(data_file)
            for tabs in range (10):
                    #print "jfklsdfjlkds"
                    for widget in self.groupBoxes[tabs].children():
                        #print widget.objectName()
                        if isinstance(widget, QtGui.QPushButton):
                            if "guideStringPushButton_" in widget.objectName():
                                if not widget.isEnabled():
                                    widget.setEnabled(True)
                            print "linedit: %s  - %s" %(widget.objectName(),widget.text())
                            #widget.deleteLater()

                    guideActKey = 'act_' + str(tabs + 1)
                    for i in range (len(guideJson['guide'][guideActKey]['text'])):
                        if guideJson['guide'][guideActKey]['text'][i]['isCompleted']:
                            guideJson['guide'][guideActKey]['text'][i]['isCompleted'] = False
            self.writeJson(guideJson, self.curGuide)

    def dialogYesNo(self, title, question):
        result = QtGui.QMessageBox.question(self, title, question, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            return True
        else:
            print False

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

    def loadConfig(self):
        #try:
            # with open('Configs\config.json') as data_file:
            guideJson = self.readJson('Configs\config.json') #load(data_file)
            if guideJson['curGuide']:
                print "Yes"
                self.curGuide = guideJson["curGuide"]
                curGuideFilename = os.path.basename(self.curGuide)
                self.guideLineEdit.setText(curGuideFilename)
                self.curDir = os.path.dirname(self.curGuide)

                self.loadGuide(self.curGuide)
            else:
                self.curDir = ""
                self.curGuide = ""
                print "No"
        # except Exception, e:
        #      print "Error: " + str(e)

    def loadGuide(self, guide):
        print ""

    def browseGuide(self):
        # with open('Configs\config.json') as data_file:
        #     guideJson = load(data_file)
        # if os.path.dirname(guideJson['curGuide']):
        #     guideDir = os.path.dirname(guideJson['curGuide'])
        # else:
        #     guideDir = ""
        self.curGuide = str(QtGui.QFileDialog.getOpenFileName(self, "Select guide", filter='*.json', directory=self.curDir))
        if self.curGuide:
            # open guide and test valid
            #with open('Configs\config.json') as data_file:
            guideJson = self.readJson('Configs\config.json') #load(data_file)
            guideJson['curGuide'] = self.curGuide



            # with open('Configs\config.json', 'w') as outfile:
            #         json.dump(guideJson, outfile)
            self.writeJson(guideJson, 'Configs\config.json')

            self.guideLineEdit.setText(os.path.basename(self.curGuide))
            self.clearGuide()
            self.loadGuide(self.curGuide)


    def prepareGui(self):

        self.tabWidget.hide()
        self.completedStylesheet = "QPushButton:!enabled {font-family: Verdana; font-size: 8pt; color: green; text-align: left;  padding: 5;}"
        self.uncompletedStylesheet = "QPushButton:enabled {font-family: Verdana; font-size: 8pt; text-align: left; border: 1px solid grey; background-color: white; padding: 5; font-weight: 1bold } QPushButton:hover {background-color: rgb(187, 255, 177);}"
        #self.tabsylesheet = " QTabBar:tab {color: green; }"
        #self.disabledtabsylesheet = "QTabBar::tab::disabled {width: 1; height: 0; margin: 0; padding: 0; border: none;}"
        self.disabledtabsylesheet = ""

        # self.groupBoxes_original = [self.groupBox_1, self.groupBox_2, self.groupBox_3, self.groupBox_4, self.groupBox_5, self.groupBox_6, self.groupBox_7, self.groupBox_8, self.groupBox_9, self.groupBox_10]
        # self.gridLayouts_original = [self.gridLayout_1, self.gridLayout_2, self.gridLayout_3, self.gridLayout_4, self.gridLayout_5, self.gridLayout_6, self.gridLayout_7, self.gridLayout_8, self.gridLayout_9, self.gridLayout_10]
        # self.scrollAreas_original = [self.scrollArea_1, self.scrollArea_2, self.scrollArea_3, self.scrollArea_4, self.scrollArea_5, self.scrollArea_6, self.scrollArea_7, self.scrollArea_8, self.scrollArea_9, self.scrollArea_10]
        # self.scrollAreaWidgetContents_original = [self.scrollAreaWidgetContents_1, self.scrollAreaWidgetContents_2, self.scrollAreaWidgetContents_3, self.scrollAreaWidgetContents_4, self.scrollAreaWidgetContents_5, self.scrollAreaWidgetContents_6, self.scrollAreaWidgetContents_7, self.scrollAreaWidgetContents_8, self.scrollAreaWidgetContents_9, self.scrollAreaWidgetContents_10]
        self.actionsReset = [self.actionAct_1, self.actionAct_2, self.actionAct_3, self.actionAct_4, self.actionAct_5, self.actionAct_6, self.actionAct_7, self.actionAct_8, self.actionAct_9, self.actionAct_10, self.actionReset_All]

        # self.font = QtGui.QFont()
        # self.font.setFamily(_fromUtf8("Verdana"))
        # self.font.setPointSize(8)

        #self.tabWidget.setStyleSheet(self.tabsylesheet)

        # for tabs in range (10):
        #     self.gridLayouts_original[tabs].setColumnStretch(0, 1)
        #     self.gridLayouts_original[tabs].setVerticalSpacing(2)


        #     #self.scrollAreas_original[tabs].setGeometry(QtCore.QRect(5, 6, 986, 691))
        #     #self.scrollAreaWidgetContents_original[tabs].setGeometry(QtCore.QRect(0, 0, 984, 689))


        #     self.groupBoxes_original[tabs].setTitle(_translate("MainWindow", "Act " + str(tabs +1 ) + " progress", None))

            #
        self.tabWidget.setStyleSheet(self.disabledtabsylesheet)

    def clearButtons(self):
        for tabs in range (10):
                #print "jfklsdfjlkds"
                for widget in self.groupBoxes_original[tabs].children():
                    #print widget.objectName()
                    if isinstance(widget, QtGui.QPushButton):
                        #print "linedit: %s  - %s" %(widget.objectName(),widget.text())
                        widget.deleteLater()


    def clearTabs(self):
        # for widget in self.tabWidget.children():
        #             #print widget.objectName()
        #             if isinstance(widget, QtGui.QWidget):
        #                 #print "linedit: %s  - %s" %(widget.objectName(),widget.text())
        #                 widget.deleteLater()

        tabs_count = self.tabWidget.count()
        print "tabs_count = " + str(tabs_count)
        #print self.tabWidget.widget(0).objectName()
        for i in range (tabs_count -1, -1, -1):
            #
            self.tabWidget.widget(i).close()
            self.tabWidget.widget(i).deleteLater()
            self.tabWidget.removeTab(i)
            #del self.tabWidget.widget(i)
        gc.collect()

    def eventFilter(self, obj, event):
        #print "Event filter"
        if obj and not obj.isEnabled() and event.type() == QEvent.Wheel:
            #print "Event"
            newEvent = QtGui.QWheelEvent(obj.mapToParent(event.pos()), event.globalPos(),
                                   event.delta(), event.buttons(),
                                   event.modifiers(), event.orientation())
            QtGui.QApplication.instance().postEvent(obj.parent(), newEvent)
            #print "QEvent: " + str(event.type())
            return True

        return QObject.eventFilter(self, obj, event)

    def loadGuide(self, guide):
        #try:
            #with open(guide) as data_file:
            guideJson = self.readJson(guide) #load(data_file)

                    #guideJson['curGuide'] = self.curGuide

            text = []

            # self.uncompletedBordersStylesheet = """
            # QPushButton:enabled {



            # }
            # QPushButton:pressed {
            # background-color: rgb(224, 0, 0);
            # }

            # """
            # self.completedBordersStylesheet = """
            # QPushButton:!enabled {
            # 1border: 1px solid grey;
            # 1background-color: white;

            # }
            # QPushButton:pressed {
            # background-color: rgb(224, 0, 0);
            # }
            # QPushButton:hover {
            # background-color: rgb(235, 235, 235);
            # }
            # """
            # self.isGuideLoaded = True
            # if self.isGuideLoaded:

            #self.clearButtons()
            self.clearTabs()


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

            #tabs = 11


            # self.buttonsText[0,1] = 1
            # self.buttonsText[1,0] = 2
            # print self.buttonsText[0,1]
            # print self.buttonsText[1,0]
            #self.tabWidget.repaint()
            self.tabWidget.show()

            tabs_count = self.tabWidget.count()
            print "tabs_count init = " + str(tabs_count)

            # palette = QtGui.QPalette
            # palette.setColor(QtGui.QPalette.Shadow, QtGui.QColor('red'))
            tabsCount = len(guideJson['guide']['tabs'])
            for tabs in range (tabsCount):
                guideActKey = 'act_' + str(tabs + 1)
                if not guideJson['guide']['tabs'][tabs]['text']:
                    #self.tabWidget.setTabEnabled(tabs, False)
                    #self.tabWidget.setStyleSheet(self.disabledtabsylesheet)
                    print "tabs " + str(tabs)
                    #continue



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
                i = 0
                if textLength == 0:
                    print "Length = 0"
                    self.tabWidget.setTabEnabled(tabs, False)
                    tabs_count = self.tabWidget.count()
                    print "tabs_count = " + str(tabs_count)
                    #print self.tabWidget.widget(10).objectName()
                print "Length " + str(tabs) + " " + str(textLength)
                for i in range (textLength):
                    #print "i= " + str(i)
                    #if
                        #print ""
                        #break
                    #print str(len(guideJson['guide'][guideActKey]['text']))
                    #print str(len(guideAct))
                    #self.buttonsText.append(tabs, i)
                    #self.buttonsComplete.append(tabs, i)
                    #self.buttons.append(QtGui.QPushButton(self.groupBox, text=_fromUtf8("pushButton_" + str(i)),command=lambda i=i: self.buttonstest(i)))




                    #self.groupBoxes_original[tabs].setTitle(_translate("MainWindow", guideJson['guide']['tabs'][7]['name'] + " progress", None))

                    self.buttonsText[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
                    self.buttonsComplete[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
                    self.buttonsText[tabs, i].setObjectName(_fromUtf8("guideStringPushButton_" + str(i)))
                    self.buttonsComplete[tabs, i].setObjectName(_fromUtf8("guideStringPushButton_" + str(i)))
                    self.buttonsText[tabs, i].setText(_translate("MainWindow", "guideStringPushButton", None))
                    self.buttonsComplete[tabs, i].setText(_translate("MainWindow", "guideStringPushButton", None))

                    #self.buttonsText[tabs, i].setFont(self.font)
                    #self.buttonsComplete[tabs, i].setFont(self.font)

                    #self.buttonsText[tabs, i].setFlat(True)
                    #self.buttonsComplete[tabs, i].setFlat(True)

                    #self.buttons[i].setFlat(True)
                    #self.buttonsText[tabs, i].setStyleSheet('')
                    self.buttonsText[tabs, i].setStyleSheet(self.completedStylesheet + self.uncompletedStylesheet)
                    #self.buttonsText[tabs, i].setStyleSheet()
                    #self.buttons[i].Palette(palette)
                    #self.buttonsText[tabs, i].setEnabled(False)
                    #self.formLayout.setWidget(i, QtGui.QFormLayout.LabelRole, self.buttons[i])
                    self.gridLayouts[tabs].addWidget(self.buttonsText[tabs, i], i, 0, 1, 1)
                    self.gridLayouts[tabs].addWidget(self.buttonsComplete[tabs, i], i, 1, 1, 1)
                    #self.gridLayout.addWidget(self.buttons[i], 2, 0, 1, 1)
                    # print j
                    #a = None


                    tempString = guideJson['guide']['tabs'][tabs]['text'][i]['string']
                    #if  tempString.find(u'\u2022') >= 0:
                    if  tempString.find(u'\u25e6') >= 0:
                        tempString = "     " + tempString

                    self.buttonsText[tabs, i].setText(tempString)
                    self.buttonsText[tabs, i].setEnabled(not guideJson['guide']['tabs'][tabs]['text'][i]['isCompleted'])
                    #print str(tabs) + str(i)
                    self.buttonsText[tabs, i].installEventFilter(self)
                    #self.buttonsText[tabs, i].ItemIsSelectable = True
                    #self.buttonsText[tabs, i].ItemIsMovable = True

                    self.buttonsComplete[tabs, i].setText("Reset")

                    self.buttonsText[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonsTextClick(tabs, i))
                    self.buttonsComplete[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonsCompleteClick(tabs, i))

                #print "i= " + str(i)

                if self.actionsReset[tabs].triggered:
                    self.actionsReset[tabs].triggered.disconnect()
                self.actionsReset[tabs].triggered.connect(lambda clicked, tabs=tabs, i=i: self.menuActionResetClick(tabs, i))

                    #print
                    #self.buttonsText[tabs, i].deleteLater()
                    #self.gridLayouts[1].setColumnStretch(0, 1)
            #text.append(0)

            # methods = {'self.grid' + 'Layout': install1}

            # method_name = 'self.grid' + 'Layout' # set by the command line options
            # if method_name in methods:
            #     methods[method_name]() # + argument list of course


            #text[0] = eval('self.grid' + 'Layout')
            #text[0].setColumnStretch(0, 1)

            #self.gridLayout.setColumnStretch(0, 1)



            self.statusbar.clearMessage()

        # except Exception, e:
        #     self.tabWidget.hide()
        #     self.statusbar.showMessage("Error in loading guide: " + str(e))

    def clearGuide(self):



        print ""

    def showAbout(self):
        global formAbout
        formAbout = aboutDialog()
        formAbout.show()


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


#     def showAbout(self):
#         global formAbout
#         formAbout = aboutDialog()
#         formAbout.show()


# class aboutDialog(QtGui.QDialog, GUIAbout.Ui_Dialog):
#     def __init__(self):
#         global version
#         global link
#         super(self.__class__, self).__init__()
#         self.setupUi(self)
#         self.setWindowFlags(QtCore.Qt.WindowTitleHint)
#         self.linkLabel.linkActivated.connect(self.openURL)
#         self.versionLabel.setText("v." + version)
#         self.linkLabel.setText(link)
#         pic = self.picLabel
#         pic.setPixmap(QtGui.QPixmap(":Device-blockdevice-cubes-icon32.png"))


#     def openURL(self, linkStr):
#         QDesktopServices.openUrl(QUrl(linkStr))




def main():
    app = QtGui.QApplication(sys.argv)
    appIco = QtGui.QIcon()
    appIco.addFile(':todo-icon16.png', QtCore.QSize(16,16))
    appIco.addFile(':todo-icon32.png', QtCore.QSize(32,32))
    app.setWindowIcon(appIco)
    form = POE_fast_leveling_guideApp()
    #form.setWindowFlags(QtCore.Qt.WindowTitleHint)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()



