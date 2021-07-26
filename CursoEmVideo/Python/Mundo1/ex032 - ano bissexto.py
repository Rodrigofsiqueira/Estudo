a = int(input("Digite algum ano, para saber se ele é bissexto ou não: "))

if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
    print("O ano {} é bissexto".format(a))
else:
    print("O ano {} não é bissexto".format(a))
