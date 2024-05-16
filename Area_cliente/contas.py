import os
from time import sleep

from Print_menu_cliente import *


class conta(object):
    def __init__(self,nome,telefone,email,senha,bairro = '',rua = '',num = 0,complemento = ''):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.bairro = bairro
        self.rua = rua
        self.numero = num
        self.complemento =complemento

class pedidos(object):
    def __init__(self,pizzas,valor,cliente):
        self.pizzas = list(pizzas)
        self.valor = valor
        self.cliente = cliente
        self.status = 0

def startwith(string,sub):
    if string[:len(sub)].lower()==sub:
        return True
    return False


def verificarEmail(email):
    arquivo = open('contas.txt','r')
    arquivo.readline()
    arquivo.readline()
    linhas = arquivo.readlines()

    for i in linhas:
        aux = eval(i)
        if email.upper() == aux['email'].upper():
            arquivo.close()
            return True
    arquivo.close()
    return False


def verificarTelefone(telefone):
    arquivo = open('contas.txt','r')
    arquivo.readline()
    arquivo.readline()
    linhas = arquivo.readlines()

    for i in linhas:
        aux = eval(i)
        if str(telefone) == str(aux['telefone']):
            arquivo.close()
            return True
    arquivo.close()
    return False


def verificarNome(nome):
    arquivo = open('contas.txt','r')
    arquivo.readline()
    arquivo.readline()
    linhas = arquivo.readlines()

    for i in linhas:
        aux = eval(i)
        if nome.upper() == aux['nome'].upper():
            arquivo.close()
            return True
    arquivo.close()
    return False




def validandoEmail(string):
    arroba = 0
    validado = 0
    lista = list(string)
    lista.reverse()

    if lista[0] == 'm':
        validado += 1
    if lista[1] == 'o':
        validado += 1
    if lista[2] == 'c':
        validado += 1
    if lista[3] == '.':
        validado += 1

    for i in string:
        if i == '@':
            arroba += 1

    if arroba == 1 and validado == 4 and len(lista) > 18:
        return True
    else: 
        return False
          

