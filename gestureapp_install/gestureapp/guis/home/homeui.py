# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_home(object):
    def setupUi(self, home):

        current_dir = os.path.dirname(__file__)
        self.img_file = os.path.join(current_dir, "background.png")

        home.setObjectName("home")
        home.resize(1000, 600)
        home.setStyleSheet("")
        self.label1 = QtWidgets.QLabel(home)
        self.label1.setGeometry(QtCore.QRect(50, 50, 350, 350))
        self.label1.setStyleSheet("QLabel#label1{\n"
"    border-radius:20px;\n"
"    border-style:dashed;\n"
"    border-width:2px;\n"
"}")
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(home)
        self.label2.setGeometry(QtCore.QRect(600, 50, 350, 350))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label2.setFont(font)
        self.label2.setStyleSheet("QLabel#label2{\n"
"    border-radius:20px;\n"
"    border-style:dashed;\n"
"    border-width:2px;\n"
"}")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.textBrowser1 = QtWidgets.QTextBrowser(home)
        self.textBrowser1.setGeometry(QtCore.QRect(125, 420, 200, 55))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        self.textBrowser1.setFont(font)
        self.textBrowser1.setStyleSheet("")
        self.textBrowser1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser1.setObjectName("textBrowser1")
        self.textBrowser2 = QtWidgets.QTextBrowser(home)
        self.textBrowser2.setGeometry(QtCore.QRect(675, 420, 200, 55))
        self.textBrowser2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser2.setObjectName("textBrowser2")
        self.label3 = QtWidgets.QLabel(home)
        self.label3.setGeometry(QtCore.QRect(450, 120, 100, 100))
        self.label3.setStyleSheet("QLabel#label3{\n"
"    border-radius:20px;\n"
"    border-style:dashed;\n"
"    border-width:2px;\n"
"}")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.pushButton = QtWidgets.QPushButton(home)
        self.pushButton.setGeometry(QtCore.QRect(400, 500, 200, 50))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(home)
        self.label.setGeometry(QtCore.QRect(-160, 0, 1161, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.img_file))
        self.label.setObjectName("label")
        self.label.raise_()
        self.label1.raise_()
        self.label2.raise_()
        self.textBrowser1.raise_()
        self.textBrowser2.raise_()
        self.label3.raise_()
        self.pushButton.raise_()

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "手势识别小游戏"))
        self.label1.setText(_translate("home", "展示区"))
        self.label2.setText(_translate("home", "视频采集区"))
        self.textBrowser1.setHtml(_translate("home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'田氏颜体大字库\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#2067ff;\">展示区</span></p></body></html>"))
        self.textBrowser2.setHtml(_translate("home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'田氏颜体大字库\'; font-size:28pt; color:#ff0000;\">视频区</span></p></body></html>"))
        self.label3.setText(_translate("home", "判别区"))
        self.pushButton.setText(_translate("home", "查 看 分 数"))