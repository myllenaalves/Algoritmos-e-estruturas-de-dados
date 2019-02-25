class Pilha:
    def __init__(self, n):
        self.__arranjo = [None] * n
        self.__topo = 0
    def stack_empty(self):
        if self.__arranjo[self.__topo] == None:
            return True
        else:
            return False
    def push(self, valor):
        self.__topo = self.__topo + 1
        self.__arranjo[self.__topo] = valor
    def pop(self):
        if self.stack_empty():
            raise IndexError ("Underflow")
        else:
            self.__topo = self.__topo - 1
            return self.__arranjo[self.__topo + 1]
    def mostrarArranjo(self):
        return self.__arranjo
    def mostrarTopo(self):
        return self.__topo






