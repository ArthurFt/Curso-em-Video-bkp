from datetime import date 
ano = int(input("Em que ano voce nasceu? "))
idade = date.today().year - ano
print(f"Quem nasceu em {ano} tem {idade} anos em {date.today().year}.")

if idade < 18:
    print(f"\033[33mFaltam {18 - idade} anos para voce se alistar ao serviço militar!\nSeu alistamento será em {date.today().year + (18 - idade)} \033[m")
elif idade == 18:
    print(f"\033[32mPARABÉNS! Está na hora de voce fazer o seu ALISTAMENTO ao serviço militar!\033[m")
elif idade > 18:
    print(f"\033[31mOpa... Voce deveria ter feito seu alistamento a \033[33m{idade - 18}\033[31m anos atras.\nSeu alistamento foi em {date.today().year - (idade - 18  )} \033[m")
