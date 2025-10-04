import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setGeometry(500, 200, 400, 200)

        # Clock label
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
                   #css
        self.label.setStyleSheet("""  
                                 font-size:50px; 
                                 font-family: Arial; 
                                 color: cyan;
                                 background-color: black;
                                 """)
        self.setCentralWidget(self.label)

        # Timer
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)  
        timer.start(1000) 
      
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString("hh:mm:ss AP")  # 12-hour format
        self.label.setText(time_text)


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()








