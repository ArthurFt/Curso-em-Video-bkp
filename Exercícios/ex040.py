n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
média = (n1 + n2) / 2
print(f"Tirando {n1:.1f} e {n2:.1f}, a média é {média:.1f}")

if média < 5:
    print("O aluno \033[31mREPROVOU!\033[m")
#elif média >=5 and média < 7:
elif 7 > média >= 5:
    print("O aluno esta em \033[33mRECUPERAÇÃO.\033[m")
elif média >= 7:
    print("O aluno esta \033[32mAPROVADO\033[m")
