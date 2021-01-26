# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1045, 574)
        MainWindow.setWindowIcon(QtGui.QIcon('Dice.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Кнопка 1
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 510, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(35)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(150, 150))
        self.pushButton.setShortcut("")
        self.pushButton.setObjectName("pushButton")
        # Кнопка 2
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setGeometry(QtCore.QRect(980, 510, 40, 40))
        self.pushButton2.setIcon(icon2)
        self.pushButton2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton2.setFont(font)
        self.pushButton2.setIconSize(QtCore.QSize(150, 150))
        self.pushButton2.setShortcut("")
        self.pushButton2.setObjectName("pushButton")
        # Кнопка 3
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(930, 510, 40, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton3.setIcon(icon3)
        self.pushButton3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton3.setFont(font)
        self.pushButton3.setIconSize(QtCore.QSize(150, 150))
        self.pushButton3.setShortcut("")
        self.pushButton3.setObjectName("pushButton")
        # Кнопка NEW_window
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(880, 510, 40, 40))
        self.pushButton4.setFont(font)
        self.pushButton4.setIconSize(QtCore.QSize(150, 150))
        self.pushButton4.setShortcut("")
        self.pushButton4.setObjectName("Window")
        #Кнопка переноса данных 0-50
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(792, 507, 78, 23))
        self.pushButton5.setFont(font)
        self.pushButton5.setIconSize(QtCore.QSize(150, 150))
        self.pushButton5.setShortcut("")
        self.pushButton5.setObjectName("Copy")
        # Кнопка переноса данных 50-100
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(792, 530, 78, 23))
        self.pushButton6.setFont(font)
        self.pushButton6.setIconSize(QtCore.QSize(150, 150))
        self.pushButton6.setShortcut("")
        self.pushButton6.setObjectName("Copy2")
        # lineedit1
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(285, 509, 20, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 508, 220, 20))
        self.label.setFont(QtGui.QFont("TimesNewRoman", 10))
        # lineedit2
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(285, 534, 20, 19))
        self.lineEdit2.setObjectName("lineEdit")
        self.lineEdit2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(60, 533, 220, 20))
        self.label2.setFont(QtGui.QFont("TimesNewRoman", 10))
        # Виджеты
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1, 10, 1040, 115))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(25)
        self.tableWidget.setRowCount(3)
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(1, 135, 1040, 115))
        self.tableWidget2.setObjectName("tableWidget")
        self.tableWidget2.setColumnCount(25)
        self.tableWidget2.setRowCount(3)
        self.tableWidget3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget3.setGeometry(QtCore.QRect(1, 260, 1040, 115))
        self.tableWidget3.setObjectName("tableWidget")
        self.tableWidget3.setColumnCount(25)
        self.tableWidget3.setRowCount(3)
        self.tableWidget4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget4.setGeometry(QtCore.QRect(1, 385, 1042, 115))
        self.tableWidget4.setObjectName("tableWidget")
        self.tableWidget4.setColumnCount(25)
        self.tableWidget4.setRowCount(3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random"))
        self.label.setText(_translate("MainWindow", "Введите количество тест-объектов:"))
        self.label2.setText(_translate("MainWindow", "Введите количество тест-предметов:"))
        self.pushButton5.setText(_translate("MainWindow", "Copy 0-50"))
        self.pushButton5.setFont(QtGui.QFont("TimesNewRoman", 9))
        self.pushButton6.setFont(QtGui.QFont("TimesNewRoman", 9))
        self.pushButton6.setText(_translate("MainWindow", "Copy 50-100"))
        self.pushButton4.setText(_translate("MainWindow", "ГСЧ"))
        self.pushButton4.setFont(QtGui.QFont("TimesNewRoman", 12))
        # self.pushButton.setText(_translate("MainWindow", "Пуск"))
        # self.pushButton2.setText(_translate("MainWindow", "Печать"))
        # self.pushButton3.setText(_translate("MainWindow", "Просмотр"))

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow2")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 110, 80, 50))
        self.pushButton.setObjectName("PushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор случайных чисел"))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.label.setText(_translate("MainWindow", "Введите начальное число:"))
        self.label_2.setText(_translate("MainWindow", "Введите конечное число:"))
        self.label_3.setText(_translate("MainWindow", "Результат:"))