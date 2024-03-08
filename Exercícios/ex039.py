from datetime import date 

ano = int(input("Em que ano voce nasceu? "))
idade = date.today().year - ano

if idade < 18:
    print(f"\033[33mFaltam {18 - idade} anos para voce se alistar ao serviço militar!\033[m")
elif idade == 18:
    print(f"\033[32mPARABÉNS! Está na hora de voce fazer o seu ALISTAMENTO ao serviço militar!\033[m")
elif idade > 18:
    print(f"\033[31mOpa... Voce deveria ter feito seu alistamento a \033[33m{idade - 18}\033[31m anos atras.\033[m")
