# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_about.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(370, 167)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(370, 167))
        Dialog.setMaximumSize(QtCore.QSize(370, 167))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 130, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.labelAbout = QtGui.QLabel(Dialog)
        self.labelAbout.setGeometry(QtCore.QRect(60, 15, 301, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelAbout.setFont(font)
        self.labelAbout.setObjectName(_fromUtf8("labelAbout"))
        self.versionLabel = QtGui.QLabel(Dialog)
        self.versionLabel.setGeometry(QtCore.QRect(60, 45, 301, 16))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.linkLabel = QtGui.QLabel(Dialog)
        self.linkLabel.setGeometry(QtCore.QRect(60, 70, 301, 16))
        self.linkLabel.setObjectName(_fromUtf8("linkLabel"))
        self.picLabel = QtGui.QLabel(Dialog)
        self.picLabel.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.labelAbout.setText(_translate("Dialog", "Leveling Guide for Path of Exile", None))
        self.versionLabel.setText(_translate("Dialog", "v.0.9", None))
        self.linkLabel.setText(_translate("Dialog", "link", None))
        self.picLabel.setText(_translate("Dialog", "TextLabel", None))

