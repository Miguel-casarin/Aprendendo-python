import math
print('calculando seno,cosseno e trangente de um ângulo')
v1=float(input('digite o ângulo:'))
v2=math.sin(v1)
v3=math.cos(v1)
v4=math.tan(v1)
print('o ângulo {} tem \n seno {:.2f} \n cosseno {:.2f} \n tangente {:.2f}'.format(v1, v2, v3, v4))