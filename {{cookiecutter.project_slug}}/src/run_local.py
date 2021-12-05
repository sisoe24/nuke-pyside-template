# coding: utf-8
from __future__ import print_function

import sys

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from src.main import MainWindow, MainWindowWidgets


class _MainWindowWidgets(QWidget):
    """Main window widget that holds the main app and the fake script editor."""

    def __init__(self):
        """Init method for the _MainWindowWidget class."""
        QWidget.__init__(self)

        self.main_app = MainWindowWidgets()

        _layout = QVBoxLayout()
        _layout.addWidget(self.main_app)
        self.setLayout(_layout)


class _MainWindow(MainWindow):
    """Main Window that inherits from main.py.

    This is to add some extra functionality when testing locally, like screen
    position.
    """

    def __init__(self):
        """Init method for the _MainWindow class."""
        MainWindow.__init__(self, main_widget=_MainWindowWidgets)
        self.setWindowTitle('{{cookiecutter.project_slug}} Local')

        # personal monitor loc for rapid testing
        screen_loc = {
            'hp': {'x': -1077.296875, 'y': -5.31640625}
        }
        self.setGeometry(screen_loc['hp']['x'],
                         screen_loc['hp']['y'],
                         1080, 1980)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = _MainWindow()
    window.show()
    app.exec_()
