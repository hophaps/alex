import sys
import sqlite3
sys.path.insert(1, 'resources/res')
from PyQt5.QtWidgets import QMainWindow
from resources.res.GUI import Jarvis_GUI, GUI_Settings, GUI_comand


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class Jarvis(QMainWindow, Jarvis_GUI):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки основного интерфейса из класса Jarvis_GUI,
        self.setupUi(self)
        self.settings.clicked.connect(self.run_settings)
        self.command.clicked.connect(self.run_comands)

    def closeEvent(self, event):
        # Отработка закрытия интерфейса
        Jarvis_GUI.thread_stop(self)
        event.accept()

    def run_settings(self):
        # Запуск окна настроек
        self.settings_GUI = Jarvis_Settings()
        self.settings_GUI.show()

    def run_comands(self):
        # Запуск окна команд
        self.comand_GUI = alex_comand()
        self.comand_GUI.show()


class Jarvis_Settings(QMainWindow, GUI_Settings):
    # Экран настроек
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chat_gpt.clicked.connect(self.Settings_GPT)
        self.picovoice.clicked.connect(self.Settings_picovoice)
        self.devices.clicked.connect(self.Settings_devices)
        self.settings_3.clicked.connect(self.Settings_exit)
        self.save_btn.clicked.connect(self.Settings_save)
        self.conn = sqlite3.connect("resources/data_base")
        self.cursor = self.conn.cursor()


    def Settings_GPT(self):
        GUI_Settings.GUI_Setting_GPT(self)


    def Settings_picovoice(self):
        GUI_Settings.GUI_Setting_Picovoice(self)


    def Settings_devices(self):
        GUI_Settings.GUI_Setting_Devices(self, int(self.cursor.execute("SELECT name_device FROM device").fetchall()[0][0]))


    def Settings_exit(self):
        self.close()


    def Settings_save(self):
        GUI_Settings.save_setting(self)


class alex_comand(QMainWindow, GUI_comand):
    def __init__(self):
        # Окно команд
        super().__init__()
        self.setupUi(self)
        self.save_btn_2.clicked.connect(self.Comands_add)
        self.settings_3.clicked.connect(self.Comands_exit)
        self.save_btn.clicked.connect(self.Comands_save)
        self.Comand.currentTextChanged.connect(self.Change_value)
        self.conn = sqlite3.connect("resources/data_base")
        self.cursor = self.conn.cursor()

    def Change_value(self, text):
        GUI_comand.change_val(self, text)

    def Comands_add(self):
        GUI_comand.add_command(self)

    def Comands_exit(self):
        self.close()

    def Comands_save(self):
        GUI_comand.save_command(self)