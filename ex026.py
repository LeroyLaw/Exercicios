f = input('Digite uma frase: ').strip().lower()
print('A letra A aparece {} vezes na frase!'.format(f.count('a')))
print('A primeira vez que a letra A aparece é na posição {}!'.format(f.find('a')+1))
print('A ultima vez que a letra A aparece é na posição {}!'.format(f.rfind('a')+1))
