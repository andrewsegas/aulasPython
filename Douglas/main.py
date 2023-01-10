import random

#print('Hello World')

#baseado em uma condicional
num = random.randint(1,1000)
contador = 0

#baseado em condicionais
while num != 2:
    num = random.randint(1,1000)
    contador += 1

print('vezes que jogamos o dado:', contador)




#baseado em numero de repeticoes
i = 0
for i in range(5):
    num1 = random.randint(1,100)
    print (num1)
print ('vezes que jogamos o dado:', i)






