
# funcao para somar um array 1
def somaarray1(ar):
    somatudo = 0
    # parametros do for (start, stop, step)
    for x in range(len(ar)):
        somatudo += ar[x]
        #print(ar[x])

    return somatudo

# funcao para somar um array 2
def somaarray2(ar):
    somatudo = 0
    # parametros do for (start, stop, step)
    for x in ar:
        somatudo += x
        #print(x)

    return somatudo

# funcao para somar um array 3
def somaarray3(ar):
    return sum(ar)


meuarrayzinho = [1,1,1,1,1,1,1,1,2,3,5,6,7]

resultado=somaarray3(meuarrayzinho)

print(resultado)