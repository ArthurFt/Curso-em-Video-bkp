from time import sleep

parar = 0
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Segundo valor: "))
while parar == 0: # ou posso criar a varivel "opzao" antes com o valor atribuido de 0, e fazer while opzao != 5:
    opzao = int(input(("""[ 1 ] Somar
[ 2 ] Multiplicar 
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Digite uma opção: """)))
    if opzao == 1:
        soma = v1 + v2
        print(f"A soma entre {v1} + {v2} é {soma}")
    elif opzao == 2:
        mult = v1 * v2
        print(f"O produto de {v1} x {v2} é {mult}")
    elif opzao == 3:
        if v1 > v2:
            print(f"Entre {v1} e {v2} o maior valor é {v1}")
        else:
            print(f"Entre {v1} e {v2} o maior valor é {v2}")
    elif opzao == 4:
        print("**Digite novos valores**")
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Segundo valor: "))
    elif opzao == 5:
        parar = 1
        print("Saindo...")
    else:
        print(f"A opção {opzao} é inválida. Tente novamente")
    print("==" * 20)
    sleep(2)
print("Fim do programa! Volte sempre!")
