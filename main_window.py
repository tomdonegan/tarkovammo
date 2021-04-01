import sys
import os
import database as db
import requests
import urllib.request
# import wget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

_AppName_ = 'Tarkov Ammo'
__author__ = 'Tom Donegan'
__license__ = 'The MIT License (MIT)'
__version__ = 0.1
__maintainer__ = 'Tom Donegan'
__email__ = 'tomdonegan@live.co.uk'
__status__ = 'Beta'


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
                       '.338 Lapua Magnum', '5.7x28 mm',
                       '.366mm', '7.62x25mm',
                       '.45mm', '7.62x39 mm',
                       '12 Gauge Shot', '7.62x51mm',
                       '12 Gauge Slugs', '7.62x54R',
                       '12.7x55 mm', '9x18mm',
                       '20 Gauge', '9x19mm',
                       '23x75 mm', '9x21mm',
                       '4.6x30 mm', '9x39mm',
                       '5.45x39 mm', 'Mounted Weapons',
                       'Other', 'Check for Updates']

        for i in button_list:
            btn = QPushButton(i)
            if 'Updates' in btn.text():
                btn.clicked.connect(self.show_update_window)
                layout.addWidget(btn)
                #last_row = layout.rowCount()
                # Adds the "Check for Updates" button to the bottom of the table.
                #layout.addWidget(btn, last_row, 0, 1, 2)
            else:
                btn.clicked.connect(lambda pass_ammo, param=btn.text(): self.show_ammo_data(param))
                layout.addWidget(btn)

        self.horizontalGroupBox.setLayout(layout)

    def show_ammo_data(self, ammo_size):
        self.ammo_table_window = AmmoTableWindow(ammo_size)
        self.ammo_table_window.show()

    def show_update_window(self):
        UpdateCheck()


class UpdateCheck(QWidget):
    def __init__(self):
        # super(UpdateCheck, self).__init__()
        # self.setWindowTitle('This is the window')
        # self.progressBar = QProgressBar(self)
        super().__init__()
        self.update_check()

    # Below function checks Github for version data. If current version number is lower,
    # files will be downloaded after confirmation from the user.
    def update_check(self):
        msg = QMessageBox()
        styleSheet = (
            """
            QPushButton {
            background-color: grey;
            border-radius: 5px;
            color: white;
            font-size: 13px;
            width: 100%;
            height: 30px;
            }

            QLabel {
            background-color: white;
            color: black;
            height: 60px;
            border-radius: 5px;
            }
            """
        )
        self.setStyleSheet(styleSheet)
        try:
            git_version_data = float(requests.get('https://raw.githubusercontent.com/'
                                                  'tomdonegan/tarkovammo/master/version.txt').text)
            local_version = float(__version__)
            if local_version < git_version_data:
                update_selection = msg.information(self, 'Update Available',
                                                   f'Current Version: {local_version} '
                                                   f'\nAvailable Version: {git_version_data} '
                                                   f'\nDownload update?',
                                                   QMessageBox.Yes | QMessageBox.No)
                if update_selection == msg.Yes:
                    self.update_downloader()
            else:
                msg.information(self, 'Update Check', 'You are all up to date.', QMessageBox.Ok)
        except ValueError:
            msg.information(self, 'Update Error', 'Could not retrieve update!\nConnection Unavailable.',
                            QMessageBox.Ok)

    def get_download_path(self):
        """Returns the default downloads path for linux or windows"""
        if os.name != 'nt':
            return os.path.join(os.path.expanduser('~'), 'downloads')
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location

    def update_downloader(self):

        # specify the url of the file which is to be downloaded
        down_url = 'https://github.com/tomdonegan/tarkovammo/raw/master/dist/TarkovAmmo.rar'  # specify download url here

        # specify save location where the file is to be saved
        save_loc = self.get_download_path() + '/TarkovAmmo.rar'

        # Dowloading using urllib
        urllib.request.urlretrieve(down_url, save_loc, self.handle_progress)

    def handle_progress(self, blocknum, blocksize, totalsize):
        if totalsize > 0:
            ## calculate the progress
            read_data = blocknum * blocksize

            download_percentage = read_data * 100 / totalsize
            print(download_percentage)
            # self.progressBar.setValue(download_percentage)
            QApplication.processEvents()


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
