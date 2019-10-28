class Empreendimento:
    def __init__(self):
        pass
    def getNome(self):
        pass
    def setNome(self):
        pass
    def getCNPJ(self):
        pass
    def setCNPJ(self):
        pass
    def getEndereco(self):
        pass
    def setEndereco(self):
        pass
    def getLucro(self):
        pass
    def setVenda(self):
        pass
class Supermercado(Empreendimento):
    def __init__(self, nome, CNPJ, endereco):
        self.__nome = nome
        self.__CNPJ = CNPJ
        self.__endereco = endereco
        self.__saldo = 0
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
        return self.__nome
    def getCNPJ(self):
        return self.__CNPJ
    def setCNPJ(self, CNPJ):
       self.__CNPJ = CNPJ
       return self.__CNPJ
    def getSaldo(self):
        return self.__saldo
    def setVenda(self, valorVenda):
        self.__saldo += valorVenda
        return self.__saldo    
VarejaoCin = Supermercado("VarejaoCin", 7789789798798, "UFPE")
CompraUFPE = Supermercado("CompraUFPE", 98908098, "Várzea")
estudantesVarzea = Supermercado("EstudantesVarzea", 545454645, "Polidoro")



