import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import time

def makeGraphWidgets(title, graph):
	lay = QVBoxLayout()
	lay.addWidget(QLabel(title))
	lay.addWidget(graph)
	return lay

class seatPosGraph(FigureCanvas):
	def __init__(self, parent=None,dpi=100):
		fig = Figure( dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(seatPosGraph, self).__init__(fig)

class seatSpeedGraph(FigureCanvas):
	def __init__(self, parent=None,dpi=100):
		fig = Figure( dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(seatSpeedGraph, self).__init__(fig)

class PullForceGraphL(FigureCanvas):
	def __init__(self, parent=None,dpi=100):
		fig = Figure( dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(PullForceGraphL, self).__init__(fig)

class PullForceGraphR(FigureCanvas):
	def __init__(self, parent=None,dpi=100):
		fig = Figure( dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(PullForceGraphR, self).__init__(fig)


class App(QWidget):
	def __init__(self):
		super().__init__()
	
		layout = QGridLayout()
		self.setLayout(layout)

		self.SeatPosGraph = seatPosGraph(self, dpi=100)
		self.SeatSpeedGraph = seatSpeedGraph(self, dpi=100)
		self.PullForceGraphL = PullForceGraphL(self, dpi=100)
		self.PullForceGraphR = PullForceGraphR(self, dpi=100)

		stringSend = "Seat Position"
		self.SeatPosGraph = makeGraphWidgets(stringSend, self.SeatPosGraph)
		layout.addLayout(self.SeatPosGraph, 0,0)

		stringSend = "Seat Speed"
		self.SeatSpeedGraph = makeGraphWidgets(stringSend, self.SeatSpeedGraph)
		layout.addLayout(self.SeatSpeedGraph, 0,1)

		stringSend = "Speed"
		self.Speed = "10"
		self.SpeedIndicator = self.makeSpeedWidgets(stringSend, self.Speed)
		layout.addLayout(self.SpeedIndicator, 1, 0)

		stringSend = "Pull Force Left"
		self.PullForceLGraph = makeGraphWidgets(stringSend, self.PullForceGraphL)
		layout.addLayout(self.PullForceLGraph, 1,1)

		stringSend = "Pull Force Right"
		self.PullForceR = makeGraphWidgets(stringSend, self.PullForceGraphR)
		layout.addLayout(self.PullForceR, 1,2)

		self.timer = QtCore.QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.updatePlots)
		self.timer.start()
		
		self.SP = open("SeatPos.txt", "r")
		self.PFL = open("PullForce.txt", "r")
		self.PFR = open("PullForce.txt", "r")
		self.S = open("Speed.txt", "r")
		
		self.SPD = self.SP.readlines()
		self.PFLD = self.PFL.readlines()
		self.PFRD = self.PFR.readlines()
		self.SD = self.S.readlines()

	def makeSpeedWidgets(self, title, Speed):
		lay = QVBoxLayout()
		lay.addWidget(QLabel(title))
		lay.addWidget(QLabel(Speed))
		return lay

	def updatePlots(self):
		for i in self.SD:
			stringSend = "Speed"
			self.Speed = i
			print(type(self.Speed))
			self.SpeedIndicator = self.makeSpeedWidgets(stringSend, self.Speed)
			print(self.Speed)
			time.sleep(1)


if __name__ == '__main__':
	app = QApplication([])
	myApp = App()
	myApp.show()
	try:
		app.exec_()
	except SystemExit:
		print("Bye")