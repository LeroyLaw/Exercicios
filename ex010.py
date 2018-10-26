r=float(input('Quanto dinheiro você tem? R$'))
d = r / 3.70
e = r / 4.20
i = r / 0.033
print('Com R${} você pode comprar US${:.2f} dólares!'.format(r, d))
print('Com R${} você pode comprar €{:.2f} euros'.format(r, e))
print('Com R${} você pode comprar ¥{:.2f} ienes'.format(r, i))