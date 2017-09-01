import re

'''Função do Login'''
def recebeLogin(a):

    k = True
    if(re.match(r'^[a-z]*[a-zA-Z]*$',a)):

        k = True

    else:
        k = False

    return k

'''Função do CPF'''
def recebeCPF(b):
    x = True
    if(re.match(r'[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}',b)):
            x = True
    else:
            x = False
    return x




'''Função do Email'''
def recebeEmail(c):

    z = True
    if(re.match(r'^[A-Z]+[a-z0-9\.\-\_]+@+[a-z]+[\.a-z]*$',c)):

        z = True

    else:
        z = False

    return z

'''Função da Senha'''
def recebeSenha(d):

    if(re.search(r'00|11|22|33|44|55|66|77|88|99',d) or re.search('[A-F]{2}',d)):
            return True
    elif(re.search(r'[A-F\d]{2}[\.][A-F\d]{2}[\.][A-F\d]{2}[\.][A-F\d]{2}',d)):
            return False


'''Função do nome do App'''
def recebeNomeApp(e):
    t = True
    if(re.match(r'^[a-z]*[a-zA-Z]*$',e)):
        t = True
    else:
        t = False
    return t

'''Função da versão do App'''
def recebeVersao(f):
    r = True
    if(re.compile(r'[0-9][\.][0-9]',f)):
        r = True
    else:
        r = False
    return r
'''Função da plataforma'''
def recebePlataforma(g):
    s = True
    if(re.match(r'^[a-z]*[a-zA-Z]*$',g)):

            s = True

    else:

            s = False

    return s

l=[]
ent = input()
l = ent.split(" ")
m = True
if(recebeLogin(l[0]) == True and recebeCPF(l[1]) == True and recebeEmail(l[2]) == True and recebeSenha(l[3]) == True and recebeNomeApp(l[4]) ==  True and recebeVersao(l[5]) == True and recebePlataforma(l[6]) == True and recebeLogin(l[7]) == True and recebeEmail(l[8]) == True and recebeLogin(l[9]) == True and recebeEmail(l[10]) == True):
    print(m)
else:
    m = False
    
print(m)

