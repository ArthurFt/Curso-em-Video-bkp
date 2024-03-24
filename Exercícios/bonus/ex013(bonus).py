escolha = int(input("Digite o número do que deseja: Desconto(1) ou Acréscimo(2)? "))

if escolha == 1:
    preço = float(input("Qual o preço do produto que você deseja aplicar o desconto? R$"))
    porcen = int(input("Qual a porcentagem do desconto? "))
    desconto = preço - (preço * porcen / 100)
    print(f"O preço que antes era R${preço:.2f}, com o desconto de {porcen}%, passou a custar R${desconto:.2f}.")

elif escolha == 2:
    preço = float(input("Qual o preço do produto que você deseja aplicar o acréscimo? R$"))
    porcen = int(input("Qual a porcentagem do acréscimo? "))
    acres = preço + (preço * porcen / 100)
    print(f"O preço que antes era R${preço:.2f}, com o ácrescimo de {porcen}%, passou a custar R${acres:.2f}.")

else:
    print("Por favor, insira um número válido (1 ou 2).")

