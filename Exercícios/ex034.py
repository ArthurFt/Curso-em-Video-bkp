salar = float(input("Digite o seu salário: R$"))

if salar > 1250:
    print(f"Com um aumento de 10%, voce irá passar a receber R${salar + (salar * 10 / 100)}")
else:
    print(f"Com um aumento de 15%, voce irá passar a receber R${salar + (salar * 15 / 100)}")
