a = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(a)))

print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalpha())
print('Está tudo em maiusculo?', a.isupper())
print('Está tudo em minusculo?', a.islower())
print('Está capitalizada? ', a.istitle())
