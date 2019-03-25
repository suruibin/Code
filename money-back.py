# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'money.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox,QDialog,QProgressDialog,QLineEdit
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 250)
        MainWindow.setStyleSheet("*\n"
"{\n"
"background:white;\n"
"}\n"
"QLaber\n"
"{\n"
"color:rgb(0,0,255);\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"border:1px solid blue;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"color:black;\n"
"background:rgb(255, 85, 0);\n"
"border: 1px solid red;\n"
"border-color:rgb(255, 85, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#lhb\n"
"{\n"
"color:black;\n"
"background:rgb(255, 85, 127);\n"
"border: 1px solid red;\n"
"border-color:red;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#jbm\n"
"{\n"
"color:black;\n"
"background:rgb(255, 170, 127);\n"
"border: 1px solid red;\n"
"border-color:rgb(255, 170, 127);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#history\n"
"{\n"
"color:black;\n"
"background:rgb(170, 85, 255);\n"
"border: 1px solid red;\n"
"border-color:rgb(170, 85, 255);\n"
"border-radius:10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.money = QtWidgets.QPushButton(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.money.setObjectName("money")
        self.lhb = QtWidgets.QPushButton(self.centralwidget)
        self.lhb.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.lhb.setObjectName("lhb")
        self.jbm = QtWidgets.QPushButton(self.centralwidget)
        self.jbm.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.jbm.setObjectName("jbm")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(110, 0, 381, 201))
        self.tableView.setObjectName("tableView")
        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.history.setObjectName("history")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.history.clicked.connect(MainWindow.close)
        self.jbm.clicked.connect(MainWindow.close)
        self.lhb.clicked.connect(MainWindow.close)
        self.money.clicked.connect(self.table_view)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def table_view(self):
        #设置数据层次结构，4行4列
        self.model=QStandardItemModel(7,7)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['名称','代码','涨幅','股价','昨日资金','今日资金','流通盘'])
        for row in range(10):
            for column in range(7):
                item=QStandardItem('row %s,column %s'%(row,column))
                #设置每个位置的文本值
                self.model.setItem(row,column,item)

        #实例化表格视图，设置模型为自定义的模型
        #self.tableView=QTableView()
        self.tableView.setModel(self.model)
        # #todo 优化1 表格填满窗口
        # #水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # #水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #
        # #TODO 优化3 删除当前选中的数据
        # indexs=self.tableView.selectionModel().selection().indexes()
        # print(indexs)
        # if len(indexs)>0:
        #     index=indexs[0]
        #     self.model.removeRows(index.row(),1)

        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        #self.setLayout(layout)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小散变大户数据获取软件V2.0"))
        self.money.setText(_translate("MainWindow", "实时资金"))
        self.lhb.setText(_translate("MainWindow", "龙虎榜"))
        self.jbm.setText(_translate("MainWindow", "基本面"))
        self.history.setText(_translate("MainWindow", "历史数据"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

