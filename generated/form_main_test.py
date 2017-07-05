# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main_test.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1092, 825)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.openGuidePushButton = QtGui.QPushButton(self.centralwidget)
        self.openGuidePushButton.setObjectName(_fromUtf8("openGuidePushButton"))
        self.verticalLayout_2.addWidget(self.openGuidePushButton)
        self.guideLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.guideLineEdit.setEnabled(False)
        self.guideLineEdit.setObjectName(_fromUtf8("guideLineEdit"))
        self.verticalLayout_2.addWidget(self.guideLineEdit)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGuide = QtGui.QMenu(self.menubar)
        self.menuGuide.setObjectName(_fromUtf8("menuGuide"))
        self.menuReset_progress = QtGui.QMenu(self.menuGuide)
        self.menuReset_progress.setObjectName(_fromUtf8("menuReset_progress"))
        self.menuComplete_progress = QtGui.QMenu(self.menuGuide)
        self.menuComplete_progress.setObjectName(_fromUtf8("menuComplete_progress"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuActionOpen = QtGui.QAction(MainWindow)
        self.menuActionOpen.setObjectName(_fromUtf8("menuActionOpen"))
        self.actionAct_1 = QtGui.QAction(MainWindow)
        self.actionAct_1.setObjectName(_fromUtf8("actionAct_1"))
        self.actionAct_2 = QtGui.QAction(MainWindow)
        self.actionAct_2.setObjectName(_fromUtf8("actionAct_2"))
        self.actionAct_3 = QtGui.QAction(MainWindow)
        self.actionAct_3.setObjectName(_fromUtf8("actionAct_3"))
        self.actionAct_4 = QtGui.QAction(MainWindow)
        self.actionAct_4.setObjectName(_fromUtf8("actionAct_4"))
        self.actionAct_5 = QtGui.QAction(MainWindow)
        self.actionAct_5.setObjectName(_fromUtf8("actionAct_5"))
        self.actionAct_6 = QtGui.QAction(MainWindow)
        self.actionAct_6.setObjectName(_fromUtf8("actionAct_6"))
        self.actionAct_7 = QtGui.QAction(MainWindow)
        self.actionAct_7.setObjectName(_fromUtf8("actionAct_7"))
        self.actionAct_8 = QtGui.QAction(MainWindow)
        self.actionAct_8.setObjectName(_fromUtf8("actionAct_8"))
        self.actionAct_9 = QtGui.QAction(MainWindow)
        self.actionAct_9.setObjectName(_fromUtf8("actionAct_9"))
        self.actionAct_10 = QtGui.QAction(MainWindow)
        self.actionAct_10.setObjectName(_fromUtf8("actionAct_10"))
        self.actionReset_All = QtGui.QAction(MainWindow)
        self.actionReset_All.setObjectName(_fromUtf8("actionReset_All"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCreate_empty_guide_file = QtGui.QAction(MainWindow)
        self.actionCreate_empty_guide_file.setObjectName(_fromUtf8("actionCreate_empty_guide_file"))
        self.actionImport_text_to_guide = QtGui.QAction(MainWindow)
        self.actionImport_text_to_guide.setObjectName(_fromUtf8("actionImport_text_to_guide"))
        self.actionComplete_All = QtGui.QAction(MainWindow)
        self.actionComplete_All.setObjectName(_fromUtf8("actionComplete_All"))
        self.menuReset_progress.addAction(self.actionReset_All)
        self.menuComplete_progress.addAction(self.actionComplete_All)
        self.menuGuide.addAction(self.menuActionOpen)
        self.menuGuide.addAction(self.menuReset_progress.menuAction())
        self.menuGuide.addAction(self.menuComplete_progress.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionCreate_empty_guide_file)
        self.menuTools.addAction(self.actionImport_text_to_guide)
        self.menubar.addAction(self.menuGuide.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PoE Leveling Guide", None))
        self.openGuidePushButton.setText(_translate("MainWindow", "Open guide", None))
        self.label.setText(_translate("MainWindow", "Progress:", None))
        self.menuGuide.setTitle(_translate("MainWindow", "Guide", None))
        self.menuReset_progress.setTitle(_translate("MainWindow", "Reset progress", None))
        self.menuComplete_progress.setTitle(_translate("MainWindow", "Complete progress", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuActionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionAct_1.setText(_translate("MainWindow", "Act 1", None))
        self.actionAct_2.setText(_translate("MainWindow", "Act 2", None))
        self.actionAct_3.setText(_translate("MainWindow", "Act 3", None))
        self.actionAct_4.setText(_translate("MainWindow", "Act 4", None))
        self.actionAct_5.setText(_translate("MainWindow", "Act 5", None))
        self.actionAct_6.setText(_translate("MainWindow", "Act 6", None))
        self.actionAct_7.setText(_translate("MainWindow", "Act 7", None))
        self.actionAct_8.setText(_translate("MainWindow", "Act 8", None))
        self.actionAct_9.setText(_translate("MainWindow", "Act 9", None))
        self.actionAct_10.setText(_translate("MainWindow", "Act 10", None))
        self.actionReset_All.setText(_translate("MainWindow", "Reset all", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionCreate_empty_guide_file.setText(_translate("MainWindow", "Create guide file", None))
        self.actionImport_text_to_guide.setText(_translate("MainWindow", "Import text to guide", None))
        self.actionComplete_All.setText(_translate("MainWindow", "Complete all", None))

