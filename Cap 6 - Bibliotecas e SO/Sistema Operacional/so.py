import platform
import getpass
from datetime import datetime

print("Nome máquina:................:", platform.node())
print("Arquitetura:.................:", platform.architecture())
print("Sistema Operacional..........:", platform.system())
print("Versão do SO.................:", platform.release())
print("Processador..................:", platform.processor())
print("Versão do Python.............:", platform.python_version())

print(' ')
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == 'migue' and senha == 'Hello':
    print('Bem vindo, Migue KKKKK')

else:
    print('You are not Migue')