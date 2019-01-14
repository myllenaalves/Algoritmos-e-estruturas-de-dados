# Vamos supor que estamos comparando implementações de ordenação por inserção e ordenação por intercalação na mesma máquina. 
# Para entradas de tamanho n, a ordenação por inserção é executada em 8n2 etapas, enquanto a ordenação por intercalação é executada em 64n Ig n etapas. 
# Para que valores de n a ordenação por inserção supera a ordenação por intercalação?

import numpy
for n in range(1000):
    if 8 * n **2 < numpy.log2(n) * 64 * n:
        print("Ainda não")
    else:
        print(n)