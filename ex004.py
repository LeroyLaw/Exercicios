c = input('Digite algo = ')
print('O tipo primitivo desse valor é:', type(c))
print('Só tem espaços?', c.isspace())
print('É um número?', c.isnumeric())
print('É alfabético?', c.isalpha())
print('É alfanúmerico?', c.isalnum())
print('Está Maiuscula?', c.isupper())
print('Está Menuscula?', c.islower())
print('Está captalizada?', c.istitle())