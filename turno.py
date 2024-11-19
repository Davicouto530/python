turno = input("Digite M(matutino) para se você estuda de manhã, para V(vespertino) tarde ou N(noturno) para noite: ")

if turno == 'm' or turno == "M":
    print("Bom dia!")
elif turno == 'v' or turno == "V":
    print("Boa tarde!")
elif turno == 'n' or turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido")