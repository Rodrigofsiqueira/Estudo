frase = str(input("Digite uma frase: ")).upper().strip()

print('A letra "A" apareceu {} vezes na frase'.format(frase.count("A")))
print('Apareceu na primeira vez na posição {}'.format(frase.find("A")+1))
print('E sua última aparição foi na posição {}'.format(frase.rfind("A")+1))
