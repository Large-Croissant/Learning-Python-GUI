from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        # init stuff
        super().__init__()
        self.setWindowTitle("Button Holder App")
        
        # add elements
        button = QPushButton("Press me :P")

        #assign elements
        self.setCentralWidget(button)
