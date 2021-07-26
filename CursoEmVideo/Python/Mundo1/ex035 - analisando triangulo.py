a = float(input("Digite o tamanho de um lado de um triangulo: "))
b = float(input("Digite o valor de um segundo lado do triangulo: "))
c = float(input("Digite o valor do terceiro lado do triangulo: "))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print("Pode ser um triangulo")
else:
    print("Não pode ser um triangulo")
