# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Tue Dec 18 14:56:29 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(487, 597)
        self.centralWidget = QtGui.QWidget(Calculator)
        self.centralWidget.setObjectName("centralWidget")
        self.val_1 = QtGui.QPushButton(self.centralWidget)
        self.val_1.setGeometry(QtCore.QRect(70, 150, 71, 71))
        self.val_1.setObjectName("val_1")
        self.val_2 = QtGui.QPushButton(self.centralWidget)
        self.val_2.setGeometry(QtCore.QRect(160, 150, 71, 71))
        self.val_2.setObjectName("val_2")
        self.val_3 = QtGui.QPushButton(self.centralWidget)
        self.val_3.setGeometry(QtCore.QRect(250, 150, 71, 71))
        self.val_3.setObjectName("val_3")
        self.val_4 = QtGui.QPushButton(self.centralWidget)
        self.val_4.setGeometry(QtCore.QRect(70, 240, 71, 71))
        self.val_4.setObjectName("val_4")
        self.val_5 = QtGui.QPushButton(self.centralWidget)
        self.val_5.setGeometry(QtCore.QRect(160, 240, 71, 71))
        self.val_5.setObjectName("val_5")
        self.val_6 = QtGui.QPushButton(self.centralWidget)
        self.val_6.setGeometry(QtCore.QRect(250, 240, 71, 71))
        self.val_6.setObjectName("val_6")
        self.val_7 = QtGui.QPushButton(self.centralWidget)
        self.val_7.setGeometry(QtCore.QRect(70, 330, 71, 71))
        self.val_7.setObjectName("val_7")
        self.val_8 = QtGui.QPushButton(self.centralWidget)
        self.val_8.setGeometry(QtCore.QRect(160, 330, 71, 71))
        self.val_8.setObjectName("val_8")
        self.val_9 = QtGui.QPushButton(self.centralWidget)
        self.val_9.setGeometry(QtCore.QRect(250, 330, 71, 71))
        self.val_9.setObjectName("val_9")
        self.val_add = QtGui.QPushButton(self.centralWidget)
        self.val_add.setGeometry(QtCore.QRect(70, 420, 71, 71))
        self.val_add.setObjectName("val_add")
        self.val_0 = QtGui.QPushButton(self.centralWidget)
        self.val_0.setGeometry(QtCore.QRect(160, 420, 71, 71))
        self.val_0.setObjectName("val_0")
        self.val_sub = QtGui.QPushButton(self.centralWidget)
        self.val_sub.setGeometry(QtCore.QRect(250, 420, 71, 71))
        self.val_sub.setObjectName("val_sub")
        self.op_box = QtGui.QTextEdit(self.centralWidget)
        self.op_box.setGeometry(QtCore.QRect(70, 50, 341, 61))
        self.op_box.setObjectName("op_box")
        self.val_mul = QtGui.QPushButton(self.centralWidget)
        self.val_mul.setGeometry(QtCore.QRect(340, 240, 71, 71))
        self.val_mul.setObjectName("val_mul")
        self.val_div = QtGui.QPushButton(self.centralWidget)
        self.val_div.setGeometry(QtCore.QRect(340, 330, 71, 71))
        self.val_div.setObjectName("val_div")
        self.val_tot = QtGui.QPushButton(self.centralWidget)
        self.val_tot.setGeometry(QtCore.QRect(340, 420, 71, 71))
        self.val_tot.setObjectName("val_tot")
        self.val_dot = QtGui.QPushButton(self.centralWidget)
        self.val_dot.setGeometry(QtCore.QRect(340, 150, 71, 71))
        self.val_dot.setObjectName("val_dot")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # Calculator.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(Calculator)
        self.mainToolBar.setObjectName("mainToolBar")
        # Calculator.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Calculator)
        self.statusBar.setObjectName("statusBar")
        # Calculator.setStatusBar(self.statusBar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QtGui.QApplication.translate("Calculator", "Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.val_1.setText(QtGui.QApplication.translate("Calculator", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.val_2.setText(QtGui.QApplication.translate("Calculator", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.val_3.setText(QtGui.QApplication.translate("Calculator", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.val_4.setText(QtGui.QApplication.translate("Calculator", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.val_5.setText(QtGui.QApplication.translate("Calculator", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.val_6.setText(QtGui.QApplication.translate("Calculator", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.val_7.setText(QtGui.QApplication.translate("Calculator", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.val_8.setText(QtGui.QApplication.translate("Calculator", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.val_9.setText(QtGui.QApplication.translate("Calculator", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.val_add.setText(QtGui.QApplication.translate("Calculator", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.val_0.setText(QtGui.QApplication.translate("Calculator", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.val_sub.setText(QtGui.QApplication.translate("Calculator", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.val_mul.setText(QtGui.QApplication.translate("Calculator", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.val_div.setText(QtGui.QApplication.translate("Calculator", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.val_tot.setText(QtGui.QApplication.translate("Calculator", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.val_dot.setText(QtGui.QApplication.translate("Calculator", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Calculator", "Calculator", None, QtGui.QApplication.UnicodeUTF8))

