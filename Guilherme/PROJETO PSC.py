
pergunta1 = 'O que te faz aqui?'
pergunta2= 'especifique melhor o seu problema?'
pergunta3= 'pra gente entender melhor, me explique de outra maneira?'

resposta1= input(pergunta1)

#BUSCAR EM BANCO DE DADOS A PALAVRA CHAVE

a= respostaDoBd(resposta1)

if a== '':
    #FAZER OUTRA PERGUNTA
    input(pergunta2)
    #BUSCAR EM BANCO DE DADOS A PALAVRA CHAVE

    a= respostaDoBd()
    if a=='':
        input(pergunta3) 
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

 