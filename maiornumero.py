num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

if num1 > num2: 
    print(f"O valor maior é {num1}")
elif num2 > num1:
    print(f"O valor maior é {num2}")
else:
    print("Valor inválido")