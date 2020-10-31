import sys
import database as db
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainMenuUi(QWidget):

    def __init__(self):
        super(MainMenuUi, self).__init__()
        self.css = QUrl("qrc:/index.html")
        self.setWindowTitle('Tarkov Ammo Data by ToMiSmE')
        self.setFixedSize(340, 400)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.styleSheet = (
            """
            QPushButton {
            background-color: grey;
            border-radius: 5px;
            color: white;
            font-size: 13px;
            width: 140px;
            height: 30px;
            }
    
            MainMenuUi {
            background: rgb(241,241,241);
            }
            
            QLabel {
            background-color: grey;
            color: white;
            height: 60px;
            border-radius: 5px;
            }
            
            QGroupBox {
            border: 3px solid grey;
            border-radius: 5px;
            }"""
        )
        self.setStyleSheet(self.styleSheet)
        self.setWindowIcon(QIcon('tarkov.ico'))
        self.createGridLayout()


        window_layout = QVBoxLayout()
        window_layout.addWidget(self.horizontalGroupBox)
        self.setLayout(window_layout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 3)
        layout.setColumnStretch(1, 3)

        self.btn1 = QPushButton('12 Gauge Shot')
        self.btn1.clicked.connect(lambda: self.show_ammo_data('12 Gauge Shot'))

        self.btn2 = QPushButton('20 Gauge')
        self.btn2.clicked.connect(lambda: self.show_ammo_data('20 Gauge'))

        self.btn3 = QPushButton('23x75 mm')
        self.btn3.clicked.connect(lambda: self.show_ammo_data('23x75 mm'))

        self.btn4 = QPushButton('9x18mm')
        self.btn4.clicked.connect(lambda: self.show_ammo_data('9x18mm'))

        self.btn5 = QPushButton('7.62x25mm')
        self.btn5.clicked.connect(lambda: self.show_ammo_data('7.62x25mm'))

        self.btn6 = QPushButton('9x19mm')
        self.btn6.clicked.connect(lambda: self.show_ammo_data('9x19mm'))

        self.btn7 = QPushButton('0.45')
        self.btn7.clicked.connect(lambda: self.show_ammo_data(0.45))

        self.btn8 = QPushButton('9x21mm')
        self.btn8.clicked.connect(lambda: self.show_ammo_data('9x21mm'))

        self.btn9 = QPushButton('5.7x28 mm')
        self.btn9.clicked.connect(lambda: self.show_ammo_data('5.7x28 mm'))

        self.btn10 = QPushButton('4.6x30 mm')
        self.btn10.clicked.connect(lambda: self.show_ammo_data('4.6x30 mm'))

        self.btn11 = QPushButton('9x39mm')
        self.btn11.clicked.connect(lambda: self.show_ammo_data('9x39mm'))

        self.btn12 = QPushButton('0.366')
        self.btn12.clicked.connect(lambda: self.show_ammo_data(0.366))

        self.btn13 = QPushButton('5.45x39 mm')
        self.btn13.clicked.connect(lambda: self.show_ammo_data('5.45x39 mm'))

        self.btn14 = QPushButton('5.56x45 mm')
        self.btn14.clicked.connect(lambda: self.show_ammo_data('5.56x45 mm'))

        self.btn15 = QPushButton('7.62x39 mm')
        self.btn15.clicked.connect(lambda: self.show_ammo_data('7.62x39 mm'))

        self.btn16 = QPushButton('7.62x51 mm')
        self.btn16.clicked.connect(lambda: self.show_ammo_data('7.62x51 mm'))

        self.btn17 = QPushButton('7.62x54R')
        self.btn17.clicked.connect(lambda: self.show_ammo_data('7.62x54R'))

        self.btn18 = QPushButton('12.7x55 mm')
        self.btn18.clicked.connect(lambda: self.show_ammo_data('12.7x55 mm'))

        self.btn19 = QPushButton('Mounted Weapons')
        self.btn19.clicked.connect(lambda: self.show_ammo_data('Mounted Weapons'))

        self.btn20 = QPushButton('Other')
        self.btn20.clicked.connect(lambda: self.show_ammo_data('Other'))

        self.btn22 = QPushButton('12 Gauge Slugs')
        self.btn22.clicked.connect(lambda: self.show_ammo_data('12 Gauge Slugs'))

        layout.addWidget(self.btn12, 0, 0)
        layout.addWidget(self.btn7, 1, 0)
        layout.addWidget(self.btn1, 2, 0)
        layout.addWidget(self.btn22, 3, 0)
        layout.addWidget(self.btn18, 4, 0)
        layout.addWidget(self.btn2, 5, 0)
        layout.addWidget(self.btn3, 6, 0)
        layout.addWidget(self.btn10, 7, 0)
        layout.addWidget(self.btn13, 8, 0)
        layout.addWidget(self.btn14, 9, 0)
        layout.addWidget(self.btn5, 0, 1)
        layout.addWidget(self.btn15, 1, 1)
        layout.addWidget(self.btn16, 2, 1)
        layout.addWidget(self.btn17, 3, 1)
        layout.addWidget(self.btn4, 4, 1)
        layout.addWidget(self.btn6, 5, 1)
        layout.addWidget(self.btn8, 6, 1)
        layout.addWidget(self.btn11, 7, 1)
        layout.addWidget(self.btn19, 8, 1)
        layout.addWidget(self.btn20, 9, 1)

        self.horizontalGroupBox.setLayout(layout)

    def show_ammo_data(self, ammo_size):
        self.ammo_table_window = AmmoTableWindow(ammo_size)
        self.ammo_table_window.show()


