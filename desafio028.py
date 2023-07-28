import random

print('adivinhe o múmero que o computador escolheu')
lista=['0','1','2','3','4','5']
print('escolha um número de 0 à 5')
nesc=input('qual número o computador escolheu?')
p=random.choice(lista)

if nesc == p:
    print('{} vc acertou'.format(p))
else:
    print('errou, o número e {}'.format(p))

