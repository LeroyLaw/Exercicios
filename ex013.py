s = float(input('Quanto o funcionário ganha? R$'))
v = s + (s * 15 /100) 
print('O funcionário que ganha R${}, com 15% de aumento, passará a receber R${:.2f}!'.format(s, v))