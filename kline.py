# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import tushare as ts
import datetime
from matplotlib.dates import date2num
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 771, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class CandlestickItem(pg.GraphicsObject):  
    def __init__(self, data):  
        pg.GraphicsObject.__init__(self) 
        self.data = data ## data must have fields: time, open, close, min, max  
        self.generatePicture()
 
    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setBrush(pg.mkBrush('r'))
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
 
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
 
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

def chart():
    hist_data = ts.get_hist_data('300618',start='2017-05-01')
    data_list = []
    for dates,row in hist_data.iterrows():
        # 将时间转换为数字
        date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
        
        str_t=str(date_time).replace("-",'')
        str_t=str_t[:9]
        
        #t=int(str_t)
        
        t = date2num(date_time)
        
        # t = dict(enumerate(datetime))
        open,high,close,low = row[:4]
        #print(date_time,t,str_t,open,close,low,high)
        datas = (t,open,close,low,high)
        data_list.append(datas)
    #axis_dict = dict(enumerate(axis))
    item = CandlestickItem(data_list)
    plt = pg.PlotWidget()
    plt.addItem(item,)
    plt.showGrid(x=True,y=True)
    return plt

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.verticalLayout.addWidget(chart())
    sys.exit(app.exec_())

