#n = int(input('Me diga um número qualquer: '))
#nr = n%2
#if nr == 0:
#    print('O número {} é PAR!'.format(n))
#else:
#    print('O número {} é IMPAR'.format(n))

n = int(input('Me diga um número qualquer: '))%2
print('O número é PAR!'if n==0 else 'O número é IMPAR')
