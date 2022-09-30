import time
import keyboard

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

def main():
    keyboard.add_hotkey(hotkey, lambda: print_1000_7())
    keyboard.wait()


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
    keyboard.write("What is 1000-7?")
    keyboard.press_and_release(send_msg_hotkey) 
    if enable_open_chat_hotkey:
        keyboard.press_and_release(open_hotkey)

    for i in range(5):
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
        var = x - 7
        if enable_open_chat_hotkey:
            keyboard.press_and_release(open_hotkey)
            keyboard.press_and_release('ctrl+a')
            keyboard.press_and_release('backspace')
            time.sleep(interval)
        keyboard.write(f"{x} - 7 = {var}", character_interval)
        print(f"{x} - 7 = {var}")
        x = var
        time.sleep(interval)
        keyboard.press_and_release(send_msg_hotkey)



if __name__ == '__main__':
    main()
