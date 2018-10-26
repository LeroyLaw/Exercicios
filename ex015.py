a = float(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos Km foram rodados? '))
v = (a * 60) + (k * 0.15)
print('O total a pagar é de R${:.2f}'.format(v))