from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from PyQt5.QtGui import QImage, QPixmap
import os

dic = {
    7:"../../biz/home/img/7.png",
    6:"../../biz/home/img/6.png",
    5:"../../biz/home/img/5.png",
    4:"../../biz/home/img/4.png",
    3:"../../biz/home/img/3.png",
    2:"../../biz/home/img/2.png",
    1:"../../biz/home/img/1.png",
    "perfect":"../../biz/home/img/perfect.png",
    "great":"../../biz/home/img/great.png",
    "sorry":"../../biz/home/img/sorry.png"
}

class JudgeThread(QThread):

    signal_judge = pyqtSignal(int, int, int, bytes)
    signal_score = pyqtSignal(int)

    def __init__(self):
        super(JudgeThread, self).__init__()
        self.ok = False
        current_dir = os.path.dirname(__file__)
        for i in dic:
            dic[i] = os.path.join(current_dir, dic[i])
    
    def run(self):
        for i in range(20):
            self.ok = False
            for j in (7, 6, 5, 4, 3, 2, 1):
                self.count_down(j)
                if self.ok:
                    QThread.sleep(1)
                    break
            if not self.ok:
                self.filename = dic["sorry"]
                self.img = cv2.imread(self.filename)
                h, w, c = self.img.shape
                self.signal_judge.emit(h, w, c, self.img.tobytes())
                QThread.sleep(1)
            
    def count_down(self, t):
        self.filename = dic[t]
        self.img = cv2.imread(self.filename)
        h, w, c = self.img.shape
        self.signal_judge.emit(h, w, c, self.img.tobytes())
        for i in range(10):
            QThread.usleep(100000)
            if self.ok:
                if t > 4:
                    self.filename = dic["perfect"]
                    self.signal_score.emit(5)
                else:
                    self.filename = dic["great"]
                    self.signal_score.emit(3)
                self.img = cv2.imread(self.filename)
                h, w, c = self.img.shape
                self.signal_judge.emit(h, w, c, self.img.tobytes())
                break
    
    def close(self):
        self.terminate()