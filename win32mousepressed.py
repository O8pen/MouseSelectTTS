import win32api
import time
import pyttsx3


# width = win32api.GetSystemMetrics(0)
# height = win32api.GetSystemMetrics(1)
# midWidth = int((width + 1) / 2)
# midHeight = int((height + 1) / 2)

engine = pyttsx3.init() 

state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
while True:
    a = win32api.GetKeyState(0x01)
    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')   
            x, y = win32api.GetCursorPos()
            print(x)
            print(y)         
        else:
            print('Left Button Released')
            engine.say("Hello World!")
            engine.runAndWait()
            # win32api.SetCursorPos((midWidth, midHeight))
    # time.sleep(0.001)