# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
#import res.res
import sys
import re
import os
from json import load
from json import loads
import json
#import modules.DPSCalc as DPSCalcModule
import generated.form_main as GUIMain
#import generated.about as GUIAbout
from Tkinter import Tk
import ctypes


myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

form = None
formAbout = None
version = '0.9.0'
link = '<a href="https://github.com/Doberm4n/POEWeaponDPSCalculator">Github</a>'


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



        self.loadConfig()


    def buttonstest(self, tab, index):
        print str(tab) + " " + str(index)


    def loadConfig(self):
        with open('Configs\config.json') as data_file:
            guideJson = load(data_file)
        if guideJson['curGuide']:
            print "Yes"
            self.curGuide = os.path.basename(guideJson['curGuide'])
            self.guideLineEdit.setText(self.curGuide)
            self.curDir = os.path.dirname(guideJson['curGuide'])
            self.loadGuide(guideJson["curGuide"])
        else:
            self.curDir = ""
            self.curGuide = ""
            print "No"

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
            with open('Configs\config.json') as data_file:
                guideJson = load(data_file)
                guideJson['curGuide'] = self.curGuide
            with open('Configs\config.json', 'w') as outfile:
                    json.dump(guideJson, outfile)

            self.guideLineEdit.setText(os.path.basename(self.curGuide))
            self.clearGuide()
            self.loadGuide(self.curGuide)


    def prepareGui(self):

        self.tabWidget.hide()
        tabStylesheet = " QTabBar:tab {color: green; }"
        disabledTabStylesheet = "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;}"

        self.groupBoxes = [self.groupBox_1, self.groupBox_2, self.groupBox_3, self.groupBox_4, self.groupBox_5, self.groupBox_6, self.groupBox_7, self.groupBox_8, self.groupBox_9, self.groupBox_10]
        self.gridLayouts = [self.gridLayout_1, self.gridLayout_2, self.gridLayout_3, self.gridLayout_4, self.gridLayout_5, self.gridLayout_6, self.gridLayout_7, self.gridLayout_8, self.gridLayout_9, self.gridLayout_10]
        self.scrollAreas = [self.scrollArea_1, self.scrollArea_2, self.scrollArea_3, self.scrollArea_4, self.scrollArea_5, self.scrollArea_6, self.scrollArea_7, self.scrollArea_8, self.scrollArea_9, self.scrollArea_10]
        self.scrollAreaWidgetContents = [self.scrollAreaWidgetContents_1, self.scrollAreaWidgetContents_2, self.scrollAreaWidgetContents_3, self.scrollAreaWidgetContents_4, self.scrollAreaWidgetContents_5, self.scrollAreaWidgetContents_6, self.scrollAreaWidgetContents_7, self.scrollAreaWidgetContents_8, self.scrollAreaWidgetContents_9, self.scrollAreaWidgetContents_10]

        self.font = QtGui.QFont()
        self.font.setFamily(_fromUtf8("Verdana"))
        self.font.setPointSize(8)

        self.tabWidget.setStyleSheet(tabStylesheet)

        for tabs in range (10):
            self.gridLayouts[tabs].setColumnStretch(0, 1)
            self.gridLayouts[tabs].setVerticalSpacing(2)
            self.scrollAreas[tabs].setGeometry(QtCore.QRect(5, 6, 986, 691))
            self.scrollAreaWidgetContents[tabs].setGeometry(QtCore.QRect(0, 0, 984, 689))
            self.groupBoxes[tabs].setTitle(_translate("MainWindow", "Act " + str(tabs +1 ) + " progress", None))

            #self.tabWidget.setTabEnabled(tabs, False)
            self.tabWidget.setStyleSheet(disabledTabStylesheet)


    def loadGuide(self, guide):

        with open(guide) as data_file:
                guideJson = load(data_file)

                #guideJson['curGuide'] = self.curGuide

        text = []
        completedStylesheet = "QPushButton:!enabled {color: green; text-align: left; }"
        uncompletedStylesheet = "QPushButton {text-align: left; font-weight: 1bold }"
        uncompletedBordersStylesheet = """
        QPushButton {
        border: 1px solid grey;
        background-color: white;
        padding: 5;
        }
        QPushButton:pressed {
        background-color: rgb(224, 0, 0);
        }
        QPushButton:hover {
        background-color: grey;
        }
        """
        completedBordersStylesheet = """
        QPushButton:!enabled {
        border: 1px solid grey;
        background-color: white;
        padding: 5;
        }
        QPushButton:pressed {
        background-color: rgb(224, 0, 0);
        }
        QPushButton:hover {
        background-color: rgb(235, 235, 235);
        }
        """



        self.buttonsText = {}
        self.buttonsComplete = {}



        # self.buttonsText[0,1] = 1
        # self.buttonsText[1,0] = 2
        # print self.buttonsText[0,1]
        # print self.buttonsText[1,0]
        self.tabWidget.show()
        # palette = QtGui.QPalette
        # palette.setColor(QtGui.QPalette.Shadow, QtGui.QColor('red'))
        for tabs in range (10):
            guideActKey = 'act_' + str(tabs + 1)
            if not guideJson['guide'][guideActKey]['text']:
                break
            for i in range (len(guideJson['guide'][guideActKey]['text'])):
                #print str(len(guideAct))
                #self.buttonsText.append(tabs, i)
                #self.buttonsComplete.append(tabs, i)
                #self.buttons.append(QtGui.QPushButton(self.groupBox, text=_fromUtf8("pushButton_" + str(i)),command=lambda i=i: self.buttonstest(i)))
                self.buttonsText[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
                self.buttonsComplete[tabs, i] = QtGui.QPushButton(self.groupBoxes[tabs])
                self.buttonsText[tabs, i].setObjectName(_fromUtf8("pushButton_" + str(i)))
                self.buttonsComplete[tabs, i].setObjectName(_fromUtf8("pushButton_" + str(i)))
                self.buttonsText[tabs, i].setText(_translate("MainWindow", "PushButton", None))
                self.buttonsComplete[tabs, i].setText(_translate("MainWindow", "PushButton", None))


                self.buttonsText[tabs, i].setFont(self.font)
                self.buttonsComplete[tabs, i].setFont(self.font)

                #self.buttonsText[tabs, i].setFlat(True)
                #self.buttonsComplete[tabs, i].setFlat(True)

                #self.buttons[i].setFlat(True)
                self.buttonsText[tabs, i].setStyleSheet(completedStylesheet + uncompletedStylesheet + uncompletedBordersStylesheet + completedBordersStylesheet)
                #self.buttonsText[tabs, i].setStyleSheet()
                #self.buttons[i].Palette(palette)
                self.buttonsText[tabs, i].setEnabled(False)
                #self.formLayout.setWidget(i, QtGui.QFormLayout.LabelRole, self.buttons[i])
                self.gridLayouts[tabs].addWidget(self.buttonsText[tabs, i], i, 0, 1, 1)
                self.gridLayouts[tabs].addWidget(self.buttonsComplete[tabs, i], i, 1, 1, 1)
                #self.gridLayout.addWidget(self.buttons[i], 2, 0, 1, 1)
                # print j
                #a = None
                self.buttonsText[tabs, i].setText("  " + guideJson['guide'][guideActKey]['text'][i])
                self.buttonsComplete[tabs, i].setText("Reset")

                self.buttonsText[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonstest(tabs, i))
                self.buttonsComplete[tabs, i].clicked.connect(lambda clicked, tabs=tabs, i=i: self.buttonstest(tabs, i))
                #print

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


    def clearGuide(self):



        print ""






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
    # appIco = QtGui.QIcon()
    # appIco.addFile(':Device-blockdevice-cubes-icon16.png', QtCore.QSize(16,16))
    # appIco.addFile(':Device-blockdevice-cubes-icon32.png', QtCore.QSize(32,32))
    # app.setWindowIcon(appIco)
    form = POE_fast_leveling_guideApp()
    #form.setWindowFlags(QtCore.Qt.WindowTitleHint)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()




