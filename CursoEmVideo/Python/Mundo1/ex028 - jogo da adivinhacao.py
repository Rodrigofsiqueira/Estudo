from random import randint

print("Tente acertar o número entre 1 e 5.")

r = randint(1, 5)

n = int(input("Digite um número: "))

if n == r:
    print("Parabéns!! Você acertou!")
    print("Você escolheu o número {} assim como eu".format(r))
else:
    print("Que pena, você errou.")
    print("Você escolheu o número {} e eu estava pensando no {}.".format(n, r))
