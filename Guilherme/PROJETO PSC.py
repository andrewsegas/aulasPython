#variavel LISTA, aqui pode colocar varias coisas dentro de uma unica variavel e encontrar com o indice (iniciando pelo zero)
pergunta = ['O que te faz aqui?', 'especifique melhor o seu problema?', 'pra gente entender melhor, me explique de outra maneira?']


resposta1= input(pergunta[0])

#BUSCAR EM BANCO DE DADOS A PALAVRA CHAVE

a= respostaDoBd(resposta1)

if a== '':
    #FAZER OUTRA PERGUNTA
    input(pergunta[1])
    #BUSCAR EM BANCO DE DADOS A PALAVRA CHAVE

    a= respostaDoBd()
    if a=='':
        input(pergunta[2]) 
        #BUSCAR EM BANCO DE DADOS A PALAVRA CHAVE

        a= respostaDoBd()
        if a=='':
            
            print('no momento nossa equipe nao pode te ajudar')
        else:
            print(a)

    else:
        print(a)

else:
    print(a)
    


















if x == 'nao':
    print('renuncie todos os prazeres e expectativas da vida')
elif x == 'sim':
    print('va embora, voce nao esta preparaado para esse assunto!')

z= 'mas vamos continuar... voce e H ou M? '
a= input(z)
if a == 'H':
    print('use cueca!')
elif a == 'M':
    print('use calcinha!')

 