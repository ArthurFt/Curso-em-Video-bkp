"""Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago = (dias * 60) + (km * 0.15)
print(f"O total a ser pago é de R${pago:.2f}")
