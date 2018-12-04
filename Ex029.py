v = int(input('Qual é a velocidade atual do seu carro? '))
if v <= 80:
    print('Bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h \nVocê deve pagar uma multa de R${}!'.format((v-80)*7))
