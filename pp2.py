import sys
def ver_espaco(item):
        if((item == '(') or (item == ')') or (item == '[') or (item == ']') or (item == '{') or (item == '}')):
                return True
        else:
                return False

def casamento(lista1):
        lista = list(filter(ver_espaco, lista1))
        pilha = []
        topo = -1
        for i in range(0, len(lista)):
                if(lista[i] == '('):
                        pilha.append(lista[i])
                elif(lista[i] == '['):
                        pilha.append(lista[i])
                elif(lista[i] == '{'):
                        pilha.append(lista[i])
                
                elif(len(pilha) == 0):
                        return False
                
                elif((lista[i] == ')')):
                        if(pilha[topo] == '('):
                                pilha.pop()
                        else:
                                return False
                
                elif((lista[i] == '}')):
                        if(pilha[topo] == '{'):
                                pilha.pop()
                        else:
                                return False
                
                elif((lista[i] == ']')):
                        if(pilha[topo] == '['):
                                pilha.pop()
                        else:
                                return False
                else:
                        return False
                
        if(len(pilha)==0):
                return True
        else:
                return False

try:
        entrada = input()
        print(casamento(entrada))
except:
        print(True)