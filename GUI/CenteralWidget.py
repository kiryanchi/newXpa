from UI.CenteralWidget.CenteralWidget import Ui_CenteralWidget
from PyQt5.QtWidgets import QWidget


class MyCenteralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CenteralWidget()
        self.ui.setupUi(self)