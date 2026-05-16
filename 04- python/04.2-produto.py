#criando variaveis e solicitando as informações ao usuario
nome_produto = input("digite o nome do pruduto: ")
valor = float(input("digite o valor do produto: "))
desconto = float(input("digite o percentual de desconto: "))

#calculado a porcentagem e o valor do desconto
valor_desconto = valor * (desconto / 100)

preco_final = valor - valor_desconto

# apresentando preço final do produto ao usuario
print("--------------------------------------")
print(f"Produto: {nome_produto} - preco_final: {preco_final}")
print("--------------------------------------")