class AmmoTableWindow(QWidget):

    def __init__(self, ammo_size):
        super(AmmoTableWindow, self).__init__()
        self.setWindowTitle('Tarkov Ammo Data - ' + str(ammo_size))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.styleSheet = (
            """
            AmmoTableWindow {
            background: rgb(241,241,241);
            }

            #TableWidget {
            background-color: rgb(241,241,241);
            color: black;
            border-radius: 1px;
            border:1px solid grey;
            gridline-color: grey;
            }
            
            QPushButton {
            background-color: grey;
            border-radius: 5px;
            color: black;
            font-weight: bold;
            font-size: 13px;
            height: 30px;
            }

            QHeaderView::section:horizontal {
            background: rgb(217, 217, 217);
            font-weight: bold;
            color: black;
            }

            QGroupBox {
            border: 3px solid grey;
            border-radius: 5px;
            }"""
        )
        self.setStyleSheet(self.styleSheet)
        self.setWindowIcon(QIcon('tarkov.ico'))

        self.ammo_size = ammo_size

        self.table_widget = QTableWidget()
        self.table_widget.setSortingEnabled(True)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.verticalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.reset_button = QPushButton('Reset Data')
        self.reset_button.clicked.connect(self.reset_table)

        self.create_table(self.ammo_size)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.reset_button)
        self.setLayout(self.layout)

        self.show()
        self.setFixedSize(self.width(), self.height())

    # This section of code is fucking garbage
    def reset_table(self):
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(0)
        self.create_table(self.ammo_size)


    def create_table(self, ammo_size):
        db.ammo_data_list = []

        self.ammo_size = ammo_size

        self.table_widget.setColumnCount(len(db.titles_list)-1)
        self.table_widget.setObjectName('TableWidget')
        self.row = self.table_widget.rowCount()
        self.col = self.table_widget.columnCount()
        self.table_widget.setRowCount(self.row)
        self.table_widget.verticalHeader().hide()
        self.table_widget.verticalScrollBar().hide()
        self.table_widget.horizontalScrollBar().hide()
        self.table_widget.setHorizontalHeaderLabels(db.titles_list[1:])

        db.ammo_by_size(self.ammo_size)

        for i in db.ammo_data_list:
            self.add_table_row(self.table_widget, i)

        self.table_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_widget.resizeColumnsToContents()

    def add_table_row(self, table, row_data):
        self.row = self.table_widget.rowCount()
        self.table_widget.setRowCount(self.row + 1)
        col = 0

        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(self.row, col, cell)
            col += 1

        # Change color of cell depending on the value.
        for row in range(self.row + 1):
            for col in range(5, 11):
                if self.table_widget.item(row, col).text() == '6':
                    self.table_widget.item(row, col).setBackground(QColor(75, 240,86))
                elif self.table_widget.item(row, col).text() == '5':
                    self.table_widget.item(row, col).setBackground(QColor(134,212,61))
                elif self.table_widget.item(row, col).text() == '4':
                    self.table_widget.item(row, col).setBackground(QColor(192,184,37))
                elif self.table_widget.item(row, col).text() == '3':
                    self.table_widget.item(row, col).setBackground(QColor(249,157,14))
                elif self.table_widget.item(row, col).text() == '2':
                    self.table_widget.item(row, col).setBackground(QColor(234,108,10))
                elif self.table_widget.item(row, col).text() == '1':
                    self.table_widget.item(row, col).setBackground(QColor(220,59,7))
                elif self.table_widget.item(row, col).text() == '0':
                    self.table_widget.item(row, col).setBackground(QColor(206,11,4))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainMenuUi()
    m.show()
    sys.exit(app.exec_())