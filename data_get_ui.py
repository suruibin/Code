# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_get_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_Data_Get(object):
    def setupUi(self, Data_Get):
        Data_Get.setObjectName("Data_Get")
        Data_Get.resize(299, 144)
        self.label = QtWidgets.QLabel(Data_Get)
        self.label.setGeometry(QtCore.QRect(10, 30, 48, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Data_Get)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 48, 12))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Data_Get)
        self.label_3.setGeometry(QtCore.QRect(60, 0, 191, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(Data_Get)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(70, 30, 231, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Data_Get)
        self.progressBar_2.setGeometry(QtCore.QRect(70, 70, 231, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_4 = QtWidgets.QLabel(Data_Get)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 281, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Data_Get)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 281, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Data_Get)
        
        Data_Get.rejected.connect(Data_Get.my_exit)
        QtCore.QMetaObject.connectSlotsByName(Data_Get)
        
    def retranslateUi(self, Data_Get):
        _translate = QtCore.QCoreApplication.translate
        Data_Get.setWindowTitle(_translate("Data_Get", "当日数据获取"))
        self.label.setText(_translate("Data_Get", "数据获取"))
        self.label_2.setText(_translate("Data_Get", "数据创建"))
        self.label_3.setText(_translate("Data_Get", "此界面主要用于盘后数据再次同步"))
        self.progressBar.setFormat(_translate("Data_Get", "%p%"))
        self.label_4.setText(_translate("Data_Get", "数据获取类型:资金,龙虎榜，融资融券，板块数据等"))
        self.label_5.setText(_translate("Data_Get", "盘中点击后台运行按钮，以获取实时资金和板块数据！"))

    def my_exit(self):
            print("退出数据获取界面!")
            
            
    def my_pro(self):
        print("....")
        self.progressBar.setValue(66) 