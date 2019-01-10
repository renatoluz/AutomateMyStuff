# ~ import subprocess
# ~ import os

# ~ os.startfile("outlook")

# ~ subprocess.call(['C:/Users/rmour/AppData/Local/WhatsApp/WhatsApp.exe'])


# ~ from pywinauto.application import Application
# ~ app = Application().start("C:\Users\rmour\AppData\Local\WhatsApp\WhatsApp.exe")
# ~ WhatsApp.exe
# ~ C:\Users\rmour\AppData\Local\WhatsApp\WhatsApp.exe

 # ~ ~ conda activate py2
# ~ import pywinauto
# ~ pwa_app = pywinauto.application.Application() 
# ~ pwa_app.start_(r'C:\Users\rmour\AppData\Local\WhatsApp\WhatsApp.exe') 


# ~ import sys


from pywinauto import application
app=application.Application()
app.start(r"C:\Users\rmour\AppData\Local\WhatsApp\WhatsApp.exe")


# ~ sys.exit()

# ~ ESPERAR

# ~ ENCONTRAR POSIÇÃO AONDE SE DIGITA O CONTATO
# ~ DIGITAR O CONTATO  - agua + ENTER
# ~ ENCONTRAR POSIÇÃO AONDE SE DIGITA A MENSAGEM
# ~ DIGITAR A MENSAGEM: olá bom dia. gostaria de solicitar duas águas aqui para a rua síria, 204. ap.31 2 de 20L agua boa por favor. no cartao de débito

