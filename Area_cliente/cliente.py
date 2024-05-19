import sys

from contas import *

sys.path.append('Area_proprietário')

from pizzas import cardapio

def cliente_p():
    sair1= False

    while not sair1:
        os.system('cls')
        menuPrincipal_cliente()
        op1 = int(input("Digite a opção desejada: "))

        if op1 == 1:
            entrou,usuario = entrarConta()
            if entrou:
                sair2 = False

                while not sair2:
                    os.system('cls')
                    menuSecundario_cliente()
                    op2 = int(input("Digite a opção desejada: "))
                    
                    if op2 == 1:
                        os.system('cls')
                        cardapio()
                        pass
                    elif op2 == 2:
                        fazer_pedido(usuario)
                    elif op2 == 3:
                        pass
                    elif op2 == 4:
                       Acessar_Perfil(usuario)
                       usuario = atualizando(usuario)
                    elif op2 == 5:
                        sair2 = True
                    else:
                        pass
        elif op1 == 2:
            inserirConta()
        elif op1 == 3:
            os.system('cls')
            sair_menu_cliente()
            sleep(2)
            sair1 = True
        else:
            os.system('cls')
            valor_inválido()
            sleep(2)

if __name__ == '__main__':
    cliente_p()