from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget


class tabPageWidget (QWidget):

    add_library_signal = Signal(str)
    add_reader_signal = Signal(str)

    def __init__(self):
        super().__init__()