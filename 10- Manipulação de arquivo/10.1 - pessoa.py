# solicitando nome e email ao usuario
nome = input("digite seu nome: ")
email = input("digite seu e-mail: ")

# acessando arquivo e gravando dados do usuario
arquivo = open("10.1 - pessoa.txt","a")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()
