from random import randint 
from time import sleep
print(20*'-=-', '\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n', 20*'-=-')
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
c = randint(0, 5)
if c == n:
    print('Parabéns! você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(c, n))
