salario = float(input("Digite o salário do funcionário: "))

if salario <= 280:
    valoraumento = salario * 20 / 100
    novosalario = salario + valoraumento
    print(f"O antigo salário é {salario}, e foi reajustado em 20%. O valor do aumento é {valoraumento} e o novo salario {novosalario}")
elif salario > 280 and salario <= 700:
    valoraumento = salario * 15 / 100
    novosalario = salario + valoraumento
    print(f"O antigo salário é {salario}, e foi reajustado em 15%. O valor do aumento é {valoraumento} e o novo salario {novosalario}")
elif salario > 700 and salario <= 1500:
    valoraumento = salario * 10 / 100
    novosalario = salario + valoraumento
    print(f"O antigo salário é {salario}, e foi reajustado em 10%. O valor do aumento é {valoraumento} e o novo salario {novosalario}")
else:
    valoraumento = salario * 5 / 100
    novosalario = salario + valoraumento
    print(f"O antigo salário é {salario}, e foi reajustado em 5%. O valor do aumento é {valoraumento} e o novo salario {novosalario}")