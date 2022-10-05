import codecs
import sys
import time
from pathlib import Path
import colorama
import keyboard
from Tools.i18n.makelocalealias import pprint
from art import text2art
import yaml
import pyautogui as pag
pag.FAILSAFE = True
colorama.init()

# Клавиша для активации
hotkey = "9"
# Клавиша для открытия чата
open_hotkey = "shift+t"
# Включить кнопку открытия чата
enable_open_chat_hotkey = True
# Клавиша для отправки сообщения
send_msg_hotkey = "enter"
# Интервал между символами
character_interval = 0
# Интервал между сообщениями
interval = 0.15

close_hotkey = "H+J"


can_run = True




def initConfig():
    global hotkey, open_hotkey, enable_open_chat_hotkey, send_msg_hotkey, character_interval, interval, close_hotkey
    if Path("config.yml").is_file():
        with codecs.open('config.yml', encoding="UTF-8") as f:
            loadedConfig = yaml.safe_load(f)
            hotkey = loadedConfig['hotkey']
            open_hotkey = loadedConfig['open_hotkey']
            enable_open_chat_hotkey = loadedConfig['enable_open_chat_hotkey']
            send_msg_hotkey = loadedConfig['send_msg_hotkey']
            character_interval = loadedConfig['character_interval']
            interval = loadedConfig['interval']
            close_hotkey = loadedConfig['close_hotkey']

            print(
                f"Клавиша активации: {hotkey}\n"
                f"Клавиша открытия чата (если включено): {open_hotkey}\n"
                f"Включить ли клавишу для открытия чата в играх?: " + ("Нет", "Да")[enable_open_chat_hotkey] + "\n"
                f"Интервал между символами: {character_interval}\n"
                f"Интервал между сообшениями (рекомендуем оставить 0.2, меньше Дота не тянет): {interval}\n"
                f"Клавиша деактивации: {close_hotkey}\n"
            )

def main():
    print(text2art("1000-7      SCRIPT", "standart"))

    print(
        "Привет, твои текущие настройки программы: \n")
    initConfig()

    keyboard.add_hotkey(hotkey, lambda: print_1000_7())
    """
    Создать горячую клавишу для включения/выключения цикла либо invert_run(), а также чтоб другие клавиши игнорировались
    """
    keyboard.add_hotkey(close_hotkey, lambda: invert_run(), suppress=True) #, suppress=True

    keyboard.wait()

def invert_run():
    global can_run
    can_run = not can_run
    print(can_run)

def print_1000_7():
    print("What is 1000-7?")
    if enable_open_chat_hotkey:
        keyboard.press_and_release(open_hotkey)
        keyboard.press_and_release('ctrl+a')
        keyboard.press_and_release('backspace')
        time.sleep(interval)

    keyboard.write("What is 1000-7?", character_interval)
    keyboard.press_and_release(send_msg_hotkey)

    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('F9')
    keyboard.write("What is 1000-7?", character_interval)
    keyboard.press_and_release(send_msg_hotkey)
    if enable_open_chat_hotkey:
        keyboard.press_and_release(open_hotkey)

    for i in range(5):
        if not can_run:
            return
        print(5 - i)
        if enable_open_chat_hotkey:
            keyboard.press_and_release(open_hotkey)
            keyboard.press_and_release('ctrl+a')
            keyboard.press_and_release('backspace')
            time.sleep(interval)
        keyboard.write(str(5-i), character_interval)
        keyboard.press_and_release(send_msg_hotkey)
        time.sleep(1)

    x = 1000
    while x > 0:
        if not can_run:
            return
        var = x - 7
        if enable_open_chat_hotkey:
            keyboard.press_and_release(open_hotkey)
            keyboard.press_and_release('ctrl+a')
            keyboard.press_and_release('backspace')
            time.sleep(interval)
        keyboard.write(f"{x} - 7 = {var}", character_interval)
        # print(f"{x} - 7 = {var}")
        x = var
        time.sleep(interval)
        keyboard.press_and_release(send_msg_hotkey)



if __name__ == '__main__':
    main()
    while True:
        keyboard.wait(close_hotkey)
        invert_run()



