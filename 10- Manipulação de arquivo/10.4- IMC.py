# Criando as variaveis e pedindo as informações ao usuario
nome = input("digite seu nome: ")
peso = float(input("digite seu peso(kg): "))
altura = float(input("digite sua altura(m): "))

#calculando o IMC do usuario
imc = peso / (altura * altura)

#apresentando a situaçao de saude ao paciente
if imc >= 30:
    msg = "cuidado com a saúde"
    print(msg)
else:
    msg = "tudo ok"
    print(msg)

# apresentando a situaçao de saude ao paciente
if imc < 18.5:
    situaçao = "abaixo do peso!"
    print(situaçao)
elif imc < 24.9:
    situaçao = "peso normal"
    print(situaçao)
elif imc < 29.9:
    situaçao = "sobrepeso"
    print(situaçao)
elif imc < 34.9:
    situaçao = "obesidade grau I"
    print(situaçao)
elif imc < 39.9:
    situaçao = "obesidade grau II"
    print(situaçao)
else:
    situaçao = "obesidade grau III"
    print(situaçao)

# Gravando o nome, peso, altura, situação e mensagem
with open("10.4- IMC.txt","a",encoding="utf-8") as arquivo:
    arquivo.write(nome + " | " + str(peso) + " | " + str(altura) + " | " + situaçao + " | " + msg + "\n")




