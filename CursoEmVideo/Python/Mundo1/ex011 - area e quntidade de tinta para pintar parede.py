altura = float(input("Informe a altura em metros de uma parede: "))
largura = float(input("Digite a largura: "))

area = altura * largura

print("A parede tem um total de {}m²".format(area))
print("E serão necessários {}l de tinta, para pinta-la".format(area / 2))
