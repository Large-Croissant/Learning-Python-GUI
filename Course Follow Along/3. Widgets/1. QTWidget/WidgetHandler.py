from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import random

class RockWidget(QWidget):
    def __init__(self):
        # init setup
        super().__init__()
        self.setWindowTitle("RockWidget")

        # add elements
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")

        # add actions
        button1.clicked.connect(self.b1_click)
        button2.clicked.connect(self.b2_click)
        
        # setup layout
        button_layout = QHBoxLayout() if random.randint(0, 1) == 1 else QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        self.setLayout(button_layout)

    def b1_click(self):
        print("Button 1 has been clicked")

    def b2_click(self):
        print("Button 2 has been clicked")