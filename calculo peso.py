print('calculador de sob peso 2000\n')

sexo=str(input('Informe seu sexo:'))
altura=float(input('qual sua altura:'))
peso=float(input('qual seu peso'))

if sexo=='feminino':
    pesoidealmulher= ( 62.1 * altura) - 44.7
    variacaomulher= (pesoidealmulher * ( 8/100 )) + pesoidealmulher
    if peso <= variacaomulher:
        print('vc esta dento do peso')
    else:
        sobpesomulher= peso - variacaomulher
        print('vc esta com sob peso de {}\n'.format(sobpesomulher))

else:
    academia=str(input('vc e maronba?'))
    if academia =='sim':
        print('foda-se\n')

    else:
     pesoidealhomem= (62.1 * altura) - 58
     variacaohomem= (pesoidealhomem * (8/100)) + pesoidealhomem
     if peso <= variacaohomem:
        print('vc ta dentro do peso')
     else:
        sobpesohomem=peso - variacaohomem
        print('vc esta com sob peso de {}\n'.format(sobpesohomem))


