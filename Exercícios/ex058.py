import random
n = random.randint(0, 10)
acerto = False
tentativas = 0
print("-=-" * 15)
print("Pensando em um número de 0 a 10...")
print("-=-" * 15)
while not acerto:
    chute = int(input("Qual número entre 0 e 10 eu pensei? "))
    tentativas += 1
    if chute == n:
        print(f"Parabéns, voce acertou! O número que pensei era {n}.")
        acerto = True
    else:
        if chute < n:
            print("Mais... Try again!")
        elif chute > n:
            print("Menos... Try again!")
print(f"Voce precisou de {tentativas} tentativas para acertar. PARABÉNS!")
