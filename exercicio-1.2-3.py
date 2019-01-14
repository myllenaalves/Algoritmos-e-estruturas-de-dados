def menorValor():
    for n in range(1000):
        if 100 * (n**2) < 2 ** n and n != 0:
            return "Esse é o valor " + str(n)

print(menorValor())
