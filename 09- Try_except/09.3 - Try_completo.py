try:    
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))

    resultado = num1 / num2

#caso o erro seja de divisão por zero (denominador = 0)
except ZeroDivisionError:
    print("erro: divisão por zero não é permitida.")

#caso o erro seja pro algum valor não numerico (digitar letras, por exemplo)
except ValueError:
    print("erro: voce precisa digitar apenas numeros inteiros.")

# caso nao haja erro,mostramos o resultado
else:
    print(f"resultado da divisão: {resultado}")

#este bloco sempre sera executado, nao importa se houve erro ou não 
finally:
    print("operação finalizada")