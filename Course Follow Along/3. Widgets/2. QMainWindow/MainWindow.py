from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        # init setup
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        # menu bar
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        # toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        

        # assign actions
        quit_action.triggered.connect(self.quit_app)
        toolbar.addAction(quit_action)

        action1 = QAction("An Action", self)
        action1.setStatusTip("Status message for this Action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("./start.png"), "Another action", self)
        action2.setStatusTip("Status message for another action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click me :P"))

        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.b1_click)
        self.setCentralWidget(button1)

        # make layout
        self.addToolBar(toolbar)

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        # print("Action triggered")
        self.statusBar().showMessage("Action triggered", 3000)

    def b1_click(self):
        print("Clikced on the main button")