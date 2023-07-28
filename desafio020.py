from random import shuffle

a=input('1° aluno:  ')
b=input('2° aluno:  ')
c=input('3° aluno:  ')
d=input('4° aluno:  ')

list=[a, b, c, d]
shuffle(list)
print('a ordem fica')
print(list)