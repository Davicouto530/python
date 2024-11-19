n1 = int(input("Digite um número: ")) # Convertendo de string para inteiro, colocando o "int"
n2 = int(input("Digite outro número: "))

soma = n1 + n2
subtrair = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto = n1 % n2

print(f"O resultado da soma é {soma} o tipo da variável é {type(soma)}") # "type" mostra o tipo da variável 
print(f"O resultado da subtração é {subtrair} o tipo da variável é {type(subtrair)}")
print(f"O resultado da multiplicacao é {multiplicacao} o tipo da variável é {type(multiplicacao)}")
print(f"O resultado da divisao é {divisao} o tipo da variável é {type(divisao)}")
print(f"O resultado da resto é {resto} o tipo da variável é {type(resto)}")