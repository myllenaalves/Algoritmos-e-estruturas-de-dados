class Aluno:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = str(cpf)
        self.__nota1 = [0,False]
        self.__nota2 = [0,False]
        self.__nota3 = [0,False]
    def inicializarNota(self, nota, numeroProva):
        if numeroProva == 1:
            self.__nota1 = [nota, True]
        if numeroProva == 2:
            self.__nota2 = [nota, True]
        if numeroProva == 3:
            self.__nota3 = [nota,True]
    def verificaSituacaoMedia(self):
        if self.__nota1[1] +  self.__nota2[1] +  self.__nota3[1] >= 1:
            media = (self.__nota1[0] +  self.__nota2[0] +  self.__nota3[0]) / 3
            if media >= 7:
                return True
            else:
                return False
        else:
            print("Notas não foram atribuídas")
            return False
    def imprimeInformacoes(self):
        if self.__nota1[1] == False:
            self.__nota1[0] = "Nota não fornecida"
        if self.__nota2[1] == False:
            self.__nota2[0] = "Nota não fornecida"
        if self.__nota3[1] == False:
            self.__nota3[0] = "Nota não fornecida"
        return (self.__nome, self.__cpf, "NOTA 1: " + str(self.__nota1[0]), "NOTA 2: " + str(self.__nota2[0]), "NOTA 3: " + str(self.__nota3[0]))



     
