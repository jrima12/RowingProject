import random
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import math

class App(QWidget):
    def __init__(self):
        super().__init__()
        #self.showMaximized()
        self.zeroline = [0]*1000
        self.y_valsSpeed = []
        self.y_valsSeatPos = []
        self.y_valsPFL = []
        self.y_valsPFR = []
        self.x_vals = []

        layout = QGridLayout()
        self.setLayout(layout)

        pg.setConfigOptions(antialias = True)
        imv = pg.ImageView()

        self.SpeedGraph = pg.plot(x = self.x_vals, y = self.y_valsSpeed)
        self.SpeedGraph.setXRange(0, 20, padding=0)
        self.SpeedGraph.setYRange(-5, 25, padding=0)
        self.SpeedGraph.getPlotItem().hideAxis('bottom')

        self.SeatPosGraph = pg.plot(x = self.x_vals, y = self.y_valsSeatPos)
        self.SeatPosGraph.setXRange(0, 20, padding=0)
        self.SeatPosGraph.setYRange(-5, 25, padding=0)
        self.SeatPosGraph.getPlotItem().hideAxis('bottom')


        self.PFLGraph = pg.plot(x = self.x_vals, y = self.y_valsPFL)
        self.PFLGraph.setXRange(0, 20, padding=0)
        self.PFLGraph.setYRange(-5, 25, padding=0)
        self.PFLGraph.getPlotItem().hideAxis('bottom')


        self.PFRGraph = pg.plot(x = self.x_vals, y = self.y_valsPFR)
        self.PFRGraph.setXRange(0, 20, padding=0)
        self.PFRGraph.setYRange(-5, 25, padding=0)
        self.PFRGraph.getPlotItem().hideAxis('bottom')

        self.Speed = QLabel("10mph")
        self.Speed.setFixedWidth(300)
        self.Speed.setStyleSheet("width: 500px; border: 1px solid black; font-size:60px; text-align: center")
        self.Speed.setAlignment(QtCore.Qt.AlignCenter)
        # self.Speed.resize(500,500)
        
        self.txt = QLabel("Hello \n put more stuff here")
        self.txt.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(self.Speed, 0,1)
        layout.addWidget(self.txt, 1,1)
        layout.addWidget(self.SpeedGraph, 0,0)
        layout.addWidget(self.SeatPosGraph, 0,2)
        layout.addWidget(self.PFLGraph, 1,0)
        layout.addWidget(self.PFRGraph, 1,2)

        self.count = 0
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)

    def update(self):
        self.SpeedGraph.clear()
        self.SeatPosGraph.clear()
        self.PFLGraph.clear()
        self.PFRGraph.clear()
        if self.count**1.1 < 10:
            self.y_valsSpeed.append(self.count**1.1)
            self.Speed.setText(str(int(self.count**1.1))+"mph")
        else:
            ri = random.randint(9,11)
            self.y_valsSpeed.append(ri)
            self.Speed.setText(str(ri)+"mph")

        self.y_valsSeatPos.append(math.sin(self.count/2.2)*10 + 10)

        if self.count % 5 ==0:
            self.y_valsPFL.append(0)
            self.y_valsPFR.append(0)
        else:
            self.y_valsPFL.append((self.count%5)**2)
            self.y_valsPFR.append((self.count%5)**2)

        self.x_vals.append(self.count)

        self.SpeedGraph.plot(x = self.x_vals, y = self.y_valsSpeed)
        self.SeatPosGraph.plot(x = self.x_vals, y = self.y_valsSeatPos)
        self.PFLGraph.plot(x = self.x_vals, y = self.y_valsPFL)
        self.PFRGraph.plot(x = self.x_vals, y = self.y_valsPFR)

        self.SpeedGraph.plot(y = self.zeroline)
        self.SeatPosGraph.plot(y = self.zeroline)
        self.PFLGraph.plot(y = self.zeroline)
        self.PFRGraph.plot(y = self.zeroline)
        
        if self.count > 20:
            self.SpeedGraph.setXRange(self.count - 19, self.count +1, padding=0)
            self.SeatPosGraph.setXRange(self.count - 19, self.count +1, padding=0)
            self.PFLGraph.setXRange(self.count - 19, self.count +1, padding=0)
            self.PFRGraph.setXRange(self.count - 19, self.count +1, padding=0)

        self.count+=1
        
        time.sleep(.1)

if __name__ == '__main__':
    app = QApplication([])
    myApp = App()
    # myApp.show()
    myApp.showMaximized()
    try:
        app.exec_()
    except SystemExit:
        print("Bye")
