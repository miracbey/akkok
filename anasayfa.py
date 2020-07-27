# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from yenikayit import Ui_MainWindow
import mysql.connector
import sys

class Ui_anasayfa(object):

    def combo(self):
        self.mydb = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "akkok")
        self.mycursor = self.mydb.cursor()        
        self.mycursor.execute('''SELECT adi FROM calisanlar''')
        data = self.mycursor.fetchall()
        for i in data :
            print(i[0])
            self.comboBox.addItem(i[0])
        



    def yeniac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.pencere)
        self.pencere.show()
        

    
    




    def setupUi(self, anasayfa):
        anasayfa.setObjectName("anasayfa")
        anasayfa.resize(811, 252)
        self.centralwidget = QtWidgets.QWidget(anasayfa)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 30, 261, 22))
        self.comboBox.setObjectName("comboBox")

    


        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(470, 10, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 80, 81, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 80, 111, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(270, 80, 121, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(100, 120, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 122, 51, 21))
        self.label_2.setObjectName("label_2")
        self.btn_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kaydet.setGeometry(QtCore.QRect(240, 120, 141, 23))
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikis.setGeometry(QtCore.QRect(40, 160, 141, 23))
        self.btn_cikis.setObjectName("btn_cikis")

        

        self.btn_yenikayit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yenikayit.setGeometry(QtCore.QRect(240, 160, 141, 23))
        self.btn_yenikayit.setObjectName("btn_yenikayit")

        self.btn_yenikayit.clicked.connect(self.yeniac)

        anasayfa.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(anasayfa)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        anasayfa.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(anasayfa)
        self.statusbar.setObjectName("statusbar")
        anasayfa.setStatusBar(self.statusbar)

        self.retranslateUi(anasayfa)
        QtCore.QMetaObject.connectSlotsByName(anasayfa)

    def retranslateUi(self, anasayfa):
        _translate = QtCore.QCoreApplication.translate
        anasayfa.setWindowTitle(_translate("anasayfa", "MainWindow"))
        self.label.setText(_translate("anasayfa", "ADI SOYADI :"))
        self.radioButton.setText(_translate("anasayfa", "GELMEDİ"))
        self.radioButton_2.setText(_translate("anasayfa", "MESAİ NORMAL"))
        self.radioButton_3.setText(_translate("anasayfa", "MESAİ RESMİ TATİL"))
        self.label_2.setText(_translate("anasayfa", "SAAT"))
        self.btn_kaydet.setText(_translate("anasayfa", "Kaydet"))
        self.btn_cikis.setText(_translate("anasayfa", "Çıkış"))
        self.btn_yenikayit.setText(_translate("anasayfa", "Yeni Kayit"))
