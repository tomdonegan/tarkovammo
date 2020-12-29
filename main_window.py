import sys
import database as db
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainMenuUi(QWidget):

    def __init__(self):
        super(MainMenuUi, self).__init__()
        self.setWindowTitle('Tarkov Ammo Data by ToMiSmE')
        self.setWindowIcon(QIcon('tarkov.ico'))

        # Stops the window from being resized
        self.setFixedSize(340, 400)

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # The below is a in-script css sheet, this removes the requirement for an external css file
        # and makes packing into an .exe easier
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

        # When adding a "clicked" signal to a button, "lamda" must be used to
        # allow the passing of a parameter within the function call
        btn1 = QPushButton('12 Gauge Shot')
        btn1.clicked.connect(lambda: self.show_ammo_data('12 Gauge Shot'))

        btn2 = QPushButton('20 Gauge')
        btn2.clicked.connect(lambda: self.show_ammo_data('20 Gauge'))

        btn3 = QPushButton('23x75 mm')
        btn3.clicked.connect(lambda: self.show_ammo_data('23x75 mm'))

        btn4 = QPushButton('9x18mm')
        btn4.clicked.connect(lambda: self.show_ammo_data('9x18mm'))

        btn5 = QPushButton('7.62x25mm')
        btn5.clicked.connect(lambda: self.show_ammo_data('7.62x25mm'))

        btn6 = QPushButton('9x19mm')
        btn6.clicked.connect(lambda: self.show_ammo_data('9x19mm'))

        btn7 = QPushButton('0.45')
        btn7.clicked.connect(lambda: self.show_ammo_data(0.45))

        btn8 = QPushButton('9x21mm')
        btn8.clicked.connect(lambda: self.show_ammo_data('9x21mm'))

        btn9 = QPushButton('5.7x28 mm')
        btn9.clicked.connect(lambda: self.show_ammo_data('5.7x28 mm'))

        btn10 = QPushButton('4.6x30 mm')
        btn10.clicked.connect(lambda: self.show_ammo_data('4.6x30 mm'))

        btn11 = QPushButton('9x39mm')
        btn11.clicked.connect(lambda: self.show_ammo_data('9x39mm'))

        btn12 = QPushButton('0.366')
        btn12.clicked.connect(lambda: self.show_ammo_data(0.366))

        btn13 = QPushButton('5.45x39 mm')
        btn13.clicked.connect(lambda: self.show_ammo_data('5.45x39 mm'))

        btn14 = QPushButton('5.56x45 mm')
        btn14.clicked.connect(lambda: self.show_ammo_data('5.56x45 mm'))

        btn15 = QPushButton('7.62x39 mm')
        btn15.clicked.connect(lambda: self.show_ammo_data('7.62x39 mm'))

        btn16 = QPushButton('7.62x51 mm')
        btn16.clicked.connect(lambda: self.show_ammo_data('7.62x51 mm'))

        btn17 = QPushButton('7.62x54R')
        btn17.clicked.connect(lambda: self.show_ammo_data('7.62x54R'))

        btn18 = QPushButton('12.7x55 mm')
        btn18.clicked.connect(lambda: self.show_ammo_data('12.7x55 mm'))

        btn19 = QPushButton('Mounted Weapons')
        btn19.clicked.connect(lambda: self.show_ammo_data('Mounted Weapons'))

        btn20 = QPushButton('Other')
        btn20.clicked.connect(lambda: self.show_ammo_data('Other'))

        btn22 = QPushButton('12 Gauge Slugs')
        btn22.clicked.connect(lambda: self.show_ammo_data('12 Gauge Slugs'))

        btn23 = QPushButton('.338 Lapua Magnum')
        btn23.clicked.connect(lambda: self.show_ammo_data('.338 Lapua Magnum'))

        btn24 = QPushButton('.300 Blackout')
        btn24.clicked.connect(lambda: self.show_ammo_data('300 BLK'))

        layout.addWidget(btn12, 0, 0)
        layout.addWidget(btn7, 1, 0)
        layout.addWidget(btn1, 2, 0)
        layout.addWidget(btn22, 3, 0)
        layout.addWidget(btn18, 4, 0)
        layout.addWidget(btn2, 5, 0)
        layout.addWidget(btn3, 6, 0)
        layout.addWidget(btn10, 7, 0)
        layout.addWidget(btn13, 8, 0)
        layout.addWidget(btn14, 9, 0)
        layout.addWidget(btn5, 0, 1)
        layout.addWidget(btn15, 1, 1)
        layout.addWidget(btn16, 2, 1)
        layout.addWidget(btn17, 3, 1)
        layout.addWidget(btn4, 4, 1)
        layout.addWidget(btn6, 5, 1)
        layout.addWidget(btn8, 6, 1)
        layout.addWidget(btn11, 7, 1)
        layout.addWidget(btn24, 8, 1)
        layout.addWidget(btn23, 9, 1)
        layout.addWidget(btn20, 10, 0)
        layout.addWidget(btn19, 10, 1)

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
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.verticalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.reset_button = QPushButton('Reset Data')
        self.reset_button.clicked.connect(self.reset_table)

        self.table_widget.horizontalHeader()

        self.create_table(self.ammo_size)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.reset_button)
        self.setLayout(self.layout)

        self.show()
        self.setFixedSize(self.width(), self.height())
        self.table_widget.setSortingEnabled(True)

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
        row = self.table_widget.rowCount()
        col = self.table_widget.columnCount()
        self.table_widget.setRowCount(row)
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
        row = self.table_widget.rowCount()
        self.table_widget.setRowCount(row + 1)
        col = 0

        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

        # Change color of cell depending on the value.
        for row in range(row + 1):
            for col in range(5, 11):
                if self.table_widget.item(row, col).text() == '6':
                    self.table_widget.item(row, col).setBackground(QColor(75, 240, 86))
                elif self.table_widget.item(row, col).text() == '5':
                    self.table_widget.item(row, col).setBackground(QColor(134, 212, 61))
                elif self.table_widget.item(row, col).text() == '4':
                    self.table_widget.item(row, col).setBackground(QColor(192, 184, 37))
                elif self.table_widget.item(row, col).text() == '3':
                    self.table_widget.item(row, col).setBackground(QColor(249, 157, 14))
                elif self.table_widget.item(row, col).text() == '2':
                    self.table_widget.item(row, col).setBackground(QColor(234, 108, 10))
                elif self.table_widget.item(row, col).text() == '1':
                    self.table_widget.item(row, col).setBackground(QColor(220, 59, 7))
                elif self.table_widget.item(row, col).text() == '0':
                    self.table_widget.item(row, col).setBackground(QColor(206, 11, 4))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainMenuUi()
    m.show()
    sys.exit(app.exec_())