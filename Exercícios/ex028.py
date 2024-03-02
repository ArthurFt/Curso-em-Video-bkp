import random
n = random.randint(0, 5)

print("-=-" * 15)
print("Pensando em um número de 0 a 5...")
print("-=-" * 15)

chute = int(input("Qual número entre 0 e 5 eu pensei? "))
if chute == n:
    print(f"Parabéns, voce acertou! O número que pensei era {n}.")
else:
    print(f"Voce errou, o número era {n}! Tente novamente.")
