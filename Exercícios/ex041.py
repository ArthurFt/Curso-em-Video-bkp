from datetime import date
ano = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = ano - nascimento

print(f"O atleta tem {idade} anos.")
if idade <=9:
    print("Classificado: MIRIM")
elif idade <=14:
    print("Classificado: INFANTIL")
elif idade <=19:
    print("Classificado: JUNIOR")
elif idade <=25:
    print("Classificado: SENIOR")
else:
    print("Classificado: MASTER")   
