# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saatkayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hesap(object):
    def setupUi(self, hesap):
        hesap.setObjectName("hesap")
        hesap.resize(811, 252)
        self.centralwidget = QtWidgets.QWidget(hesap)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 120, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 160, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 160, 141, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        hesap.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hesap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        hesap.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hesap)
        self.statusbar.setObjectName("statusbar")
        hesap.setStatusBar(self.statusbar)

        self.retranslateUi(hesap)
        QtCore.QMetaObject.connectSlotsByName(hesap)

    def retranslateUi(self, hesap):
        _translate = QtCore.QCoreApplication.translate
        hesap.setWindowTitle(_translate("hesap", "MainWindow"))
        self.label.setText(_translate("hesap", "ADI SOYADI :"))
        self.radioButton.setText(_translate("hesap", "GELMEDİ"))
        self.radioButton_2.setText(_translate("hesap", "MESAİ NORMAL"))
        self.radioButton_3.setText(_translate("hesap", "MESAİ RESMİ TATİL"))
        self.label_2.setText(_translate("hesap", "SAAT"))
        self.pushButton.setText(_translate("hesap", "Kaydet"))
        self.pushButton_2.setText(_translate("hesap", "Çıkış"))
        self.pushButton_3.setText(_translate("hesap", "Yeni Kayit"))
