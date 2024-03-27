from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        # init stuff
        super().__init__()
        self.setWindowTitle("App 1")
        self.setFixedSize(QSize(500, 300))
        
        # main button
        self.button = QPushButton("Press me :P")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_toggled)
        self.setCentralWidget(self.button)

    # what to do when button clicked
    def button_clicked(self):
        print("The button was clicked :P")
        self.button.setText("Button has been clicked :)")
        self.setWindowTitle(f"App {random.randint(0, 100)}")
        #self.setEnabled(False)

    def button_toggled(self, checked):
        print(checked)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main(sys.argv)