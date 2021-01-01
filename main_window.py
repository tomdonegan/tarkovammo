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

        button_list = ['.300 Blackout', '5.56x45 mm',
                       '.338 Lapua Magnum', '7.62x25mm',
                       '.366mm', '7.62x39 mm',
                       '.45mm', '7.62x51 mm',
                       '12 Gauge Shot', '7.62x54R',
                       '12 Gauge Slugs', '9x18mm',
                       '12.7x55 mm', '9x19mm',
                       '20 Gauge', '9x21mm',
                       '23x75 mm', '9x39mm',
                       '4.6x30 mm', 'Mounted Weapons',
                       '5.45x39 mm', 'Other']

        for i in button_list:
            btn = QPushButton(i)
            btn.clicked.connect(lambda pass_ammo, param=btn.text(): self.show_ammo_data(param))
            layout.addWidget(btn)

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

        self.table_widget.setColumnCount(len(db.titles_list) - 1)
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
        for col, item in enumerate(row_data):
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)

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