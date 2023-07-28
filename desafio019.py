import random

print('sorteio de alunos')
v1=input('qual o nome do primeiro aluno?')
v2=input('qual o nome do segundo aluno?')
v3=input('qual o nome do terceiro aluno?')
v4=input('qual o nome do quarto aluno?')
list=[v1, v2, v3, v4]
x=random.choice(list)
print('O ESCOLIDO FOI {:>4}'.format(x))