# Python 3.7
# pip install clipboard
# pip install pywin32
# pip install pyautogui
# pip install pynput
# Google chrome Keyboard Shortcuts for Google Translate https://chrome.google.com/webstore/detail/keyboard-shortcuts-for-go/akjhnbnjanndggbcegmdggfjjclohjpo
# alt+j listen google translate
# Google chrome Dark Reader https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh
# Microsoft edge 110% zoom
# Google chrome 110% zoom

from clipboard import copy, paste
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from time import sleep
from pyautogui import hotkey
from pynput.keyboard import Listener, Key

next_x = 612
next_y = 562

prev_x = 359
prev_y = 562

phrasereader_blank_x = 946
phrasereader_blank_y = 994

translate_text_x = 1356
translate_text_y = 352

translate_blank_x = 1392
translate_blank_y = 222

text = ""
x = []
hasbeencaptured = False
last_key = 0

was_pressed_next = False
was_pressed_prev = False
was_pressed_typing = False
was_pressed_delete = False
was_pressed_backspace = False
was_pressed_listen = False

was_pressed_one = False
was_pressed_two = False
was_pressed_three = False
was_pressed_four = False
was_pressed_five = False
was_pressed_six = False
was_pressed_seven = False
was_pressed_eight = False
was_pressed_nine = False
was_pressed_ten = False
was_pressed_allwords = False

