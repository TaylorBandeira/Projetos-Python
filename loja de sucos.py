#loja de sucos

pedido = "s"
total = 0

while pedido == "s" :
    sabor = input('Digite o sabor do seu suco: ')
    tamanho = input('Digite o tamanho do seu suco (P,M,G): ')

    if tamanho == 'P' :
        preço = 5

    elif tamanho == "M" :
        preço = 7

    else :
        preço = 10

    total = total + preço

    print('Valor do suco: ', preço)
    print('Valor ate agora: ', total)

    pedido = input('Deseja comprar mais? (s/n): ')

    if pedido == 'n':
        print('Valor a pagar: ',total, 'reais')

