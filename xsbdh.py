# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:45:44 2019

@author: Suruibin
"""
#python D:\Work\Tools\pyinstaller-develop\pyinstaller.py -F C:\Users\Suruibin\Desktop\xsbdh\xsbdh.py -i D:\Work\Tools\pyinstaller-develop\DataSync.ico -w

import sys
import xsbdh_ui
import xsbdh_func
import trayicon
import table
import data_get_ui
from global_value import *

import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox,QDialog,QProgressDialog,QLineEdit

from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

Ui_MainWindow = xsbdh_ui.Ui_MainWindow#指定Ui_MainWindow 为main_menu文件下的Ui_MainWindow对象。

def Set_Background(self):
    palette1 = QtGui.QPalette()
    palette1.setColor(palette1.Background,QtGui.QColor(255,255,255))
    self.setWindowIcon(QIcon("DataSync.ico"))
    self.setPalette(palette1)
    self.setStyleSheet("QLabel{color:rgb(255,0,0,255);font-size:12px;font-weight:normal;font-family:宋体;}")
    self.setFixedSize(self.width(), self.height())#固定窗口大小   
    self.setAutoFillBackground(True)

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):#创建一个Qt对象
#这里的第一个变量是你该窗口的类型，第二个是该窗口对象。
#这里是主窗口类型。所以设置成当QtWidgets.QMainWindow。
#你的窗口是一个会话框时你需要设置成:QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        #Ui_MainWindow.__init__(self)#主界面对象初始化
        self.setupUi(self)  #配置主界面对象
        self.setWindowIcon(QIcon("DataSync.ico"))
        Set_Background(self)
        self.center()
        #ti=trayicon.TrayIcon(self)
        #ti.show()
        #窗口透明控件不透明
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        #self.setAttribute(Qt.WA_TranslucentBackground)
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,  
        (screen.height() - size.height()) / 2)
        
    def SJHQ_Get_Data(self):
        QtWidgets.QMessageBox.information(self.pushButton,"标题","这是第一个PyQt5 GUI程序")
    
Ui_ChildWindows=table.Ui_Dialog

class childWindow(QtWidgets.QDialog,Ui_ChildWindows):
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        Set_Background(self)
        self.edit.setText("100")
        self.btn.clicked.connect(self.showDialog)
        self.btn2.clicked.connect(self.table_view)
    def hello(self):
        print("1111111111111111111")
        xsbdh_func.lhb_tt()
    def showDialog(self):
        
        num = int(self.edit.text())
        progress =QProgressDialog(self)
        progress.setWindowTitle("请稍等")  
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0,num) 
        self.pgb.setRange(0,num) 
        
        for i in range(num):
            self.pgb.setValue(i) 
            progress.setValue(i) 
            time.sleep(0.1)
            if progress.wasCanceled():
                QMessageBox.warning(self,"提示","操作失败") 
                break
        else:
            self.pgb.setValue(num)
            progress.setValue(num) 
            QMessageBox.information(self,"提示","操作成功")
    
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
        self.setLayout(layout)


ui_get_data=data_get_ui.Ui_Data_Get
class Get_Data(QtWidgets.QDialog,ui_get_data):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        Set_Background(self)
    
def pushButton_clicked(self):
    print("11") 
    Get_Data_Show=Get_Data()
    Get_Data_Show.my_pro()
    
    
   
   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #设置样式
    app.setStyle("Fusion")
    #设置按钮文字颜色
    palette = QPalette()
    #palette.setColor(QPalette.ButtonText, Qt.red)
    app.setPalette(palette) 

    window = MainWindow()#创建QT对象
    window.show()#QT对象显示
    child=childWindow()
    
    #数据获取
    #print("global_value:%d"%(auto_run))
    Get_Data_Show=Get_Data()
    window.pushButton.clicked.connect(Get_Data_Show.show)
    window.pushButton.clicked.connect(Get_Data_Show.my_pro)
    
    #设置快捷键
    window.pushButton.setShortcut("Alt+F7")

    #window.pushButton_7.clicked.connect(window.func)
    window.pushButton_8.clicked.connect(child.show)
    sys.exit(app.exec_())
     
"""
import xsbdh_func

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
   设置窗口不能拉伸 setFixedSize
        
"""