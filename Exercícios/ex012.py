preço = float(input("Qual o preço do produto? R$"))
novo = preço - (preço * 5 / 100)

print(f"O produto que custava R${preço:.2f}, com desconto de 5% custará R${novo:.2f}")
