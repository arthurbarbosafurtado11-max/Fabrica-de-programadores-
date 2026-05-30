# Criando as variaveis e pedindo as informações ao usuario
nome = input("digite seu nome: ")
peso = float(input("digite seu peso(kg): "))
altura = float(input("digite sua altura(m): "))

#calculando o IMC do usuario
imc = peso / (altura * altura)

#apresentando a situaçao de saude ao paciente
if imc >= 30:
    print("cuidado com a saúde!")
else
    print("tudo ok!")

# apresentando a situaçao de saude ao paciente
if imc < 18.5:
    print("abaixo do peso!")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print("sobrepeso")
elif imc < 34.9:
    print("obesidade grau I")
elif imc < 39.9:
    print("obesidade grau II")
else:
    print("obesidade grau III")

