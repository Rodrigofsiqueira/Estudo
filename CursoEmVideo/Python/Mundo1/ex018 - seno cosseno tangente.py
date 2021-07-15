from math import sin, cos, tan, radians

angulo = float(input("Digite o valor de um ângulo: "))

seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print("Ângulo de {}° \n"
      "Seno {:.2f} \n"
      "Cosseno {:.2f} \n"
      "Tangente {:.2f}"
      .format(angulo, seno, coss, tang))
