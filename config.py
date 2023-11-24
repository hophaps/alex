import sqlite3

conn = sqlite3.connect("resources/data_base")
cursor = conn.cursor()

# Получение ID микрофона
MICROPHONE_INDEX = int(cursor.execute("SELECT name_device FROM device").fetchall()[0][0])
# Путь к браузеру

# Получение API ключей
OPENAI_TOKEN = cursor.execute("SELECT openai_token FROM api").fetchall()[0][0]
PICOVOICE_TOKEN = cursor.execute("SELECT picovoice_token FROM api").fetchall()[0][0]
cursor.close()