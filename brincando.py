from random import choice
print('\nOcorrerá um sorteio no dia 2 de Dezembro, sorteando um aumento de 20% sobre o funcionário Ganhador')
print(100*'=')
print('Preencha o pequeno formulário, para o sorteio acontecer')
f1 = input('Nome do funcionário: ')
r1 = float(input('Quanto recebe? R$'))
f2 = input('Nome do funcionário: ')
r2 = float(input('Quanto recebe? R$'))
f3 = input('Nome do funcionário: ')
r3 = float(input('Quanto Recebe? R$'))
f4 = input('Nome do funcionário: ')
r4 = float(input('Quanto Recebe? R$'))
r = choice([f1, f2, f3, f4])
if (r == f1):
    print('Parabéns {}, você foi o vencedor, recebia R${:.2f}, receberá a partir do dia 2, R${:.2f}'.format(f1, r1, r1+(r1*20/100)))
elif r == f2:
    print('Parabéns {}, você foi o vencedor, recebia R${:.2f}, receberá a partir do dia 2, R${:.2f}'.format(f2, r2, r2+(r2*20/100)))
elif r == f3:
    print('Parabéns {}, você foi o vencedor, recebia R${:.2f}, receberá a partir do dia 2, R${:.2f}'.format(f3, r3, r3+(r3*20/100)))
elif r == f4:
    print('Parabéns {}, você foi o vencedor, recebia R${:.2f}, receberá a partir do dia 2, R${:.2f}'.format(f4, r4, r4+(r4*20/100)))
