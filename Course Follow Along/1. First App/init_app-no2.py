# V2 - not "maintainable" enough

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        # init stuff
        super().__init__()
        self.setWindowTitle("Button Holder App")
        
        # add elements
        button = QPushButton("Press me :P")

        #assign elements
        self.setCentralWidget(button)

# init setup
app = QApplication(sys.argv)
window = ButtonHolder()

# start
window.show()
app.exec()
