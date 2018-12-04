s = float(input('Quanto o funcionário recebia? R$'))
if s <= 1250:
    print('O funcionário passará a receber R${:.2f}!'.format(s+(s*15/100)))
else:
    print('O funcionário passará a receber R${:.2f}!'.format(s+(s*10/100)))
