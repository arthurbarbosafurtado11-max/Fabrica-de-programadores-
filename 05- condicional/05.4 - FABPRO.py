# criando variaveis e solicitando as informaçoes ao usuario
nome_aluno = input("digite seu nome: ")
nota_1 = float(input("digite sua primeira nota: "))
nota_2 = float(input("digite sua segunda nota: "))
nota_3 = float(input("digite sua terceira nota: "))

#calculando a media do aluno

media = (nota_1 + nota_2 + nota_3) / 3

#mostrando a media ao aluno
print(f"a média do aluno(a) {nome_aluno} é {media}")

# criando regras da condição Se
if media >= 7:
    print("aprovado!")
elif media > 4:
    print("recuperação!")
else:
    print("reprovado!")