import pyautogui as py
import time

py.click(x=640, y=1056)
time.sleep(1)
py.doubleClick(x=352, y=522)
time.sleep(1)
py.write('cd botrepository', interval=0.1)
py.hotkey('enter')
time.sleep(1)

py.write('git add .')
py.hotkey('enter')
time.sleep(2)
py.write('git commit -m ', interval=0.1)
py.write("'UP'")
time.sleep(1)
py.hotkey('enter')
time.sleep(2)
py.write('git push', interval=0.1)
time.sleep(1)
py.hotkey('enter')
