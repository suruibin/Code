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

import requests,time
from global_value import global_val

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 300)
        MainWindow.setStyleSheet("*\n"
"{\n"
"background:white;\n"
"font-family:宋体;\n"
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
        self.money.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.money.setObjectName("money")
        self.lhb = QtWidgets.QPushButton(self.centralwidget)
        self.lhb.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.lhb.setObjectName("lhb")
        self.jbm = QtWidgets.QPushButton(self.centralwidget)
        self.jbm.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.jbm.setObjectName("jbm")
        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.history.setObjectName("history")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(90, 0, 450, 250))
        self.tableView.setObjectName("tableView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        


        self.retranslateUi(MainWindow)
        self.history.clicked.connect(lambda:self.table_view("history"))
        self.jbm.clicked.connect(lambda:self.table_view("jbm"))
        self.lhb.clicked.connect(lambda:self.table_view("lhb"))
        self.money.clicked.connect(lambda:self.table_view("money"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def table_view(self,text):
        #设置数据层次结构，4行4列
        print(text)
        self.model=QStandardItemModel(4000,7)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['名称','代码','涨幅','股价','昨日资金','今日资金','流通盘'])
        
        
        requests.adapters.DEFAULT_RETRIES = 15
        requests.packages.urllib3.disable_warnings()
        url=global_val.url_money
        recv_data = ''
        while recv_data == '':
            try:
                recv_data = requests.get(url, headers=global_val.headers)#获取数据'
            except:
                time.sleep(5)
                print(u"远端服务器无响应,正在尝试重新连接..")
                continue
        
        data=recv_data.text.split("data:")[-1][2:-1]
        #print(data)
        money_list=[""]
        money_list=data.split("\",\"")
        #print(len(money_list))
        stock_num=0
        stock_num=len(money_list)
        
        for i in range(stock_num):
            str_time = money_list[i].split(',')
            #print(tmp)
            net_time = str_time[15].replace("-","").split(" ")[0]
            break
        
        #print(net_time)
        
        for i in range(stock_num):
            tmp = money_list[i].split(',')
            if str(tmp[1])[0]=='0' or str(tmp[1])[0]=='3':
                prefix = 0
            else:
                prefix = 1

            if len(tmp[5]) <=1:
                tmp[5]='0'
        
            print((str(prefix)+'|'+tmp[1]+'|'+net_time+'|'+tmp[5]+'\r\n'))
        
        for row in range(stock_num):
            for column in range(7):
                item=QStandardItem('%s'%(net_time))
                #设置每个位置的文本值
                self.model.setItem(row,column,item)

        #实例化表格视图，设置模型为自定义的模型
        #self.tableView=QTableView()
        self.tableView.setModel(self.model)
        # #todo 优化1 表格填满窗口
        # #水平方向标签拓展剩下的窗口部分，填满表格
        #self.tableView.horizontalHeader().setStretchLastSection(True)
        # #水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
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

