import sys
import os
import json

from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTabBar, QFrame,
                             QStackedLayout)

from PyQt6.QtGui import QIcon, QWindow, QImage
from PyQt6.QtCore import *


class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sift Browser")
        self.setBaseSize(1366, 768)
        self.createApp()

    def createApp(self):
        self.layout = QVBoxLayout()

        self.tabBar = QTabBar()

        self.tabBar.addTab("Tab 1")
        self.tabBar.addTab("Tab 2")

        self.tabBar.setCurrentIndex(0)

        self.layout.addWidget(self.tabBar)
        self.setLayout(self.layout)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec())
