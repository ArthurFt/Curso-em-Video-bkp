list = []

for c in range(0, 5):
    peso = float(input("Digite um peso: (Kg) "))
    list.append(peso)
list.sort()
print(f"O maior peso digitado foi {list[4]}Kg e o menor foi {list[0]}Kg")
