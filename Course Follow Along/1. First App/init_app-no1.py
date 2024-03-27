# V1 - don't use

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# init setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("First PySide6 App")

# add elements
button = QPushButton()
button.setText("Press me :P")

# assign elements
window.setCentralWidget(button)

# start
window.show()
app.exec()