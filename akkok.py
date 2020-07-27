# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'akkok.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from saatkayit import Ui_hesap

class Ui_MainWindow(object):
    def yeniac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_hesap()
        self.ui.setupUi(self.pencere)
        self.pencere.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 256)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 101, 41))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 41))
        self.label.setObjectName("label")
        self.ad_soyad_2 = QtWidgets.QLabel(self.centralwidget)
        self.ad_soyad_2.setGeometry(QtCore.QRect(410, 80, 71, 21))
        self.ad_soyad_2.setObjectName("ad_soyad_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 80, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(520, 130, 161, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 130, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.ad_soyad_4 = QtWidgets.QLabel(self.centralwidget)
        self.ad_soyad_4.setGeometry(QtCore.QRect(270, 130, 81, 31))
        self.ad_soyad_4.setObjectName("ad_soyad_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(360, 130, 101, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.ad_soyad_3 = QtWidgets.QLabel(self.centralwidget)
        self.ad_soyad_3.setGeometry(QtCore.QRect(30, 130, 131, 31))
        self.ad_soyad_3.setObjectName("ad_soyad_3")
        self.ad_soyad_5 = QtWidgets.QLabel(self.centralwidget)
        self.ad_soyad_5.setGeometry(QtCore.QRect(470, 130, 51, 31))
        self.ad_soyad_5.setObjectName("ad_soyad_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 30, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 41, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 80, 211, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(520, 180, 161, 31))
        self.btn_open.setObjectName("btn_open")
        
        self.btn_open.clicked.connect(self.yeniac)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 71, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 0, 211, 22))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "İŞE GİRİŞ TARİHİ"))
        self.label.setText(_translate("MainWindow", "ADI"))
        self.ad_soyad_2.setText(_translate("MainWindow", "MAAŞ:"))
        self.ad_soyad_4.setText(_translate("MainWindow", "MESAİ TOPLAM"))
        self.ad_soyad_3.setText(_translate("MainWindow", "GELMEDİĞİ SAAT TOPLAM"))
        self.ad_soyad_5.setText(_translate("MainWindow", "HAKEDİŞ"))
        self.label_2.setText(_translate("MainWindow", "SOYADI"))
        self.btn_open.setText(_translate("MainWindow", "YAZDIR"))
        self.label_4.setText(_translate("MainWindow", "ADI SOYADI :"))
