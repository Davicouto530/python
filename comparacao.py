num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"O valor {num1} é maior")
elif num2 > num1 and num2 > num3:
    print(f"O valor {num2} é maior")
else: 
    print(f"O valor {num3} é maior")