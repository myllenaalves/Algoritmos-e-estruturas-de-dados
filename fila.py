class Fila:
    def __init__(self, N):
        self.__arranjo = [None] * (N)
        self.__arranjo[0] = "-"
        self.__comprimento = N - 1
        self.__inicio = self.__fim = 1
    def enqueue(self, valor):
        self.__arranjo[self.__fim] = valor
        if  self.__fim == self.__comprimento:
            self.__fim = 1
        else:
            self.__fim = self.__fim + 1
    def dequeue(self):
        x = self.__inicio
        self.__arranjo[self.__inicio] = None
        if self.__inicio == self.__comprimento:
            self.__inicio = 1
        else:
            self.__inicio = self.__inicio + 1
        return x
    def mostrarArranjo(self):
        return self.__arranjo
    def mostrarInicio(self):
        return self.__inicio
    def mostrarFim(self):
        return self.__fim
    def mostrarComprimento(self):
        return self.__comprimento







        