real = float(input("Quanto dinheiro voce tem na carteira? R$"))
dolar = real / 4.94
euro = real / 5.33
iene = real / 0.034

print(f"Com R${real:.2f} voce pode comprar US${dolar:.2f}, €{euro:.2f} e ¥{iene:.2f}")
