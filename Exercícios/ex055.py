list = []

for c in range(1, 6):
    peso = float(input(f"Peso da {c}ª pessoa: (Kg) "))
    list.append(peso)
list.sort()
print(f"O maior peso digitado foi {list[4]}Kg e o menor foi {list[0]}Kg")

'''guanabara version:
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f"Peso da {p}ª pessoa: "))
    if p == 1:
        maior == peso
        menor == peso
    else:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
'''
