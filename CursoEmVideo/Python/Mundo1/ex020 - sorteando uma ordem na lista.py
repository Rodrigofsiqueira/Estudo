import random
from random import shuffle

a1 = input("Nome do primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1, a2, a3, a4]
shuffle(lista)

print("O primeiro aluno será... {} \n"
      "O segundo será... {} \n"
      "O terceiro será... {} \n"
      "O quarto será... {}".format(lista[0], lista[1], lista[2], lista[3]))
