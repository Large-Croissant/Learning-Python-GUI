# responding for syntax learning
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QSlider

def clicked(checked):
    print(f"You clicked the button :P\nchecked : {checked}")
    
def slider_respond(value):
    print(f"Slider moved to {value}")

# init
app = QApplication()

# add elements
button = QPushButton("Click me :)")
button.setCheckable(True)
slider = QSlider(Qt.Horizontal)
slider.setRange(1,100)
slider.setValue(25)

# assign actions
button.clicked.connect(clicked)
slider.valueChanged.connect(slider_respond)

# start
button.show()
slider.show()
app.exec()

