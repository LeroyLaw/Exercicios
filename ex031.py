d = float(input('Qual é a distância da sua viagem? '))
'''if d <= 200:
    print('O valor da sua passagem é R${}!'.format(d*0.5))
else:
    print('O valor da sua passagem é R${}!'.format(d*0.45))'''
p = d * 0.5 if d <= 200 else d *0.45
print('O valor da sua passagem é R${}!'.format(p))
