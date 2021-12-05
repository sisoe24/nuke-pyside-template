import os
import pytest

from src.main import MainWindowWidgets


def test_main(_main_ui):
    assert isinstance(_main_ui, MainWindowWidgets)


@pytest.mark.rapidtest
def test_simple(_package):
    assert os.path.exists(_package)
