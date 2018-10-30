from math import sin, cos, radians, tan
a = float(input('Digite o ângulo: '))
r = radians(a)
print ('O ângulo de {} tem o seno de {:.2f}'.format(a, sin(r)))
print ('O ângulo de {} tem o cosseno de {:.2f}'.format(a, cos(r)))
print ('O ângulo de {} tem o tangente de {:.2f}'.format(a, tan(r)))