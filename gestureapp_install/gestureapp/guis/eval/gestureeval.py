from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5 import QtGui
from gestureapp.guis.eval.evalui import Ui_eval
from PyQt5.QtCore import Qt


class GestureEval(QDialog):
    def __init__(self, grade):
        super(GestureEval, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui = Ui_eval()
        self.ui.setupUi(self)
        self.ui.label.setText(F"恭喜完成游戏!\n\n您的得分为:{grade}分!\n")
