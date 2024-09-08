from math  import * 


class Main:
    def __init__(self):
        pass

        

class EnergiaEletrica:
    def __init__(self):
        self.eEletrica = input("Digite a energia elétrica:")
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)

    def converterParaEnergiaMag(self):
        self.eMagnetica = self.c / self.eEletrica 

    def converterParaIntesidade(self):
        self.Intesidade = (self.eEletrica ** 2) / (2 * self.mi *self.c)

class EnergiaMagnetica:
    def __init__(self):
        self.eMagnetica = input("Digite a energia magnética")
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)

    def converterParaEnergiaEletrica(self):
        self.eEletrica = self.c * self.eMagnetica

    def converterParaIntesidade(self):
        self.Intesidade = (self.c * (self.eMagnetica ** 2) )/ (2 * self.mi)

class Intensidade:
    def __init__(self):
        self.intensidade = input("Digite a Intensidade")
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)

    def converterParaEnergiaEletrica(self):
        self.eEletrica = sqrt(2* self.mi * self.c)

    def converterParaEnergiaMag(self):
        self.eMagnetica = sqrt((2* self.mi) / self.c)

class Frequencia:
    def __init__(self):
        self.frequencia = input("Digite a frequencia: ")
        self.c = 3*(10**8)

    def converterComprimentoDeOnda(self):
        self.cOnda = self.c / self.frequencia

    def converterFrenquenciaAngular(self):
        self.fAngular = 2 *pi() * self.frequencia

    def converterNumeroDeOnda(self):
        self.nOnda = (2 *pi() * self.frequencia) / self.c

class ComprimentoDeOnda:
    def __init__(self):
        self.cOnda = input("Digite a comprimento de onda: ")
        self.c = 3*(10**8)

    def converterFrenquenciaAngular(self):
        self.fAngular = (2 * pi() * self.c) / self.cOnda

    def converterFrequencia(self):
        self.frequencia = self.c / self.cOnda

    def converterNumeroDeOnda(self):
        self.nOnda = (2* pi()) / self.cOnda

class NumeroDeOnda:
    def __init__(self):
        self.nOnda = input("Digite um numero de onda: ")
        self.c = 3*(10**8)

    def converterFrequencia(self):
        self.frequencia = (self.nOnda * self.c) / (2* pi()) 

    def converterFrenquenciaAngular(self):
        self.fAngular = self.nOnda * self.c

    def converterComprimentoDeOnda(self):
        self.cOnda = (2* pi()) / self.nOnda 

class FrequenciaAngular:
    def __init__(self):
        self.fAngular = input("Digite a frequencia angular: ")
        self.c = 3*(10**8)

    def converterFrequencia(self):
        self.frequencia = self.fAngular / (2*pi())

    def converterComprimentoDeOnda(self):
        self.cOnda = (2*pi() * self.c) / self.fAngular

    def converterNumeroDeOnda(self):
        self.nOnda = self.fAngular / self.c

if __name__ == '__main__':
    pass