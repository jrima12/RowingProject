import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# def makeGraphWidgets(title, graph):
# 	lay = QVBoxLayout()
# 	lay.addWidget(QLabel(title))
# 	lay.addWidget(graph)
# 	return lay

class graph(FigureCanvas):
    def __init__(self, parent=None):
        self.x_vals = [1,2,3,4,5]
        self.y_vals = [1,2,4,3,5]
        self.index = count()
        fig = Figure()
        self.axes = fig.add_subplot(111)
        plt.plot(self.x_vals, self.y_vals)
        super(graph, self).__init__(fig)
        # plt.show()
        # plt.plot(self.x_vals, self.y_vals)

        
    def animate(self, i):
        self.x_vals.append(next(self.index))
        self.y_vals.append(random.randint(0,5))

        plt.cla() #clears axis
        plt.plot(self.x_vals, self.y_vals)

class App(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.G1 = graph(self)
        self.G2 = graph(self)
        self.G3 = graph(self)
        self.G4 = graph(self)
        self.G5 = graph(self)

        # layout.addLayout(makeGraphWidgets("G1", self.G1), 0,0)
        # layout.addLayout(makeGraphWidgets("G2", self.G2), 0,1)
        # layout.addLayout(makeGraphWidgets("G3", self.G3), 1,0)
        # layout.addLayout(makeGraphWidgets("G4", self.G4), 1,1)
        # layout.addLayout(makeGraphWidgets("G5", self.G5), 1,2)

        layout.addWidget(self.G1, 0,0)
        layout.addWidget(self.G2, 0,1)
        layout.addWidget(self.G3, 1,0)
        layout.addWidget(self.G4, 1,1)
        layout.addWidget(self.G5, 1,2)

    # def animate(i, gt):
    #     gt.x_vals.append(next(gt.index))
    #     gt.y_vals.append(random.randint(0,5))

    #     gt.cla() #clears axis
    #     gt.plot(gt.x_vals, gt.y_vals)

        ani = FuncAnimation(plt.gcf(), self.G1.animate, interval = 1000)
        # ani1 = FuncAnimation(plt.gcf(), self.G2.animate, interval = 1000)
        # ani2 = FuncAnimation(plt.gcf(), self.G3.animate, interval = 1000)
        # ani3 = FuncAnimation(plt.gcf(), self.G4.animate, interval = 1000)
        # ani4 = FuncAnimation(plt.gcf(), self.G5.animate, interval = 1000)
        # plt.show()

if __name__ == '__main__':
    app = QApplication([])
    myApp = App()
    myApp.show()
    try:
        app.exec_()
    except SystemExit:
        print("Bye")

##################################################
##################################################
# import random
# from itertools import count
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')

# # x_vals = [0,1,2,3,4,5]
# # y_vals = [0,1,3,2,3,5]
# # plt.plot(x_vals, y_vals)

# x_vals = []
# y_vals = []

# index = count() #count function is part of itertools and it just increments index each time its called

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0,5))

#     plt.cla() #clears axis
#     plt.plot(x_vals, y_vals)
    


# ani = FuncAnimation(plt.gcf(), animate, interval = 100)

# plt.tight_layout()
# plt.show()
################################################################
####################################################################