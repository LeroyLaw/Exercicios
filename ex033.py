a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#valor menor
if b < a and b < c:
    m = b
if c < a and c < b:
    m = c
#valor maior
mo = a
if b > a and b > c:
    mo = b
if c > a and c > b:
    mo = b
print('O menor valor foi {}!'.format(m))
print('O maior valor foi {}!'.format(mo))
