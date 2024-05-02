# Utilizando o [0], qualquer palavra que for digitada que possua 'F' ou 'M', será validada, farinha será registrada como Feminino.
sexo = str(input("Escreva seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MmFf": 
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")
