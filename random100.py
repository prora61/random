from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
from qq import Ui_MainWindow, Ui_MainWindow2 # импорт нашего сгенерированного файла
import random
import sys
from PyQt5.QtWidgets import QTableWidgetItem

global A, B, W

class mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ranran)

    def ranran(self):
        self.errors()

    def errors(self):
        try:
            A = self.ui.lineEdit.text()
            B = self.ui.lineEdit_2.text()
            num1 = int(A)
            num2 = int(B)
            if (int(A) > int(B)):
                raise Exception('Конечное число меньше начального значения')
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введите два целых числа')
            self.ui.lineEdit_3.clear()
        except Exception:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Конечное число меньше начального значения')
            self.ui.lineEdit_3.clear()
        else:
            k = random.randint(int(A), int(B))
            self.ui.lineEdit_3.setText(str(k))

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.clickbut)
        self.ui.pushButton2.clicked.connect(self.print_doc)
        self.ui.pushButton3.clicked.connect(self.preview)
        self.ui.pushButton4.clicked.connect(self.new_form)
        self.ui.tableWidget.setHorizontalHeaderLabels(["j=1", "j=2", "j=3", "j=4", "j=5", "j=6", "j=7", "j=8", "j=9", "j=10", "j=11",
                                                       "j=12", "j=13", "j=14", "j=15", "j=16", "j=17", "j=18", "j=19", "j=20", "j=21",
                                                       "j=22", "j=23", "j=24", "j=25"])
        self.ui.tableWidget2.setHorizontalHeaderLabels(["j=26", "j=27", "j=28", "j=29", "j=30", "j=31", "j=32", "j=33",
                                                        "j=34", "j=35", "j=36", "j=37", "j=38", "j=39", "j=40", "j=41", "j=42",
                                                        "j=43", "j=44", "j=45", "j=46", "j=47", "j=48", "j=49", "j=50"])
        self.ui.tableWidget3.setHorizontalHeaderLabels(["j=51", "j=52", "j=53", "j=54", "j=55", "j=56", "j=57", "j=58", "j=59",
                                                        "j=60", "j=61", "j=62", "j=63", "j=64", "j=65", "j=66", "j=67", "j=68",
                                                        "j=69", "j=70", "j=71", "j=72", "j=73", "j=74", "j=75"])
        self.ui.tableWidget4.setHorizontalHeaderLabels(["j=76", "j=77", "j=78", "j=79", "j=80", "j=81", "j=82", "j=83", "j=84",
                                                        "j=85", "j=86", "j=87", "j=88", "j=89", "j=90", "j=91", "j=92", "j=93",
                                                        "j=94", "j=95", "j=96", "j=97", "j=98", "j=99", "j=100"])
        # Изменение шрифта и форматирование
        self.ui.tableWidget.setVerticalHeaderLabels(['Индекс испытания Gj', 'Индекс тест-объекта', 'Индекс тест-предмета'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size: 8pt; }")
        self.ui.tableWidget.verticalHeader().setStyleSheet("QHeaderView { font-size: 9pt; }")
        self.ui.tableWidget.setFont(QtGui.QFont("TimesNewRoman", 9))
        self.ui.tableWidget.resizeColumnsToContents()

        self.ui.tableWidget2.setVerticalHeaderLabels(['Индекс испытания Gj', 'Индекс тест-объекта', 'Индекс тест-предмета'])
        self.ui.tableWidget2.horizontalHeader().setStyleSheet("QHeaderView { font-size: 8pt; }")
        self.ui.tableWidget2.verticalHeader().setStyleSheet("QHeaderView { font-size: 9pt; }")
        self.ui.tableWidget2.setFont(QtGui.QFont("TimesNewRoman", 9))
        self.ui.tableWidget2.resizeColumnsToContents()

        self.ui.tableWidget3.setVerticalHeaderLabels(['Индекс испытания Gj', 'Индекс тест-объекта', 'Индекс тест-предмета'])
        self.ui.tableWidget3.horizontalHeader().setStyleSheet("QHeaderView { font-size: 8pt; }")
        self.ui.tableWidget3.verticalHeader().setStyleSheet("QHeaderView { font-size: 9pt; }")
        self.ui.tableWidget3.setFont(QtGui.QFont("TimesNewRoman", 9))
        self.ui.tableWidget3.resizeColumnsToContents()

        self.ui.tableWidget4.setVerticalHeaderLabels(['Индекс испытания Gj', 'Индекс тест-объекта', 'Индекс тест-предмета'])
        self.ui.tableWidget4.horizontalHeader().setStyleSheet("QHeaderView { font-size: 8pt; }")
        self.ui.tableWidget4.verticalHeader().setStyleSheet("QHeaderView { font-size: 9pt; }")
        self.ui.tableWidget4.setFont(QtGui.QFont("TimesNewRoman", 9))
        self.ui.tableWidget4.resizeColumnsToContents()

    def clickbut(self):
        # Заполнение тест-предметов с исключениями
        try:
            massX = []
            if (self.ui.lineEdit2.text() == ''):
                raise Exception
            H = self.ui.lineEdit2.text()
            A = 1
            B = 100
            a = []
            ran1 = random.randint(A, B)
            a.append(ran1)
            b = []
            i = 1
            while i < 50:
                ran2 = random.randint(A, B)
                if ran2 not in a:
                    a.append(ran2)
                else:
                    i = i - 1
                i += 1
            # Заполнение '0' и '1'
            k = 0
            z = 0
            while z < 100:
                m = 0
                while m < 50:
                    if a[m] == z + 1:
                        k = a[m]
                    m += 1
                if k == z + 1:
                    b.append(1)
                    #Генерация тест-предметов
                    key2 = random.randrange(51444836949)
                    random.seed(key2)
                    num = random.randint(1, int(H))
                    massX.append(num)
                else:
                    b.append(0)
                    massX.append('X')
                z += 1

            # Разделение на 4 массива
            list_1 = b[0:25]
            list_2 = b[25:50]
            list_3 = b[50:75]
            list_4 = b[75:100]
            massX_1 = massX[0:25]
            massX_2 = massX[25:50]
            massX_3 = massX[50:75]
            massX_4 = massX[75:100]

            # Преобразование в Кортеж со списком внутри (1 столбец row=0)
            listt_1 = []
            listt_2 = []
            listt_3 = []
            listt_4 = []
            q1 = tuple(list_1)
            listt_1.append(q1)
            q2 = tuple(list_2)
            listt_2.append(q2)
            q3 = tuple(list_3)
            listt_3.append(q3)
            q4 = tuple(list_4)
            listt_4.append(q4)

            # Преобразование в Кортеж со списком внутри (3 столбец row=2)
            m_1 = []
            m_2 = []
            m_3 = []
            m_4 = []
            y1 = tuple(massX_1)
            m_1.append(y1)
            y2 = tuple(massX_2)
            m_2.append(y2)
            y3 = tuple(massX_3)
            m_3.append(y3)
            y4 = tuple(massX_4)
            m_4.append(y4)

            # Заполнение таблиц
            for tup in listt_1:
                col = 0
                for item in tup:
                    cellinfo1 = QTableWidgetItem(str(item))
                    self.ui.tableWidget.setItem(0, col, cellinfo1)
                    cellinfo1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in listt_2:
                col = 0
                for item in tup:
                    cellinfo2 = QTableWidgetItem(str(item))
                    self.ui.tableWidget2.setItem(0, col, cellinfo2)
                    cellinfo2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in listt_3:
                col = 0
                for item in tup:
                    cellinfo3 = QTableWidgetItem(str(item))
                    self.ui.tableWidget3.setItem(0, col, cellinfo3)
                    cellinfo3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in listt_4:
                col = 0
                for item in tup:
                    cellinfo4 = QTableWidgetItem(str(item))
                    self.ui.tableWidget4.setItem(0, col, cellinfo4)
                    cellinfo4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1

            for tup in m_1:
                col = 0
                for item in tup:
                    cellinfo11 = QTableWidgetItem(str(item))
                    self.ui.tableWidget.setItem(2, col, cellinfo11)
                    cellinfo11.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in m_2:
                col = 0
                for item in tup:
                    cellinfo12 = QTableWidgetItem(str(item))
                    self.ui.tableWidget2.setItem(2, col, cellinfo12)
                    cellinfo12.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in m_3:
                col = 0
                for item in tup:
                    cellinfo13 = QTableWidgetItem(str(item))
                    self.ui.tableWidget3.setItem(2, col, cellinfo13)
                    cellinfo13.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in m_4:
                col = 0
                for item in tup:
                    cellinfo14 = QTableWidgetItem(str(item))
                    self.ui.tableWidget4.setItem(2, col, cellinfo14)
                    cellinfo14.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введите натуральное число тест-предметов')
            self.ui.lineEdit2.clear()
        except Exception:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Поле не заполнено. Введите количество тест-предметов')
            self.ui.lineEdit2.clear()

        #Заполнение тест-объектов с исключениями
        try:
            transfer = []
            if (self.ui.lineEdit.text() == ''):
                raise Exception
            W = self.ui.lineEdit.text()
            i = 0
            while (i < 100):
                key = random.randrange(21474836409)
                random.seed(key)
                num = random.randint(1, int(W))
                transfer.append(num)
                i += 1
            random.shuffle(transfer)

            # Разбиение для формы
            t_1 = transfer[0:25]
            t_2 = transfer[25:50]
            t_3 = transfer[50:75]
            t_4 = transfer[75:100]

            # Преобразование в Кортеж со списком внутри (1 столбец row=0)
            tt_1 = []
            tt_2 = []
            tt_3 = []
            tt_4 = []
            q1 = tuple(t_1)
            tt_1.append(q1)
            q2 = tuple(t_2)
            tt_2.append(q2)
            q3 = tuple(t_3)
            tt_3.append(q3)
            q4 = tuple(t_4)
            tt_4.append(q4)

            for tup in tt_1:
                col = 0
                for item in tup:
                    cell1 = QTableWidgetItem(str(item))
                    self.ui.tableWidget.setItem(1, col, cell1)
                    cell1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in tt_2:
                col = 0
                for item in tup:
                    cell2 = QTableWidgetItem(str(item))
                    self.ui.tableWidget2.setItem(1, col, cell2)
                    cell2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in tt_3:
                col = 0
                for item in tup:
                    cell3 = QTableWidgetItem(str(item))
                    self.ui.tableWidget3.setItem(1, col, cell3)
                    cell3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
            for tup in tt_4:
                col = 0
                for item in tup:
                    cell4 = QTableWidgetItem(str(item))
                    self.ui.tableWidget4.setItem(1, col, cell4)
                    cell4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                    col += 1
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введите натуральное число тест-объектов')
            self.ui.lineEdit.clear()
        except Exception:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Поле не заполнено. Введите количество тест-объектов')
            self.ui.lineEdit.clear()

    def preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec_()

    def print_doc(self):
        # Cохранение документа - не рабочий
        # l = QtPrintSupport.QPrinterInfo.availablePrinterNames()
        # for p in l:
        #     print(p)
        # fn, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All Files ()")
        # if fn != "":
        #     if QtWidgets.QFileInfo(fn).suffix() == "": fn += '.pdf'
        # printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        # printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        # printer.setOutputFileName(fn)

        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handle_paint_request(dialog.printer())

    def handle_paint_request(self, printer):
        printer.setPageOrientation(QtGui.QPageLayout.Landscape)
        painter = QtGui.QPainter(printer)
        # painter.setViewport(self.ui.tableWidget.rect())
        # painter.setWindow(self.ui.tableWidget.rect())
        self.ui.centralwidget.render(painter)
        painter.end()

    def new_form(self):
        self.qwe = mywindow2()
        self.qwe.show()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())