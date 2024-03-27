from PySide6.QtWidgets import QApplication
import sys
from button_hodler import ButtonHolder

# init setup
app = QApplication(sys.argv)
window = ButtonHolder()

# start
window.show()
app.exec()