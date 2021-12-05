# Nuke Pyside2 Template

Python PySide2 cookiecutter template for Nuke.

## Description

Cookiecutter template to create a basic application in PySide2. The application can also be
run outside Nuke. This is to allow faster development and iteration.

## Features

- Initial setup for a `QMainWindow` widget.
- `QToolBar` with a floating dialog to display custom widgets.
- About widget to display various information about the package.
- A custom `QMessageBox` used for errors and bug reports.
- Internal function `color_widget` to quickly color the widget layout.
- Custom `logging`.
- Custom `nuke` module.
- Custom hook for `git pre push`.
- `pytest` initial setup with some tests and configuration.
  - `_package` fixture for the package root path.
  - `_main_ui` fixture for main widget.
  - `rapidtest` marker.

If installing dependencies with Poetry the following dependencies will be installed:

- `pytest`
- `pytest-cov`
- `pytest-qt`
- `pytest-randomly`
- `pytest-repeat`
- `requests`

If using Visual Studio Code the following tasks will be available

- `Clean .pyc`: clean .pyc files.
- `Toggle UI Color`: Toggle widget color state.
- `RunApp`: Run application locally.

## Usage

Simple create the cookiecutter template in `~/.nuke` or in your `pluginsPath` and import it in your menu.py. The plugin will be available in: Windows -> Custom.

## Run Local

To run the application outside of Nuke, [Poetry](https://python-poetry.org) is used as a package manager to
install the dependencies.

Poetry assumes that Python3 will be used. If Python3 syntax is avoided, there shouldn't be any problem when using <= Nuke 12. However, if Python2 is preferred, one could change the python version in the _pyproject.toml_ or use the requirements.txt to install the base dependencies.

> When using Python2 inside pyproject.toml there may be some dependencies issues due to version restrictions.

Once the dependencies have been installed:

- `poetry run python -m src.run_local`: to run the app.
- `poetry run pytest`: to test the app.

## Custom `nuke` module

If invoking a `nuke` command outside Nuke will obviously throw an exception.

Although limited in some regards, in order to run the application outside Nuke, a "fake" `nuke` module must be created. This allows the application to successfully import `nuke` as a package and search inside for the method invoked.

This requires the user to write its own version of the `nuke` method called. The method
could be implemented just as a placeholder and does not require an exact copy of the builtin module.

Example:

If invoking `nuke.createNode('Blur')`, the fake `nuke` module must have a function named `createNode(arg)`. The return of the function depends on the application requirements. It could be a string placeholder or a custom `Node` class with some methods.

Some action could not be faked, but the for the majority it will work. For a code example check here: [ProfileInspector](https://github.com/sisoe24/ProfileInspector/blob/f4320395219c47aaab6c22bed9b0791ec6b911a4/src/_nuke/fake_nuke.py#L22)

## Install `cookiecutter` ([Official Instructions](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter))

```bash
python3 -m pip install --user cookiecutter
```
