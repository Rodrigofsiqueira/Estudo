n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if n3 > maior:
    maior = n3

if n3 < menor:
    menor = n3

print("O maior é {}".format(maior))
print("O menor é {}".format(menor))
