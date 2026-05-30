# criando variavel e solicitando a temperattura ao usuario
temperatura = float(input("digite a temperatura em celsius: "))

# criando as regra da condição de Se
if temperatura < 10:
    print("está muito frio!")
elif temperatura < 20:
    print("está frio")
elif temperatura < 30:
    print("está agradavel")
else:
    print("está quente")

