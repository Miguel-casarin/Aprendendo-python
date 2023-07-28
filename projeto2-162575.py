print('1 - Cadastrar Empresa')
print('2 - Cadastrar Usuário')
print('3 - Registrar Compra de um Usuário')
print('4 - Mostrar Saldo de um Usuário')
print('5 - Resgatar Saldo de um Usuário')
print('6 - Excluir Empresa')
print('0 - Sair')


menu=int(input(':'))

saldos=[]

if menu == 1:
    strart=input('quer iniciar cadastros:')

    usuarios=[]
    empresas=['ALB','MM','CZB']
    descontos=[10,8,5]

    while strart == 'sim':
    
     cliente=input('client:')
     empresa=input('empresa:')
     desconto=float(input('desconto:'))
     usuarios.append(cliente)
     empresas.append(empresa)
     descontos.append(desconto)
     strart=input('quer iniciar cadastros:')
    
if menu == 2: 
 local=input('local:')
 valorcompra=float(input('valor da compra:'))
 cliente=input('client:')

 if empresa in empresas:
  pos=empresas.index(empresa)
 cashback = valorcompra*(descontos[pos]/100)

 saldos.append(cashback)

 if cliente in usuarios:
    poscliente=usuarios.index(cliente)
    saidasaldo=saldos[poscliente]
print(saldos)
print(saidasaldo)