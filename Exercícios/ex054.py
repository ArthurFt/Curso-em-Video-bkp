from datetime import date

totmaior= 0
totmenor = 0
for c in range(1, 8):
    ano = int(input(f"Em que ano a {c} pessoa nasceu? "))
    idade = date.today().year - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"{totmaior} pessoas já atingiram a maioridade")
print(f"E {totmenor} pessoas não já atingiram a maioridade")
