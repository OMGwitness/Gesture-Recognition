from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from PyQt5.QtGui import QImage, QPixmap
from random import random
import os

lis = ["../../biz/home/img/good.png",
       "../../biz/home/img/bad.png",
       "../../biz/home/img/666.png",
       "../../biz/home/img/yeah.png",
       "../../biz/home/img/ok.png",
       "../../biz/home/img/gun.png",
       "../../biz/home/img/pray.png",
       "../../biz/home/img/c.png",
       "../../biz/home/img/fist.png",
       "../../biz/home/img/love.png"
]

class DisplayThread(QThread):

    signal_display = pyqtSignal(int, int, int, bytes)
    signal_num = pyqtSignal(int)
    signal_change = pyqtSignal()

    def __init__(self):
        super(DisplayThread, self).__init__()
        self.ok = False
        current_dir = os.path.dirname(__file__)
        for i in range(10):
            lis[i]= os.path.join(current_dir, lis[i])
    
    def run(self):
        for i in range(20):
            self.ok = False
            num = (int)(random()*10)
            self.filename = lis[num]
            self.signal_num.emit(num)
            self.img = cv2.imread(self.filename)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            h, w, c = self.img.shape
            self.signal_display.emit(h, w, c, self.img.tobytes())
            for i in range(80):
                if self.ok:
                    QThread.sleep(1)
                    break
                QThread.usleep(100000)
        self.signal_change.emit()
    
    def close(self):
        self.terminate()