#criando variaveis e pedindo as informações ao usuario
nome = input("qual é o seu nome? ")
idade = int(input("qual é a sua idade? "))
possui_carteira = int(input("você possui carteira de motorista? \n (1-sim / 2-Não)"))


# criando a condição de desvio
if idade >= 18:
    if possui_carteira == 1:
        print("pode dirigir ")
    else:
        print("Não pode dirigir")
    
else:
    print("menor de idade ")