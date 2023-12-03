from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import Qt
import sounddevice as sd
import psutil
import sqlite3
import openai
import threading
import time
import resources1


class Jarvis_GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(698, 719)
        MainWindow.setMinimumSize(QtCore.QSize(698, 719))
        MainWindow.setMaximumSize(QtCore.QSize(698, 719))
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font-family: Noto Sans SC;\n"
                                 "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(41, 0, 68, 255), stop:0.427447 rgba(20, 30, 66, 235), stop:1 rgba(77, 39, 82, 255));\n"
                                 "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(31, 0, 51, 255), stop:0.427447 rgba(15, 23, 50, 235), stop:1 rgba(54, 27, 57, 255));\n"
                                 "")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(-10, 0, 710, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(19)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setStyleSheet("\n"
                                "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(31, 0, 51, 255), stop:0.427447 rgba(15, 23, 50, 235), stop:1 rgba(54, 27, 57, 255));")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(65)
        self.shadow.setColor(Qt.black)
        self.shadow.setOffset(9, 9)
        self.line.setGraphicsEffect(self.shadow)

        self.btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.btn_frame.setGeometry(QtCore.QRect(190, 10, 481, 61))
        self.btn_frame.setStyleSheet("background-color: transparent;")
        self.btn_frame.setObjectName("btn_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.settings = QtWidgets.QPushButton(self.btn_frame)
        self.settings.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.settings.setFont(font)
        self.settings.setStyleSheet("QPushButton{\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "     background-color:rgba(255,255,255,30);\n"
                                    "     border: 1px solid rgba(255,255,255,40);\n"
                                    "     border-radius:7px;\n"
                                    "width: 230;\n"
                                    "height: 50;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgba(255,255,255,50);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background-color:rgba(255,255,255,70);\n"
                                    "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon)
        self.settings.setIconSize(QtCore.QSize(40, 40))
        self.settings.setObjectName("settings")
        self.horizontalLayout_2.addWidget(self.settings)

        self.command = QtWidgets.QPushButton(self.btn_frame)
        self.command.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.command.setFont(font)
        self.command.setStyleSheet("QPushButton{\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "     background-color:rgba(255,255,255,30);\n"
                                   "     border: 1px solid rgba(255,255,255,40);\n"
                                   "     border-radius:7px;\n"
                                   "width: 230;\n"
                                   "height: 50;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgba(255,255,255,50);\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "background-color:rgba(255,255,255,70);\n"
                                   "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/services_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.command.setIcon(icon1)
        self.command.setIconSize(QtCore.QSize(40, 40))
        self.command.setObjectName("command")
        self.horizontalLayout_2.addWidget(self.command)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(50, 0, 81, 81))
        self.label.setStyleSheet("\n"
                                 "background: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icon/Yandex_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(50, 550, 182, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #00bf08;\n"
                                   "\n"
                                   "background: transparent;")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 552, 154, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ff8130;\n"
                                   "background: transparent;")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 550, 144, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #1b78a6;\n"
                                   "background: transparent;")
        self.label_4.setObjectName("label_4")

        self.microphone = QtWidgets.QLabel(self.centralwidget)
        self.microphone.setGeometry(QtCore.QRect(50, 590, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.microphone.setFont(font)
        self.microphone.setAutoFillBackground(False)
        self.microphone.setStyleSheet("background: transparent;\n"
                                      "color: #7f8b95;")
        devices = sd.query_devices()
        self.dev = {}
        # получение устройств ввода
        for i, device in enumerate(devices):
            if i > 0 and i < 6:
                self.dev.update({device['name']: device['index']})

        # получение используемого устройства ввода
        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k

        self.conn = sqlite3.connect("resources/data_base")
        self.cursor = self.conn.cursor()
        self.microphone.setText(
            get_key(self.dev, int(self.cursor.execute("SELECT name_device FROM device").fetchall()[0][0]) + 1))
        self.microphone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.microphone.setWordWrap(True)
        self.microphone.setObjectName("microphone")

        self.gpt = QtWidgets.QLabel(self.centralwidget)
        self.gpt.setGeometry(QtCore.QRect(280, 590, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.gpt.setFont(font)
        self.gpt.setAutoFillBackground(False)
        self.gpt.setStyleSheet("background: transparent;\n"
                               "color: #7f8b95;")
        self.status_gpt = "Ок"
        openai.api_key = self.cursor.execute("SELECT openai_token FROM api").fetchall()[0][0]
        model_engine = "text-davinci-003"
        prompt = "Hello world"
        try:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                temperature=0.5,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
        except:
            self.status_gpt = "Ошибка API ключа"
        self.gpt.setText(self.status_gpt)
        self.gpt.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.gpt.setWordWrap(True)
        self.gpt.setObjectName("gpt")

        self.resources = QtWidgets.QLabel(self.centralwidget)
        self.resources.setGeometry(QtCore.QRect(500, 590, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.resources.setFont(font)
        self.resources.setAutoFillBackground(False)
        self.resources.setStyleSheet("background: transparent;\n"
                                     "color: #7f8b95;")

        # Замер нагрузки
        def get_memory_usage():
            process = psutil.Process()
            memory_info = process.memory_info()
            memory_usage = memory_info.rss / (1024 ** 2)  # в мегабайтах
            return f"{round(memory_usage, 2)} Мб"

        self.stop_thread = False

        def worker():
            while True:
                if self.stop_thread:
                    break
                self.resources.setText(get_memory_usage())
                time.sleep(2)

        self.thread = threading.Thread(target=worker)
        self.thread.start()
        self.resources.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.resources.setWordWrap(True)
        self.resources.setObjectName("resources")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 100, 411, 411))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "     border-radius:205px;\n"
                                   "\n"
                                   "background: transparent;\n"
                                   "}")
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName("label_5")
        self.movie = QMovie("resources/res/core_1.gif")
        self.movie.setScaledSize(self.size())
        self.label_5.setMovie(self.movie)
        self.movie.start()
        self.shadow1 = QGraphicsDropShadowEffect()
        self.shadow1.setBlurRadius(65)
        self.shadow1.setColor(Qt.black)
        self.shadow1.setOffset(9, 9)
        self.label_5.setGraphicsEffect(self.shadow1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def thread_stop(self):
        self.stop_thread = True
        self.thread.join()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis 0.2"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.command.setText(_translate("MainWindow", "Команды"))
        self.label_2.setText(_translate("MainWindow", "Микрофон"))
        self.label_3.setText(_translate("MainWindow", "Chat GPT"))
        self.label_4.setText(_translate("MainWindow", "Ресурсы"))


class GUI_Settings(object):
    def setupUi(self, MainWindow, ):
        self.conn = sqlite3.connect("resources/data_base")
        self.cursor = self.conn.cursor()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(698, 719)
        MainWindow.setMinimumSize(QtCore.QSize(698, 719))
        MainWindow.setMaximumSize(QtCore.QSize(698, 719))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font-family: Noto Sans SC;\n"
                                 "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 0, 25, 255), stop:0.427447 rgba(7, 11, 25, 235), stop:1 rgba(27, 13, 28, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(-10, 0, 701, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(19)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color:  rgba(0, 0, 0, 255);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.btn_frame.setGeometry(QtCore.QRect(110, 10, 481, 61))
        self.btn_frame.setStyleSheet("background-color: transparent;")
        self.btn_frame.setObjectName("btn_frame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.bt = QtWidgets.QPushButton(self.btn_frame)
        self.bt.setEnabled(False)
        self.bt.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.bt.setFont(font)
        self.bt.setStyleSheet("QPushButton{\n"
                              "    color: rgb(255, 255, 255);\n"
                              "     background-color:rgba(255,255,255,30);\n"
                              "     border: 1px solid rgba(255,255,255,40);\n"
                              "     border-radius:7px;\n"
                              "width: 230;\n"
                              "height: 50;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "background-color:rgba(255,255,255,30);\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "background-color:rgba(255,255,255,70);\n"
                              "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt.setIcon(icon)
        self.bt.setIconSize(QtCore.QSize(40, 40))
        self.bt.setObjectName("bt")
        self.horizontalLayout_2.addWidget(self.bt)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(60, 120, 591, 141))
        self.line_2.setStyleSheet("\n"
                                  " background-color:rgb(37, 38, 43);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 170, 51, 41))
        self.label.setStyleSheet("background: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icon/trademark.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent;\n"
                                   "    color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 160, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: transparent;\n"
                                   "    color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 350, 600, 5))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("\n"
                                  " background-color:rgb(55, 58, 64);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.devices = QtWidgets.QPushButton(self.centralwidget)
        self.devices.setGeometry(QtCore.QRect(50, 290, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.devices.setFont(font)
        self.devices.setStyleSheet("background: transparent;\n"
                                   "color: rgb(116, 184, 22);")
        self.devices.setIcon(icon)
        self.devices.setIconSize(QtCore.QSize(40, 40))
        self.devices.setObjectName("devices")

        self.chat_gpt = QtWidgets.QPushButton(self.centralwidget)
        self.chat_gpt.setGeometry(QtCore.QRect(260, 290, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.chat_gpt.setFont(font)
        self.chat_gpt.setStyleSheet("background: transparent;\n"
                                    "color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/Icon/imgonline_com_ua_Replace_color_ym7njDDBaUH_PhotoRoom_PhotoRoom_negate.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chat_gpt.setIcon(icon1)
        self.chat_gpt.setIconSize(QtCore.QSize(40, 40))
        self.chat_gpt.setObjectName("chat_gpt")

        self.picovoice = QtWidgets.QPushButton(self.centralwidget)
        self.picovoice.setGeometry(QtCore.QRect(460, 290, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.picovoice.setFont(font)
        self.picovoice.setStyleSheet("background: transparent;\n"
                                     "color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icon/services_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.picovoice.setIcon(icon2)
        self.picovoice.setIconSize(QtCore.QSize(40, 40))
        self.picovoice.setObjectName("picovoice")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 380, 400, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent;\n"
                                   "color: rgb(138, 200, 50);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 400, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent;\n"
                                   "color: rgb(144, 146, 150);")
        self.label_5.setObjectName("label_5")

        self.microphones = QtWidgets.QComboBox(self.centralwidget)
        self.microphones.setGeometry(QtCore.QRect(50, 450, 601, 51))
        self.microphones.setStyleSheet("    color: rgb(255, 255, 255);\n"
                                       " background-color:rgb(37, 38, 43);\n"
                                       "     border-radius:7px;")
        self.microphones.setObjectName("microphones")
        devices = sd.query_devices()
        self.dev = {}
        # Получение списка микрофонов
        for i, device in enumerate(devices):
            if i > 0 and i < 6:
                self.dev.update({device['name']: device['index']})
                self.microphones.addItem(device['name'])

        self.microphones.setCurrentIndex(int(self.cursor.execute("SELECT name_device FROM device").fetchall()[0][0]))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 400, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setEnabled(True)
        self.save_btn.setGeometry(QtCore.QRect(80, 530, 561, 50))
        self.save_btn.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton{\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "     background-color:rgb(116, 184, 22);\n"
                                    "     border-radius:10px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgba(116, 184, 22,195);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background-color:rgba(116, 184, 22,100);\n"
                                    "}")
        self.save_btn.setIconSize(QtCore.QSize(40, 40))
        self.save_btn.setObjectName("save_btn")

        self.settings_3 = QtWidgets.QPushButton(self.centralwidget)
        self.settings_3.setEnabled(True)
        self.settings_3.setGeometry(QtCore.QRect(80, 600, 561, 50))
        self.settings_3.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.settings_3.setFont(font)
        self.settings_3.setStyleSheet("QPushButton{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "     background-color:rgb(73, 80, 87);\n"
                                      "     border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgba(73, 80, 87,195);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color:rgba(73, 80, 87,100);\n"
                                      "}")
        self.settings_3.setIconSize(QtCore.QSize(40, 40))
        self.settings_3.setObjectName("settings_3")

        self.Picovoice_API_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Picovoice_API_input.setGeometry(QtCore.QRect(50, 460, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        self.Picovoice_API_input.setFont(font)
        self.Picovoice_API_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Picovoice_API_input.setStyleSheet("    color: rgb(138, 200, 50);\n"
                                               "     background-color:rgb(44, 46, 51);\n"
                                               "     border-radius:9px;")
        self.Picovoice_API_input.setFrame(True)
        self.Picovoice_API_input.setCursorPosition(51)
        self.Picovoice_API_input.setAlignment(QtCore.Qt.AlignCenter)
        self.Picovoice_API_input.setObjectName("lineEdit")
        self.Picovoice_API_input.setText(self.cursor.execute("SELECT picovoice_token FROM api").fetchall()[0][0])
        self.Picovoice_API_input.hide()

        self.GPT_API_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GPT_API_input.setGeometry(QtCore.QRect(50, 460, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        self.GPT_API_input.setFont(font)
        self.GPT_API_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.GPT_API_input.setStyleSheet("    color: rgb(138, 200, 50);\n"
                                         "     background-color:rgb(44, 46, 51);\n"
                                         "     border-radius:9px;")
        self.GPT_API_input.setFrame(True)
        self.GPT_API_input.setCursorPosition(56)
        self.GPT_API_input.setAlignment(QtCore.Qt.AlignCenter)
        self.GPT_API_input.setObjectName("lineEdit")
        self.GPT_API_input.setText(self.cursor.execute("SELECT openai_token FROM api").fetchall()[0][0])
        self.GPT_API_input.hide()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt.setText(_translate("MainWindow", "Настройки"))
        self.label_2.setText(_translate("MainWindow", "БЕТА версия!"))
        self.label_3.setText(_translate("MainWindow", "Часть функций может работать некорректно.\n"
                                                      "Не сообщайте о найденных багах НИКОМУ"))
        self.devices.setText(_translate("MainWindow", "Устройства"))
        self.chat_gpt.setText(_translate("MainWindow", "Chat GPT"))
        self.picovoice.setText(_translate("MainWindow", "Picovoice"))
        self.label_4.setText(_translate("MainWindow", "Выберите микрофон"))
        self.label_5.setText(_translate("MainWindow", "Его будет слушать ассистент."))
        self.label_6.setText(_translate("MainWindow", "....................................................."))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))
        self.settings_3.setText(_translate("MainWindow", "Назад"))

    def GUI_Setting_GPT(self):
        self.microphones.hide()
        self.Picovoice_API_input.hide()
        self.GPT_API_input.show()
        self.devices.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.picovoice.setStyleSheet("background: transparent;\n"
                                     "color: rgb(255, 255, 255);")
        self.chat_gpt.setStyleSheet("background: transparent;\n"
                                    "color: rgb(116, 184, 22);")
        self.label_4.setText("Введите API токен для Chat GPT")
        self.label_5.setText("Без него некоторые функции не будут работать")
        self.label_6.setText("..................................................................................")

    def GUI_Setting_Picovoice(self):
        self.microphones.hide()
        self.GPT_API_input.hide()
        self.Picovoice_API_input.show()
        self.devices.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.picovoice.setStyleSheet("background: transparent;\n"
                                     "color: rgb(116, 184, 22);")
        self.chat_gpt.setStyleSheet("background: transparent;\n"
                                    "color: rgb(255, 255, 255);")
        self.label_4.setText("Введите API токен для Picovoice")
        self.label_5.setText("Без него распознавание голоса работать")
        self.label_6.setText("..................................................................................")

    def GUI_Setting_Devices(self, name):
        self.microphones.show()
        self.GPT_API_input.hide()
        self.Picovoice_API_input.hide()
        self.devices.setStyleSheet("background: transparent;\n"
                                   "color: rgb(116, 184, 22);")
        self.picovoice.setStyleSheet("background: transparent;\n"
                                     "color: rgb(255, 255, 255);")
        self.chat_gpt.setStyleSheet("background: transparent;\n"
                                    "color: rgb(255, 255, 255);")
        self.label_4.setText("Выберите микрофон")
        self.label_5.setText("Его будет слушать ассистент.")
        self.label_6.setText(".....................................................")
        self.microphones.setCurrentIndex(name)

    def save_setting(self):
        self.index = self.microphones.currentIndex()
        self.cursor.execute(f"UPDATE device SET name_device = '{self.index}'")
        self.cursor.execute(f"UPDATE api SET openai_token = '{self.GPT_API_input.text()}'")
        self.cursor.execute(f"UPDATE api SET picovoice_token = '{self.Picovoice_API_input.text()}'")
        self.conn.commit()
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Сохранение")
        self.msg.setText("Для сохранения изменений необходим перезапуск приложения")
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.exec_()


class GUI_comand(object):
    def setupUi(self, MainWindow):
        self.conn = sqlite3.connect("resources/data_base")
        self.cursor = self.conn.cursor()
        self.com = self.cursor.execute("SELECT * FROM command").fetchall()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(698, 719)
        MainWindow.setMinimumSize(QtCore.QSize(698, 719))
        MainWindow.setMaximumSize(QtCore.QSize(698, 719))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font-family: Noto Sans SC;\n"
                                 "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 0, 25, 255), stop:0.427447 rgba(7, 11, 25, 235), stop:1 rgba(27, 13, 28, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(-10, 0, 701, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(19)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color:  rgba(0, 0, 0, 255);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.btn_frame.setGeometry(QtCore.QRect(110, 10, 481, 61))
        self.btn_frame.setStyleSheet("background-color: transparent;")
        self.btn_frame.setObjectName("btn_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt = QtWidgets.QPushButton(self.btn_frame)
        self.bt.setEnabled(False)
        self.bt.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.bt.setFont(font)
        self.bt.setStyleSheet("QPushButton{\n"
                              "    color: rgb(255, 255, 255);\n"
                              "     background-color:rgba(255,255,255,30);\n"
                              "     border: 1px solid rgba(255,255,255,40);\n"
                              "     border-radius:7px;\n"
                              "width: 230;\n"
                              "height: 50;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "background-color:rgba(255,255,255,30);\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "background-color:rgba(255,255,255,70);\n"
                              "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt.setIcon(icon)
        self.bt.setIconSize(QtCore.QSize(40, 40))
        self.bt.setObjectName("bt")
        self.horizontalLayout_2.addWidget(self.bt)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setEnabled(True)
        self.save_btn.setGeometry(QtCore.QRect(70, 560, 561, 50))
        self.save_btn.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton{\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "     background-color:rgb(116, 184, 22);\n"
                                    "     border-radius:10px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgba(116, 184, 22,195);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background-color:rgba(116, 184, 22,100);\n"
                                    "}")
        self.save_btn.setIconSize(QtCore.QSize(40, 40))
        self.save_btn.setObjectName("save_btn")
        self.settings_3 = QtWidgets.QPushButton(self.centralwidget)
        self.settings_3.setEnabled(True)
        self.settings_3.setGeometry(QtCore.QRect(70, 630, 561, 50))
        self.settings_3.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.settings_3.setFont(font)
        self.settings_3.setStyleSheet("QPushButton{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "     background-color:rgb(73, 80, 87);\n"
                                      "     border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgba(73, 80, 87,195);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color:rgba(73, 80, 87,100);\n"
                                      "}")
        self.settings_3.setIconSize(QtCore.QSize(40, 40))
        self.settings_3.setObjectName("settings_3")
        self.save_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn_2.setEnabled(True)
        self.save_btn_2.setGeometry(QtCore.QRect(70, 490, 561, 50))
        self.save_btn_2.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn_2.setFont(font)
        self.save_btn_2.setStyleSheet("QPushButton{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "     background-color:rgb(116, 184, 22);\n"
                                      "     border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgba(116, 184, 22,195);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color:rgba(116, 184, 22,100);\n"
                                      "}")
        self.save_btn_2.setIconSize(QtCore.QSize(40, 40))
        self.save_btn_2.setObjectName("save_btn_2")
        self.Comand = QtWidgets.QComboBox(self.centralwidget)
        self.Comand.setGeometry(QtCore.QRect(50, 100, 601, 51))
        self.Comand.setStyleSheet("    color: rgb(204, 204, 204);\n"
                                  " background-color:rgb(37, 38, 43);\n"
                                  "     border-radius:7px;")
        self.Comand.setObjectName("Comand")
        for i in range(len(self.com)):
            self.Comand.addItem(self.com[i][1])
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(30, 200, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.name.setStyleSheet("    color: rgb(138, 200, 50);\n"
                                "     background-color:rgb(44, 46, 51);\n"
                                "     border-radius:9px;")
        self.name.setText("")
        self.name.setFrame(True)
        self.name.setCursorPosition(0)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent;\n"
                                   "color: rgb(138, 200, 50);")
        self.label_4.setObjectName("label_4")
        self.comands = QtWidgets.QLineEdit(self.centralwidget)
        self.comands.setGeometry(QtCore.QRect(30, 300, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        self.comands.setFont(font)
        self.comands.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.comands.setStyleSheet("    color: rgb(138, 200, 50);\n"
                                   "     background-color:rgb(44, 46, 51);\n"
                                   "     border-radius:9px;")
        self.comands.setText("")
        self.comands.setFrame(True)
        self.comands.setCursorPosition(0)
        self.comands.setAlignment(QtCore.Qt.AlignCenter)
        self.comands.setObjectName("comands")
        self.action = QtWidgets.QLineEdit(self.centralwidget)
        self.action.setGeometry(QtCore.QRect(30, 400, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(11)
        self.action.setFont(font)
        self.action.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.action.setStyleSheet("    color: rgb(138, 200, 50);\n"
                                  "     background-color:rgb(44, 46, 51);\n"
                                  "     border-radius:9px;")
        self.action.setText("")
        self.action.setFrame(True)
        self.action.setCursorPosition(0)
        self.action.setAlignment(QtCore.Qt.AlignCenter)
        self.action.setObjectName("action")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 280, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent;\n"
                                   "color: rgb(138, 200, 50);")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 360, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background: transparent;\n"
                                   "color: rgb(138, 200, 50);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 380, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.name.setText(self.Comand.currentText())
        self.comands.setText(self.cursor.execute("SELECT commands FROM command WHERE name=?", (self.Comand.currentText(),)).fetchall()[0][0])
        self.action.setText(self.cursor.execute("SELECT action FROM command WHERE name=?", (self.Comand.currentText(),)).fetchall()[0][0])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt.setText(_translate("MainWindow", "Команды"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))
        self.settings_3.setText(_translate("MainWindow", "Назад"))
        self.save_btn_2.setText(_translate("MainWindow", "Создать"))
        self.label_6.setText(_translate("MainWindow", "........................."))
        self.label_4.setText(_translate("MainWindow", "Название"))
        self.label_7.setText(_translate("MainWindow", ".............................................................."))
        self.label_5.setText(_translate("MainWindow", "Команды через запятую"))
        self.label_8.setText(_translate("MainWindow", "Действие"))
        self.label_9.setText(_translate("MainWindow", "........................"))

    def change_val(self, text):
        self.name.setText(text)
        self.comands.setText(self.cursor.execute("SELECT commands FROM command WHERE name=?", (text,)).fetchall()[0][0])
        self.action.setText(self.cursor.execute("SELECT action FROM command WHERE name=?", (text,)).fetchall()[0][0])

    def add_command(self):
        self.Comand.addItem("Название")
        self.name.setText("Название")
        self.comands.setText("Команды")
        self.action.setText("Действие")

    def save_command(self):
        # Check if the command exists
        existing_command = self.cursor.execute("SELECT commands FROM command WHERE name=?",
                                               (self.name.text(),)).fetchall()
        try:
            if not existing_command:
                # Insert new command
                self.cursor.execute('''
                    INSERT INTO command (name, commands, action) VALUES (?, ?, ?)
                ''', (self.name.text(), self.comands.text(), self.action.text()))
            else:
                # Update existing command
                self.cursor.execute('''
                    UPDATE command SET commands=?, action=? WHERE name=?
                ''', (self.comands.text(), self.action.text(), self.name.text()))

            # Save changes
            self.conn.commit()
        except Exception as e:
            pass