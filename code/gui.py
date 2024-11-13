from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStyleHints,)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QTableView,QVBoxLayout,
    QWidget,QLineEdit,QFormLayout,QLabel,QComboBox,QDialog)

import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,app):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.ui = MainWindow
        self.app = app
        self.global_pallete = self.setPallete(self.app.styleHints().colorScheme())
        self.app.setPalette(self.global_pallete)
        self.current_state = ""
        self.current_machine_id = -1
        self.tb = u"background-color: rgb(240, 240, 240);\n""color: rgb(0, 0, 0);\n""font: 600 12pt \"Segoe UI\";"
        self.bt = u"background-color: rgb(30, 167, 233);\n""color: rgb(0, 0, 0);\n""font: 600 12pt \"Segoe UI\";"
        self.class_list = ["Стандарт", "Эконом"]

        self.roller_list = ["","840","1050"]

        self.machine_names = ["Станок 1", "Lt-245", "ИРИС", 150, "Дополнительно"]

        self.today_machine_1_list = []
        self.today_machine_2_list = []
        self.today_machine_3_list = []

        self.reserve_machine_1_list = []
        self.reserve_machine_2_list = []
        self.reserve_machine_3_list = []

        self.tommorow_machine_1_list = []
        self.tommorow_machine_2_list = []
        self.tommorow_machine_3_list = []

        self.thf_list = []
        self.additional_list = []

        self.result_list = []
        
        self.ui.resize(1366, 600)
        self.ui.setMinimumSize(QSize(1366, 600))
        self.ui.setMaximumSize(QSize(1366, 600))
        self.centralwidget = QWidget(self.ui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.navigation = QFrame(self.centralwidget)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setGeometry(QRect(10, 10, 170, 580))

        self.navigation.setPalette(self.global_pallete)
        font = QFont()
        font.setPointSize(16)
        self.navigation.setFont(font)
        self.navigation.setStyleSheet(u"")
        self.navigation.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigation.setFrameShadow(QFrame.Shadow.Raised)

        self.smeta_today_nav = QPushButton(self.navigation)
        self.smeta_today_nav.setObjectName(u"smeta_today_nav")
        self.smeta_today_nav.setGeometry(QRect(4, 20, 161, 61))
        font1 = QFont()
        font1.setPointSize(15)
        self.smeta_today_nav.setFont(font1)
        self.smeta_today_nav.setStyleSheet(u"")
        self.smeta_today_nav.clicked.connect(self.smeta_today_nav_clicked)


        self.smeta_tommorow_nav = QPushButton(self.navigation)
        self.smeta_tommorow_nav.setObjectName(u"smeta_tommorow_nav")
        self.smeta_tommorow_nav.setGeometry(QRect(4, 100, 161, 61))
        self.smeta_tommorow_nav.setFont(font1)
        # self.smeta_tommorow_nav.setEnabled(False)
        self.smeta_tommorow_nav.setStyleSheet(u"")
        self.smeta_tommorow_nav.clicked.connect(self.smeta_tommorow_nav_clicked)

        self.addition_nav = QPushButton(self.navigation)
        self.addition_nav.setObjectName(u"addition_nav")
        self.addition_nav.setGeometry(QRect(4, 180, 161, 61))
        self.addition_nav.setFont(font1)
        self.addition_nav.setAutoFillBackground(False)
        # self.addition_nav.setEnabled(False)
        self.addition_nav.setStyleSheet(u"")
        self.addition_nav.clicked.connect(self.addition_nav_clicked)

        #страница сметы на сегодня

        self.smeta_today_page = QFrame(self.centralwidget)
        self.smeta_today_page.setObjectName(u"additional_page")
        self.smeta_today_page.setGeometry(QRect(180, 10, 1181, 580))
        self.smeta_today_page.setVisible(False)
        palette1 = QPalette()

        self.smeta_today_page.setPalette(self.global_pallete)
        self.smeta_today_page.setFont(font1)
        self.smeta_today_page.setFrameShape(QFrame.Shape.StyledPanel)
        self.smeta_today_page.setFrameShadow(QFrame.Shadow.Raised)

        self.smeta_today_but = QPushButton(self.smeta_today_page)
        self.smeta_today_but.setObjectName(u"smeta_today_but")
        self.smeta_today_but.setGeometry(QRect(20, 20, 161, 41))
        self.smeta_today_but.setStyleSheet(self.bt)
        self.smeta_today_but.clicked.connect(self.smeta_today_but_clicked)
        self.smeta_today_but.setCheckable(True)
        
        self.reserve_today_but = QPushButton(self.smeta_today_page)
        self.reserve_today_but.setObjectName(u"reserve_today_but")
        self.reserve_today_but.setGeometry(QRect(220, 20, 161, 41))
        self.reserve_today_but.setStyleSheet(self.bt)
        self.reserve_today_but.clicked.connect(self.reserve_today_but_clicked)
        self.reserve_today_but.setCheckable(True)

        #страница сметы (смета сегодня)
        self.smeta_today_panel = QFrame(self.smeta_today_page)
        self.smeta_today_panel.setObjectName(u"smeta_today_panel")
        self.smeta_today_panel.setGeometry(QRect(10, 60, 1151, 510))
        self.smeta_today_panel.setPalette(self.global_pallete)
        self.smeta_today_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.smeta_today_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.smeta_today_panel.setVisible(False)
        
        #навигация по станкам 
        self.machine_1_smeta = QPushButton(self.smeta_today_panel)
        self.machine_1_smeta.setGeometry(QRect(10, 10, 161, 41))
        self.machine_1_smeta.setStyleSheet(self.bt)
        self.machine_1_smeta.clicked.connect(self.machine_1_today_clicked)
        self.machine_1_smeta.setCheckable(True)

        self.machine_2_smeta = QPushButton(self.smeta_today_panel)
        self.machine_2_smeta.setGeometry(QRect(211, 10, 161, 41))
        self.machine_2_smeta.setStyleSheet(self.bt)
        self.machine_2_smeta.clicked.connect(self.machine_2_today_clicked)
        self.machine_2_smeta.setCheckable(True)

        
        self.machine_3_smeta = QPushButton(self.smeta_today_panel)
        self.machine_3_smeta.setGeometry(QRect(421, 10, 161, 41))
        self.machine_3_smeta.setStyleSheet(self.bt)
        self.machine_3_smeta.clicked.connect(self.machine_3_today_clicked)
        self.machine_3_smeta.setCheckable(True)

        #кнопка добавления
        self.smeta_machine_add = QPushButton(self.smeta_today_panel)
        self.smeta_machine_add.setGeometry(QRect(10, 61, 161, 41))
        self.smeta_machine_add.setStyleSheet(u"background-color: rgb(30, 167, 233);\n" "color: rgb(0, 0, 0);")
        self.smeta_machine_add.clicked.connect(self.smeta_machine_add_clicked)
        #шапка таблицы 
        self.smeta_header = QWidget(self.smeta_today_panel)
        self.smeta_header.setGeometry(QRect(16, 120, 1118, 31))
        self.smeta_header.setStyleSheet(u"background-color: rgb(240, 240, 240);\n" "color: rgb(0, 0, 0);")
        self.smeta_label = QLabel(self.smeta_header)
        self.smeta_label.setObjectName(u"label")
        self.smeta_label.setGeometry(QRect(10, 0, 1101, 20))
        font = QFont()
        font.setPointSize(12)
        self.smeta_label.setFont(font)

        #скролл панели резерва
        self.smeta_machine_1_scrollArea = QScrollArea(self.smeta_today_panel)
        self.smeta_machine_1_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.smeta_machine_1_scrollArea.setWidgetResizable(True)
        self.smeta_machine_1_scrollArea.setVisible(False)
        self.smeta_machine_1_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.smeta_machine_1_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.smeta_machine_1_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.smeta_machine_1_scrollAreaWidgetContents = QWidget()
        self.smeta_machine_1_scrollAreaWidgetContents.move(0, 0)
        self.smeta_machine_1_verticalLayout = QFormLayout()
        self.smeta_machine_1_scrollAreaWidgetContents.setLayout(self.smeta_machine_1_verticalLayout)
        self.smeta_machine_1_scrollArea.setWidget(self.smeta_machine_1_scrollAreaWidgetContents)

        self.smeta_machine_2_scrollArea = QScrollArea(self.smeta_today_panel)
        self.smeta_machine_2_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.smeta_machine_2_scrollArea.setWidgetResizable(True)
        self.smeta_machine_2_scrollArea.setVisible(False)
        self.smeta_machine_2_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.smeta_machine_2_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.smeta_machine_2_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.smeta_machine_2_scrollAreaWidgetContents = QWidget()
        self.smeta_machine_2_scrollAreaWidgetContents.move(0, 0)
        self.smeta_machine_2_verticalLayout = QFormLayout()
        self.smeta_machine_2_scrollAreaWidgetContents.setLayout(self.smeta_machine_2_verticalLayout)
        self.smeta_machine_2_scrollArea.setWidget(self.smeta_machine_2_scrollAreaWidgetContents)

        self.smeta_machine_3_scrollArea = QScrollArea(self.smeta_today_panel)
        self.smeta_machine_3_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.smeta_machine_3_scrollArea.setWidgetResizable(True)
        self.smeta_machine_3_scrollArea.setVisible(False)
        self.smeta_machine_3_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.smeta_machine_3_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.smeta_machine_3_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.smeta_machine_3_scrollAreaWidgetContents = QWidget()
        self.smeta_machine_3_scrollAreaWidgetContents.move(0, 0)
        self.smeta_machine_3_verticalLayout = QFormLayout()
        self.smeta_machine_3_scrollAreaWidgetContents.setLayout(self.smeta_machine_3_verticalLayout)
        self.smeta_machine_3_scrollArea.setWidget(self.smeta_machine_3_scrollAreaWidgetContents)

        #страница резерва (смета сегодня)
        self.smeta_reserve_panel = QFrame(self.smeta_today_page)
        self.smeta_reserve_panel.setGeometry(QRect(10, 60, 1151, 510))
        self.smeta_reserve_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.smeta_reserve_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.smeta_reserve_panel.setVisible(False)

        #навигация по станкам 
        self.machine_1_reserve = QPushButton(self.smeta_reserve_panel)
        self.machine_1_reserve.setObjectName(u"machine_1_reserve")
        self.machine_1_reserve.setGeometry(QRect(10, 10, 161, 41))
        self.machine_1_reserve.setStyleSheet(self.bt)
        self.machine_1_reserve.clicked.connect(self.machine_1_reserve_clicked)
        self.machine_1_reserve.setCheckable(True)

        self.machine_2_reserve = QPushButton(self.smeta_reserve_panel)
        self.machine_2_reserve.setObjectName(u"machine_2_reserve")
        self.machine_2_reserve.setGeometry(QRect(211, 10, 161, 41))
        self.machine_2_reserve.setStyleSheet(self.bt)
        self.machine_2_reserve.clicked.connect(self.machine_2_reserve_clicked)
        self.machine_2_reserve.setCheckable(True)
        
        self.machine_3_reserve = QPushButton(self.smeta_reserve_panel)
        self.machine_3_reserve.setObjectName(u"machine_3_reserve")
        self.machine_3_reserve.setGeometry(QRect(421, 10, 161, 41))
        self.machine_3_reserve.setStyleSheet(self.bt)
        self.machine_3_reserve.clicked.connect(self.machine_3_reserve_clicked)
        self.machine_3_reserve.setCheckable(True)
        
        #кнопка добавления
        self.reserve_machine_add = QPushButton(self.smeta_reserve_panel)
        self.reserve_machine_add.setObjectName(u"reserve_machine_add")
        self.reserve_machine_add.setGeometry(QRect(10, 61, 161, 41))
        self.reserve_machine_add.setStyleSheet(u"background-color: rgb(30, 167, 233);\n" "color: rgb(0, 0, 0);")
        self.reserve_machine_add.clicked.connect(self.reserve_machine_add_clicked)

        #шапка таблицы
        self.reserve_header = QWidget(self.smeta_reserve_panel)
        self.reserve_header.setObjectName(u"widget_2")
        self.reserve_header.setGeometry(QRect(16, 120, 1118, 31))
        self.reserve_header.setStyleSheet(u"background-color: rgb(240, 240, 240);\n""color: rgb(0, 0, 0);")
        self.reserve_label = QLabel(self.reserve_header)
        self.reserve_label.setGeometry(QRect(10, 0, 1101, 20))
        font = QFont()
        font.setPointSize(12)
        self.reserve_label.setFont(font)

        #скролл панели резерва
        self.reserve_machine_1_scrollArea = QScrollArea(self.smeta_reserve_panel)
        self.reserve_machine_1_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.reserve_machine_1_scrollArea.setWidgetResizable(True)
        self.reserve_machine_1_scrollArea.setVisible(False)
        self.reserve_machine_1_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.reserve_machine_1_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.reserve_machine_1_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.reserve_machine_1_scrollAreaWidgetContents = QWidget()
        self.reserve_machine_1_scrollAreaWidgetContents.move(0, 0)
        self.reserve_machine_1_verticalLayout = QFormLayout()
        self.reserve_machine_1_scrollAreaWidgetContents.setLayout(self.reserve_machine_1_verticalLayout)
        self.reserve_machine_1_scrollArea.setWidget(self.reserve_machine_1_scrollAreaWidgetContents)

        self.reserve_machine_2_scrollArea = QScrollArea(self.smeta_reserve_panel)
        self.reserve_machine_2_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.reserve_machine_2_scrollArea.setWidgetResizable(True)
        self.reserve_machine_2_scrollArea.setVisible(False)
        self.reserve_machine_2_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.reserve_machine_2_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.reserve_machine_2_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.reserve_machine_2_scrollAreaWidgetContents = QWidget()
        self.reserve_machine_2_scrollAreaWidgetContents.move(0, 0)
        self.reserve_machine_2_verticalLayout = QFormLayout()
        self.reserve_machine_2_scrollAreaWidgetContents.setLayout(self.reserve_machine_2_verticalLayout)
        self.reserve_machine_2_scrollArea.setWidget(self.reserve_machine_2_scrollAreaWidgetContents)

        self.reserve_machine_3_scrollArea = QScrollArea(self.smeta_reserve_panel)
        self.reserve_machine_3_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.reserve_machine_3_scrollArea.setWidgetResizable(True)
        self.reserve_machine_3_scrollArea.setVisible(False)
        self.reserve_machine_3_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.reserve_machine_3_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.reserve_machine_3_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.reserve_machine_3_scrollAreaWidgetContents = QWidget()
        self.reserve_machine_3_scrollAreaWidgetContents.move(0, 0)
        self.reserve_machine_3_verticalLayout = QFormLayout()
        self.reserve_machine_3_scrollAreaWidgetContents.setLayout(self.reserve_machine_3_verticalLayout)
        self.reserve_machine_3_scrollArea.setWidget(self.reserve_machine_3_scrollAreaWidgetContents)


        #------------------------------------------------------

        #страница сметы на завтра
        self.smeta_tommorow_page = QFrame(self.centralwidget)
        self.smeta_tommorow_page.setObjectName(u"additional_page")
        self.smeta_tommorow_page.setGeometry(QRect(180, 10, 1181, 580))
        self.smeta_tommorow_page.setVisible(False)
        self.smeta_tommorow_page.setPalette(self.global_pallete)
        self.smeta_tommorow_page.setFont(font1)
        self.smeta_tommorow_page.setFrameShape(QFrame.Shape.StyledPanel)
        self.smeta_tommorow_page.setFrameShadow(QFrame.Shadow.Raised)

        self.machine_1_tommorow = QPushButton(self.smeta_tommorow_page)
        self.machine_1_tommorow.setObjectName(u"machine_1_tommorow")
        self.machine_1_tommorow.setStyleSheet(self.bt)
        self.machine_1_tommorow.clicked.connect(self.machine_1_tommorow_clicked)
        self.machine_1_tommorow.setGeometry(QRect(20, 20, 161, 41))
        self.machine_1_tommorow.setCheckable(True)

        self.machine_2_tommorow = QPushButton(self.smeta_tommorow_page)
        self.machine_2_tommorow.setObjectName(u"machine_2_tommorow")
        self.machine_2_tommorow.setStyleSheet(self.bt)
        self.machine_2_tommorow.clicked.connect(self.machine_2_tommorow_clicked)
        self.machine_2_tommorow.setGeometry(QRect(201, 20, 161, 41))
        self.machine_2_tommorow.setCheckable(True)
        
        self.machine_3_tommorow = QPushButton(self.smeta_tommorow_page)
        self.machine_3_tommorow.setObjectName(u"machine_3_tommorow")
        self.machine_3_tommorow.setStyleSheet(self.bt)
        self.machine_3_tommorow.clicked.connect(self.machine_3_tommorow_clicked)
        self.machine_3_tommorow.setGeometry(QRect(380, 20, 161, 41))
        self.machine_3_tommorow.setCheckable(True)

        self.add_tommorow = QPushButton(self.smeta_tommorow_page)
        self.add_tommorow.setStyleSheet(self.bt)
        self.add_tommorow.setGeometry(QRect(20, 71, 161, 41))
        self.add_tommorow.clicked.connect(self.tommorow_machine_add_clicked)

        #шапка таблицы 
        self.tommorow_header = QWidget(self.smeta_tommorow_page)
        self.tommorow_header.setGeometry(QRect(16, 120, 1118, 31))
        self.tommorow_header.setStyleSheet(u"background-color: rgb(240, 240, 240);\n" "color: rgb(0, 0, 0);")
        self.tommorow_label = QLabel(self.tommorow_header)
        self.tommorow_label.setObjectName(u"label")
        self.tommorow_label.setGeometry(QRect(10, 0, 1101, 20))
        font = QFont()
        font.setPointSize(12)
        self.tommorow_label.setFont(font)
        
        #скролл панели завтра
        self.tommorow_machine_1_scrollArea = QScrollArea(self.smeta_tommorow_page)
        self.tommorow_machine_1_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.tommorow_machine_1_scrollArea.setWidgetResizable(True)
        self.tommorow_machine_1_scrollArea.setVisible(False)
        self.tommorow_machine_1_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tommorow_machine_1_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tommorow_machine_1_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.tommorow_machine_1_scrollAreaWidgetContents = QWidget()
        self.tommorow_machine_1_scrollAreaWidgetContents.move(0, 0)
        self.tommorow_1_verticalLayout = QFormLayout()
        self.tommorow_machine_1_scrollAreaWidgetContents.setLayout(self.tommorow_1_verticalLayout)
        self.tommorow_machine_1_scrollArea.setWidget(self.tommorow_machine_1_scrollAreaWidgetContents)

        self.tommorow_machine_2_scrollArea = QScrollArea(self.smeta_tommorow_page)
        self.tommorow_machine_2_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.tommorow_machine_2_scrollArea.setWidgetResizable(True)
        self.tommorow_machine_2_scrollArea.setVisible(False)
        self.tommorow_machine_2_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tommorow_machine_2_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tommorow_machine_2_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.tommorow_machine_2_scrollAreaWidgetContents = QWidget()
        self.tommorow_machine_2_scrollAreaWidgetContents.move(0, 0)
        self.tommorow_2_verticalLayout = QFormLayout()
        self.tommorow_machine_2_scrollAreaWidgetContents.setLayout(self.tommorow_2_verticalLayout)
        self.tommorow_machine_2_scrollArea.setWidget(self.tommorow_machine_2_scrollAreaWidgetContents)

        self.tommorow_machine_3_scrollArea = QScrollArea(self.smeta_tommorow_page)
        self.tommorow_machine_3_scrollArea.setGeometry(QRect(20, 161, 1111, 330))
        self.tommorow_machine_3_scrollArea.setWidgetResizable(True)
        self.tommorow_machine_3_scrollArea.setVisible(False)
        self.tommorow_machine_3_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tommorow_machine_3_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tommorow_machine_3_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.tommorow_machine_3_scrollAreaWidgetContents = QWidget()
        self.tommorow_machine_3_scrollAreaWidgetContents.move(0, 0)
        self.tommorow_3_verticalLayout = QFormLayout()
        self.tommorow_machine_3_scrollAreaWidgetContents.setLayout(self.tommorow_3_verticalLayout)
        self.tommorow_machine_3_scrollArea.setWidget(self.tommorow_machine_3_scrollAreaWidgetContents)

        #страница ролика
        self.roller_nav = QPushButton(self.navigation)
        self.roller_nav.setObjectName(u"roller_nav")
        self.roller_nav.setGeometry(QRect(4, 260, 161, 61))
        self.roller_nav.setFont(font1)
        self.roller_nav.setStyleSheet(u"")
        self.roller_nav.clicked.connect(self.roller_nav_clicked)   

        #страница ролика
        self.roller_page = QFrame(self.centralwidget)
        self.roller_page.setObjectName(u"additional_page")
        self.roller_page.setGeometry(QRect(180, 10, 1181, 580))
        self.roller_page.setPalette(self.global_pallete)
        self.roller_page.setVisible(False)
        self.roller_page.setFont(font1)
        self.roller_page.setFrameShape(QFrame.Shape.StyledPanel)
        self.roller_page.setFrameShadow(QFrame.Shadow.Raised)

        #кнопка добавления
        self.roller_process = QPushButton(self.roller_page)
        self.roller_process.setObjectName(u"reserve_machine_add")
        self.roller_process.setGeometry(QRect(10, 20, 161, 51))
        self.roller_process.setStyleSheet(u"background-color: rgb(30, 167, 233);\n" "color: rgb(0, 0, 0);")
        self.roller_process.clicked.connect(self.calculate_roller)
        
        #шапка таблицы
        self.roller_header = QWidget(self.roller_page)
        self.roller_header.setObjectName(u"widget_2")
        self.roller_header.setGeometry(QRect(16, 80, 1118, 31))
        self.roller_header.setStyleSheet(u"background-color: rgb(240, 240, 240);\n""color: rgb(0, 0, 0);")
        self.roller_label = QLabel(self.roller_header)
        self.roller_label.setGeometry(QRect(10, 0, 1101, 20))
        font = QFont()
        font.setPointSize(12)
        self.roller_label.setFont(font)

        #скролл панель 
        self.roller_scrollArea = QScrollArea(self.roller_page)
        self.roller_scrollArea.setGeometry(QRect(20, 115, 1151, 330))
        self.roller_scrollArea.setWidgetResizable(True)
        self.roller_scrollArea.setVisible(True)
        self.roller_scrollArea.setFixedHeight(705)
        self.roller_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.roller_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.roller_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.roller_scrollAreaWidgetContents = QWidget()
        self.roller_scrollAreaWidgetContents.move(0, 0)
        self.roller_verticalLayout = QFormLayout()
        self.roller_scrollAreaWidgetContents.setLayout(self.roller_verticalLayout)
        self.roller_scrollArea.setWidget(self.roller_scrollAreaWidgetContents)

        #-----------------------------------------------------

        #страница доп
        self.additional_page = QFrame(self.centralwidget)
        self.additional_page.setObjectName(u"additional_page")
        self.additional_page.setGeometry(QRect(180, 10, 1181, 580))
        self.additional_page.setPalette(self.global_pallete)
        self.additional_page.setVisible(False)
        self.additional_page.setFont(font1)
        self.additional_page.setFrameShape(QFrame.Shape.StyledPanel)
        self.additional_page.setFrameShadow(QFrame.Shadow.Raised)
        
        self.thf = QPushButton(self.additional_page)
        self.thf.setObjectName(u"thf")
        self.thf.setGeometry(QRect(20, 20, 161, 41))
        self.thf.setStyleSheet(self.bt)
        self.thf.setCheckable(True)
        self.thf.clicked.connect(self.thf_clicked)
        self.another = QPushButton(self.additional_page)
        self.another.setObjectName(u"another")
        self.another.setGeometry(QRect(201, 20, 161, 41))
        self.another.setStyleSheet(self.bt)
        self.another.setCheckable(True)
        self.another.clicked.connect(self.another_clicked)
        #addition 150
        self.thf_panel = QFrame(self.additional_page)
        self.thf_panel.setObjectName(u"thf_panel")
        self.thf_panel.setGeometry(QRect(10, 60, 1151, 510))
        self.thf_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.thf_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.thf_panel.setVisible(False)
        self.add = QPushButton(self.thf_panel)
        self.add.setObjectName(u"add")
        self.add.setStyleSheet(self.bt)
        self.add.setGeometry(QRect(10, 20, 161, 41))
        self.add.clicked.connect(self.thf_add_clicked)

        self.thf_header = QWidget(self.thf_panel)
        self.thf_header.setGeometry(QRect(11, 81, 1118, 31))
        self.thf_header.setStyleSheet(u"background-color: rgb(240, 240, 240);\n" "color: rgb(0, 0, 0);")
        self.thf_label = QLabel(self.thf_header)
        self.thf_label.setObjectName(u"label")
        self.thf_label.setGeometry(QRect(10, 0, 1101, 20))
        font = QFont()
        font.setPointSize(12)
        self.thf_label.setFont(font)

        self.thf_scrollArea = QScrollArea(self.thf_panel)
        self.thf_scrollArea.setGeometry(QRect(10, 121, 1111, 330))
        self.thf_scrollArea.setWidgetResizable(True)
        self.thf_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.thf_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.thf_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.thf_scrollAreaWidgetContents = QWidget()
        self.thf_scrollAreaWidgetContents.move(0, 0)
        self.thf_scrollArea_verticalLayout = QFormLayout()
        self.thf_scrollAreaWidgetContents.setLayout(self.thf_scrollArea_verticalLayout)
        self.thf_scrollArea.setWidget(self.thf_scrollAreaWidgetContents)
        #addition another 
        self.another_panel = QFrame(self.additional_page)
        self.another_panel.setObjectName(u"thf_panel_another")
        self.another_panel.setGeometry(QRect(10, 60, 1151, 510))
        self.another_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.another_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.another_panel.setVisible(False)
        self.add_another = QPushButton(self.another_panel)
        self.add_another.setObjectName(u"add_another")
        self.add_another.setGeometry(QRect(10, 20, 161, 41))
        self.add_another.setStyleSheet(self.bt)
        self.add_another.clicked.connect(self.additional_add_clicked)

        self.another_header = QWidget(self.another_panel)
        self.another_header.setGeometry(QRect(11, 81, 1118, 31))
        self.another_header.setStyleSheet(u"background-color: rgb(240, 240, 240);\n" "color: rgb(0, 0, 0);")
        self.another_label = QLabel(self.another_header)
        self.another_label.setObjectName(u"label")
        self.another_label.setGeometry(QRect(10, 0, 1101, 20))
        font = QFont()
        font.setPointSize(12)
        self.another_label.setFont(font)

        self.another_scrollArea = QScrollArea(self.another_panel)
        self.another_scrollArea.setGeometry(QRect(10, 121, 1111, 330))
        self.another_scrollArea.setWidgetResizable(True)
        self.another_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.another_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.another_scrollArea.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Fixed)
        self.another_scrollAreaWidgetContents = QWidget()
        self.another_scrollAreaWidgetContents.move(0, 0)
        self.another_scrollArea_verticalLayout = QFormLayout()
        self.another_scrollAreaWidgetContents.setLayout(self.another_scrollArea_verticalLayout)
        self.another_scrollArea.setWidget(self.another_scrollAreaWidgetContents)

        self.ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.ui)
        QMetaObject.connectSlotsByName(self.ui)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.smeta_today_nav.setText(QCoreApplication.translate("MainWindow", u"Смена (сегодня)", None))
        self.smeta_tommorow_nav.setText(QCoreApplication.translate("MainWindow", u"Смена (завтра)", None))
        self.addition_nav.setText(QCoreApplication.translate("MainWindow", u"Дополнительно", None))
        self.roller_nav.setText(QCoreApplication.translate("MainWindow", u"Ролик", None))
        self.thf.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.another.setText(QCoreApplication.translate("MainWindow", u"Дополнительно", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"Добавить", None))
        self.add_another.setText(QCoreApplication.translate("MainWindow", "Добавить", None))
        self.machine_1_tommorow.setText(QCoreApplication.translate("MainWindow", "Станок 1", None))
        self.machine_2_tommorow.setText(QCoreApplication.translate("MainWindow", "Lt-245", None))
        self.machine_3_tommorow.setText(QCoreApplication.translate("MainWindow", "ИРИС", None))
        self.add_tommorow.setText(QCoreApplication.translate("MainWindow", u"Добавить", None))
        self.smeta_today_but.setText(QCoreApplication.translate("MainWindow", "Навивка", None))
        self.reserve_today_but.setText(QCoreApplication.translate("MainWindow", "Резерв", None))
        self.machine_1_smeta.setText(QCoreApplication.translate("MainWindow", "Станок 1", None))
        self.machine_2_smeta.setText(QCoreApplication.translate("MainWindow", "Lt-245", None))
        self.machine_3_smeta.setText(QCoreApplication.translate("MainWindow", "ИРИС", None))
        self.machine_1_reserve.setText(QCoreApplication.translate("MainWindow", "Станок 1", None))
        self.machine_2_reserve.setText(QCoreApplication.translate("MainWindow", "Lt-245", None))
        self.machine_3_reserve.setText(QCoreApplication.translate("MainWindow", "ИРИС", None))
        self.reserve_machine_add.setText(QCoreApplication.translate("MainWindow", u"Добавить", None))
        self.smeta_machine_add.setText(QCoreApplication.translate("MainWindow", "Добавить", None))
        self.smeta_label.setText(QCoreApplication.translate("MainWindow", u"Номер  | Класс                                                             | Толщина шпули, мм                   | Ширина полосы, мм              | Вес, кг", None))
        self.reserve_label.setText(QCoreApplication.translate("MainWindow", u"Номер | Класс                                                                    | Ширина полосы, мм                                            | Кол-во, шт", None))
        self.tommorow_label.setText(QCoreApplication.translate("MainWindow", u"Номер  | Класс                                                             | Толщина шпули, мм                   | Ширина полосы, мм              | Вес, кг", None))
        self.another_label.setText(QCoreApplication.translate("MainWindow", u"Номер | Класс                                                             | Толщина шпули, мм                   | Ширина полосы, мм              | Вес, кг", None))
        self.thf_label.setText(QCoreApplication.translate("MainWindow", u"Номер | Класс                                                                                                         | Кол-во, шт", None))
        self.roller_process.setText(QCoreApplication.translate("MainWindow", "Посчитать", None))
        self.roller_label.setText(QCoreApplication.translate("MainWindow", "Номер  | Класс                                                                                                         | Толщина картона, мм     | Ролик                             | Станок", None))
    # retranslateUi

    #функции кнопок навигации
    def smeta_today_nav_clicked(self):
        self.roller_page.setVisible(False)
        self.additional_page.setVisible(False)
        self.smeta_tommorow_page.setVisible(False)
        self.smeta_today_page.setVisible(True)
        if self.smeta_machine_1_scrollArea.isVisible():
            self.clear_empty_rows_today_m_1()
        if self.smeta_machine_2_scrollArea.isVisible():
            self.clear_empty_rows_today_m_2()
        if self.smeta_machine_3_scrollArea.isVisible():
            self.clear_empty_rows_today_m_3()
        if self.reserve_machine_1_scrollArea.isVisible():
            self.clear_empty_rows_reserve_m_1()
        if self.reserve_machine_2_scrollArea.isVisible():
            self.clear_empty_rows_reserve_m_2()
        if self.reserve_machine_3_scrollArea.isVisible():
            self.clear_empty_rows_reserve_m_3()
    
    def smeta_tommorow_nav_clicked(self):
        self.smeta_today_page.setVisible(False)
        self.roller_page.setVisible(False)
        self.additional_page.setVisible(False)
        self.smeta_tommorow_page.setVisible(True)
        if self.tommorow_machine_1_scrollArea.isVisible():
            self.clear_empty_rows_tommorow_m_1()
        if self.tommorow_machine_2_scrollArea.isVisible():
            self.clear_empty_rows_tommorow_m_2()
        if self.tommorow_machine_3_scrollArea.isVisible():
            self.clear_empty_rows_tommorow_m_3()

    def addition_nav_clicked(self):
        self.smeta_today_page.setVisible(False)
        self.roller_page.setVisible(False)
        self.smeta_tommorow_page.setVisible(False)
        self.additional_page.setVisible(True)
        if self.thf_panel.isVisible():
            self.clear_empty_rows_thf()
        if self.another_panel.isVisible():
            self.clear_empty_rows_additional()

    def roller_nav_clicked(self):
        self.smeta_today_page.setVisible(False)
        self.smeta_tommorow_page.setVisible(False)
        self.additional_page.setVisible(False)
        self.roller_page.setVisible(True)
    #-------------------------------------------------------

    #функции кнопок страницы смета (сегодня)
    def smeta_today_but_clicked(self):
        match self.reserve_get_current_machine():
            case 1:
                self.clear_empty_rows_reserve_m_1()
            case 2: 
                self.clear_empty_rows_reserve_m_2()
            case 3:
                self.clear_empty_rows_reserve_m_3()
        self.reserve_today_but.setChecked(False)
        self.smeta_reserve_panel.setVisible(False)
        self.smeta_today_panel.setVisible(True)
        self.current_machine_id = self.today_get_current_machine()

    def reserve_today_but_clicked(self):
        match self.today_get_current_machine():
            case 1:
                self.clear_empty_rows_today_m_1()
            case 2: 
                self.clear_empty_rows_today_m_2()
            case 3:
                self.clear_empty_rows_today_m_3()
        self.smeta_today_but.setChecked(False)
        self.smeta_today_panel.setVisible(False)
        self.smeta_reserve_panel.setVisible(True)
        self.current_machine_id = self.reserve_get_current_machine()

    #кнопки сметы
    def machine_1_today_clicked(self):
        self.clear_empty_rows_today_m_1()
        self.machine_2_smeta.setChecked(False)
        self.machine_3_smeta.setChecked(False)
        self.machine_1_smeta.setChecked(True)
        self.smeta_machine_2_scrollArea.setVisible(False)
        self.smeta_machine_3_scrollArea.setVisible(False)
        self.smeta_machine_1_scrollArea.setVisible(True)
        self.current_machine_id = self.today_get_current_machine()

    def machine_2_today_clicked(self):
        self.clear_empty_rows_today_m_2()
        self.machine_1_smeta.setChecked(False)
        self.machine_3_smeta.setChecked(False)
        self.machine_2_smeta.setChecked(True)
        self.smeta_machine_1_scrollArea.setVisible(False)
        self.smeta_machine_3_scrollArea.setVisible(False)
        self.smeta_machine_2_scrollArea.setVisible(True)
        self.current_machine_id = self.today_get_current_machine()

    def machine_3_today_clicked(self):
        self.clear_empty_rows_today_m_3()
        self.machine_1_smeta.setChecked(False)
        self.machine_2_smeta.setChecked(False)
        self.machine_3_smeta.setChecked(True)
        self.smeta_machine_1_scrollArea.setVisible(False)
        self.smeta_machine_2_scrollArea.setVisible(False)
        self.smeta_machine_3_scrollArea.setVisible(True)
        self.current_machine_id = self.today_get_current_machine()

    def today_get_current_machine(self):
        if self.smeta_machine_1_scrollArea.isVisible():
            return 1
        if self.smeta_machine_2_scrollArea.isVisible():
            return 2
        if self.smeta_machine_3_scrollArea.isVisible():
            return 3
        return -1

    def smeta_machine_add_clicked(self):
        if(self.current_machine_id == 1):
            _Len = len(self.today_machine_1_list)+1
            self.today_machine_1_list.append(self.add_row_smeta(self.smeta_machine_1_verticalLayout,_Len))
        elif(self.current_machine_id == 2):
            _Len = len(self.today_machine_2_list)+1
            self.today_machine_2_list.append(self.add_row_smeta(self.smeta_machine_2_verticalLayout,_Len))
        elif(self.current_machine_id == 3):
            _Len = len(self.today_machine_3_list)+1
            self.today_machine_3_list.append(self.add_row_smeta(self.smeta_machine_3_verticalLayout,_Len))

    #кнопки резерва
    def machine_1_reserve_clicked(self):
        self.clear_empty_rows_reserve_m_1()
        self.machine_2_reserve.setChecked(False)
        self.machine_3_reserve.setChecked(False)
        self.machine_1_reserve.setChecked(True)
        self.reserve_machine_2_scrollArea.setVisible(False)
        self.reserve_machine_3_scrollArea.setVisible(False)
        self.reserve_machine_1_scrollArea.setVisible(True)
        self.current_machine_id = self.reserve_get_current_machine()

    def machine_2_reserve_clicked(self):
        self.clear_empty_rows_reserve_m_2()
        self.machine_1_reserve.setChecked(False)
        self.machine_3_reserve.setChecked(False)
        self.machine_2_reserve.setChecked(True)
        self.reserve_machine_1_scrollArea.setVisible(False)
        self.reserve_machine_3_scrollArea.setVisible(False)
        self.reserve_machine_2_scrollArea.setVisible(True)
        self.current_machine_id = self.reserve_get_current_machine()

    def machine_3_reserve_clicked(self):
        self.clear_empty_rows_reserve_m_3()
        self.machine_1_reserve.setChecked(False)
        self.machine_2_reserve.setChecked(False)
        self.machine_3_reserve.setChecked(True)
        self.reserve_machine_1_scrollArea.setVisible(False)
        self.reserve_machine_2_scrollArea.setVisible(False)
        self.reserve_machine_3_scrollArea.setVisible(True)
        self.current_machine_id = self.reserve_get_current_machine()

    def reserve_get_current_machine(self):
        if self.reserve_machine_1_scrollArea.isVisible():
            return 1
        if self.reserve_machine_2_scrollArea.isVisible():
            return 2
        if self.reserve_machine_3_scrollArea.isVisible():
            return 3
        return -1

    def reserve_machine_add_clicked(self):
        if(self.current_machine_id == 1):
            _Len = len(self.reserve_machine_1_list)+1
            self.reserve_machine_1_list.append(self.add_row_reserve(self.reserve_machine_1_verticalLayout,_Len))
        elif(self.current_machine_id == 2):
            _Len = len(self.reserve_machine_2_list)+1
            self.reserve_machine_2_list.append(self.add_row_reserve(self.reserve_machine_2_verticalLayout,_Len))
        elif(self.current_machine_id == 3):
            _Len = len(self.reserve_machine_3_list)+1
            self.reserve_machine_3_list.append(self.add_row_reserve(self.reserve_machine_3_verticalLayout,_Len))

    #--------------------------------------------------------

    #функции кнопок резерва 

    def machine_1_tommorow_clicked(self):
        self.clear_empty_rows_tommorow_m_1()
        self.machine_2_tommorow.setChecked(False)
        self.machine_3_tommorow.setChecked(False)
        self.tommorow_machine_2_scrollArea.setVisible(False)
        self.tommorow_machine_3_scrollArea.setVisible(False)
        self.tommorow_machine_1_scrollArea.setVisible(True)
        self.current_machine_id = self.tommorow_get_current_machine()

    def machine_2_tommorow_clicked(self):
        self.clear_empty_rows_tommorow_m_2()
        self.machine_1_tommorow.setChecked(False)
        self.machine_3_tommorow.setChecked(False)
        self.tommorow_machine_1_scrollArea.setVisible(False)
        self.tommorow_machine_3_scrollArea.setVisible(False)
        self.tommorow_machine_2_scrollArea.setVisible(True)
        self.current_machine_id = self.tommorow_get_current_machine()

    def machine_3_tommorow_clicked(self):
        self.clear_empty_rows_tommorow_m_3()
        self.machine_1_tommorow.setChecked(False)
        self.machine_2_tommorow.setChecked(False)
        self.tommorow_machine_1_scrollArea.setVisible(False)
        self.tommorow_machine_2_scrollArea.setVisible(False)
        self.tommorow_machine_3_scrollArea.setVisible(True)
        self.current_machine_id = self.tommorow_get_current_machine()

    def tommorow_get_current_machine(self):
        if self.tommorow_machine_1_scrollArea.isVisible():
            return 1
        if self.tommorow_machine_2_scrollArea.isVisible():
            return 2
        if self.tommorow_machine_3_scrollArea.isVisible():
            return 3
        return -1

    def tommorow_machine_add_clicked(self):
        if(self.current_machine_id == 1):
            _Len = len(self.tommorow_machine_1_list)+1
            self.tommorow_machine_1_list.append(self.add_row_smeta(self.tommorow_1_verticalLayout,_Len))
        elif(self.current_machine_id == 2):
            _Len = len(self.tommorow_machine_2_list)+1
            self.tommorow_machine_2_list.append(self.add_row_smeta(self.tommorow_2_verticalLayout,_Len))
        elif(self.current_machine_id == 3):
            _Len = len(self.tommorow_machine_3_list)+1
            self.tommorow_machine_3_list.append(self.add_row_smeta(self.tommorow_3_verticalLayout,_Len))
    #функции кнопок страницы дополнительно

    def thf_clicked(self):
        self.clear_empty_rows_thf()
        self.another.setChecked(False)
        self.another_panel.setVisible(False)
        self.thf_panel.setVisible(True)

    def another_clicked(self):
        self.clear_empty_rows_additional()
        self.thf.setChecked(False)
        self.thf_panel.setVisible(False)
        self.another_panel.setVisible(True)

    def thf_add_clicked(self):
        self.thf_list.append(self.add_row_thf())

    def additional_add_clicked(self):
        _Len = len(self.additional_list)+1
        self.additional_list.append(self.add_row_smeta(self.another_scrollArea_verticalLayout,_Len, -2))

    #вспомогательные функции
    def getClassIndex(self,name):
        return self.class_list.index(name)
    
    def getRollerIndex(self,roller):
        if roller in self.roller_list:
            return self.roller_list.index(roller)
        return 0

    def getMachineById(self,id):
        if -1 < id and id < 5:
            return self.machine_names[id]
        return "None"
    #--------------------------------------------

    #функции добавления в таблицы
    def add_row_smeta(self,parent_widget,massLen, stop_id = -1):
        if(self.current_machine_id != stop_id):
            widget12 = QWidget()
            widget12.setObjectName(u"widget")
            widget12.setFixedHeight(41)
            widget12.setFixedWidth(1111)
            widget12.show()
            lineEdit_5 = QLineEdit(widget12)
            lineEdit_5.setGeometry(QRect(10, 10, 36, 31))
            lineEdit_5.setStyleSheet(self.tb)
            lineEdit_5.setText(QCoreApplication.translate("MainWindow", str(massLen), None))
            lineEdit_5.show()
            lineEdit_5.setEnabled(False)
            comboBox = QComboBox(widget12)
            comboBox.setStyleSheet(self.tb)
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.setObjectName(u"comboBox")
            comboBox.setGeometry(QRect(65, 10, 301, 31))
            comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Стандарт", None))
            comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Эконом", None))
            comboBox.show()
            lineEdit_2 = QLineEdit(widget12)
            lineEdit_2.setGeometry(QRect(380, 10, 221, 31))
            lineEdit_2.setStyleSheet(self.tb)
            lineEdit_2.show()
            lineEdit_2.setPlaceholderText(u"10")
            lineEdit_3 = QLineEdit(widget12)
            lineEdit_3.setGeometry(QRect(620, 10, 201, 31))
            lineEdit_3.setStyleSheet(self.tb)
            lineEdit_3.show()
            lineEdit_3.setPlaceholderText(u"(70/100/150/166)")
            lineEdit_4 = QLineEdit(widget12)
            lineEdit_4.setGeometry(QRect(840, 10, 201, 31))
            lineEdit_4.setStyleSheet(self.tb)
            lineEdit_4.show()
            lineEdit_4.setPlaceholderText(u"1000")
            parent_widget.addRow(widget12)
            return widget12
        
    def add_row_reserve(self,parent_widget,massLen):
        if(self.current_machine_id != -1):
            widget12 = QWidget()
            widget12.setObjectName(u"widget")
            widget12.setFixedHeight(41)
            widget12.setFixedWidth(1111)
            widget12.show()
            lineEdit_5 = QLineEdit(widget12)
            lineEdit_5.setGeometry(QRect(10, 10, 36, 31))
            lineEdit_5.setStyleSheet(self.tb)
            lineEdit_5.setText(QCoreApplication.translate("MainWindow", str(massLen), None))
            lineEdit_5.show()
            lineEdit_5.setEnabled(False)
            comboBox = QComboBox(widget12)
            comboBox.setStyleSheet(self.tb)
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.addItem("")
            comboBox.setObjectName(u"comboBox")
            comboBox.setGeometry(QRect(60, 10, 331, 31))
            comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Стандарт", None))
            comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Эконом", None))
            comboBox.show()
            lineEdit_2 = QLineEdit(widget12)
            lineEdit_2.setGeometry(QRect(410, 10, 331, 31))
            lineEdit_2.setStyleSheet(self.tb)
            lineEdit_2.show()
            lineEdit_2.setPlaceholderText(u"(70/100/150/166)")
            lineEdit_3 = QLineEdit(widget12)
            lineEdit_3.setGeometry(QRect(760, 10, 331, 31))
            lineEdit_3.setStyleSheet(self.tb)
            lineEdit_3.show()
            lineEdit_3.setPlaceholderText(u"10")
            parent_widget.addRow(widget12)
            return widget12
        
    def add_row_thf(self):
        widget12 = QWidget()
        widget12.setObjectName(u"widget")
        widget12.setFixedHeight(41)
        widget12.setFixedWidth(1111)
        widget12.show()
        lineEdit_5 = QLineEdit(widget12)
        lineEdit_5.setGeometry(QRect(10, 10, 36, 31))
        lineEdit_5.setStyleSheet(self.tb)
        lineEdit_5.setText(QCoreApplication.translate("MainWindow", str(len(self.thf_list)+1), None))
        lineEdit_5.show()
        lineEdit_5.setEnabled(False)
        comboBox = QComboBox(widget12)
        comboBox.setStyleSheet(self.tb)
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.setObjectName(u"comboBox")
        comboBox.setGeometry(QRect(60, 10, 496, 31))
        comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Стандарт", None))
        comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Эконом", None))
        comboBox.show()
        lineEdit_3 = QLineEdit(widget12)
        lineEdit_3.setGeometry(QRect(576, 10, 496, 31))
        lineEdit_3.setStyleSheet(self.tb)
        lineEdit_3.show()
        lineEdit_3.setPlaceholderText(u"10")
        self.thf_scrollArea_verticalLayout.addRow(widget12)
        return widget12

    def add_row_result(self,_enable=False):
        _len = len(self.result_list)+1
        widget12 = QWidget()
        widget12.setObjectName(u"widget")
        widget12.setFixedHeight(41)
        widget12.setFixedWidth(1111)
        widget12.show()
        lineEdit_5 = QLineEdit(widget12)
        lineEdit_5.setGeometry(QRect(10, 10, 36, 31))
        lineEdit_5.setStyleSheet(self.tb)
        lineEdit_5.setText(QCoreApplication.translate("MainWindow", str(_len), None))
        lineEdit_5.show()
        lineEdit_5.setEnabled(False)
        comboBox = QComboBox(widget12)
        comboBox.setStyleSheet(self.tb)
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.addItem("")
        comboBox.setObjectName(u"comboBox")
        comboBox.setGeometry(QRect(65, 10, 491, 31))
        comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Стандарт", None))
        comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Эконом", None))
        comboBox.show()
        comboBox.setEnabled(_enable)
        lineEdit_1 = QLineEdit(widget12)
        lineEdit_1.setGeometry(QRect(570, 10, 171, 31))
        lineEdit_1.setStyleSheet(self.tb)
        lineEdit_1.show()
        lineEdit_1.setPlaceholderText(u"(70/100/150/166)")
        lineEdit_1.setEnabled(_enable)
        comboBox1 = QComboBox(widget12)
        comboBox1.setStyleSheet(self.tb)
        comboBox1.addItem("")
        comboBox1.addItem("")
        comboBox1.addItem("")
        comboBox1.setObjectName(u"comboBox")
        comboBox1.setGeometry(QRect(760, 10, 161, 31))
        comboBox1.setItemText(0, QCoreApplication.translate("MainWindow", u" ", None))
        comboBox1.setItemText(1, QCoreApplication.translate("MainWindow", u"840", None))
        comboBox1.setItemText(2, QCoreApplication.translate("MainWindow", u"1050", None))
        comboBox1.show()
        comboBox1.setEnabled(_enable)
        lineEdit_2 = QLineEdit(widget12)
        lineEdit_2.setGeometry(QRect(940, 10, 161, 31))
        lineEdit_2.setStyleSheet(self.tb)
        lineEdit_2.show()
        lineEdit_2.setPlaceholderText(u"№")
        lineEdit_2.setEnabled(_enable)
        self.roller_verticalLayout.addRow(widget12)
        self.result_list.append(widget12)
        return widget12

    #кнопка вычисления

    def calculate_roller(self):
        self.clear_empty_rows_all()
        self.clear_roller_table()
        self.method.main()


    #Функции чтения
    
    def get_today_m_1(self):
        massive = []
        for i in range(len(self.today_machine_1_list)):
            local_massive = []
            local_massive.append(self.today_machine_1_list[i].children()[1].currentText())
            local_massive.append(self.today_machine_1_list[i].children()[2].text())
            local_massive.append(self.today_machine_1_list[i].children()[3].text())
            local_massive.append(self.today_machine_1_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    def get_today_m_2(self):
        massive = []
        for i in range(len(self.today_machine_2_list)):
            local_massive = []
            local_massive.append(self.today_machine_2_list[i].children()[1].currentText())
            local_massive.append(self.today_machine_2_list[i].children()[2].text())
            local_massive.append(self.today_machine_2_list[i].children()[3].text())
            local_massive.append(self.today_machine_2_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    def get_today_m_3(self):
        massive = []
        for i in range(len(self.today_machine_3_list)):
            local_massive = []
            local_massive.append(self.today_machine_3_list[i].children()[1].currentText())
            local_massive.append(self.today_machine_3_list[i].children()[2].text())
            local_massive.append(self.today_machine_3_list[i].children()[3].text())
            local_massive.append(self.today_machine_3_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    def get_reserve_m_1(self):
        massive = []
        for i in range(len(self.reserve_machine_1_list)):
            local_massive = []
            local_massive.append(self.reserve_machine_1_list[i].children()[1].currentText())
            local_massive.append(self.reserve_machine_1_list[i].children()[2].text())
            local_massive.append(self.reserve_machine_1_list[i].children()[3].text())
            massive.append(local_massive)
        return massive

    def get_reserve_m_2(self):
        massive = []
        for i in range(len(self.reserve_machine_2_list)):
            local_massive = []
            local_massive.append(self.reserve_machine_2_list[i].children()[1].currentText())
            local_massive.append(self.reserve_machine_2_list[i].children()[2].text())
            local_massive.append(self.reserve_machine_2_list[i].children()[3].text())
            massive.append(local_massive)
        return massive

    def get_reserve_m_3(self):
        massive = []
        for i in range(len(self.reserve_machine_3_list)):
            local_massive = []
            local_massive.append(self.reserve_machine_3_list[i].children()[1].currentText())
            local_massive.append(self.reserve_machine_3_list[i].children()[2].text())
            local_massive.append(self.reserve_machine_3_list[i].children()[3].text())
            massive.append(local_massive)
        return massive

    def get_roller(self):
        massive = []
        for i in range(len(self.result_list)):
            local_massive = []
            local_massive.append(self.result_list[i].children()[1].currentText())
            local_massive.append(self.result_list[i].children()[2].text())
            local_massive.append(self.result_list[i].children()[3].currentText())
            local_massive.append(self.result_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    def get_tommorow_m_1(self):
        massive = []
        for i in range(len(self.tommorow_machine_1_list)):
            local_massive = []
            local_massive.append(self.tommorow_machine_1_list[i].children()[1].currentText())
            local_massive.append(self.tommorow_machine_1_list[i].children()[2].text())
            local_massive.append(self.tommorow_machine_1_list[i].children()[3].text())
            local_massive.append(self.tommorow_machine_1_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    def get_tommorow_m_2(self):
        massive = []
        for i in range(len(self.tommorow_machine_2_list)):
            local_massive = []
            local_massive.append(self.tommorow_machine_2_list[i].children()[1].currentText())
            local_massive.append(self.tommorow_machine_2_list[i].children()[2].text())
            local_massive.append(self.tommorow_machine_2_list[i].children()[3].text())
            local_massive.append(self.tommorow_machine_2_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    def get_tommorow_m_3(self):
        massive = []
        for i in range(len(self.tommorow_machine_3_list)):
            local_massive = []
            local_massive.append(self.tommorow_machine_3_list[i].children()[1].currentText())
            local_massive.append(self.tommorow_machine_3_list[i].children()[2].text())
            local_massive.append(self.tommorow_machine_3_list[i].children()[3].text())
            local_massive.append(self.tommorow_machine_3_list[i].children()[4].text())
            massive.append(local_massive)
        return massive
    
    def get_thf(self):
        massive = []
        for i in range(len(self.thf_list)):
            local_massive = []
            local_massive.append(self.thf_list[i].children()[1].currentText())
            local_massive.append(self.thf_list[i].children()[2].text())
            massive.append(local_massive)
        return massive

    def get_addititonal(self):
        massive = []
        for i in range(len(self.additional_list)):
            local_massive = []
            local_massive.append(self.additional_list[i].children()[1].currentText())
            local_massive.append(self.additional_list[i].children()[2].text())
            local_massive.append(self.additional_list[i].children()[3].text())
            local_massive.append(self.additional_list[i].children()[4].text())
            massive.append(local_massive)
        return massive

    #функции полной очистки
    def clear_today_m_1(self):
        for i in range(len(self.today_machine_1_list)):
            self.smeta_machine_1_verticalLayout.removeRow(self.today_machine_1_list[i])
        self.today_machine_1_list.clear()

    def clear_today_m_2(self):
        for i in range(len(self.today_machine_2_list)):
            self.smeta_machine_2_verticalLayout.removeRow(self.today_machine_2_list[i])
        self.today_machine_2_list.clear()

    def clear_today_m_3(self):
        for i in range(len(self.today_machine_3_list)):
            self.smeta_machine_3_verticalLayout.removeRow(self.today_machine_3_list[i])
        self.today_machine_3_list.clear()

    def clear_reserve_m_1(self):
        for i in range(len(self.reserve_machine_1_list)):
            self.reserve_machine_1_verticalLayout.removeRow(self.reserve_machine_1_list[i])
        self.reserve_machine_1_list.clear()

    def clear_today_m_2(self):
        for i in range(len(self.reserve_machine_2_list)):
            self.reserve_machine_2_verticalLayout.removeRow(self.reserve_machine_2_list[i])
        self.reserve_machine_2_list.clear()

    def clear_today_m_3(self):
        for i in range(len(self.reserve_machine_3_list)):
            self.reserve_machine_3_verticalLayout.removeRow(self.reserve_machine_3_list[i])
        self.reserve_machine_3_list.clear()

    def clear_roller_table(self):
        for i in range(len(self.result_list)):
            self.roller_verticalLayout.removeRow(self.result_list[i])
        self.result_list.clear()

    def clear_tommorow_m_1(self):
        for i in range(len(self.tommorow_machine_1_list)):
            self.tommorow_1_verticalLayout.removeRow(self.tommorow_machine_1_list[i])
        self.tommorow_machine_1_list.clear()

    def clear_tommorow_m_2(self):
        for i in range(len(self.tommorow_machine_2_list)):
            self.tommorow_2_verticalLayout.removeRow(self.tommorow_machine_2_list[i])
        self.tommorow_machine_2_list.clear()

    def clear_tommorow_m_3(self):
        for i in range(len(self.tommorow_machine_3_list)):
            self.tommorow_3_verticalLayout.removeRow(self.tommorow_machine_3_list[i])
        self.tommorow_machine_3_list.clear()

    def clear_thf(self):
        for i in range(len(self.thf_list)):
            self.thf_scrollArea_verticalLayout.removeRow(self.thf_list[i])
        self.thf_list.clear()

    def clear_additional(self):
        for i in range(len(self.additional_list)):
            self.another_scrollArea_verticalLayout.removeRow(self.additional_list[i])
        self.additional_list.clear()


    #очистка пустых строк

    def check_empty_rows_today(self, row):
        for i in range(2,5,1):
            if row.children()[i].text() == "":
                return True
        return False

    def check_empty_rows_reserve(self, row):
        for i in range(2,4,1):
            if row.children()[i].text() == "":
                return True
        return False
    
    def check_empty_rows_thf(self, row):
        if row.children()[2].text() == "":
            return True
        return False


    def clear_empty_rows_today_m_1(self):
        i = 0
        while i < len(self.today_machine_1_list):
            row = self.today_machine_1_list[i]
            if self.check_empty_rows_today(row):
                self.smeta_machine_1_verticalLayout.removeRow(row)
                self.today_machine_1_list.remove(row)
                i = 0
            else: i+=1
        

    def clear_empty_rows_today_m_2(self):
        i = 0
        while i < len(self.today_machine_2_list):
            row = self.today_machine_2_list[i]
            if self.check_empty_rows_today(row):
                self.smeta_machine_2_verticalLayout.removeRow(row)
                self.today_machine_2_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_today_m_3(self):
        i = 0
        while i < len(self.today_machine_3_list):
            row = self.today_machine_3_list[i]
            if self.check_empty_rows_today(row):
                self.smeta_machine_3_verticalLayout.removeRow(row)
                self.today_machine_3_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_reserve_m_1(self):
        i = 0
        while i < len(self.reserve_machine_1_list):
            row = self.reserve_machine_1_list[i]
            if self.check_empty_rows_reserve(row):
                self.reserve_machine_1_verticalLayout.removeRow(row)
                self.reserve_machine_1_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_reserve_m_2(self):
        i = 0
        while i < len(self.reserve_machine_2_list):
            row = self.reserve_machine_2_list[i]
            if self.check_empty_rows_reserve(row):
                self.reserve_machine_2_verticalLayout.removeRow(row)
                self.reserve_machine_2_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_reserve_m_3(self):
        i = 0
        while i < len(self.reserve_machine_3_list):
            row = self.reserve_machine_3_list[i]
            if self.check_empty_rows_reserve(row):
                self.reserve_machine_3_verticalLayout.removeRow(row)
                self.reserve_machine_3_list.remove(row)
                i = 0
            else: i+=1
    
    def clear_empty_rows_tommorow_m_1(self):
        i = 0
        while i < len(self.tommorow_machine_1_list):
            row = self.tommorow_machine_1_list[i]
            if self.check_empty_rows_today(row):
                self.tommorow_1_verticalLayout.removeRow(row)
                self.tommorow_machine_1_list.remove(row)
                i = 0
            else: i+=1
        

    def clear_empty_rows_tommorow_m_2(self):
        i = 0
        while i < len(self.tommorow_machine_2_list):
            row = self.tommorow_machine_2_list[i]
            if self.check_empty_rows_today(row):
                self.tommorow_2_verticalLayout.removeRow(row)
                self.tommorow_machine_2_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_tommorow_m_3(self):
        i = 0
        while i < len(self.tommorow_machine_3_list):
            row = self.tommorow_machine_3_list[i]
            if self.check_empty_rows_today(row):
                self.tommorow_3_verticalLayout.removeRow(row)
                self.tommorow_machine_3_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_thf(self):
        i = 0
        while i < len(self.thf_list):
            row = self.thf_list[i]
            if self.check_empty_rows_thf(row):
                self.thf_scrollArea_verticalLayout.removeRow(row)
                self.thf_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_additional(self):
        i = 0
        while i < len(self.additional_list):
            row = self.additional_list[i]
            if self.check_empty_rows_today(row):
                self.another_scrollArea_verticalLayout.removeRow(row)
                self.additional_list.remove(row)
                i = 0
            else: i+=1

    def clear_empty_rows_all(self):
        self.clear_empty_rows_today_m_1()
        self.clear_empty_rows_today_m_2()
        self.clear_empty_rows_today_m_3()
        self.clear_empty_rows_reserve_m_1()
        self.clear_empty_rows_reserve_m_2()
        self.clear_empty_rows_reserve_m_3()
        self.clear_empty_rows_tommorow_m_1()
        self.clear_empty_rows_tommorow_m_2()
        self.clear_empty_rows_tommorow_m_3()
        self.clear_empty_rows_thf()
        self.clear_empty_rows_additional()

        #функция заполнения
    def fill_today_m_1(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.today_machine_1_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 1
            for i in range(len(mass)):
                _Len = len(self.today_machine_1_list)+1
                self.today_machine_1_list.append(self.add_row_smeta(self.smeta_machine_1_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.today_machine_1_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.today_machine_1_list[i].children()[2].setText(str(mass[i][1]))
                self.today_machine_1_list[i].children()[3].setText(str(mass[i][2]))
                self.today_machine_1_list[i].children()[4].setText(str(mass[i][3]))
            self.current_machine_id = last_current_machine


    def fill_today_m_2(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.today_machine_2_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 2
            for i in range(len(mass)):
                _Len = len(self.today_machine_2_list)+1
                self.today_machine_2_list.append(self.add_row_smeta(self.smeta_machine_2_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.today_machine_2_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.today_machine_2_list[i].children()[2].setText(str(mass[i][1]))
                self.today_machine_2_list[i].children()[3].setText(str(mass[i][2]))
                self.today_machine_2_list[i].children()[4].setText(str(mass[i][3]))
            self.current_machine_id = last_current_machine

    def fill_today_m_3(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.today_machine_3_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 3
            for i in range(len(mass)):
                _Len = len(self.today_machine_3_list)+1
                self.today_machine_3_list.append(self.add_row_smeta(self.smeta_machine_3_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.today_machine_3_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.today_machine_3_list[i].children()[2].setText(str(mass[i][1]))
                self.today_machine_3_list[i].children()[3].setText(str(mass[i][2]))
                self.today_machine_3_list[i].children()[4].setText(str(mass[i][3]))
            self.current_machine_id = last_current_machine
    
    def fill_reserve_m_1(self, mass):  #вход [ [класс, ширина полосы, Вес], ...]
        if len(self.reserve_machine_1_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 3
            for i in range(len(mass)):
                _Len = len(self.reserve_machine_1_list)+1
                self.reserve_machine_1_list.append(self.add_row_reserve(self.reserve_machine_1_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.reserve_machine_1_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.reserve_machine_1_list[i].children()[2].setText(str(mass[i][1]))
                self.reserve_machine_1_list[i].children()[3].setText(str(mass[i][2]))
            self.current_machine_id = last_current_machine  
    
    def fill_reserve_m_2(self, mass):  #вход [ [класс, ширина полосы, Вес], ...]
        if len(self.reserve_machine_2_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 3
            for i in range(len(mass)):
                _Len = len(self.reserve_machine_2_list)+1
                self.reserve_machine_2_list.append(self.add_row_reserve(self.reserve_machine_2_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.reserve_machine_2_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.reserve_machine_2_list[i].children()[2].setText(str(mass[i][1]))
                self.reserve_machine_2_list[i].children()[3].setText(str(mass[i][2]))
            self.current_machine_id = last_current_machine    

    def fill_reserve_m_3(self, mass): #вход [ [класс, ширина полосы, Вес], ...]
        if len(self.reserve_machine_3_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 3
            for i in range(len(mass)):
                _Len = len(self.reserve_machine_3_list)+1
                self.reserve_machine_3_list.append(self.add_row_reserve(self.reserve_machine_3_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.reserve_machine_3_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.reserve_machine_3_list[i].children()[2].setText(str(mass[i][1]))
                self.reserve_machine_3_list[i].children()[3].setText(str(mass[i][2]))
            self.current_machine_id = last_current_machine

    def fill_tommorow_m_1(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.tommorow_machine_1_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 1
            for i in range(len(mass)):
                _Len = len(self.tommorow_machine_1_list)+1
                self.tommorow_machine_1_list.append(self.add_row_smeta(self.tommorow_1_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.tommorow_machine_1_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.tommorow_machine_1_list[i].children()[2].setText(str(mass[i][1]))
                self.tommorow_machine_1_list[i].children()[3].setText(str(mass[i][2]))
                self.tommorow_machine_1_list[i].children()[4].setText(str(mass[i][3]))
            self.current_machine_id = last_current_machine


    def fill_tommorow_m_2(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.tommorow_machine_2_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 2
            for i in range(len(mass)):
                _Len = len(self.tommorow_machine_2_list)+1
                self.tommorow_machine_2_list.append(self.add_row_smeta(self.tommorow_2_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.tommorow_machine_2_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.tommorow_machine_2_list[i].children()[2].setText(str(mass[i][1]))
                self.tommorow_machine_2_list[i].children()[3].setText(str(mass[i][2]))
                self.tommorow_machine_2_list[i].children()[4].setText(str(mass[i][3]))
            self.current_machine_id = last_current_machine

    def fill_tommorow_m_3(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.tommorow_machine_3_list) == 0:
            last_current_machine = self.current_machine_id
            self.current_machine_id = 3
            for i in range(len(mass)):
                _Len = len(self.tommorow_machine_3_list)+1
                self.tommorow_machine_3_list.append(self.add_row_smeta(self.tommorow_3_verticalLayout,_Len))
            
            for i in range(len(mass)):
                self.tommorow_machine_3_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.tommorow_machine_3_list[i].children()[2].setText(str(mass[i][1]))
                self.tommorow_machine_3_list[i].children()[3].setText(str(mass[i][2]))
                self.tommorow_machine_3_list[i].children()[4].setText(str(mass[i][3]))
            self.current_machine_id = last_current_machine

    def fill_thf(self, mass): #вход [ [класс, ширина полосы, Вес], ...]
        if len(self.thf_list) == 0:
            for i in range(len(mass)):
                self.thf_list.append(self.add_row_thf())
            
            for i in range(len(mass)):
                self.thf_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.thf_list[i].children()[2].setText(str(mass[i][1]))

    def fill_additional(self, mass): #вход [ [класс, толщина шпули, ширина полосы, Вес], ...]
        if len(self.additional_list) == 0:
            for i in range(len(mass)):
                _Len = len(self.additional_list)+1
                self.additional_list.append(self.add_row_smeta(self.another_scrollArea_verticalLayout,_Len,-2))
            for i in range(len(mass)):
                self.additional_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.additional_list[i].children()[2].setText(str(mass[i][1]))
                self.additional_list[i].children()[3].setText(str(mass[i][2]))
                self.additional_list[i].children()[4].setText(str(mass[i][3]))

    #полное добавление в пустую таблицу
    def fill_roller_table(self,mass):  #вход [ [класс, Толщина картона, Ролик, Станок], ...]
        if len(self.result_list) == 0:
            for i in range(len(mass)):
                self.add_row_result()

            for i in range(len(mass)):
                self.result_list[i].children()[1].setCurrentIndex(self.getClassIndex(mass[i][0]))
                self.result_list[i].children()[2].setText(str(mass[i][1]))
                self.result_list[i].children()[3].setCurrentIndex(self.getRollerIndex(mass[i][2]))
                self.result_list[i].children()[4].setText(self.getMachineById(int(mass[i][3])))

    #единичное добавление
    def add_roller_row(self,row):   #вход [класс, Толщина картона, Ролик, Станок]
        self.add_row_result()
        last_index = 0
        if len(self.result_list) != 0:
            last_index = len(self.result_list)-1
        self.result_list[last_index].children()[1].setCurrentIndex(self.getClassIndex(row[0]))
        self.result_list[last_index].children()[2].setText(str(row[1]))
        self.result_list[last_index].children()[3].setCurrentIndex(self.getRollerIndex(row[2]))
        self.result_list[last_index].children()[4].setText(self.getMachineById(int(row[3])))
        if self.getRollerIndex(row[2]) == 0:
            #app = QApplication(sys.argv)
            dialog = InputDialog("Введите данные:")
            if dialog.exec() == QDialog.Accepted:
                user_input = dialog.get_input()
                self.result_list[last_index].children()[3].setCurrentIndex(self.getRollerIndex(user_input))
                return user_input
        return 0

    def setPallete(self,_theme):
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(250, 250, 250, 255))
        brush1.setStyle(Qt.SolidPattern)
        brush1_l = QBrush(QColor(227, 234, 240, 255))
        brush1_l.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(242, 247, 250, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(115, 119, 122, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(153, 159, 163, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1_l)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1_l)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(115, 119, 122, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        return palette

    def assign_fuction(self,func): #связь с классом выполнения
        self.method = func
        

class InputDialog(QDialog):
    def __init__(self, prompt):
        super().__init__()
        self.setWindowTitle("Выбор ролика")
        self.layout = QVBoxLayout()

        self.label = QLabel(prompt)
        self.layout.addWidget(self.label)

        self.comboBox1 = QComboBox()
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.setItemText(0, QCoreApplication.translate("MainWindow", u"840", None))
        self.comboBox1.setItemText(1, QCoreApplication.translate("MainWindow", u"1050", None))
        self.layout.addWidget(self.comboBox1)

        self.submit_button = QPushButton("Подтвердить")
        self.submit_button.clicked.connect(self.accept)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def get_input(self):
        return self.comboBox1.currentText()
