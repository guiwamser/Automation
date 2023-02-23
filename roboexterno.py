import webbrowser
import pyautogui as py
import time
import threading


py.alert("🤖 O CÓDIGO VAI COMEÇAR. NÃO UTILIZE NADA DO COMPUTADOR ATÉ O CÓDIGO FINALIZAR!🤖")

webbrowser.open("https://www.google.com")

time.sleep(1)

py.write('externo proway', interval=0.1)


py.hotkey('enter')

#py.moveTo(x=382, y=362)


time.sleep(1)


py.click(x=382, y=362)

time.sleep(1)

py.click(x=974, y=647)

py.click(x=974, y=647)

time.sleep(1)

py.hotkey('enter')

time.sleep(1)
py.click(x=1764, y=363)

time.sleep(1)
py.click(x=1076, y=402)
py.click(x=1085, y=600)
py.click(x=1084, y=734)
py.click(x=1079, y=870)

py.scroll(-750) 
time.sleep(1)

py.click(x=1081, y=365)
py.click(x=1083, y=510)
py.click(x=1082, y=642)

py.click(x=1019, y=807)



# Escreva o comentario sobre a aula aqui

with open("osmeiabomba.txt", "r", encoding="UTF-8") as arquivo:
    texto = arquivo.read()

    py.write(texto, interval= 0.01)

py.scroll(-750) 
time.sleep(1)
# Esse ultimo click envia a avaliação
#py.click(x=1147, y=970)

py.hotkey('windowns')
py.click(x=33, y=989)