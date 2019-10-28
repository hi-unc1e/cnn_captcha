# -*- coding: utf-8 -*-

import os
import shutil
import sys

# Form implementation generated from reading ui file 'HelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver


class Ui_MainWindow(object):
    def getverify(self):
        shutil.copyfile('codeImage.png', os.path.join('./verify', self.lineEdit.text() + '.jpg'))
        global driver, img

        img.click()
        # 页面截图
        driver.get_screenshot_as_file(os.path.join('.', 'screenshot.png'))
        im = Image.open(os.path.join('.', 'screenshot.png'))
        # 验证码位置
        box = [194, 387, 268, 416]
        region = im.crop(box)
        region.save(os.path.join('.', 'codeImage.png'))
        pix = QPixmap('codeImage.png')
        self.label.setPixmap(pix)
        self.lineEdit.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 370, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 100, 151, 141))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 300, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getverify)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        global driver
        img = driver.find_element_by_id('img')
        img.click()
        # 页面截图
        driver.get_screenshot_as_file(os.path.join('.', 'screenshot.png'))
        im = Image.open(os.path.join('.', 'screenshot.png'))
        # 验证码位置
        box = [194, 387, 268, 416]
        region = im.crop(box)
        region.save(os.path.join('.', 'codeImage.png'))
        pix = QPixmap('codeImage.png')
        self.label.setPixmap(pix)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "提交"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == '__main__':
    url = 'http://jw.xujc.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    img = driver.find_element_by_id('img')
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    pix = QPixmap('codeImage.png')
    ui.label.setPixmap(pix)
    sys.exit(app.exec_())