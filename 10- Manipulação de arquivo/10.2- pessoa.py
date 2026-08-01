# solicitando nome e email ao usuario
nome = input("digite seu nome: ")
email = input("digite seu e-mail: ")

# acessando arquivo e gravando dados do usuario
with open("10.2-pessoa.txt","a") as arquivo:
    arquivo.write(nome + " | " + email + "\n")
    
