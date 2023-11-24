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
from resources.Jarvis_GUI import Jarvis

opts = {
    "alias": ('кеша','кеш','инокентий','иннокентий','кишун','киш',
              'кишаня','кяш','кяша','кэш','кэша'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси')
}

VA_CMD_LIST = yaml.safe_load(
    open('resources/commands.yaml', 'rt', encoding='utf8'),
)

model = Model("resources/vosk-model-small")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, input_device_index=config.MICROPHONE_INDEX, frames_per_buffer=8000)
stream.start_stream()

# Создание объекта речи
engine = pyttsx3.init()

# Инициация ChatGPT
openai.api_key = config.OPENAI_TOKEN

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer["text"]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def gpt_answer(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=text,
        max_tokens=256,
        temperature=0.7,
        top_p=1,
        stop=None
    )
    return response.choices[0].text.strip()

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

def command(text):
    try:
        cmd = text
        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()

        RC = {'cmd': '', 'percent': 0}
        for c, v in VA_CMD_LIST.items():

            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > RC['percent']:
                    RC['cmd'] = c
                    RC['percent'] = vrt
        if execute_cmd(RC['cmd']) != None:
            speak(gpt_answer(text))

    except Exception:
        print("Ошибка какаято")
def run_gui():
    app = QApplication(sys.argv)
    ex = Jarvis()
    ex.show()
    sys.exit(app.exec_())

# Запуск GUI в отдельном потоке
if __name__ == '__main__':
    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()

speak("Здравствуйте, сэр")

for text in listen():
    if text.lower().startswith(opts["alias"]):
        command(text.lower())