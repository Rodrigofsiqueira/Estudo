from math import hypot
catAdj = float(input("Digite o valor do cateto adjacente: "))
catOpos = float(input("Digite o valor do cateto oposto: "))

hipotenusa = hypot(catAdj, catOpos)

print("Com o cateto adjacente valendo {} e o cateto oposto valendo {}".format(catAdj, catOpos))
print("O valor da hipotenusa é de {:.2f}".format(hipotenusa))
