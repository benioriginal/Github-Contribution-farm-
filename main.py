import keyboard as kbd
import pydirectinput
import time
time.sleep(3)
i = 1
while i <= 10:
    pydirectinput.dragTo(x=1400, y=500, duration=0.5)
    pydirectinput.click()
    time.sleep(0.5)
    kbd.write("heheheheheheehe")
    pydirectinput.dragTo(x=1400, y=306, duration=0.5)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.dragTo(x=900, y=650, duration=0.5)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.dragTo(x=1450, y=440, duration=0.5)
    pydirectinput.click()
    time.sleep(0.5)
    i+=1

