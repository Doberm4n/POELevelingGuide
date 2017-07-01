# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
#import res.res
import sys
import re
import os
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
        # self.pasteButton.clicked.connect(self.pasteFromClipboard)
        # self.actionAbout.triggered.connect(self.showAbout)
        # tab1 = QtGui.QScrollArea()
        # tab1.setWidget(QtGui.QWidget())
        # self.scrollArea.setWidget(QtGui.QWidget())
        # self.verticalLayout = QtGui.QVBoxLayout(tab1.widget())
        #global j

        completedStylesheet = "QPushButton:!enabled {color: green; }"


        self.buttonsText = []
        self.buttonsComplete = []

        # palette = QtGui.QPalette
        # palette.setColor(QtGui.QPalette.Shadow, QtGui.QColor('red'))
        for i in range (55):
            self.buttonsText.append(i)
            self.buttonsComplete.append(i)
            #self.buttons.append(QtGui.QPushButton(self.groupBox, text=_fromUtf8("pushButton_" + str(i)),command=lambda i=i: self.buttonstest(i)))






            self.buttonsText[i] = QtGui.QPushButton(self.groupBox)
            self.buttonsComplete[i] = QtGui.QPushButton(self.groupBox)
            self.buttonsText[i].setObjectName(_fromUtf8("pushButton_" + str(i)))
            self.buttonsComplete[i].setObjectName(_fromUtf8("pushButton_" + str(i)))
            self.buttonsText[i].setText(_translate("MainWindow", "PushButton", None))
            self.buttonsComplete[i].setText(_translate("MainWindow", "PushButton", None))
            #self.buttons[i].setFlat(True)
            self.buttonsText[i].setStyleSheet(completedStylesheet)
            #self.buttons[i].Palette(palette)
            self.buttonsText[i].setEnabled(False)
            #self.formLayout.setWidget(i, QtGui.QFormLayout.LabelRole, self.buttons[i])
            self.gridLayout.addWidget(self.buttonsText[i], i, 0, 1, 1)
            self.gridLayout.addWidget(self.buttonsComplete[i], i, 1, 1, 1)
            #self.gridLayout.addWidget(self.buttons[i], 2, 0, 1, 1)
            # print j
            #a = None

            self.buttonsText[i].clicked.connect(lambda clicked, i=i: self.buttonstest(i))
            self.buttonsComplete[i].clicked.connect(lambda clicked, i=i: self.buttonstest(i))
            #print




        self.gridLayout.setColumnStretch(0, 1)

    def buttonstest(self, index):
        print str(index)


    #     self.btn=[]
    #     for x in range(5) :
    #        self.btn.append(x)
    #        self.btn[x]= qg.QPushButton(self)
    #        self.btn[x].setText('this is btn number{0}'.format(x))
    #        self.btn[x].setGeometry(qc.QRect(0,100+(x*20), 100,20))
    #        self.btn[x].clicked.connect(lambda : self.notifyMe(x))

    # def notifyMe(self,index):
    #     print index

    # def pasteFromClipboard(self):
    #     temp = Tk()
    #     try:
    #         clipboardData = temp.selection_get(selection = "CLIPBOARD")
    #         self.POEWeaponDataTextEdit.setPlainText(clipboardData)
    #     except:
    #         pass
    #     self.calcDPS()


    # def calcDPS(self):
    #     self.POEDPSCalc = DPSCalcModule.DPSCalc()
    #     unicodeData = unicode(self.POEWeaponDataTextEdit.toPlainText())
    #     if self.POEDPSCalc.Calc(unicodeData):
    #         self.populateData()
    #     else:
    #         self.POEWeaponDataTextEdit.setPlainText('Wrong data')
    #         self.resetData()


#     def populateData(self):
#         self.pDPSLabel.setText("pDPS: " + str(self.POEDPSCalc.valuePhysical))
#         self.eDPSLabel.setText("eDPS: " + str(self.POEDPSCalc.valueElemental))
#         self.cDPSLabel.setText("cDPS: " + str(self.POEDPSCalc.valueChaos))
#         self.fireDPSLabel.setText(str(self.POEDPSCalc.valueFire))
#         self.lightningDPSLabel.setText(str(self.POEDPSCalc.valueLightning))
#         self.coldDPSLabel.setText(str(self.POEDPSCalc.valueCold))
#         self.totalDPSLabel.setText(str(self.POEDPSCalc.totalDPS))


#     def resetData(self):
#         self.pDPSLabel.setText("pDPS: 0")
#         self.eDPSLabel.setText("eDPS: 0")
#         self.cDPSLabel.setText("cDPS: 0")
#         self.fireDPSLabel.setText("0")
#         self.lightningDPSLabel.setText("0")
#         self.coldDPSLabel.setText("0")
#         self.totalDPSLabel.setText("0")


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
    form.setWindowFlags(QtCore.Qt.WindowTitleHint)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()




