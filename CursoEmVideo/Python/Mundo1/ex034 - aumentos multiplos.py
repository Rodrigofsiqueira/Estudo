salario = float(input("Digite o valor do salário: "))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
    
print("Seu novo salário é de {:.2f}".format(aumento))
