from PyQt5.QtWidgets import QDialog
from gestureapp.guis.tip.tipui import Ui_tip
from PyQt5.QtCore import Qt

class GestureTip(QDialog):
    def __init__(self):
        super(GestureTip, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui = Ui_tip()
        self.ui.setupUi(self)
