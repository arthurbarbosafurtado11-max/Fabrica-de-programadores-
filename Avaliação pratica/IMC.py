# Solicitando nome, peso e altura ao usuario
nome = input("digite seu nome: ")
peso = float(input("digite seu peso(Kg): "))
altura = float(input("digite sua altura(m): "))

#calculando o IMC do usuario
imc = peso / (altura ** 2) 



#apresentando a situaçao de saude ao paciente
if imc >= 30:
    msg = "cuidado com a saúde"
    print
else:
    msg = "tudo ok"
    print

# apresentando a situaçao de saude ao paciente
if imc < 18.5:
    situaçao = "abaixo do peso!"
    print
elif imc < 24.9:
    situaçao = "com peso normal"
    print
elif imc < 29.9:
    situaçao = "sobrepeso"
    print
elif imc < 34.9:
    situaçao = "com obesidade grau I"
    print
elif imc < 39.9:
    situaçao = "com obesidade grau II"
    print
else:
    situaçao = "com obesidade grau III"

print(f"{nome} seu IMC é {imc:.2f}, {msg} você está {situaçao}")



