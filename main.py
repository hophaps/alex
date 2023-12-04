from vosk import Model, KaldiRecognizer
import pyaudio, json
from fuzzywuzzy import fuzz
import yaml, pyttsx3, webbrowser
from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume
)
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
import datetime, openai, sys
import config, threading
from PyQt5.QtWidgets import QApplication
from resources.Alex_GUI import Alex
import sqlite3
import os
import csv

# получение путей
with open('resources/conf.cvs', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index == 1:
            commands = row[0].split(", ")[1]
        elif index == 2:
            model = row[0].split(", ")[1]

# фразы и имена которые нужно вырезать из запроса
opts = {
    "alias": ('алекс','аликс','ал','леша','лекс',
              'ликс'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси')
}

# подключение файла с командами
VA_CMD_LIST = yaml.safe_load(
    open(commands, 'rt', encoding='utf8'),
)

# Настройки модели для распознавания речи
model = Model(model)
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, input_device_index=config.MICROPHONE_INDEX, frames_per_buffer=8000)
stream.start_stream()

# Создание объекта речи
engine = pyttsx3.init()

# Инициация ChatGPT
openai.api_key = config.OPENAI_TOKEN

# Функция записи звука
def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer["text"]

# Озвучка текста
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Обращение к ChatGPT
def gpt_answer(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=text,
            max_tokens=256,
            temperature=0.7,
            top_p=1,
            stop=None
        )
        return response.choices[0].text.strip()
    except Exception:
        return "Проблемы с вашим ключом ассистента"

# Выполнение команды
def execute_cmd(cmd):
    if cmd == "off":
        speak("Всего хорошего сэр")
        quit()
    elif cmd == "open_browser":
        speak("Конечно")
        webbrowser.open('https://www.google.ru/', new=2)
    elif cmd == "open_youtube":
        speak("Конечно")
        webbrowser.open('https://youtube.com/', new=2)
    elif cmd == 'sound_off':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None)
    elif cmd == 'sound_on':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)
    elif cmd == "thanks":
        speak("Рада служить")
    elif cmd == "time":
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif cmd == "gpt":
        return True

# Определение команды
def command(text):
    try:
        cmd = text
        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()
        conn = sqlite3.connect("resources/data_base")
        cursor = conn.cursor()
        a = cursor.execute("SELECT action, commands FROM command").fetchall()
        RC = {'cmd': '', 'percent': 0}
        for i in a:
            for x in i[1].split(", "):
                vrt = fuzz.ratio(cmd.lower().replace(" ", ""), x.lower().replace(" ", ""))
                if vrt > RC['percent']:
                    RC['cmd'] = i[0]
                    RC['percent'] = vrt
        if RC['percent'] >= 75:
            os.system(RC["cmd"])
            conn.close()
            return
        else:
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            RC = {'cmd': '', 'percent': 0}
            for c, v in VA_CMD_LIST.items():
                for x in v:
                    vrt = fuzz.ratio(cmd, x)
                    if vrt > RC['percent']:
                        RC['cmd'] = c
                        RC['percent'] = vrt
            if RC["percent"] >= 50 and RC["cmd"] != "gpt":
                execute_cmd(RC['cmd'])
                return
        if "глубокий поиск" in text or "углубленный поиск" in text:
            speak(gpt_answer(text))
        else:
            speak("Извините, я не понимаю чего вы хотите")
    except Exception:
        print("Неизвестная ошибка")

# Функция запуска интерфейса
def run_gui():
    app = QApplication(sys.argv)
    ex = Alex()
    ex.show()
    sys.exit(app.exec_())

# Запуск GUI в отдельном потоке
if __name__ == '__main__':
    gui_thread = threading.Thread(target=run_gui, daemon=True)
    gui_thread.start()

speak("Здравствуйте, сэр")

# Прослушивание команд
for text in listen():
    if text.lower().startswith(opts["alias"]):
        command(text.lower())