x = "Bem-vindo(a) à consulta. Tudo bem, meu paciente?"

#print mostra um texto na tela
print(x)

#input espera uma entrada do usuario e atribui para a variavel y
y = input("Responda:").lower()

#if cria uma condicional
if y == 'sim':
    print("Excelente. A consulta custou R$450. Ass: Jônia.")
    
#elif cria uma condicional caso nao entre na aneterior
elif y == 'não':
    print("O que está acontecendo, meu amigo? Depois discutimos valores.")    
    
#else é a opção caso não entre em nenhum dos if ou elif anteriores
else:
    
    #while repete enquanto a condição for verdadeira
    while y != 'sim' and y != 'não':
        print("Meu tempo é valioso - por favor responda 'Sim' ou 'Não'. E não se esqueça da acentuação!")
        y = input("Responda:").lower()
        if y == 'sim':
            print("Excelente. A consulta custou R$450. Ass: Jônia.")
        elif y == 'não':
            print("O que está acontecendo, meu amigo? Depois discutimos valores.")