a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a>=b+c or b>=c+a or c>a+b:
    print('Não consegue formar um triangulo!')
else:
    print('Consegue formar um triangulo!')
