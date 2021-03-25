# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Login(object):
    def setupUi(self, Login):

        current_dir = os.path.dirname(__file__)
        self.img_file = os.path.join(current_dir, "background.png")
        self.font_file = os.path.join(current_dir, "../田氏颜体大字库.ttf")

        Login.setObjectName("Login")
        Login.resize(1023, 600)
        Login.setStyleSheet("")
        self.lbl_title = QtWidgets.QLabel(Login)
        self.lbl_title.setGeometry(QtCore.QRect(120, 10, 91, 521))
        QtGui.QFontDatabase.addApplicationFont(self.font_file)
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_version = QtWidgets.QLabel(Login)
        self.lbl_version.setGeometry(QtCore.QRect(610, 540, 68, 20))
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_subtitle = QtWidgets.QLabel(Login)
        self.lbl_subtitle.setGeometry(QtCore.QRect(540, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_subtitle.setFont(font)
        self.lbl_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_subtitle.setObjectName("lbl_subtitle")
        self.line = QtWidgets.QFrame(Login)
        self.line.setGeometry(QtCore.QRect(7, 560, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lbl_face_video = QtWidgets.QLabel(Login)
        self.lbl_face_video.setGeometry(QtCore.QRect(330, 130, 661, 381))
        self.lbl_face_video.setMaximumSize(QtCore.QSize(16777215, 381))
        self.lbl_face_video.setStyleSheet("QLabel#lbl_face_video{\n"
"    border-radius:20px;\n"
"    border-style:dashed;\n"
"    border-width:2px;\n"
"}")
        self.lbl_face_video.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_face_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_face_video.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_face_video.setObjectName("lbl_face_video")
        self.line_2 = QtWidgets.QFrame(Login)
        self.line_2.setGeometry(QtCore.QRect(97, 30, 20, 541))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Login)
        self.line_3.setGeometry(QtCore.QRect(37, 530, 271, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Login)
        self.line_4.setGeometry(QtCore.QRect(70, 70, 20, 521))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Login)
        self.line_5.setGeometry(QtCore.QRect(540, 80, 201, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Login)
        self.line_6.setGeometry(QtCore.QRect(610, 90, 191, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Login)
        self.line_7.setGeometry(QtCore.QRect(560, 40, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(-80, 0, 1151, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.img_file))
        self.label.setObjectName("label")
        self.label.raise_()
        self.lbl_title.raise_()
        self.lbl_version.raise_()
        self.lbl_subtitle.raise_()
        self.line.raise_()
        self.lbl_face_video.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "手势识别小游戏"))
        self.lbl_title.setText(_translate("Login", "手\n"
"势\n"
"识\n"
"别\n"
"小\n"
"游\n"
"戏"))
        self.lbl_version.setText(_translate("Login", "v 1.0"))
        self.lbl_subtitle.setText(_translate("Login", "智 能 登 录"))
        self.lbl_face_video.setText(_translate("Login", "登录视频"))