def on_press(key):
    global was_pressed_next
    global was_pressed_prev
    global was_pressed_typing
    global was_pressed_delete
    global was_pressed_backspace
    global was_pressed_listen
    global last_key
    
    global was_pressed_one
    global was_pressed_two
    global was_pressed_three
    global was_pressed_four
    global was_pressed_five
    global was_pressed_six
    global was_pressed_seven
    global was_pressed_eight
    global was_pressed_nine
    global was_pressed_ten
    global was_pressed_allwords

    global translate_text_x
    global translate_text_y
    global translate_blank_x
    global translate_blank_y

    # hasattr(key, 'vk')
    # print("Key pressed: {0}".format(key))
    # print(key.vk)

    if hasattr(key, 'vk') and key.vk == 101: # Numpad 5 (Next Button)
        if was_pressed_next == False:
            was_pressed_next = True
            if last_key == 110 or last_key == 104 or last_key == 103: # (start writing) or (Deletes translate, start writing) or (backspace)
                hotkey('backspace')
                sleep(0.005)
            last_key = 101
            nextbutton()
    elif hasattr(key, 'vk') and key.vk == 100: # Numpad 4 (Prev button)
        if was_pressed_prev == False:
            was_pressed_prev = True
            if last_key == 110 or last_key == 104 or last_key == 103:
                hotkey('backspace')
                sleep(0.005)
            last_key = 100
            prevbutton()
    elif hasattr(key, 'vk') and key.vk == 104: # Numpad 8 (start writing)
        if was_pressed_typing == False:
            was_pressed_typing = True
            # if last_key == 102:
            #     last_key = 102
            #     click(translate_text_x,translate_text_y)
            #     hotkey('ctrl', 'a')
            #     sleep(0.1)
            #     hotkey('backspace')
            # else:
            last_key = 104
            click(translate_text_x,translate_text_y)
    elif hasattr(key, 'vk') and key.vk == 103: # Numpad 7 (Backspace)
        if was_pressed_backspace == False:
            was_pressed_backspace = True
            last_key = 103
            hotkey('backspace')
            # sleep(0.1)
            hotkey('backspace')
    elif hasattr(key, 'vk') and key.vk == 110: # Numpad . (Deletes translate, start writing)
        if was_pressed_delete == False:
            was_pressed_delete = True
            last_key = 110
            click(translate_text_x,translate_text_y)
            hotkey('ctrl', 'a')
            sleep(0.1)
            hotkey('backspace')
    elif hasattr(key, 'vk') and key.vk == 107: # Numpad + (alt + j, Translate listen)
        if was_pressed_listen == False:
            was_pressed_listen = True
            # if last_key == 98:
            #     last_key = 98
            #     click(translate_blank_x,translate_blank_y)
            #     sleep(0.05)
            #     hotkey('alt', 'j')
            # else:
            last_key = 107
            hotkey('backspace')
            sleep(0.005)
            click(translate_blank_x,translate_blank_y)
            sleep(0.25)
            hotkey('alt', 'j')
            sleep(0.005)
            click(translate_blank_x,translate_blank_y)
    elif hasattr(key, 'vk') and key.vk == 96: # Numpad 0 (all words listen)
        if was_pressed_allwords == False:
            was_pressed_allwords = True
            if last_key == 96:
                last_key = 96
                click(translate_blank_x,translate_blank_y)
                sleep(0.05)
                hotkey('alt', 'j')
            else:
                last_key = 96
                capture()
                copy(text)
                playsound()
    elif hasattr(key, 'vk') and key.vk == 97:
        if was_pressed_one == False:
            was_pressed_one = True
            if last_key == 97:
                last_key = 97
                click(translate_blank_x,translate_blank_y)
                sleep(0.05)
                hotkey('alt', 'j')
            else:
                last_key = 97
                capture()
                if(len(x) >= int(key.vk)-96):
                    copy(x[int(key.vk)-97])
                    playsound()
    elif hasattr(key, 'vk') and key.vk == 50+48:
        if was_pressed_two == False:
            was_pressed_two = True
            if last_key == 50+48:
                last_key = 50+48
                click(translate_blank_x,translate_blank_y)
                sleep(0.05)
                hotkey('alt', 'j')
            else:
                last_key = 50+48
                capture()
                if(len(x) >= int(key.vk)-48-48):
                    copy(x[int(key.vk)-49-48])
                    playsound()
    elif hasattr(key, 'vk') and key.vk == 51+48:
        if was_pressed_three == False:
            was_pressed_three = True
            if last_key == 51+48:
                last_key = 51+48
                click(translate_blank_x,translate_blank_y)
                sleep(0.05)
                hotkey('alt', 'j')
            else:
                last_key = 51+48
                capture()
                if(len(x) >= int(key.vk)-48-48):
                    copy(x[int(key.vk)-49-48])
                    playsound()
    elif hasattr(key, 'vk') and key.vk == 52+48+2:
        if was_pressed_four == False:
            was_pressed_four = True
            if last_key == 52+48+2:
                last_key = 52+48+2
                click(translate_blank_x,translate_blank_y)
                sleep(0.05)
                hotkey('alt', 'j')
            else:
                last_key = 52+48+2
                capture()
                if(len(x) >= int(key.vk)-48-48-2):
                    copy(x[int(key.vk)-49-48-2])
                    playsound()
    elif hasattr(key, 'vk') and key.vk == 53+48+4:
        if was_pressed_five == False:
            was_pressed_five = True
            if last_key == 53+48+4:
                last_key = 53+48+4
                click(translate_blank_x,translate_blank_y)
                sleep(0.05)
                hotkey('alt', 'j')
            else:
                last_key = 53+48+4
                capture()
                if(len(x) >= int(key.vk)-48-48-4):
                    copy(x[int(key.vk)-49-48-4])
                    playsound()
    # elif hasattr(key, 'vk') and key.vk == 54:
    #     if was_pressed_six == False:
    #         was_pressed_six = True
    #         if last_key == 54:
    #             last_key = 54
    #             click(translate_blank_x,translate_blank_y)
    #             sleep(0.05)
    #             hotkey('alt', 'j')
    #         else:
    #             last_key = 54
    #             capture()
    #             if(len(x) >= int(key.vk)-48):
    #                 copy(x[int(key.vk)-49])
    #                 playsound()
    # elif hasattr(key, 'vk') and key.vk == 55:
    #     if was_pressed_seven == False:
    #         was_pressed_seven = True
    #         if last_key == 55:
    #             last_key = 55
    #             click(translate_blank_x,translate_blank_y)
    #             sleep(0.05)
    #             hotkey('alt', 'j')
    #         else:
    #             last_key = 55
    #             capture()
    #             if(len(x) >= int(key.vk)-48):
    #                 copy(x[int(key.vk)-49])
    #                 playsound()
    # elif hasattr(key, 'vk') and key.vk == 56:
    #     if was_pressed_eight == False:
    #         was_pressed_eight = True
    #         if last_key == 56:
    #             last_key = 56
    #             click(translate_blank_x,translate_blank_y)
    #             sleep(0.05)
    #             hotkey('alt', 'j')
    #         else:
    #             last_key = 56
    #             capture()
    #             if(len(x) >= int(key.vk)-48):
    #                 copy(x[int(key.vk)-49])
    #                 playsound()
    # elif hasattr(key, 'vk') and key.vk == 57:
    #     if was_pressed_nine == False:
    #         was_pressed_nine = True
    #         if last_key == 57:
    #             last_key = 57
    #             click(translate_blank_x,translate_blank_y)
    #             sleep(0.05)
    #             hotkey('alt', 'j')
    #         else:
    #             last_key = 57
    #             capture()
    #             if(len(x) >= int(key.vk)-48):
    #                 copy(x[int(key.vk)-49])
    #                 playsound()
    # elif hasattr(key, 'vk') and key.vk == 58:
    #     if was_pressed_ten == False:
    #         was_pressed_ten = True
    #         if last_key == 58:
    #             last_key = 58
    #             click(translate_blank_x,translate_blank_y)
    #             sleep(0.05)
    #             hotkey('alt', 'j')
    #         else:
    #             last_key = 58
    #             capture()
    #             if(len(x) >= int(key.vk)-48):
    #                 copy(x[int(key.vk)-49])
    #                 playsound()


