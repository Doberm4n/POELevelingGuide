# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main.ui'
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
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea_1 = QtGui.QScrollArea(self.tab_1)
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollArea_1.setObjectName(_fromUtf8("scrollArea_1"))
        self.scrollAreaWidgetContents_1 = QtGui.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 1048, 631))
        self.scrollAreaWidgetContents_1.setObjectName(_fromUtf8("scrollAreaWidgetContents_1"))
        self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContents_1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBox_1 = QtGui.QGroupBox(self.scrollAreaWidgetContents_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_1.sizePolicy().hasHeightForWidth())
        self.groupBox_1.setSizePolicy(sizePolicy)
        self.groupBox_1.setObjectName(_fromUtf8("groupBox_1"))
        self.gridLayout_1 = QtGui.QGridLayout(self.groupBox_1)
        self.gridLayout_1.setVerticalSpacing(2)
        self.gridLayout_1.setObjectName(_fromUtf8("gridLayout_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_1)
        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_1)
        self.verticalLayout.addWidget(self.scrollArea_1)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.scrollArea_4 = QtGui.QScrollArea(self.tab_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.formLayout_4 = QtGui.QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_4)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.addWidget(self.scrollArea_4)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.scrollArea_5 = QtGui.QScrollArea(self.tab_5)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName(_fromUtf8("scrollArea_5"))
        self.scrollAreaWidgetContents_5 = QtGui.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_5.setObjectName(_fromUtf8("scrollAreaWidgetContents_5"))
        self.formLayout_5 = QtGui.QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_5)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_6.addWidget(self.scrollArea_5)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.scrollArea_6 = QtGui.QScrollArea(self.tab_6)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName(_fromUtf8("scrollArea_6"))
        self.scrollAreaWidgetContents_6 = QtGui.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_6.setObjectName(_fromUtf8("scrollAreaWidgetContents_6"))
        self.formLayout_6 = QtGui.QFormLayout(self.scrollAreaWidgetContents_6)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_6)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_7.addWidget(self.scrollArea_6)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_7)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea_7 = QtGui.QScrollArea(self.tab_7)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName(_fromUtf8("scrollArea_7"))
        self.scrollAreaWidgetContents_7 = QtGui.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_7.setObjectName(_fromUtf8("scrollAreaWidgetContents_7"))
        self.formLayout_7 = QtGui.QFormLayout(self.scrollAreaWidgetContents_7)
        self.formLayout_7.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.groupBox_7 = QtGui.QGroupBox(self.scrollAreaWidgetContents_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setVerticalSpacing(2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_7)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_8.addWidget(self.scrollArea_7)
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.scrollArea_8 = QtGui.QScrollArea(self.tab_8)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName(_fromUtf8("scrollArea_8"))
        self.scrollAreaWidgetContents_8 = QtGui.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_8.setObjectName(_fromUtf8("scrollAreaWidgetContents_8"))
        self.formLayout_8 = QtGui.QFormLayout(self.scrollAreaWidgetContents_8)
        self.formLayout_8.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.groupBox_8 = QtGui.QGroupBox(self.scrollAreaWidgetContents_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_8.setVerticalSpacing(2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_8)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_9.addWidget(self.scrollArea_8)
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_9)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.scrollArea_9 = QtGui.QScrollArea(self.tab_9)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName(_fromUtf8("scrollArea_9"))
        self.scrollAreaWidgetContents_9 = QtGui.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_9.setObjectName(_fromUtf8("scrollAreaWidgetContents_9"))
        self.formLayout_9 = QtGui.QFormLayout(self.scrollAreaWidgetContents_9)
        self.formLayout_9.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.groupBox_9 = QtGui.QGroupBox(self.scrollAreaWidgetContents_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_9.setVerticalSpacing(2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.formLayout_9.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_9)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_10.addWidget(self.scrollArea_9)
        self.tabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_10)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.scrollArea_10 = QtGui.QScrollArea(self.tab_10)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName(_fromUtf8("scrollArea_10"))
        self.scrollAreaWidgetContents_10 = QtGui.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 98, 51))
        self.scrollAreaWidgetContents_10.setObjectName(_fromUtf8("scrollAreaWidgetContents_10"))
        self.formLayout_10 = QtGui.QFormLayout(self.scrollAreaWidgetContents_10)
        self.formLayout_10.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.groupBox_10 = QtGui.QGroupBox(self.scrollAreaWidgetContents_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_10.setVerticalSpacing(2)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_10)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.verticalLayout_11.addWidget(self.scrollArea_10)
        self.tabWidget.addTab(self.tab_10, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGuide = QtGui.QMenu(self.menubar)
        self.menuGuide.setObjectName(_fromUtf8("menuGuide"))
        self.menuReset_progress = QtGui.QMenu(self.menuGuide)
        self.menuReset_progress.setObjectName(_fromUtf8("menuReset_progress"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
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
        self.menuReset_progress.addAction(self.actionAct_1)
        self.menuReset_progress.addAction(self.actionAct_2)
        self.menuReset_progress.addAction(self.actionAct_3)
        self.menuReset_progress.addAction(self.actionAct_4)
        self.menuReset_progress.addAction(self.actionAct_5)
        self.menuReset_progress.addAction(self.actionAct_6)
        self.menuReset_progress.addAction(self.actionAct_7)
        self.menuReset_progress.addAction(self.actionAct_8)
        self.menuReset_progress.addAction(self.actionAct_9)
        self.menuReset_progress.addAction(self.actionAct_10)
        self.menuReset_progress.addAction(self.actionReset_All)
        self.menuGuide.addAction(self.menuActionOpen)
        self.menuGuide.addAction(self.menuReset_progress.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuGuide.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PoE Leveling Guide", None))
        self.openGuidePushButton.setText(_translate("MainWindow", "Open guide", None))
        self.label.setText(_translate("MainWindow", "Act progress:", None))
        self.groupBox_1.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Act 1", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Act 2", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Act 3", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Act 4", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Act 5", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Act 6", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Act 7", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Act 8", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Act 9", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Act 10", None))
        self.menuGuide.setTitle(_translate("MainWindow", "Guide", None))
        self.menuReset_progress.setTitle(_translate("MainWindow", "Reset progress", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
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
        self.actionReset_All.setText(_translate("MainWindow", "Reset All", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

