salar = float(input("Digite o salario de um funcionario: R$"))

if salar >= 1250:
    print(f"Com um aumento de 10%, ele irá passar a receber R${salar + (salar * 10 / 100):.2f}")
else:
    print(f"Com um aumento de 15%, ele irá passar a receber R${salar + (salar * 15 / 100):.2f}")
