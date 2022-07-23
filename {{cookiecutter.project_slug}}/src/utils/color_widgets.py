# coding: utf-8
from __future__ import print_function

import json
from random import randint

from PySide2.QtGui import QColor, QPalette


def color_widget(func):
    """Color widget layout.

    This is a wrapper function which can be used to randomly color a QWidget
    layout.

    Optionally, the function checks a configuration file to toggle the color state.
    The file can be created by using the vscode command `Toggle Ui Color`.
    """
    def inner_wrapper(*args):

        self = args[0]
        func(self)

        should_color = True

        try:
            with open('src/utils/widgets_color_state.json', encoding='utf-8') as file:
                state = json.load(file).get('color', True)
        except FileNotFoundError:
            pass
        else:
            should_color = state

        self.setAutoFillBackground(should_color)

        palette = QPalette()
        palette.setColor(
            QPalette.Window, QColor(
                randint(0, 255), randint(0, 255), randint(0, 255)
            )
        )

        self.setPalette(palette)
    return inner_wrapper
