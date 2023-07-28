print('1 - Cadastrar Empresa\n2 - Cadastrar Usuário\n3 - Registrar Compra de um Usuário\n4 - Mostrar Saldo de um Usuário\n5 - Resgatar Saldo de um Usuário\n6 - Excluir Empresa\n0 - Sair')

valorinicialsaldo=0
saldos=[]
usuarios=[]
empresas=['ALB','MM','CZB']
descontos=[10,8,5]

menu=int(input('opção menu:'))
while menu!=0:

 if menu == 1:
    strart=input('quer iniciar cadastros de empresas:').upper()
   
    while strart == 'SIM':
     empresa=input('empresa:').upper()
     empresas.append(empresa)
     descont=int(input('desconto:'))
     descontos.append(descont)
     strart=input('quer cadastrar empresas:').upper()
    menu=int(input('opção menu:'))
    print(empresas)
    
 elif menu ==2:
    strart2=input('quer iniciar cadastros de usuarios:').upper()
    
    while strart2 == 'SIM':
     cliente=input('client:').upper()
     usuarios.append(cliente)
     saldos.append(valorinicialsaldo)
     strart2=input('quer iniciar cadastros de usuarios:').upper()
    menu=int(input('opção menu:')) 
    print(usuarios)

 elif menu == 3:
   start3=input('quer registar as compras:').upper()
   
   while start3 == 'SIM':
    idusuario=input('cliente:').upper()
    x=usuarios.index(idusuario)
    valordacompra=int(input('valor compra:'))
    posempresa=input('local:').upper()
    pos=empresas.index(posempresa)
    valorcomdesc = valordacompra*(descontos[pos]/100)
    saldos.insert(x,valorcomdesc)
    start3=input('quer registar as compras:').upper()
   menu=int(input('opções menu:'))

 elif menu == 4:
        start4 = input('Quer conferir o saldo:').upper()
        
        while start4 == 'SIM':
            alusuario = input('Cliente: ').upper()
            
            if alusuario in usuarios:
                pos = usuarios.index(alusuario)
                valorsaldo = saldos[pos]
                print('Saldo:', valorsaldo)
            else:
                print('Usuário não cadastrado')
            
            start4 = input('Quer conferir o saldo de outro usuário: ').upper()
        
        menu = int(input('Opção do menu: '))

 elif menu ==5:
   start5=input('quer resgatar saldo:').upper()

   while start5 == 'SIM':
     pesquisa=input('client:').upper()

     if pesquisa in usuarios:
       pospesquisa=usuarios.index(pesquisa)
       valorsaldo2=saldos[pospesquisa]
       print('saldo de {} resgatado'.format(valorsaldo2))
     else:
      print('usuario não cadastrado')
     start5=input('quer resgatar saldo:')
   menu=int(input('opções menu:'))

 elif menu == 6:
    empresaexcluida=input('qual empresa excluir:').upper()
    
    if empresaexcluida in empresas:
        empresas.remove(empresaexcluida)
        
        print('Empresa', empresaexcluida, 'foi excluída com sucesso.')
    else:
        print('Empresa não encontrada.')

    menu = int(input('Opção do menu: '))

print('empresas: {}\ndescontos:{}\nusuarios:{}'.format(empresas,descontos,usuarios))
   
 
 