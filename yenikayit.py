# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yenikayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.label_3.setObjectName("label_3")
        self.ad_soyad_2 = QtWidgets.QLabel(self.centralwidget)
        self.ad_soyad_2.setGeometry(QtCore.QRect(370, 70, 71, 21))
        self.ad_soyad_2.setObjectName("ad_soyad_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 70, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 41, 41))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 20, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 70, 211, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.btn_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kaydet.setGeometry(QtCore.QRect(170, 140, 181, 31))
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 111, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 110, 211, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 100, 61, 41))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 110, 211, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.btn_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikis.setGeometry(QtCore.QRect(480, 140, 181, 31))
        self.btn_cikis.setObjectName("btn_cikis")


        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menubar.setObjectName("menubar")
        self.menuKAYIT = QtWidgets.QMenu(self.menubar)
        self.menuKAYIT.setObjectName("menuKAYIT")
        self.menuD_zenle = QtWidgets.QMenu(self.menubar)
        self.menuD_zenle.setObjectName("menuD_zenle")
        self.menuMaa_Yazd_r = QtWidgets.QMenu(self.menubar)
        self.menuMaa_Yazd_r.setObjectName("menuMaa_Yazd_r")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuKAYIT.menuAction())
        self.menubar.addAction(self.menuD_zenle.menuAction())
        self.menubar.addAction(self.menuMaa_Yazd_r.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "İŞE GİRİŞ TARİHİ"))
        self.ad_soyad_2.setText(_translate("MainWindow", "MAAŞ:"))
        self.label_2.setText(_translate("MainWindow", "SOYADI"))
        self.label.setText(_translate("MainWindow", "ADI"))
        self.btn_kaydet.setText(_translate("MainWindow", "KAYDET"))
        self.label_4.setText(_translate("MainWindow", "BANKA ADI"))
        self.label_5.setText(_translate("MainWindow", "HESAP NO:"))
        self.btn_cikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.menuKAYIT.setTitle(_translate("MainWindow", "Yeni Kayıt"))
        self.menuD_zenle.setTitle(_translate("MainWindow", "Düzenle"))
        self.menuMaa_Yazd_r.setTitle(_translate("MainWindow", "Maaş Yazdır"))
