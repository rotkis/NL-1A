from math import *

class Main:
    def __init__(self):
        while True:
            print("\n--------------------------------------------------------------------------\n")
            print("Selecione o que você tem: ")
            classe = input("Digite de (0-6)\nCampo elétrico = 0 \nCampo magnético = 1 \nIntensidade = 2 \nFrequência = 3 \nComprimento de onda = 4 \nNúmero de onda = 5 \nFrequência Angular = 6\nSair = 7\n")
            if classe == "0":
                CampoEletrico()
            elif classe == "1":
                CampoMagnetico()
            elif classe == "2":
                Intensidade()
            elif classe == "3":
                    Frequencia()
            elif classe == "4":
                ComprimentoDeOnda()
            elif classe == "5":
                NumeroDeOnda()
            elif classe == "6":
                FrequenciaAngular()
            else:
                break


class CampoEletrico:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.cEletrico = float(input("Digite o campo elétrico (em V/m):"))
        print("\n--------------------------------------------------------------------------\n")
        self.converterParaIntesidade()
        self.converterParaCampoMag()

    def converterParaCampoMag(self):
        self.cMagnetico = self.cEletrico / self.c 
        print(f"Campo Magnético: {self.cMagnetico:.3e} T")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.cEletrico ** 2) / (2 * self.mi * self.c)
        print(f"Intensidade: {self.Intesidade:.3e} W/m²")  # Notação científica com 3 casas decimais

class CampoMagnetico:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.cMagnetico = float(input("Digite o campo magnético (em T): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterParaCampoEletrico()
        self.converterParaIntesidade()

    def converterParaCampoEletrico(self):
        self.cEletrico = self.c * self.cMagnetico
        print(f"Campo Elétrico: {self.cEletrico:.3e} V/m")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.c * (self.cMagnetico ** 2)) / (2 * self.mi)
        print(f"Intensidade: {self.Intesidade:.3e} W/m²")  # Notação científica com 3 casas decimais

class Intensidade:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * pi) * (10 ** (-7))
        self.intensidade = float(input("Digite a Intensidade (em W/m²): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterParaCampoEletrico()
        self.converterParaCampoMag()


    def converterParaCampoEletrico(self):
        self.cEletrico = sqrt(self.intensidade * 2 * self.mi * self.c)
        print(f"Campo Elétrico: {self.cEletrico:.3e} V/m")  # Notação científica com 3 casas decimais

    def converterParaCampoMag(self):
        self.cMagnetico = sqrt((self.intensidade * 2 * self.mi) / self.c)
        print(f"Campo Magnético: {self.cMagnetico:.3e} T")  # Notação científica com 3 casas decimais

class Frequencia:
    def __init__(self):
        self.c = 3*(10**8)
        self.frequencia = float(input("Digite a frequência (em Hz): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterComprimentoDeOnda()
        self.converterFrenquenciaAngular()
        self.converterNumeroDeOnda()

    def converterComprimentoDeOnda(self):
        self.cOnda = self.c / self.frequencia
        print(f"Comprimento de Onda: {self.cOnda:.3e} m")  # Notação científica com 3 casas decimais

    def converterFrenquenciaAngular(self):
        self.fAngular = 2 * pi * self.frequencia
        print(f"Frequência Angular: {self.fAngular:.3e} rad/s")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = (2 * pi * self.frequencia) / self.c
        print(f"Número de Onda: {self.nOnda:.3e} rad/m")  # Notação científica com 3 casas decimais

class ComprimentoDeOnda:
    def __init__(self):
        self.c = 3*(10**8)
        self.cOnda = float(input("Digite o comprimento de onda (em m): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterNumeroDeOnda()
        self.converterFrenquenciaAngular()
        self.converterFrequencia()

    def converterFrenquenciaAngular(self):
        self.fAngular = (2 * pi * self.c) / self.cOnda
        print(f"Frequência Angular: {self.fAngular:.3e} rad/s")  # Notação científica com 3 casas decimais

    def converterFrequencia(self):
        self.frequencia = self.c / self.cOnda
        print(f"Frequência: {self.frequencia:.3e} Hz")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = (2 * pi) / self.cOnda
        print(f"Número de Onda: {self.nOnda:.3e} rad/m")  # Notação científica com 3 casas decimais

class NumeroDeOnda:
    def __init__(self):
        self.c = 3*(10**8)
        self.nOnda = float(input("Digite o número de onda (em rad/m): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterFrequencia()
        self.converterFrenquenciaAngular()
        self.converterComprimentoDeOnda()
     
    def converterFrequencia(self):
        self.frequencia = (self.nOnda * self.c) / (2 * pi)
        print(f"Frequência: {self.frequencia:.3e} Hz")  # Notação científica com 3 casas decimais

    def converterFrenquenciaAngular(self):
        self.fAngular = self.nOnda * self.c
        print(f"Frequência Angular: {self.fAngular:.3e} rad/s")  # Notação científica com 3 casas decimais

    def converterComprimentoDeOnda(self):
        self.cOnda = (2 * pi) / self.nOnda
        print(f"Comprimento de Onda: {self.cOnda:.3e} m")  # Notação científica com 3 casas decimais

class FrequenciaAngular:
    def __init__(self):
        self.c = 3*(10**8)
        self.fAngular = float(input("Digite a frequência angular (em rad/s): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterFrequencia()
        self.converterNumeroDeOnda()
        self.converterComprimentoDeOnda()

    def converterFrequencia(self):
        self.frequencia = self.fAngular / (2 * pi)
        print(f"Frequência: {self.frequencia:.3e} Hz")  # Notação científica com 3 casas decimais

    def converterComprimentoDeOnda(self):
        self.cOnda = (2 * pi * self.c) / self.fAngular
        print(f"Comprimento de Onda: {self.cOnda:.3e} m")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = self.fAngular / self.c
        print(f"Número de Onda: {self.nOnda:.3e} rad/m")  # Notação científica com 3 casas decimais

if __name__ == '__main__':
    print("Autores: Aline Rocha de Jesus, Arthur Carvalho Rotkis, Bianca Silva Oliveira")
    print("O objetivo deste projeto é demonstrar, por meio de um código Python, as ondas eletromagnéticas,\nque são ondas capazes de propagar no vácuo e de se formarem pela combinação entre os campos elétricos e magnéticos,\nque são responsáveis pela onda de rádio, micro-ondas, infravermelho, luz visível, raios ultravioletas, raio X e raios gama.\nAlém disso, as ondas eletromagnéticas são classificadas de acordo com a frequência, oscilação e comprimento de onda, que também são representados dentro do código.")
    
    app = Main()

