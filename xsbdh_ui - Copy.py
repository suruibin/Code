# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xsbdh.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import xsbdh_func
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("MainWindow")
        #Dialog.resize(350, 200)
        Dialog.setFixedSize(350, 200)
        Dialog.setWindowOpacity(1.0)
        Dialog.setAutoFillBackground(True)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(41, 68, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(41, 108, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(135, 68, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(135, 108, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 68, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 108, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(41, 28, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(135, 28, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setShortcut("")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 28, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小散变大户数据获取软件V2.0"))
        self.pushButton_2.setText(_translate("Dialog", "盘中预警"))
        self.pushButton_3.setText(_translate("Dialog", "后台运行"))
        self.pushButton_5.setText(_translate("Dialog", "龙虎数据"))
        self.pushButton_6.setText(_translate("Dialog", "使用说明"))
        self.pushButton_8.setText(_translate("Dialog", "每日复盘"))
        self.pushButton_9.setText(_translate("Dialog", "数据清理"))
        self.pushButton.setText(_translate("Dialog", "数据获取"))
        self.pushButton_4.setText(_translate("Dialog", "早盘竞价"))
        self.pushButton_7.setText(_translate("Dialog", "历史数据"))
        
    def showDialog(self):
        sender = self.sender()
        print(sender)
        if sender == self.pushButton_8:
            QMessageBox.aboutQt(self,'关于Qt')
        else:
            QMessageBox.aboutQt(self,'hahah')
            
    def func(self):
        print(self)
        xsbdh_func.lhb_func(self)
    

