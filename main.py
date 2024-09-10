from math import *

class Main:
    def __init__(self):
        print("Selecione o que você tem: ")
        classe = input("Digite de (0-6)\nEnergia elétrica = 0 \nEnergia magnética = 1 \nIntensidade = 2 \nFrequência = 3 \nComprimento de onda = 4 \nNúmero de onda = 5 \nFrequência Angular = 6\n")
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
        self.eEletrica = float(input("Digite a energia elétrica (em V/m):"))
        classe = input("Digite de (0-1)\nEnergia magnética = 0 \nIntensidade = 1\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterParaEnergiaMag()
        elif classe == "1":
            self.converterParaIntesidade()
        
    def converterParaEnergiaMag(self):
        self.eMagnetica = self.eEletrica / self.c 
        print(f"Energia Magnética: {self.eMagnetica:.2e} T")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.eEletrica ** 2) / (2 * self.mi * self.c)
        print(f"Intensidade: {self.Intesidade:.2e} W/m²")  # Notação científica com 3 casas decimais

class EnergiaMagnetica:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.eMagnetica = float(input("Digite a energia magnética (em T): "))
        classe = input("Digite de (0-1)\nEnergia elétrica = 0 \nIntensidade = 1\n")
        self.selecao(classe)

    def selecao(self, classe):
        if classe == "0":
            self.converterParaEnergiaEletrica()
        elif classe == "1":
            self.converterParaIntesidade()

    def converterParaEnergiaEletrica(self):
        self.eEletrica = self.c * self.eMagnetica
        print(f"Energia Elétrica: {self.eEletrica:.2e} V/m")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.c * (self.eMagnetica ** 2)) / (2 * self.mi)
        print(f"Intensidade: {self.Intesidade:.2e} W/m²")  # Notação científica com 3 casas decimais

class Intensidade:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * pi) * (10 ** (-7))
        self.intensidade = float(input("Digite a Intensidade (em W/m²): "))
        classe = input("Digite de (0-1)\nEnergia elétrica = 0 \nEnergia magnética = 1\n")
        self.selecao(classe)
        
    def selecao(self, classe):
        if classe == "0":
            self.converterParaEnergiaEletrica()
        elif classe == "1":
            self.converterParaEnergiaMag()

    def converterParaEnergiaEletrica(self):
        self.eEletrica = sqrt(self.intensidade * 2 * self.mi * self.c)
        print(f"Energia Elétrica: {self.eEletrica:.2e} V/m")  # Notação científica com 3 casas decimais

    def converterParaEnergiaMag(self):
        self.eMagnetica = sqrt((self.intensidade * 2 * self.mi) / self.c)
        print(f"Energia Magnética: {self.eMagnetica:.2e} T")  # Notação científica com 3 casas decimais

class Frequencia:
    def __init__(self):
        self.c = 3*(10**8)
        self.frequencia = float(input("Digite a frequência (em Hz): "))
        classe = input("Digite de (0-2)\nComprimento de onda = 0 \nFrequência angular = 1\nNúmero de onda = 2\n")
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
        print(f"Comprimento de Onda: {self.cOnda:.2e} m")  # Notação científica com 3 casas decimais

    def converterFrenquenciaAngular(self):
        self.fAngular = 2 * pi * self.frequencia
        print(f"Frequência Angular: {self.fAngular:.2e} rad/s")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = (2 * pi * self.frequencia) / self.c
        print(f"Número de Onda: {self.nOnda:.2e} rad/m")  # Notação científica com 3 casas decimais

class ComprimentoDeOnda:
    def __init__(self):
        self.c = 3*(10**8)
        self.cOnda = float(input("Digite o comprimento de onda (em m): "))
        classe = input("Digite de (0-2)\nFrequência angular = 0 \nFrequência = 1\nNúmero de onda = 2\n")
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
        print(f"Frequência Angular: {self.fAngular:.2e} rad/s")  # Notação científica com 3 casas decimais

    def converterFrequencia(self):
        self.frequencia = self.c / self.cOnda
        print(f"Frequência: {self.frequencia:.2e} Hz")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = (2 * pi) / self.cOnda
        print(f"Número de Onda: {self.nOnda:.2e} rad/m")  # Notação científica com 3 casas decimais

class NumeroDeOnda:
    def __init__(self):
        self.c = 3*(10**8)
        self.nOnda = float(input("Digite o número de onda (em rad/m): "))
        classe = input("Digite de (0-2)\nFrequência angular = 0 \nFrequência = 1\nComprimento de onda = 2\n")
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
        print(f"Frequência: {self.frequencia:.2e} Hz")  # Notação científica com 3 casas decimais

    def converterFrenquenciaAngular(self):
        self.fAngular = self.nOnda * self.c
        print(f"Frequência Angular: {self.fAngular:.2e} rad/s")  # Notação científica com 3 casas decimais

    def converterComprimentoDeOnda(self):
        self.cOnda = (2 * pi) / self.nOnda
        print(f"Comprimento de Onda: {self.cOnda:.2e} m")  # Notação científica com 3 casas decimais

class FrequenciaAngular:
    def __init__(self):
        self.c = 3*(10**8)
        self.fAngular = float(input("Digite a frequência angular (em rad/s): "))
        classe = input("Digite de (0-2)\nNúmero de onda = 0 \nFrequência = 1\nComprimento de onda = 2\n")
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
        print(f"Frequência: {self.frequencia:.2e} Hz")  # Notação científica com 3 casas decimais

    def converterComprimentoDeOnda(self):
        self.cOnda = (2 * pi * self.c) / self.fAngular
        print(f"Comprimento de Onda: {self.cOnda:.2e} m")  # Notação científica com 3 casas decimais

    def converterNumeroDeOnda(self):
        self.nOnda = self.fAngular / self.c
        print(f"Número de Onda: {self.nOnda:.2e} rad/m")  # Notação científica com 3 casas decimais

if __name__ == '__main__':
    app = Main()
