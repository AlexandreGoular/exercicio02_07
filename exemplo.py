#Crie uma classe denominada Elevador para armazenar as informações de um elevador
#dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares
#no prédio, excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes
#nele.

#A classe deve também disponibilizar os seguintes métodos:
#Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de
#andares no prédio (os elevadores sempre começam no térreo e vazio);
#Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver
#espaço);

#Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro
#dele);

#Sobe: para subir um andar (não deve subir se já estiver no último andar);
#Desce: para descer um andar (não deve descer se já estiver no térreo);
#Encapsular todos os atributos da classe. Criar um Loop com um menu solicitando qual
#opção acima deve ser executada e, a cada repetição, informar os dados de andar e
#quantidade de pessoas.

class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade_elevador, pessoas_elevador):
        self.andar_atual = andar_atual
        self.total_andares = total_andares
        self.capacidade_elevador = capacidade_elevador
        self.pessoas_elevador = pessoas_elevador

    def inicializa(self, capacidade_elevador, total_andares):
        self.capacidade_elevador 
        self.total_andares = 0


    def entra(self, pessoas_elevador, capacidade_elevador):
        if(pessoas_elevador > capacidade_elevador):
            return print("O Elevador esta lotado")
        else:
            capacidade_elevador =- 1

    def sai(self, pessoas_elevador, capacidade_elevador):
        capacidade_elevador += 1

def menu():
    print("[1] - Iniciar")
    print("[2] - Entrar")
    print("[3] - Sair")


menu()

opcao = int(input("Qual opção deseja: "))

if(opcao == 1):
    capacidade_elevador = int(input("Digite quantas pessoas cabem no Elevador: "))
    total_andares = int(input("Digite o total de andares que tem no predio: "))
    elevador1 = Elevador(capacidade_elevador, total_andares=)
elif(opcao == 2):

elif(opcao == 3):

else:
    print("Opção Invalida")