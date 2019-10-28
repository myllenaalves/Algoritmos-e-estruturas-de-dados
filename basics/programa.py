class Programa:
    def __init__(self, dataCriacao, codigo, nomeDono,emailDono, numeroLinhas):
        self.__dataCriacao = dataCriacao
        self.__codigo = codigo
        self.__nomeDono = nomeDono
        self.__emailDono = emailDono
        self.__numeroLinhas = numeroLinhas
    def getDataCriacao(self):
        return self.__dataCriacao
    def getCodigo(self):
        return self.__codigo
    def getNomeDono(self):
        return self.__nomeDono
    def getEmailDono(self):
        return self.__emailDono
    def getNumeroLinhas(self):
        return self.__numeroLinhas
    def setDataCriacao(self, dataCriacao):
        self.__dataCriacao = dataCriacao
        return self.__dataCriacao
    def setCodigo(self, codigo):
        self.__codigo = codigo
        return self.__codigo
    def setNomeDono(self,nomeDono):
        self.__nomeDono = nomeDono
        return self.__nomeDono
    def setEmailDono(self, emailDono):
        self.__emailDono = emailDono
        return self.__emailDono
    def setNumeroLinhas(self, numeroLinhas):
        self.__numeroLinhas = numeroLinhas
        return self.__numeroLinhas
    def calculaNumeroLinhas(self):
        pass
        # (acessa o código do Programa, conta a quantidade de linhas desse código e atualiza o atributo numeroLinhas);
    def calculaIdadeCodigo(self):
        pass
        # (acessa a data de criação do código e verifica a idade do código de acordo com o parâmetro anoAtual fornecido como parâmetro).
def comparaCodigo(programa1,programa2):
    pass
    #que recebe dois objetos do tipo Programa como #parâmetros e compara os códigos. O programa deve contar a
    #quantidade de linhas iguais do programa1 no programa2 e retornar
    #essa quantidade. As linhas iguais não precisam estar na mesma
    #posição, basta aparecerem em alguma linha dos programas.