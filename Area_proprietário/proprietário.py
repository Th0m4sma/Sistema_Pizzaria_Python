from pizzas import *

def proprientario_p():
    sair = False

    if entrando():
        while not sair:
            os.system('cls')
            menuPrincipal_proprietario()
            op = int(input("Digite a opção desejada: "))

            if op == 1:
                registrar_pizza()
            elif op == 2:
                removendo_pizza()
            elif op == 3:
                os.system('cls')
                imprimindo_pedidos()
                sleep(4)
            elif op == 4:
                os.system('cls')
                cardapio()
            elif op == 5:
                os.system('cls')
                sair_menu_proprietario()
                sleep(2)
                sair = True


if __name__ == '__main__':
    proprientario_p()



