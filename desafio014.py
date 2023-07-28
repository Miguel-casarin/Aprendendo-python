print('conversor de graus °c para °f e k')
tc=float(input('digite sua temp em °c:'))
op1=tc*180+3200
op2=op1/100
op3=(op2-32)*5/9
op4=op3+273
print('a temperatura {:.2f} °c \n convertida em °f fica {:.2f} \n em k fica {:.2f}'.format(tc, op2, op4))