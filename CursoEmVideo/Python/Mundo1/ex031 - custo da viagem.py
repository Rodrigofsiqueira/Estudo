d = int(input("Digite em Km, a distância da viagem: "))

if d <= 200:
    v = d * 0.5
else:
    v = d * 0.45

print("O valor que deve ser pago, em sua passagem de ônibus, é de R${:.2f}".format(v))
