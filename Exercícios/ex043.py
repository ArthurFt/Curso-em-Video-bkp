peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print("Voce está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25: #se o peso estiver entre 18.5 e 25:
    print("PARABÉNS, voce está  na faixa de PESO IDEAL")
elif 25 <= imc < 30:
    print("Voce está em SOBREPESO")
elif 30 <= imc < 40:
    print("Voce está em OBESIDADE!")
elif imc >= 40:
    print("Voce está em OBESIDADE MÓRBIDA, cuidado!")
