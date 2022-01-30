#UI
print('***'*30)
print('CALCULADORA DE PAGAMENTOS - DIGITE O VALOR DAS SUAS COMPRAS ABAIXO: ')
print('***'*30)
valorProduto = float(input('Digite o valor das compras: '))

#Formas de pagamento
print('***'*30)
print('ESCOLHA A FORMA DE PAGAMENTO:\n [ 1 ] À VISTA, NO DINHEIRO OU CHEQUE \n [ 2 ] 2X NO CARTÃO \n [ 3 ] À VISTA NO '
      'CARTÃO \n [ 4 ] 3X OU ' 'MAIS NO CARTÃO ')
print('***'*30)
formaPgt = int(input('Digite o número da forma de pagamento: '))

#Condições
'''
1 = 10% DE DESCONTO 
2 = PREÇO NORMAL
3 = 5% DE DESCONTO
4 - 20% DE JUROS
'''

if formaPgt == 1:
    valorTotal = valorProduto - (valorProduto * 10 / 100)
    print('Sua compra de {} vai custar no final {:.2f}, com um desconto de 10%'.format(valorProduto, valorTotal))
    print('\n')
elif formaPgt == 2:
    valorTotal = valorProduto
    print('Sua compra de {}, vai custar no final {}'.format(valorProduto, valorTotal))
    print('\n')
elif formaPgt == 3:
    valorTotal = valorProduto - (valorProduto * 5 / 100)
    print('Sua compra de {}, vai custar no final {}, com um desconto de 5%'.format(valorProduto, valorTotal))
    print('\n')
else:
    parcelamento = int(input('Quantas parcelas? '))
    valorTotal = valorProduto + (valorProduto * 20 / 100)
    valorDividido = valorTotal / parcelamento
    print('Sua compra de {} vai ser parceladada em {}x de R${} COM JUROS '.format(valorProduto, parcelamento, valorDividido))
    print('Sua compra de {}, vai custar {} no final, com juros de 20%'.format(valorProduto, valorTotal))

#Output
print('***'*30)
print('CALCULADORA DE PAGAMENTO DESENVOLVIDA POR LUCAS RODRIGUES')
print('***'*30)
