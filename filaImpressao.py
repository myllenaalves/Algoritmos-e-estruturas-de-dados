class Arquivo():
    def __init__(self, id,t,d,p):
        self.id = id
        self.t = t
        self.d = d
        self.p = p
class listaImpressão():
    def __init__(self, lista):
        self.__listaImpressao = []
        self.__primeiro = self.__ultimo = None
    def imprimindo(self):
        if self.__primeiro == None:
            self.__listaImpressao.append(lista[0])
            self.__primeiro = lista[0]
        else:
            for index in range(len(lista)):
                if lista[index][4] > self.__primeiro:
                    self.__ultimo = self.__primeiro
                    self.__primeiro = lista[index][4] 
                    lista[0] = self.__primeiro
                    lista.append(self.__ultimo)
        return lista

##SCRIPT##
if __name__ == '__main__':
    lista = []
    n = int(input("Digite o número de arquivos a serem impressos: "))
    contador = 1
    while contador <= n:
        id = contador
        p = int(input("Digite a prioridade do arquivo " + str(contador)+ ": "))
        t = int(input("Digite o instante que o arquivo " + str(contador) + " foi submetido para impressão: "))
        d = int(input("Digite a duração estimada de impressão do arquivo " + str(contador)+ ": "))
        arquivo = Arquivo(id,t, d, p)
        lista.append((arquivo.id, arquivo.t, arquivo.d, arquivo.p))
        lista.sort(key=lambda x:x[1])
        contador += 1
    listaImpressão = listaImpressão(lista)
    print(listaImpressão.imprimindo())





