dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
distancia = float(input('Digite quantos Km foram percorridos com o carro alugado: '))

valor = (dias * 60) + (distancia * 0.15)

print('Por {} dias de aluguel e {}Km rodados /nDeve ser pago um total de: R$  {:.2f}'.format(dias, distancia, valor))
