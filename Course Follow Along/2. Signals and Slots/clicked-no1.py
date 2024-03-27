# responding for syntax learning
from PySide6.QtWidgets import QApplication, QPushButton

def clicked():
    print("You clicked the button :P")

# init
app = QApplication()

# add elements
button = QPushButton("Click me :)")

# assign actions
button.clicked.connect(clicked)

# start
button.show()
app.exec()

