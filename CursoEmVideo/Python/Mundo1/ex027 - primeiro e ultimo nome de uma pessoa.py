nome = str(input("Digite um nome completo: ")).title().split()

print("Seu primeiro nome é {} e seu último nome é {}".format(nome[0], nome[len(nome)-1]))
