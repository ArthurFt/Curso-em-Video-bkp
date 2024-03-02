'''
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
#Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")
'''
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

lista = [n1, n2, n3]
lista.sort() #O método .sort() ordena os números da lista em ordem crescente, tornando o programa mais compacto
print(f"O maior número é {lista[2]} e o menor é {lista[0]}")
