v = float(input("Digite em Km/h velocidade em que o carro estava: "))

if v > 80:
    print("Você foi multado.")

    m = (v - 80) * 7
    print("Deve pagar uma multa no valor de R${:.2f}".format(m))
print("Dirija com cuidado!")