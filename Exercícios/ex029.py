velo = float(input("Qual é a velocidade atual do carro? "))
if velo > 80:
    print("\033[31mMULTADO! Voce excedeu o limite de velocidade que é de 80Km/h")
    print(f"Voce deve pagar uma multa de \033[33mR${(velo-80) * 7:.2f}")
print("\033[32mTenha um bom dia! Dirija com segurança!\033[m")
