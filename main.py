import sys
import os
import time

sys.path.append('Area_cliente')
sys.path.append('Area_proprietário')

from cliente import *
from proprietário import *

def Imprime_menu():
    print("]|[=============================================]|[")
    print("]|[==-----------[-MENU-PRINCIPAL-]------------==]|[")
    print("]|[=============================================]|[")
    print("]|[==----------[-(1)-MENU-CLIENTE-]-----------==]|[")
    print("]|[==--------[-(2)-MENU-PROPRIETÁRIO-]--------==]|[")
    print("]|[==--------------[-(3)-SAIR-]---------------==]|[")
    print("]|[=============================================]|[")

def principal():
    sair = False

    while not sair:
        os.system("cls")
        Imprime_menu()
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            os.system("cls")
            cliente_p()
        elif opcao == 2:
            os.system("cls")
            proprientario_p()
        elif opcao == 3:
            os.system("cls")
            sair_menu_proprietario()
            sleep(2)
            sair = True
        else:
            pass
    os.system('cls')
    
if __name__ == '__main__':
    principal()