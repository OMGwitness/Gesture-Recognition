from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from yolov4_gesture.gesturedet import GestureDetector
from gestureapp.biz.home.gestures import GestureDAO

class GestureThread(QThread):
    signal_gesture = pyqtSignal(int, int, int, bytes, bool) 
    def __init__(self):
        super(GestureThread, self).__init__()
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.is_ok = False
        # 构建一个智能侦测对象
        self.detector = GestureDetector()
        # 识别结果存储
        self.gestures = []
        self.counter = 0
        # 数据验证模块
        self.dao = GestureDAO()
        self.num = -1

    def run(self):
        while not self.is_ok:
            # 采集视频
            status, frame = self.dev.read()
            if not status:
                self.is_ok = True
                continue
            # 发送信号
            h, w, c = frame.shape
            # 做登录检测，与验证，
            home_ok = False
            # frame = self.detector.detect_mark(frame)
            pred = self.detector.detect(frame)
            if pred is not None:
                # 循环处理识别结果
                for x1, y1, x2, y2, p, cls_id in pred:
                    # 概率过滤
                    if p > 0.2:
                        cls_id = int(cls_id)
                        name = self.detector.get_name(cls_id)
                        self.gestures.append(name)
                        self.counter += 1
                        # 实现标注
                        x1 = int(x1)
                        y1 = int(y1)
                        x2 = int(x2)
                        y2 = int(y2)
                        cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=4)
                        cv2.putText(
                            frame, 
                            F"{name}:{p:.2f}", 
                            org=(x1, y1 - 50 ), 
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.5,
                            color=(0, 0, 255),
                            thickness=1)
            if self.counter >= 1:
                # 验证/先取识别最多的人名
                most_name = max(self.gestures, key=self.gestures.count)
                # 调用业务模块，验证
                home_ok = self.dao.validate(most_name, self.num)
                self.counter = 0
                self.gestures = [] 
            frame = frame[:,:,::-1]
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.signal_gesture.emit(h, w, c, frame.tobytes(), home_ok)
            if home_ok:
                QThread.sleep(1)
            QThread.usleep(10000)

    def close(self):
        self.is_ok=True
        # 结束线程-暴力型
        self.terminate()
        # while isRunning():
        #     pass
        # 释放设备
        self.dev.release()