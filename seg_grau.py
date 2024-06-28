a = int(input('Digite seu a: '))
b = int(input('Digite seu b: '))
c = int(input('Digite seu c: '))

def b_elebado(b):
    quadrado_b = b ** 2
    return quadrado_b

def delta(a, quadrado, c):
    resultado_delta = quadrado - (4 * a * c)
    return resultado_delta 

def a_multi(a):
    multi = 2 * a
    return multi

def primeira_linha(b, raiz, a_multi):
    calculo = (-b + (raiz ** 0.5)) / a_multi
    return calculo

def segunda_linha(b, raiz, a_multi):
    calculo = (-b - (raiz ** 0.5)) / a_multi
    return calculo

quadrado = b_elebado(b)
raiz = delta(a, quadrado, c)
divisor = a_multi(a)

if raiz < 0 or raiz == 0:
    print('Sem raiz')

else:
    linha_1 = primeira_linha(b, raiz, divisor)
    print('Primeira linha:', linha_1)

    linha_2 = segunda_linha(b, raiz, divisor)
    print('Segunda linha:', linha_2)
