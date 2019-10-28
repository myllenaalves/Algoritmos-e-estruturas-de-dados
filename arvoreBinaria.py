class No:
    def __init__(self, chave, valor, esq=None, dir=None,p=None):
        self.chave = chave
        self.valor = valor
        self.esq = esq
        self.dir = dir
        self.p = p
class Arvore:
    def __init__(self):
        self.raiz = No(None,None)
        self.tamanho = 0
    def __len__(self):
        return self.tamanho
    def __str__(self):
        x = self.raiz
        return self.em_ordem(x)    
    
    def em_ordem(self,x):
        msg = ""
        if x!= None:
            msg += str(x.chave)
            self.em_ordem(x.esq)
            msg += str(x.chave)
            self.em_ordem(x.dir)
            msg += str(x.chave)
        return msg
    
    def inserir(self, chave, valor):
        y = None 
        x = self.raiz
        no_inserir = No(chave, valor)
        while x!= None and x.chave != None:
            y = x
            if no_inserir.chave < x.chave:
                x = x.esq
            else:
                x = x.dir
        no_inserir.p = y
        if y == None:
            self.raiz = no_inserir
        elif no_inserir.chave < y.chave:
            y.esq = no_inserir
        else:
            y.dir = no_inserir
        self.tamanho += 1

    def buscarIterativo(self, chave):
        x = self.raiz
        while x.chave != None and chave != x.chave:
            if chave < x.chave:
                x = x.esq
            else:
                x = x.dir
        return x.valor
    #def remover(self):
    #método remoção, aqui você deve implementar uma função que remove um elemento(chave,valor) a sua árvore
tree = Arvore()
tree.inserir(15,'quinze')
tree.inserir(66,'sessenta e seis')
tree.inserir(1,'um')
tree.inserir(50,'cinquenta')
tree.inserir(11,'onze')

