login = "Login: "
senha = "Senha: "
deubom = False
def minhaFuncao(a,b):
    
    if a!='galabuger' and b!='321':     
       return False
    else:
        return True


while deubom ==False:
    a=input(login)
    b=input(senha)
    deubom = minhaFuncao(a,b)

