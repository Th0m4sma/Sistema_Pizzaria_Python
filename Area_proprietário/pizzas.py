import os
import sys

sys.path.append('Area_cliente')
from contas import *
from time import sleep
from Print_menu_proprietário import *


class pizza(object):
    def __init__(self,sabor,descrição,valor):
        self.sabor = sabor
        self.valor = valor
        self.descricao = descrição
    
    
class salgadas(pizza):
    def __init__(self,sabor,descrição,valor):
        super(salgadas,self).__init__(sabor,descrição,valor)
        self.tipo = 'salgada'
    
    def imprimindo(self):
        print("]|[=-Sabor: %s" %(self.sabor))
        print("]|[=-Descrição: %s" %(self.descricao))
        print("]|[=-Valor: %.2f" %(self.valor))
        print("]|[=-Tipo de pizza: %s" %(self.tipo))
        print("]|[==-----------------------------------------==]|[")

class doces(pizza):
    def __init__(self,sabor,descrição,valor):
        super(doces,self).__init__(sabor,descrição,valor)
        self.tipo = 'doce'
    
    def imprimindo(self):
        print("]|[=-Sabor: %s" %(self.sabor))
        print("]|[=-Descrição: %s" %(self.descricao))
        print("]|[=-Valor: %.2f" %(self.valor))
        print("]|[=-Tipo de pizza: %s" %(self.tipo))
        print("]|[==-----------------------------------------==]|[")
    
    


def startwith(string,sub):
    if string[:len(sub)].lower()==sub.lower():
        return True
    return False

def registrar_pizza():
    validado = False
    valor_validado = False
    tipo_validado = False
    arquivo = open('cardapio.txt','a')
    

    while not validado:
        os.system('cls')
        adicionando_pizza()
                    
        if not valor_validado:
            sabor = input("Digite o sabor da pizza: ")
            descrição = input("Digite uma descrição: ")
            valor = float(input("Digite o valor em reais: "))
            valor_validado = True
        
        if valor_validado and not tipo_validado:
            tipo = input("Digite o tipo: ")

            if startwith(tipo,'sal'):
                tipo_validado = True
                obj = salgadas(sabor,descrição,valor)
                validado = True
            elif startwith(tipo,'doc'):
                tipo_validado = True
                obj = doces(sabor,descrição,valor)
                validado = True
            else:
                os.system('cls')
                tipo_inválido()
                sleep(2)

    os.system('cls')
    confirmando()
    obj.imprimindo()
    deseja = input("Deseja inserir a pizza: ")
    
    if startwith(deseja,'s'):
        arquivo.write(str(obj.__dict__))
        arquivo.write('\n')
    arquivo.close()
            

def verifica(senha):
    arquivo = open('informações.txt','r')
    arquivo.readline()
    arquivo.readline()
    aux = arquivo.readline()

    if int(aux[8:16]) == int(senha):
        arquivo.close()
        return True
    else:
        arquivo.close()
        return False
    

def entrando():
    validado = False
    chance = 0

    while not validado and chance != 3:
        os.system('cls')
        insira_senha()
        senha = int(input("Digite a senha: "))

        if verifica(senha):
            return True
        else:
            os.system('cls')
            senha_inválida()
            chance += 1
            sleep(2)
    
    return False

def imprimindo_pizzas_salgadas():
    arquivo = open('cardapio.txt','r')
    arquivo.readline()
    arquivo.readline()
    linhas = (arquivo.readlines())  

    for i in linhas:
       aux = eval(i)
       if aux['tipo'] == 'salgada':
           print("===---------------------------------------------===")
           print('=> Pizza de %s\t\t%10.2f' %(aux['sabor'],aux['valor']))
           print('-%s' %(aux['descricao']))

def imprimindo_pizzas_doces():
    arquivo = open('cardapio.txt','r')
    arquivo.readline()
    arquivo.readline()
    linhas = (arquivo.readlines())

    for i in linhas:
       aux = eval(i)
       if aux['tipo'] == 'doce':
           print("===---------------------------------------------===")
           print('=> Pizza de %s\t%.2f' %(aux['sabor'],aux['valor']))
           print('-%s' %(aux['descricao']))
    
    print("]|[=============================================]|[")


def fazendo_backup():
    arquivo = open('cardapio.txt','r')
    lista = arquivo.readlines()
    return lista


def cardapio():
    imprimir_cardápio()
    imprimindo_pizzas_salgadas()
    imprimindo_pizzas_doces()
    aux = input("")
    
def removendo_pizza():
    os.system('cls')
    sabor = input("Digite o sabor da pizza: ")
    lista = fazendo_backup()
    arquivo = open('cardapio.txt','w')

    for i in lista[2:]:
        aux = eval(i)
        if aux['sabor'] == sabor:
            print(i)
            lista.remove(i)
    
    arquivo.writelines(lista)
    arquivo.close()


def imprimindo_pedidos():
    arquivo = open("pedidos.txt","r")

    linhas = arquivo.readlines()
    print("]|[=============================================]|[")
    print("]|[==---------------[-PEDIDOS-]---------------==]|[")
    print("]|[=============================================]|[")

    for i in linhas[2:]:
        aux = eval(i)
        pizzas = list(aux['pizzas'])
        cliente = eval(str(aux["cliente"]))
        
        print("=> PIZZAS:",pizzas)
        if(aux["status"] == 1):
            print("=> STATUS: Fazendo")
        elif(aux["status"] == 0):
            print("=> STATUS: Esperando confirmação do restaurante")
        else:
            print("=> STATUS: Saindo para a entrega")
        print("=> VALOR: R$",aux["valor"])
        print("=> CLIENTE: ",cliente["nome"])
        print("=> TELEFONE: (011)",cliente["telefone"])
        print("]|[===---------------------------------------===]|[")

    



    pass

if __name__ == '__main__':
    removendo_pizza()
    

