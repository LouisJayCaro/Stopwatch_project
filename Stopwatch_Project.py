# Imported Librarires
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPalette, QColor
import winsound


class Stopwatch(QMainWindow):
    def setupUi(self, MainWindow):

        # Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 685)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        app.setStyle("Fusion")  
        self.palette = QPalette()
        
        # Window Icon
        MainWindow.setWindowIcon(QtGui.QIcon('icon\icon.png'))
        
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
        self.StartButton.pressed.connect(self.Sounds) # Connects StartButton to the Sounds method

        #Lap Button
        self.LapButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.LapButton.setFont(font)
        self.LapButton.setObjectName("LapButton")
        self.horizontalLayout.addWidget(self.LapButton)
        self.LapButton.pressed.connect(self.Lap)

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

        # Darkmode Check Button
        self.DarkMode = QtWidgets.QCheckBox(self.centralwidget)
        self.DarkMode.setGeometry(QtCore.QRect(730, 650, 91, 20))
        self.DarkMode.setObjectName("DarkMode")
        self.DarkMode.stateChanged.connect(self.Dark_Mode)
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(290, 310, 256, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set the necessary variables
        self.counter = 0
        self.minute = "00"
        self.second = '00'
        self.milisecond = "00"
        self.startWatch = False
        self.Lapnumber = 0

        # Create timer object
        timer = QTimer(self)
        # Add a method with the timer
        timer.timeout.connect(self.TimerCounter)
        # Call start() method to modify the timer value
        timer.start(10)

    # Sets Button Labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Stopwatch"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.LapButton.setText(_translate("MainWindow", "Split"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.DarkMode.setText(_translate("MainWindow", "Dark Mode"))
        
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
        self.Timer_displayed = f"{self.minute}:{self.second}:{self.milisecond}"
        self.Timer.display(self.Timer_displayed) 

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
        self.Lapnumber= 0
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.milisecond = '00'
        self.StartButton.setText("Start")
        # Set the initial values for the stop watch
        self.Timer.display(str(self.counter))
        self.listWidget.clear()
    
    def Lap(self):
        if self.startWatch == True:
            self.Lapnumber += 1
            if self.Lapnumber >= 10:
                self.listWidget.addItem(f"Lap {self.Lapnumber}                    {self.Timer_displayed}")
            elif self.Lapnumber  <10:
                self.listWidget.addItem(f"Lap {self.Lapnumber}                      {self.Timer_displayed}")

    def Dark_Mode(self, state):
        if state == QtCore.Qt.Checked:
            app.setStyle("Fusion")
            # Now use a palette to switch to dark colors:
            self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
            self.palette.setColor(QPalette.WindowText, Qt.white)
            self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
            self.palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            self.palette.setColor(QPalette.ToolTipBase, Qt.black)
            self.palette.setColor(QPalette.ToolTipText, Qt.white)
            self.palette.setColor(QPalette.Text, Qt.white)
            self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
            self.palette.setColor(QPalette.ButtonText, Qt.white)
            self.palette.setColor(QPalette.BrightText, Qt.red)
            self.palette.setColor(QPalette.Link, QColor(42, 130, 218))
            self.palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            self.palette.setColor(QPalette.HighlightedText, Qt.black)
            app.setPalette(self.palette)
        else: 
            self.palette.setColor(QPalette.Window, QColor(240, 240, 240))
            self.palette.setColor(QPalette.WindowText, Qt.black)
            self.palette.setColor(QPalette.Base, QColor(255, 255, 255))
            self.palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
            self.palette.setColor(QPalette.ToolTipBase, Qt.white)
            self.palette.setColor(QPalette.ToolTipText, Qt.black)
            self.palette.setColor(QPalette.Text, Qt.black)
            self.palette.setColor(QPalette.Button, QColor(240, 240, 240))
            self.palette.setColor(QPalette.ButtonText, Qt.black)
            self.palette.setColor(QPalette.BrightText, Qt.red)
            self.palette.setColor(QPalette.Link, QColor(0, 120, 215))
            self.palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            self.palette.setColor(QPalette.HighlightedText, Qt.white)
            app.setPalette(self.palette)
    
    def Sounds(self):
        if self.StartButton.text() == "Start":
            frequency = 1900
            duration = 300
            winsound.Beep(frequency, duration)
        elif self.StartButton.text() == "Stop":
            frequency = 1900
            duration = 300
            winsound.Beep(frequency, duration)
        elif self.StartButton.text() == "Resume":
            frequency = 1700
            duration = 300
            winsound.Beep(frequency, duration)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Stopwatch()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
=======
# Imported Librarires
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPalette, QColor


class Stopwatch(QMainWindow):
    def setupUi(self, MainWindow):

        # Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 685)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        app.setStyle("Fusion")  
        self.palette = QPalette()
        
        # Window Icon
        MainWindow.setWindowIcon(QtGui.QIcon('icon\icon.png'))
        
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
        self.LapButton.pressed.connect(self.Lap)

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

        # Darkmode Check Button
        self.DarkMode = QtWidgets.QCheckBox(self.centralwidget)
        self.DarkMode.setGeometry(QtCore.QRect(730, 650, 91, 20))
        self.DarkMode.setObjectName("DarkMode")
        self.DarkMode.stateChanged.connect(self.Dark_Mode)
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(290, 310, 256, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set the necessary variables
        self.counter = 0
        self.minute = "00"
        self.second = '00'
        self.milisecond = "00"
        self.startWatch = False
        self.Lapnumber = 0

        # Create timer object
        timer = QTimer(self)
        # Add a method with the timer
        timer.timeout.connect(self.TimerCounter)
        # Call start() method to modify the timer value
        timer.start(10)

    # Sets Button Labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Stopwatch"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.LapButton.setText(_translate("MainWindow", "Split"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.DarkMode.setText(_translate("MainWindow", "Dark Mode"))
        
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
        self.Timer_displayed = f"{self.minute}:{self.second}:{self.milisecond}"
        self.Timer.display(self.Timer_displayed) 

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
        self.Lapnumber= 0
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.milisecond = '00'
        self.StartButton.setText("Start")
        # Set the initial values for the stop watch
        self.Timer.display(str(self.counter))
        self.listWidget.clear()
    
    def Lap(self):
        if self.startWatch == True:
            self.Lapnumber += 1
            if self.Lapnumber >= 10:
                self.listWidget.addItem(f"Lap {self.Lapnumber}                    {self.Timer_displayed}")
            elif self.Lapnumber  <10:
                self.listWidget.addItem(f"Lap {self.Lapnumber}                      {self.Timer_displayed}")

    def Dark_Mode(self, state):
        if state == QtCore.Qt.Checked:
            app.setStyle("Fusion")
            # Now use a palette to switch to dark colors:
            self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
            self.palette.setColor(QPalette.WindowText, Qt.white)
            self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
            self.palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            self.palette.setColor(QPalette.ToolTipBase, Qt.black)
            self.palette.setColor(QPalette.ToolTipText, Qt.white)
            self.palette.setColor(QPalette.Text, Qt.white)
            self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
            self.palette.setColor(QPalette.ButtonText, Qt.white)
            self.palette.setColor(QPalette.BrightText, Qt.red)
            self.palette.setColor(QPalette.Link, QColor(42, 130, 218))
            self.palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            self.palette.setColor(QPalette.HighlightedText, Qt.black)
            app.setPalette(self.palette)
        else: 
            self.palette.setColor(QPalette.Window, QColor(240, 240, 240))
            self.palette.setColor(QPalette.WindowText, Qt.black)
            self.palette.setColor(QPalette.Base, QColor(255, 255, 255))
            self.palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
            self.palette.setColor(QPalette.ToolTipBase, Qt.white)
            self.palette.setColor(QPalette.ToolTipText, Qt.black)
            self.palette.setColor(QPalette.Text, Qt.black)
            self.palette.setColor(QPalette.Button, QColor(240, 240, 240))
            self.palette.setColor(QPalette.ButtonText, Qt.black)
            self.palette.setColor(QPalette.BrightText, Qt.red)
            self.palette.setColor(QPalette.Link, QColor(0, 120, 215))
            self.palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            self.palette.setColor(QPalette.HighlightedText, Qt.white)
            app.setPalette(self.palette)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Stopwatch()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
