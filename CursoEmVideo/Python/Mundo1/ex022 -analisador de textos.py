nome = str(input("Digite um nome completo: "))

print(nome.upper())
print(nome.lower())

letras = len(nome) - nome.count(" ")
print("Seu nome completo tem um total de {} letras".format(letras))

primeiro = nome.split()
print("E só o primeiro nome tem {} letras.".format(len(primeiro[0])))
