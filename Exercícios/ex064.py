numeros = cont = soma = 0
while numeros != 999:
    numeros = int(input("Digite um número inteiro [999 para parar]: "))
    if numeros != 999:
        soma += numeros
        cont += 1
print(f"Voce digitou {cont} números! E a soma de todos eles é {soma}!")
