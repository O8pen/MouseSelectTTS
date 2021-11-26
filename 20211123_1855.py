from clipboard import copy, paste
import clipboard
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from time import sleep
from pyautogui import hotkey
from pynput.keyboard import Listener, Key
from pynput import keyboard
from pynput import mouse

trashcan_position_x = 1500
trashcan_position_y = 1000

input_text_manually_position_x = 1650
input_text_manually_position_y = 750

playbutton_position_x = 1670
playbutton_position_y = 1000

def click(x,y):
    SetCursorPos((x,y))
    mouse_event(MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    mouse_event(MOUSEEVENTF_LEFTUP,0,0)

#Select text
#press mouse button

#ctrl+c
#remove new line characters and tabs and intent in the begining of the lines
#trashcan
#input text manually
#ctrl+v
#Play button

text = ""

# The key combination to check
# COMBINATION = {keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('x')}
# COMBINATION = {keyboard.Key.alt_l, keyboard.Key.down}
# COMBINATION = {keyboard.Key.ctrl_l, keyboard.KeyCode.from_char('\x03')}
COMBINATION = {keyboard.Key.alt_l}
# COMBINATION = {keyboard.Key.alt_l, keyboard.Key.ctrl_l}

# The currently active modifiers
current = set()

arr_test = ["\r","\n","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

pressed_x = 0
pressed_y = 0

def on_click(x, y, button, pressed):
    global pressed_x
    global pressed_y
    
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    
    if pressed == True:
        print("Pressedddd" + str(x) + " / " + str(y))
        pressed_x = x
        pressed_y = y
    else:
        if ((((pressed_x - x)**2) + ((pressed_y - y)**2) )**0.5) > 20.0:
            print("calisiyor")
            # myroutine()
        print("Releaseddd" + str(x) + " / " + str(y))
        
    
def myroutine():
    print('Text copied')
            
    hotkey('ctrl', 'c')
    sleep(0.1)
    text =clipboard.paste()
    print(text)
    
    # for x in range(len(text)):
    #     print(repr(text[x]))
    
    deleted_something = True
    while(deleted_something):
        deleted_something = False
        for x in range(len(text)):
            if deleted_something == False and ((text[x] == "\r" and text[x+1] not in arr_test) or (text[x] == "\n" and text[x+1] not in arr_test)):
                deleted_something = True
                text = text[:x+1] + text[(x+2):]
                
    text = text.replace('\n', ' ').replace('\r', '')
    
    # newline_added = True
    # while(newline_added):
    #     newline_added = False
    #     for x in range(len(text)):
    #         if newline_added == False and text[x] == ".":
    #             newline_added = True
    #             text = text[:x] + '\n' + text[x:]
    
    # for x in range(len(text)):
    #     print(repr(text[x]))
                
    print(text)
    
    clipboard.copy(text) 
    
    click(trashcan_position_x,trashcan_position_y)
    
    sleep(0.1)
    
    click(input_text_manually_position_x,input_text_manually_position_y)
    
    sleep(0.1)
    
    hotkey('ctrl', 'v')
    
    sleep(0.1)
    
    click(playbutton_position_x,playbutton_position_y)
    
    sleep(0.1)
    
    # SetCursorPos((1650,200))

# def on_press(key):
#     print(key)
#     if key in COMBINATION:
#         current.add(key)
#         if all(k in current for k in COMBINATION):
#             print("dddd")
#             # myroutine()
            
            
# def on_release(key):
#     try:
#         current.remove(key)
#     except KeyError:
#         pass

# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
    
#     with Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()
    
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    
# with mouse.Listener(on_click=on_click) as listener:
#     with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()