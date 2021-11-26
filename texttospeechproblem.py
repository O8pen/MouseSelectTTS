import pyttsx3
from pynput import mouse

engine = pyttsx3.init() 

def on_click(x, y, button, pressed):
    if pressed == True:
        print("Mouse Clicked at Position :" + str(x) + " / " + str(y))
        
        engine.say("Hello World!")
        engine.runAndWait()
        engine.startLoop(False)

        engine.iterate()
        engine.runAndWait()
        engine.endLoop()



with mouse.Listener(on_click=on_click) as listener:
    listener.join()