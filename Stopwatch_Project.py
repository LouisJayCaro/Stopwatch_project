# Imported Librarires
from cgitb import reset
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime


class Stopwatch(QMainWindow):
    def setupUi(self, MainWindow):

        # Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 685)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        #Widgets
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Timer display
        self.Timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.Timer.setEnabled(True)
        self.Timer.setGeometry(QtCore.QRect(48, 40, 741, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Timer.setFont(font)
        self.Timer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Timer.setSmallDecimalPoint(False)
        self.Timer.setDigitCount(9)
        self.Timer.setObjectName("Timer")

        # Lap list display
        self.LapList = QtWidgets.QListWidget(self.centralwidget)
        self.LapList.setGeometry(QtCore.QRect(290, 300, 256, 192))
        self.LapList.setFlow(QtWidgets.QListView.LeftToRight)
        self.LapList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.LapList.setUniformItemSizes(False)
        self.LapList.setObjectName("LapList")

        # Button format and placement
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 240, 239, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        #Start Button
        self.StartButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout.addWidget(self.StartButton)
        self.StartButton.pressed.connect(self.Start) # Connects StartButton to the Start method

        #Lap Button
        self.LapButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.LapButton.setFont(font)
        self.LapButton.setObjectName("LapButton")
        self.horizontalLayout.addWidget(self.LapButton)
        

        # Reset Button
        self.ResetButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.ResetButton.setFont(font)
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout.addWidget(self.ResetButton)
        self.ResetButton.pressed.connect(self.Reset)    # Connects RessetButton to the Reset method

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.LapList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set the necessary variables
        self.counter = 0
        self.minute = "00"
        self.second = '00'
        self.milisecond = "00"
        self.startWatch = False

        # Create timer object
        timer = QTimer(self)
        # Add a method with the timer
        timer.timeout.connect(self.TimerCounter)
        # Call start() method to modify the timer value
        timer.start(10)

    # Sets Button Labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.LapButton.setText(_translate("MainWindow", "Split"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        
    # Actions

    # Displays the current time 
    def TimerCounter(self):
        if self.startWatch:
            # Increment counter by 1
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter/100 - int(self.counter/100))*100)
            if cnt < 10:
                self.milisecond = "0" + str(cnt)
            else:
                self.milisecond = str(cnt)

            # Set the second value
            if int(self.counter/100) < 10 :
                self.second = '0' + str(int(self.counter / 100))
                
            else:
                self.second = str(int(self.counter / 100))
                # Set the minute value
                if self.counter / 100 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        # Merge the mintue, second and count values
        Timer_displayed = f"{self.minute}:{self.second}:{self.milisecond}"
        self.Timer.display(Timer_displayed) 

    def Start(self):
        # Set the caption of the start button based on previous caption
        if self.StartButton.text() == 'Stop':
            self.StartButton.setText('Resume')
            self.startWatch = False
        else:
            # making startWatch to true
            self.startWatch = True
            self.StartButton.setText('Stop')

    # Define method to handle the reset button
    def Reset(self):
        self.startWatch = False
        # Reset all counter variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.milisecond = '00'
        # Set the initial values for the stop watch
        self.Timer.display(str(self.counter))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Stopwatch()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
