from PyQt5.QtWidgets import QApplication
import sys
from gestureapp.guis.login.gesturelogin import GestureLogin
from gestureapp.guis.tip.gesturetip import GestureTip
from gestureapp.guis.home.gesturehome import GestureHome 
from gestureapp.guis.eval.gestureeval import GestureEval

class GestureApp(QApplication):
    def __init__(self):
        super(GestureApp, self).__init__(sys.argv)
        self.login = GestureLogin()
        self.login.signal_home.connect(self.recv_login_info)
        self.login.show()

    def recv_login_info(self):
        self.tip = GestureTip()
        self.tip.ui.pushButton.clicked.connect(self.recv_tip_info)
        self.tip.ui.pushButton_2.clicked.connect(self.exit)
        self.tip.show()
        self.login.close()
    
    def recv_tip_info(self):
        self.home = GestureHome()
        self.home.ui.pushButton.clicked.connect(self.recv_home_info)
        self.home.display_th.signal_change.connect(self.recv_home_info)
        self.home.show()
        self.tip.close()

    def recv_home_info(self):
        self.eval = GestureEval(self.home.grade)
        self.eval.ui.pushButton.clicked.connect(self.recv_eval_info)
        self.eval.ui.pushButton_2.clicked.connect(self.exit)
        self.eval.show()
    
    def recv_eval_info(self):
        self.tip = GestureTip()
        self.tip.ui.pushButton.clicked.connect(self.recv_tip_info)
        self.tip.ui.pushButton_2.clicked.connect(self.exit)
        self.tip.show()
        self.home.close()
        self.eval.close()
        