def inserirConta():
    valido = False
    telefone_valido = False
    email_valido = False
    nome_valido = False
    inserirEndereco = True
    inserido = 0
    op = ''

    arquivo = open('contas.txt','a')

    while not valido:
        os.system('cls')
        criandoConta()
        

        if not nome_valido:
            nome = input("Informe o seu nome: ")

            if not verificarNome(nome):
                nome_valido = True
            else:
                os.system('cls')
                nome_cadastrado()
                sleep(2)

        elif not telefone_valido:
            telefone = int(input("Digite o seu telefone: "))

            if 1<= (telefone//10**8) <= 9:
                if not verificarTelefone(telefone):
                    telefone_valido = True
                else:
                    os.system('cls')
                    Telefone_cadastrado()
                    sleep(2)
            else:
                os.system('cls')
                telefone_Inválido()
                sleep(2)

        elif not email_valido and telefone_valido:
            email = input("Informe seu email: ")

            if validandoEmail(email):
                if not verificarEmail(email):
                    senha = input("Digite uma senha: ")
                    email_valido = True
                else:
                    os.system('cls')
                    Email_cadastrado()
                    sleep(2)
            else:
                os.system('cls')
                email_inválido()
                sleep(2)


        elif inserirEndereco and op == '':
            op = input("Deseja inserir o endereço: ")

        elif inserirEndereco and op != '':
            if startwith(op,'s'):
                bairro = input("Informe o seu Bairro: ")
                rua = input("Informe sua rua: ")
                numero = int(input("Informe o número da sua residência: "))
                complemento = input("Digite o complemento para auxiliar na entrega: ")
                inserido = 1
            else:
                inserido = -1
                inserirEndereco = False


            
            

        if email_valido == True and telefone_valido == True and nome_valido == True:
            if inserido == 1 or inserido == -1:
                valido = True
    
    if inserido == 1:
        usuario = conta(nome,str(telefone),email,senha,bairro,rua,numero,complemento)
    elif inserido == -1:
        usuario = conta(nome,str(telefone),email,senha)
    
    arquivo.write(str(usuario.__dict__))
    arquivo.write('\n')
    arquivo.close()




def entrarConta():
    encontrado = False
    email_validado = False
    arquivo = open('contas.txt','r')
    arquivo.readline()
    arquivo.readline()
    lista = arquivo.readlines()
    chance = 0

    while not encontrado and chance < 3:
        os.system('cls')
        entrando()
        
        if not email_validado:
            email = input("Digite o seu email: ")

        for i in lista:
            aux = eval(i)
            if aux['email'] == email:
                email_validado = True
                senha = input("Digite a sua senha: ")
                if aux['senha'] == senha:
                    encontrado = True
                    break
                else:
                    os.system('cls')
                    chance += 1
                    senha_inválida_cliente()
                    sleep(2)
        if aux['email'] != email:
            os.system('cls')
            chance += 1
            email_inválido()
            sleep(2)
    
    return encontrado,aux

def fazendo_backup():
    arquivo = open('contas.txt','r')
    lista = arquivo.readlines()
    arquivo.close()
    return lista

def excluir_perfil(usuario,lista):
    arquivo = open('contas.txt','w')
    
    for i in lista[2:]:
        aux = eval(i)
        if aux['nome'] == usuario['nome']:
            lista.remove(i)
            
    arquivo.writelines(lista)
    arquivo.close()



#TERMINAR ESTA FUNÇÃO QUE ALTERA OS DADOS DE UMA CONTA
def alterar_conta(usuario):
    lista = list(fazendo_backup())
    arquivo = open('contas.txt','w')
    alterado = False
    pos = 2
    
    for i in lista[2:]:
        aux = eval(i)
        if aux['nome']==usuario['nome']:
            break
        pos += 1

    usu = eval(lista[pos])

    while not alterado:
        os.system('cls')
        alterar(usuario)
        op4 = int(input('Digite: '))   
        
        if op4 == 1:
            os.system('cls')
            usu['nome'] = input("Digite o novo usuário: ")
            lista[pos] = str(usu)
            sleep(2)
        elif op4 == 2:
            os.system('cls')
            telefone = int(input("Digite o novo número: "))
            if 1<= (telefone//10**8) <= 9:
                if not verificarTelefone(telefone):
                    usu['telefone'] = telefone
                    lista[pos] = str(usu)
                else:
                    os.system('cls')
                    Telefone_cadastrado()
                    sleep(2)
            else:
                os.system('cls')
                telefone_Inválido()
                sleep(2)
        elif op4 == 3:
            os.system('cls')
            email = input("Informe seu email: ")

            if validandoEmail(email):
                if not verificarEmail(email):
                    usu['email'] = email
                    lista[pos] = str(usu)
                else:
                    os.system('cls')
                    Email_cadastrado()
                    sleep(2)
            else:
                os.system('cls')
                email_inválido()
                sleep(2)
        elif op4 == 4:
            try:
                os.system('cls')
                senha=(input("Digite a nova senha: "))
            except:
                os.system('cls')
                senha_inválida_cliente()
                sleep(2)
            else:
                usu['senha'] = senha
                lista[pos] = str(usu)
        elif op4 == 5:
            pass #inserir endereço
        else:
            alterado = True
    arquivo.writelines(lista)
    arquivo.close()


def atualizando(usuario):
    lista = fazendo_backup()
    quant = 0
    for i in lista[2:]:
        aux = eval(i)
        if aux['nome'] == usuario['nome']:
            quant += 1
        if aux['telefone'] == usuario['telefone']:
            quant += 1
        if aux['email'] == usuario['email']:
            quant += 1
        if aux['senha'] == usuario['senha']:
            quant +=1
        
        if quant >= 2:
            return aux

def Acessar_Perfil(usuario):
    sair = False
    while not sair:
        os.system('cls')
        imprimindoPerfil(usuario)

        opcao = int(input("Digite opção: "))
        if opcao == 1:
            alterar_conta(usuario)
            usuario = atualizando(usuario)
        elif opcao == 2:
            excluir_perfil(usuario,list(fazendo_backup()))
        elif opcao == 3:
            sair = True
            sair_menu_cliente()

def fazer_pedido(usuario):
    arquivo = open("pedidos.txt",'a')
    finalizado = False
    lista_pizzas = []
    valor_total = 0


    while not finalizado:
        os.system('cls')
        fazendo_pedido()
        sabor = input("Digite o sabor da pizza: ")
        if not verifica_pizza(sabor):
            sabor_inválido()
            sleep(3)
        else:
            lista_pizzas.append(sabor)
            valor_total += valor_pizza(sabor)
            aux = input("Deseja adicionar mais pizzas: ")
            if not startwith(aux,"s"):
                finalizado = True
                
    
    pedido = pedidos(lista_pizzas,valor_total,usuario)
    os.system('cls')
    finalizando_pedido()
    deseja = input("Deseja finalizar o pedido: ")
    
    if startwith(deseja,'s'):
        arquivo.write(str(pedido.__dict__))
        arquivo.write('\n')
    arquivo.close()



def valor_pizza(sabor):
    arquivo = open('cardapio.txt','r')
    lista = arquivo.readlines()
    for i in lista[2:]:
        aux = eval(i)
        if sabor == aux['sabor']:
            arquivo.close()
            return float(aux['valor'])
    arquivo.close()
    return 0

def verifica_pizza(sabor):
    arquivo = open('cardapio.txt','r')
    lista = arquivo.readlines()
    for i in lista[2:]:
        aux = eval(i)
        if sabor == aux['sabor']:
            arquivo.close()
            return True
    arquivo.close()
    return False


if __name__ == '__main__':
   alterar_conta()
   pass