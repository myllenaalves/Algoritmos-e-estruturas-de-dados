class No:
    def __init__(self, item = None, proximo = None):
        self.item = item
        self.proximo = proximo
    def __repr__(self):
        return "_No({})".format(self.item.__repr__())
    def __str__(self):
        return self.item.__str__()

class Lista:
    def __init__(self):
        self.primeiro = self.ultimo = No()
    def insert(self, valor):
        self.ultimo.proximo = No(valor)
        self.ultimo = self.ultimo.proximo
    def delete(self, x):
        if self.primeiro == self.ultimo:
            raise ValueError("Não é possível remover itens de uma lista vazia")
        anterior = self.primeiro
        atual = anterior.proximo
        while not atual is None and atual.item != x:
            anterior = atual
            atual = anterior.proximo
        if atual == None:
            raise ValueError("{} não pertence a lista".format(repr(x)))
        else:
            anterior.proximo = atual.proximo
            atual.proximo = None
            if self.ultimo == atual:
                self.ultimo = anterior
            del atual
    ## IMPLANTAR O LIST-SEARCH    
    def __str__(self):
        string = ""
        anterior = self.primeiro
        atual = anterior.proximo
        while not atual == None:
            string += atual.item.__repr__()
            if not atual is None:
                string += ", "
            anterior = atual
            atual = anterior.proximo
        return "[{}]".format(string)
lista = Lista()
lista.insert(6)
lista.insert(-39) 
lista.insert(100)
print(lista.__str__())
lista.delete(6)
print(lista.__str__())

