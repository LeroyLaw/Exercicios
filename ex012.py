p = float(input('Qual é o preço do produto? R$'))
pr = float(input('Qual é a % de desconto? '))
v = p - (p * pr / 100)
print('O produto custava R${:.2f}, na promoção com desconto de {:.2f}% vai custar R${:.2f}'.format(p, pr, v))