from math import *

class Main:
    def __init__(self):
        print("Selecione o que vc tem: ")
        classe = input("digite de (0-7)\nEnergia eletrica = 0 \nEnergia magnetica = 1 \nIntensidade = 2 \nFrequencia = 3 \nComprimento de onda = 4 \nNumero de onda = 5 \nfrequencia Angular = 6\n")
        self.troca(classe)
        
    def troca(self, classe):
        if classe == "0":
            EnergiaEletrica()
        elif classe == "1":
            EnergiaMagnetica()
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

class EnergiaEletrica:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.eEletrica = float(input("Digite a energia elétrica:"))
        classe = input("digite de (0-1)\npara energia magnetica = 0 \npara a intensidade = 1\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterParaEnergiaMag()
        elif classe == "1":
            self.converterParaIntesidade()
        
    def converterParaEnergiaMag(self):
        self.eMagnetica = self.c / self.eEletrica
        print(f"{self.eMagnetica:.2e}")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.eEletrica ** 2) / (2 * self.mi * self.c)
        print(f"{self.Intesidade:.2e}")  # Notação científica com 3 casas decimais

class EnergiaMagnetica:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.eMagnetica = float(input("Digite a energia magnética: "))
        classe = input("digite de (0-1)\npara energia eletrica = 0 \npara a intensidade = 1\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterParaEnergiaEletrica()
        elif classe == "1":
            self.converterParaIntesidade()

    def converterParaEnergiaEletrica(self):
        self.eEletrica = self.c * self.eMagnetica
        print(f"{self.eEletrica:.2e}")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.c * (self.eMagnetica ** 2)) / (2 * self.mi)
        print(f"{self.Intesidade:.2e}")  # Notação científica com 3 casas decimais

class Intensidade:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.intensidade = float(input("Digite a Intensidade: "))
        classe = input("digite de (0-1)\npara energia eletrica = 0 \npara a energia magnetica = 1\n")
        self.selecao(classe)
        
    def selecao(self, classe):
        if classe == "0":
            self.converterParaEnergiaEletrica()
        elif classe == "1":
            self.converterParaEnergiaMag()

    def converterParaEnergiaEletrica(self):
        self.eEletrica = sqrt(2 * self.mi * self.c)
        print(f"{self.eEletrica:.2e}")  # Notação científica com 3 casas decimais

    def converterParaEnergiaMag(self):
        self.eMagnetica = sqrt((2 * self.mi) / self.c)
        print(f"{self.eMagnetica:.2e}")  # Notação científica com 3 casas decimais

class Frequencia:
    def __init__(self):
        self.c = 3*(10**8)
        self.frequencia = float(input("Digite a frequencia: "))
        classe = input("digite de (0-1)\npara Comprimento de onda = 0 \npara frequencia angular = 1\npara numero de onda = 2\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterComprimentoDeOnda()
        elif classe == "1":
            self.converterFrenquenciaAngular()
        elif classe == "2":
            self.converterNumeroDeOnda()

    def converterComprimentoDeOnda(self):
        self.cOnda = self.c / self.frequencia
        print(f"{self.cOnda:.2e}")  # Notação científica com 3 casas decimais

    def converterFrenquenciaAngular(self):
        self.fAngular = 2 * pi * self.frequencia
        print(f"{self.fAngular:.2e}")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = (2 * pi * self.frequencia) / self.c
        print(f"{self.nOnda:.2e}")  # Notação científica com 3 casas decimais

class ComprimentoDeOnda:
    def __init__(self):
        self.c = 3*(10**8)
        self.cOnda = float(input("Digite o comprimento de onda: "))
        classe = input("digite de (0-1)\npara frequencia angular = 0 \npara frequencia = 1\npara numero de onda = 2\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterFrenquenciaAngular()
        elif classe == "1":
            self.converterFrequencia()
        elif classe == "2":
            self.converterNumeroDeOnda()

    def converterFrenquenciaAngular(self):
        self.fAngular = (2 * pi * self.c) / self.cOnda
        print(f"{self.fAngular:.2e}")  # Notação científica com 3 casas decimais

    def converterFrequencia(self):
        self.frequencia = self.c / self.cOnda
        print(f"{self.frequencia:.2e}")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = (2 * pi) / self.cOnda
        print(f"{self.nOnda:.2e}")  # Notação científica com 3 casas decimais

class NumeroDeOnda:
    def __init__(self):
        self.c = 3*(10**8)
        self.nOnda = float(input("Digite o número de onda: "))
        classe = input("digite de (0-1)\npara frequencia angular = 0 \npara frequencia = 1\npara comprimento de onda = 2\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterFrenquenciaAngular()
        elif classe == "1":
            self.converterFrequencia()
        elif classe == "2":
            self.converterComprimentoDeOnda()

    def converterFrequencia(self):
        self.frequencia = (self.nOnda * self.c) / (2 * pi)
        print(f"{self.frequencia:.2e}")  # Notação científica com 3 casas decimais

    def converterFrenquenciaAngular(self):
        self.fAngular = self.nOnda * self.c
        print(f"{self.fAngular:.2e}")  # Notação científica com 3 casas decimais

    def converterComprimentoDeOnda(self):
        self.cOnda = (2 * pi) / self.nOnda
        print(f"{self.cOnda:.2e}")  # Notação científica com 3 casas decimais

class FrequenciaAngular:
    def __init__(self):
        self.c = 3*(10**8)
        self.fAngular = float(input("Digite a frequencia angular: "))
        classe = input("digite de (0-1)\npara numero de onda = 0 \npara frequencia = 1\npara comprimento de onda = 2\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterNumeroDeOnda()
        elif classe == "1":
            self.converterFrequencia()
        elif classe == "2":
            self.converterComprimentoDeOnda()

    def converterFrequencia(self):
        self.frequencia = self.fAngular / (2 * pi)
        print(f"{self.frequencia:.2e}")  # Notação científica com 3 casas decimais

    def converterComprimentoDeOnda(self):
        self.cOnda = (2 * pi * self.c) / self.fAngular
        print(f"{self.cOnda:.2e}")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = self.fAngular / self.c
        print(f"{self.nOnda:.2e}")  # Notação científica com 3 casas decimais

if __name__ == '__main__':
    app = Main()
