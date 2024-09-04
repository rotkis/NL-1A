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
        pass

    def converterComprimentoDeOnda(self):
        pass

    def converterFrenquenciaAngular(self):
        pass

    def converterNumeroDeOnda(self):
        pass

class ComprimentoDeOnda:
    def __init__(self):
        pass

    def converterFrenquenciaAngular(self):
        pass

    def converterFrequencia(self):
        pass

    def converterNumeroDeOnda(self):
        pass

class NumeroDeOnda:
    def __init__(self):
        pass

    def converterFrequencia(self):
        pass

    def converterFrenquenciaAngular(self):
        pass

    def converterComprimentoDeOnda(self):
        pass

class FrequenciaAngular:
    def __init__(self):
        pass

    def converterFrequencia(self):
        pass

    def converterComprimentoDeOnda(self):
        pass

    def converterNumeroDeOnda(self):
        pass

if __name__ == '__main__':
    pass