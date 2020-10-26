    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet(open('stylesheet.css').read())
        self.setWindowIcon(QIcon('tarkov.ico'))
        #self.setGeometry(self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 3)
        layout.setColumnStretch(1, 3)

        self.shotgun1 = QPushButton(self.show_ammo_data)
        self.shotgun1.clicked.connect(self.show_ammo_data)

        layout.addWidget(self.shotgun1, 0, 0)
        layout.addWidget(QPushButton('20 Gauge'), 1, 0)
        layout.addWidget(QPushButton('23x75 mm'), 2, 0)
        layout.addWidget(QPushButton('9x18mm'), 3, 0)
        layout.addWidget(QPushButton('7.62x25mm'), 4, 0)
        layout.addWidget(QPushButton('9x19mm'), 5, 0)
        layout.addWidget(QPushButton('0.45'), 6, 0)
        layout.addWidget(QPushButton('9x21mm'), 7, 0)
        layout.addWidget(QPushButton('5.7x28 mm'), 8, 0)
        layout.addWidget(QPushButton('4.6x30 mm'), 9, 0)
        layout.addWidget(QPushButton('9x39mm'), 10, 0)
        layout.addWidget(QPushButton('5.7x28 mm'), 0, 1)
        layout.addWidget(QPushButton('0.366'), 1, 1)
        layout.addWidget(QPushButton('5.45x39 mm'), 2, 1)
        layout.addWidget(QPushButton('5.56x45 mm'), 3, 1)
        layout.addWidget(QPushButton('7.62x39 mm'), 4, 1)
        layout.addWidget(QPushButton('7.62x51 mm'), 5, 1)
        layout.addWidget(QPushButton('7.62x54R'), 6, 1)
        layout.addWidget(QPushButton('12.7x55 mm'), 7, 1)
        layout.addWidget(QPushButton('Mounted Weapons'), 8, 1)
        layout.addWidget(QPushButton('Other'), 9, 1)
        layout.addWidget(QPushButton('Close'), 10, 1)

        self.horizontalGroupBox.setLayout(layout)

    def show_ammo_data(self):
        self.ammo_data_window = AmmoData()
        self.ammo_data_window.show()


class AmmoData(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Tarkov Ammo Data'
        self.button = QPushButton('test')

    # def create_table(self):
    #     self.table_widget = QTableWidget()
    #     self.table_widget.setColumnCount(11)
    #     self.table_widget.setRowCount(11)