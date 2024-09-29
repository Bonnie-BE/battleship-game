import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import *
# defines a thread which emits signals with values 0 to 99
class LoopThread(QThread):
    update_label_signal = pyqtSignal(str) # create signal
    def __init__(self):
        QThread.__init__(self)
    def run(self): # run executed when start() method called
        for i in range(100):
            sleep(0.15) # wait a little before emitting next signal
            self.update_label_signal.emit(str(i)) # emit signal
            
class ThreadWidget(QWidget): # defines a GUI with button when clicked updates a label with 0 to 99
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 50)
        self.setWindowTitle('Thread Window')
        self.label = QLabel()
        self.ok = QPushButton("OK")
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.ok)
        self.setLayout(hbox)
        self.loop_thread = LoopThread() # create thread
        self.loop_thread.update_label_signal.connect(self.loop_thread_slot) # connect signals to slots
        self.ok.clicked.connect(self.ok_clicked)
    def loop_thread_slot(self, txt): # slot which handles signal from thread
        self.label.setText(txt)
    def ok_clicked(self):
        self.loop_thread.start() # thread started         