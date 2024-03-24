frase = str(input("Digite uma frase: ")).strip().upper()  # solução sem o for
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um PALÍNDROMO!")
else:
    print("A frase digitada não é um palíndromo!")

"""
frase = str(input("Digite uma frase: ")).strip().upper()  # solução com o for
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um PALÍNDROMO!")
else:
    print("A frase digitada não é um palíndromo!")
"""
