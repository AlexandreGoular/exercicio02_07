# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades: 

   # • Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque. 
   # • O consumo é especificado no construtor e o nível de combustível inicial é 0. 
   # • Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina. Esse método 
   #recebe como parâmetro a distância em km. 
   # • Forneça um método obterGasolina( ), que retorna o nível atual de combustível. 
   # • Forneça um método adicionarGasolina( ), para abastecer o tanque. 

#Faça um programa para testar a classe Carro. 
#Exemplo de uso: 
#meuFusca = Carro(15); # 15 quilômetros por litro de combustível. meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
#meuFusca.andar(100); # anda 100 quilômetros. 
#meuFusca.obterGasolina() # Imprime o combustível que resta no tanque. 

class Carro:

    def __init__(self, combustivel, distanciaKm, gasolina):

        self.combustivel = combustivel
        self.distanciaKm = distanciaKm
        self.gasolina = gasolina

    def andar(self, distanciaKm):
        self.distanciaKm = distanciaKm

    def obterGasolina(self, gasolina):
        return self.gasolina

    def adicionarGasolina(self, gasolina):
        self.gasolina = gasolina

meuFusca = Carro(15, 20, 100)
meuFusca.obterGasolina()