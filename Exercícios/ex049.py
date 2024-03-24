"""m = 0
n = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    m += 1
    print(f"{n} x {m:2} = {n*m}")
"""

num = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    print(f"{num} x {c:2} = {num*c}")
