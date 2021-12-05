# coding: utf-8
from __future__ import print_function

import logging

from PySide2.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
    QLabel
)

from .utils import color_widget
from .widgets import ErrorDialog, ToolBar

LOGGER = logging.getLogger('{{cookiecutter.project_slug}}.main')
LOGGER.debug('-*- START APPLICATION -*-')


class MainWindowWidgets(QWidget):
    @color_widget
    def __init__(self):
        QWidget.__init__(self)

        label = QLabel('Blank Widget')
        label.setStatusTip('This is a label')

        _layout = QVBoxLayout()
        _layout.addWidget(label)

        self.setLayout(_layout)


class MainWindow(QMainWindow):
    """Custom QMainWindow class.

    A toolbar and a status bar will be added in the main app together with the
    main widgets.

    If app has an exception loading the main widget, will spawn an ErrorDialog
    class.
    """

    def __init__(self, main_widget=MainWindowWidgets):
        """Init method for main window widget."""
        QMainWindow.__init__(self)
        self.setWindowTitle("{{cookiecutter.project_slug}}")

        toolbar = ToolBar()
        self.addToolBar(toolbar)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        try:
            main_widgets = main_widget()
        except Exception as err:
            ErrorDialog(err, self).show()
            LOGGER.critical(err, exc_info=True)
        else:
            self.setCentralWidget(main_widgets)


try:
    import nukescripts
except ImportError as error:
    pass
else:
    nukescripts.panels.registerWidgetAsPanel(
        '{{cookiecutter.project_slug}}.src.main.MainWindow', '{{cookiecutter.project_slug}}',
        '{{cookiecutter.project_slug}}.MainWindow')
