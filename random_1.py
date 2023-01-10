import random

num = random.randint(1,10000)
contador = 0

print(num)

#baseado em uma condicionais
while num != 2:
    num = random.randint(1,10000)
    contador += 1
    # mesma coisa que
    # contador = contador + 1
    print(num)
    
print("vezes que jogamos o dado: " + str(contador))
    


#baseado no numero de repeticoes
for i in range(10):
    num = random.randint(1,10000)
    # mesma coisa que
    # contador = contador + 1
    print(num)