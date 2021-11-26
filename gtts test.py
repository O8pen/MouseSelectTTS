import clipboard
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from time import sleep
from pyautogui import hotkey
from pynput import mouse
## import pyttsx3
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


#Select text
#press mouse button

#ctrl+c
#remove new line characters and tabs and intent in the begining of the lines
#trashcan
#input text manually
#ctrl+v
#Play button


## engine = pyttsx3.init()


trashcan_position_x = 1500
trashcan_position_y = 1000

input_text_manually_position_x = 1650
input_text_manually_position_y = 750

playbutton_position_x = 1670
playbutton_position_y = 1000

text = ""

english_alphabet = ["\r","\n","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

pressed_x = 0
pressed_y = 0

def click(x,y):
    SetCursorPos((x,y))
    mouse_event(MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    mouse_event(MOUSEEVENTF_LEFTUP,0,0)

def on_click(x, y, button, pressed):
    global pressed_x
    global pressed_y
    
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    
    if pressed == True:
        print("Pressedddd" + str(x) + " / " + str(y))
        pressed_x = x
        pressed_y = y
    else:
        if ((((pressed_x - x)**2) + ((pressed_y - y)**2) )**0.5) > 20.0:
            print("calisiyor")
            myroutine()
        print("Releaseddd" + str(x) + " / " + str(y))
        
    
def myroutine():
    global tts
    print('Text copied')
            
    hotkey('ctrl', 'c')
    sleep(0.1)
    text =clipboard.paste()
    print(text)
    
    
    deleted_something = True
    while(deleted_something):
        deleted_something = False
        for x in range(len(text)-2):
            if deleted_something == False and ((text[x] == "\r" and text[x+1] not in english_alphabet) or (text[x] == "\n" and text[x+1] not in english_alphabet)):
                deleted_something = True
                text = text[:x+1] + text[(x+2):]
                
    text = text.replace('\n', ' ').replace('\r', '')
    
    # print(text)
    
    text = text.replace('.', '.\n')
                       
    # print(text)
    
    # clipboard.copy(text) 
    
    
    speaker.Speak("Hello, it works!")
    ## engine.say(text)
    ## print("dddddddddddddddddddddddddd")
    ## engine.runAndWait()
    ## print("asasasa")
    ## engine.stop()
    #3 print("asasasassssssssssssssssssssss")
    
        
    # # click(trashcan_position_x,trashcan_position_y)
    
    # # sleep(0.1)
    
    # # click(input_text_manually_position_x,input_text_manually_position_y)
    
    # # sleep(0.1)
    
    # # hotkey('ctrl', 'v')
    
    # # sleep(0.1)
    
    # # click(playbutton_position_x,playbutton_position_y)
    
    # # sleep(0.1)
    
    # # # SetCursorPos((1650,200))

    
with mouse.Listener(on_click=on_click) as listener:
    listener.join()