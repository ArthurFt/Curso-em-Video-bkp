from datetime import date

pessoas = 0
for c in range(0, 7):
    ano = int(input("Ano de nascimento: "))
    idade = date.today().year - ano
    if idade >= 21:
        pessoas += 1
print(f"{pessoas} pessoas já atingiram a maioridade")