def on_release(key):
    global was_pressed_next
    global was_pressed_prev
    global was_pressed_typing
    global was_pressed_delete
    global was_pressed_backspace
    global was_pressed_listen

    global was_pressed_one
    global was_pressed_two
    global was_pressed_three
    global was_pressed_four
    global was_pressed_five
    global was_pressed_six
    global was_pressed_seven
    global was_pressed_eight
    global was_pressed_nine
    global was_pressed_ten
    global was_pressed_allwords

    # print("Key released: {0}".format(key))

    if hasattr(key, 'vk') and key.vk == 101: # Numpad 5
        was_pressed_next = False
    elif hasattr(key, 'vk') and key.vk == 100: # Numpad 4
        was_pressed_prev = False
    elif hasattr(key, 'vk') and key.vk == 104: # Numpad 8
        was_pressed_typing = False
    elif hasattr(key, 'vk') and key.vk == 110: # Numpad .
        was_pressed_delete = False
    elif hasattr(key, 'vk') and key.vk == 103: # Numpad 7
        was_pressed_backspace = False
    elif hasattr(key, 'vk') and key.vk == 107: # Numpad +
        was_pressed_listen = False
    elif hasattr(key, 'vk') and key.vk == 96: # Numpad 0
        was_pressed_allwords = False
    elif hasattr(key, 'vk') and key.vk == 49+48: # 1
        was_pressed_one = False
    elif hasattr(key, 'vk') and key.vk == 50+48: # 2 
        was_pressed_two = False
    elif hasattr(key, 'vk') and key.vk == 51+48: # 3 
        was_pressed_three = False
    elif hasattr(key, 'vk') and key.vk == 52+48+2: # 4 
        was_pressed_four = False
    elif hasattr(key, 'vk') and key.vk == 53+48+4: # 5 
        was_pressed_five = False
    # elif hasattr(key, 'vk') and key.vk == 54: # 6 
    #     was_pressed_six = False
    # elif hasattr(key, 'vk') and key.vk == 55: # 7 
    #     was_pressed_seven = False
    # elif hasattr(key, 'vk') and key.vk == 56: # 8 
    #     was_pressed_eight = False
    # elif hasattr(key, 'vk') and key.vk == 57: # 9 
    #     was_pressed_nine = False
    # elif hasattr(key, 'vk') and key.vk == 58: # 0 
    #     was_pressed_ten = False






def click(x,y):
    SetCursorPos((x,y))
    mouse_event(MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    mouse_event(MOUSEEVENTF_LEFTUP,0,0)

def nextbutton():
    global hasbeencaptured
    global next_x
    global next_y

    click(next_x,next_y)
    hasbeencaptured = False
    
def prevbutton():
    global hasbeencaptured
    global prev_x
    global prev_y

    click(prev_x,prev_y)
    hasbeencaptured = False

def playsound():
    global translate_text_x
    global translate_text_y
    global translate_blank_x
    global translate_blank_y

    click(translate_text_x,translate_text_y)
    hotkey('ctrl', 'a')
    sleep(0.1)
    hotkey('ctrl', 'v')
    sleep(0.05)
    hotkey('alt', 'j')
    sleep(0.55)
    click(translate_blank_x,translate_blank_y)
    
def capture():
    global text
    global x
    global hasbeencaptured
    global phrasereader_blank_x
    global phrasereader_blank_y

    if hasbeencaptured == False:
        # click(phrasereader_blank_x,phrasereader_blank_y)
        click(phrasereader_blank_x,phrasereader_blank_y)
        sleep(0.25)
        hotkey('ctrl', 'a')
        sleep(0.05)
        hotkey('ctrl', 'c')
        sleep(0.05)
        click(phrasereader_blank_x,phrasereader_blank_y)
        sleep(0.05)
        click(phrasereader_blank_x-20,phrasereader_blank_y)
        sleep(0.05)
        # click(phrasereader_blank_x-20,phrasereader_blank_y-20)
        # sleep(0.05)
        # click(phrasereader_blank_x,phrasereader_blank_y-20)
        # sleep(0.05)
        # sleep(0.25)
        text = paste()
        text = text[2:]
        endNumber = text.find('\n')-1
        text = text[0:endNumber]

        text = text.rstrip('\n')  # 1!2@3#4$5%6^7&8*9(0)=-+#way
        text = text.rstrip('@')
        text = text.rstrip('#')
        text = text.rstrip('$')
        text = text.rstrip('%')
        text = text.rstrip('^')
        text = text.rstrip('&')
        text = text.rstrip('*')
        text = text.rstrip('(')
        text = text.rstrip(')')
        # text = text.rstrip('_')
        # text = text.rstrip('-')
        text = text.rstrip('=')
        text = text.rstrip('+')
        text = text.rstrip('/')
        # text = text.rstrip('\')
        text = text.rstrip('[')
        text = text.rstrip(']')
        text = text.rstrip('{')
        text = text.rstrip('}')
        text = text.rstrip(';')
        text = text.rstrip(':')
        text = text.rstrip('>')
        text = text.rstrip('<')
        text = text.rstrip('|')
        text = text.rstrip('?')
        text = text.rstrip(',')
        text = text.rstrip('.')
        # text = text.rstrip('')
        # text = text.rstrip('')
        # text = text.rstrip('')
        # text = text.rstrip('')
        # text = text.rstrip('')
        # text = text.rstrip('')
        # text = text.rstrip('')

        x = text.split(' ')
        hasbeencaptured = True

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()