# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 372)
        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.btn.setObjectName("btn")
        self.edit = QtWidgets.QLineEdit(Dialog)
        self.edit.setGeometry(QtCore.QRect(0, 20, 113, 20))
        self.edit.setObjectName("edit")
        self.pgb = QtWidgets.QProgressBar(Dialog)
        self.pgb.setGeometry(QtCore.QRect(10, 210, 118, 23))
        self.pgb.setProperty("value", 0)
        self.pgb.setObjectName("pgb")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(150, 0, 651, 371))
        self.tableView.setObjectName("tableView")
        self.btn2 = QtWidgets.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.btn2.setObjectName("btn2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn.setText(_translate("Dialog", "btn"))
        self.btn2.setText(_translate("Dialog", "PushButton"))

