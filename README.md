# Nuke Pyside2 Template

A Python PySide2 cookiecutter template for Nuke.

## Description

This project is a cookiecutter template to create a basic application in Nuke with PySide2.

## Features

The template includes:

- A ready-to-use QMainWindow with a QToolbar and a QStatusBar.
  - The toolbar offers an "About" widget with information about the application.
- A custom QMessageBox for errors and bug reports.
- A test environment with `pytest` and some sample tests to startup.
- A wrapper function to color a QWidget for layout testing.
- A startup logging module.
- The ability to launch the plugin as a standalone application, i.e., outside Nuke.

If using Visual Studio Code the following tasks will be available

- `Clean .pyc`: clean .pyc files.
- `Toggle UI Color`: Toggle widget color state.
- `RunApp`: Run application locally.

## Usage

1. Install `cookiecutter`: [Official Documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)
2. Create the cookiecutter template in `~/.nuke` or in your custom path with the following command:
  
    ```sh
    cookiecutter https://github.com/sisoe24/nuke-pyside-template
    ```

3. Import the created package in your `menu.py`.

You can find the new plugin inside Nuke -> Window -> Custom or you can run the application in [standalone](#run-local).

### Add your widget

You can add new widgets inside the class `src/main.py->MainWindowWidgets`

### Color Widget 

Inside `src/utils` there is a `color_widget.py` module that can be used as a wrapper to randomly color a QWidget. I often use this when I need to visually see the layout of some widgets.

The wrapper only works on an `__init__` method of a QWidget class instance.

```py
class Widget(QWidget):
    @color_widget
    def __init__(self):
        QWidget.__init__(self)
```

> You can toggle the color state with the vscode command `Toggle UI Color`.

## Tests

Some sample tests are already included using `pytest`.

### Fixtures

- `_main_ui`: which initializes the main UI.
- `_package`: the package root directory.

### Markers

- `_rapidtest`

## Git-Hooks

There is an inactive git hook inside `.githook` which uses `poetry` to run the tests before a push.

To use the hook you can:

1. Comment the code
2. Move the hook inside `.git/hooks` or enable `.githooks` as a folder with `git config core.hooksPath .githooks`

## Run Standalone

To run the application outside Nuke, you must install the package dependencies. You can do so with the `pyproject.toml` or the `requirements.txt`.

Note that `pyproject.toml` assumes you will use Python 3.

I am using `poetry` as the package manager for this example:

- `poetry install`: install dependency
- `poetry run python -m src.run_local`: to run the app.
- `poetry run pytest`: to test the app.

### How it works

I decided to go about this by creating a fake nuke module inside my directory. In this way, I can import nuke outside Nuke with no errors.

So let's say, for example, your application uses the `nuke.getFilename` function. Launching the application in standalone mode and executing that piece of code will throw an error.

With the fake nuke module, you can create your version of the `nuke.getFilename` (e.g., creating a QFileDialog). This way, you keep your code the same but run the application in standalone mode.

This will require some extra code sometimes, but it gives you much freedom regarding rapid prototyping and testing.

For an example check here: [ProfileInspector](https://github.com/sisoe24/ProfileInspector/blob/f4320395219c47aaab6c22bed9b0791ec6b911a4/src/_nuke/fake_nuke.py#L22)
