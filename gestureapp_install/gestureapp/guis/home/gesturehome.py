from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from gestureapp.guis.home.homeui import Ui_home
from gestureapp.devs.home.displaydev import DisplayThread
from gestureapp.devs.home.gesturedev import GestureThread
from gestureapp.devs.home.judgedev import JudgeThread
from PyQt5.QtGui import QImage, QPainter, QPainterPath, QPixmap
from PyQt5.QtCore import Qt, QRect, QRectF, pyqtSignal

class GestureHome(QDialog):

    signal_grade = pyqtSignal(int)

    def __init__(self):
        super(GestureHome, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui = Ui_home()
        self.ui.setupUi(self)
        self.grade = 0

        # 摄像头
        self.gesture_th = GestureThread()
        self.gesture_th.signal_gesture.connect(self.show_video)
        self.gesture_th.start()

        # 展示区
        self.display_th = DisplayThread()
        self.display_th.signal_display.connect(self.show_display)
        self.display_th.signal_num.connect(self.change_num)
        self.display_th.start()

        # 判别区
        self.judge_th = JudgeThread()
        self.judge_th.signal_judge.connect(self.show_judge)
        self.judge_th.signal_score.connect(self.cal_grade)
        self.judge_th.start()
    
    def show_video(self, h, w, c, data, home_ok):
        qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)
        qpixmap = self.getRoundRectPixmap(qpixmap, QRectF(2, 2, w, h), 30)
        self.ui.label2.setPixmap(qpixmap)
        self.ui.label2.setScaledContents(True)
        if not self.display_th.ok:
            self.display_th.ok = home_ok
        if not self.judge_th.ok:
            self.judge_th.ok = home_ok

    def show_display(self, h, w, c, data):
        qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)
        qpixmap = self.getRoundRectPixmap(qpixmap, QRectF(2, 2, w, h), 30)
        self.ui.label1.setPixmap(qpixmap)
        self.ui.label1.setScaledContents(True)        

    def show_judge(self, h, w, c, data):
        qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)
        qpixmap = self.getRoundRectPixmap(qpixmap, QRectF(2, 2, w, h), 30)
        self.ui.label3.setPixmap(qpixmap)
        self.ui.label3.setScaledContents(True)
    
    def getRoundRectPixmap(self, srcPixMap, rect, radius):
        # //不处理空数据或者错误数据
        if srcPixMap.isNull():
            return srcPixMap
        imageWidth = rect.width()
        imageHeight = rect.height()
        # //处理大尺寸的图片,保证图片显示区域完整
        newPixMap = srcPixMap.scaled(imageWidth, (imageWidth if imageHeight == 0 else imageHeight), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        destImage = QPixmap(imageWidth, imageHeight)
        destImage.fill(QtCore.Qt.transparent)
        painter = QPainter(destImage)
        # // 抗锯齿
        painter.setRenderHints(QPainter.Antialiasing, True)
        # // 图片平滑处理
        painter.setRenderHints(QPainter.SmoothPixmapTransform, True)
        # // 将图片裁剪为圆角
        path = QPainterPath()
        path.addRoundedRect(rect, radius, radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, imageWidth, imageHeight, newPixMap)
        return destImage
    
    def change_num(self, num):
        self.gesture_th.num = num
    
    def cal_grade(self, score):
        self.grade += score

    def closeEvent(self, event):
        self.gesture_th.dev.release()
        self.gesture_th.close()
        self.display_th.close()
        self.judge_th.close()