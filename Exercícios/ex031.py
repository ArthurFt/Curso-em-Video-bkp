km = float(input("Sua viagem terá quantos kilometros? "))

if km <= 200:
    print(f"Sua passagem custará R${km * 0.50:.2f}")
else:
    print(f"Sua passagem custará R${km * 0.45:.2f}")
