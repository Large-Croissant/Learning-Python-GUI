from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        # init setup
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        # add elements
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        # assign actions

        # make layout