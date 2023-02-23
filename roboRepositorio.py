import webbrowser
import pyautogui as py
import time

#py.alert ("🤖 VOCÊ ESTÁ PRESTES A CRIAR UM REPOSITORIO. NÃO UTILIZE NADA DO COMPUTADOR ATÉ O CÓDIGO FINALIZAR!🤖")
webbrowser.open("https://google.com")

time.sleep(1)

py.write('github', interval=0.1)

py.hotkey('enter')

time.sleep(1)

py.click(x=466, y=360)

time.sleep(1)

py.click(x=1586, y=138)

time.sleep(3)

py.hotkey('enter')

time.sleep(2)



py.click(x=1829, y=121)
time.sleep(2)
py.click(x=1726, y=342)
time.sleep(2)
py.click(x=1655, y=294)
time.sleep(2)

#Escrever nome repositorio
py.click(x=761, y=413)
time.sleep(2)
py.write('BotRepository', interval=0.1)
py.click(x=516, y=836)
py.scroll(-750)
time.sleep(1)
py.click(x=606, y=820)

#Clonando repositorio
time.sleep(4)
py.click(x=1243, y=352)
time.sleep(3)
py.click(x=1259, y=577)
time.sleep(1)

#abrindo pastas
py.click(x=570, y=1049)
time.sleep(2)
py.doubleClick(x=1366, y=349)
time.sleep(1)
py.doubleClick(x=995, y=331)
time.sleep(1)

#criando pasta repositorio
py.click(x=1096, y=152)
time.sleep(1)
py.write('BotRepository')
py.hotkey('enter')
time.sleep(1)
py.doubleClick(x=1000, y=382)
time.sleep(2)
py.rightClick(x=1280, y=462)
time.sleep(2)
py.click(x=1345, y=781)
time.sleep(1)

#gitbash
py.write('git clone ', interval=0.1)
time.sleep(1)
py.rightClick(x=568, y=369)
time.sleep(2)
py.click(x=673, y=427)
time.sleep(2)
py.hotkey('enter')
time.sleep(8)
py.write('code .')
time.sleep(1)
py.hotkey('enter')
time.sleep(4)


#criando arquivo python
py.click(x=1513, y=81)
time.sleep(1)
py.click(x=229, y=82)
time.sleep(1)
py.write('IA.py')
py.hotkey('enter')
time.sleep(1)

#escrevendo no arquivo
py.click(x=454, y=235)
py.write('print(', interval=0.1)
py.write('"A inteligencia artificial vai acabar com todos nos")', interval=0.1)
time.sleep(2)
py.click(x=1828, y=54)
time.sleep(2)

#commitando o repositorio
py.click(x=640, y=1056)
time.sleep(1)
py.click(x=508, y=423)
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


