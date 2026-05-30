#criando a variavel de contagem
contador_par = 0

# laço de repetição for 
for numero in range(1,11):
    if numero % 2 == 0:
        print(f"o numero {numero} é PAR")
        contador_par += 1
    else:
        print(f"o numero {numero} é IMPAR")

print("-" * 20)
print(f"total de numeros pares encontrados {contador_par}")
        


