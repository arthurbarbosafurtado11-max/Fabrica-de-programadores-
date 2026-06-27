# criando as variaveis
num1 = input("digite o primeiro numero: ")
num2 = input("digite o segundo numero: ")

#convertendo variaveis em numero inteiro
try:
        num1 = int(num1)
        num2 = int(num2)

        print(f"A soma dos numeros é {num1 + num2}")
# tratando a excessão de erro de numero inteiro

except:
    print("São permitidos apenas números inteiros")