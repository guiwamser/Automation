import webbrowser
import pyautogui as py
import time

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
py.write('''A aula de automação com Python que eu tive foi simplesmente incrível. O instrutor foi muito experiente e habilidoso em seu ofício. Ele apresentou os conceitos de forma clara e organizada, utilizando exemplos reais para tornar o aprendizado mais fácil e compreensível.

O material da aula foi muito bem preparado, com exercícios práticos que ajudaram a consolidar o conhecimento e aplicar as habilidades aprendidas em situações reais. Além disso, o instrutor se mostrou muito atencioso, respondendo a todas as dúvidas e ajudando os alunos a superar qualquer dificuldade que possam ter encontrado durante o curso.

A aula também ofereceu uma ótima visão geral das ferramentas e bibliotecas mais usadas para automação com Python. Os exemplos práticos e as tarefas do curso foram muito úteis para aprender como usar essas ferramentas e bibliotecas na prática.

No geral, a aula de automação com Python que eu fiz foi excelente. Eu definitivamente recomendaria essa aula a qualquer pessoa que esteja procurando aprender a usar o Python para automação de tarefas. Agradeço ao instrutor por ter criado uma experiência de aprendizado tão envolvente e produtiva.''', interval=0.1)

# Esse ultimo click envia a avaliaçãoutomao com Python que eu tive foi siml. O instrutor foi muito experiente e habilidoso eu of
#py.click(x=1147, y=970)