entrada = input()
f1 = []
f1.append(entrada)
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []
f7 = []

marc1 = 0
marc2 = 0
marc3 = 0
marc4 = 0
marc5 = 0
marc6 = 0
marc7 = 0

branco = " "

def estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7):
    if(f1[marc1] == "a"):
        f2.append(f1[marc1])
        marc1 += 1
        marc2 += 1
        marc3 = 0
        marc4 = 0
        marc5 = 0
        marc6 = 0
        marc7 = 0
        estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f1[marc1] == "b"):
        f3.append(f1[marc1])
        marc1 += 1
        marc2 = 0
        marc3 += 1
        marc4 = 0
        marc5 = 0
        marc6 = 0
        marc7 = 0
        estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f1[marc1] == "c"):
        f4.append(f1[marc1])
        marc1 += 1
        marc2 = 0
        marc3 = 0
        marc4 += 1
        marc5 = 0
        marc6 = 0
        marc7 = 0
        estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f1[marc1] == "d"):
        f5.append(f1[marc1])
        marc1 += 1
        marc2 = 0
        marc3 = 0
        marc4 = 0
        marc5 += 1
        marc6 = 0
        marc7 = 0
        estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f1[marc1] == "e"):
        f6.append(f1[marc1])
        marc1 += 1
        marc2 = 0
        marc3 = 0
        marc4 = 0
        marc5 = 0
        marc6 += 1
        marc7 = 0
        estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f1[marc1] == "f"):
        f7.append(f1[marc1])
        marc1 += 1
        marc2 = 0
        marc3 = 0
        marc4 = 0
        marc5 = 0
        marc6 = 0
        marc7 += 1
        estado0(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
        estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
def estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7):
    if(f1[marc1] == branco):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        estado1(marc1,marc2,marc3,marc4,marc5)
    elif(f2[marc2] == "a"):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f3[marc3] == "b"):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f4[marc4] == "c"):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f5[marc5] == "d"):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f6[marc6] == "e"):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        marc6 -= 1
        marc7 -= 1
        estado1(marc1,marc2,marc3,marc4,marc5,marc6,marc7)
    elif(f7[marc7] == "f"):
        marc1 = 0
        marc2 -= 1
        marc3 -= 1
        marc4 -= 1
        marc5 -= 1
        marc6 -= 1
        marc7 -= 1
    if(f1[marc1] == branco):
        marc1 = 0
        if(f2[marc2] == branco):
            marc2 = 0
            if(f3[marc3] == branco):
                marc3 = 0
                if(f4[marc4] == branco):
                    marc4 = 0
                    if(f5[marc5] == branco):
                        marc5 = 0
                        if(f6[marc6] == branco):
                            marc6 = 0
                            if(f7[marc7] == branco):
                                marc7 = 0
                                estado2()
                        
def estado2():
    print(f1)
    print("Aceita")
    print("Rejeita")