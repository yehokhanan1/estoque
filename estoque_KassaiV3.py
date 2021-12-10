import os

class estoque():
    def __init__(self):
        print("--------------------------------------------------------------------------------------")
        print("\t\t\t\tBem Vindo ao Estoque KASSAI")
        print("--------------------------------------------------------------------------------------")
    def verification(self):
        produto = input('Qual produto vai verificar?\nR: ')
        produtosTXT = produto.replace(" ", "").lower() + '.txt'
        if os.path.exists(produtosTXT):
            with open(produtosTXT, 'r') as arquivo1:
                arquivo = arquivo1.read()
                print('A quantidade em estoque de '+ produto + ' é '+ arquivo)
                start.menu()
        else:
            print('Produto não encontrado. Tente novamente')
            start.verification()
    def verificationT(self):
        produtos = []
        with open('produtos.txt', 'r') as arquivo1:
            arquivo = arquivo1.read()
            if arquivo == '':
                print('Não a produtos em estoque no momento. Volte ao menu')
                start.menu()
            else:
                with open('produtos.txt') as arquivo1:
                    for line in arquivo1:
                        produtos.append(line.split(','))
                print('\n'.join(map(str, sorted(produtos))))
                start.menu()

    def adicionarPro(self):
        add_produto = input('Qual nome do produto que vai adicionar ao estoque?\nR: ')
        arquivoTXT = add_produto.replace(" ", "").lower() + '.txt'
        quantidade = input('Qual quantidade de '+ add_produto+' vai adicionar?\nR: ')
        if quantidade.isdigit():
            with open(arquivoTXT, 'w') as digit:
                digit.write(quantidade)
            with open('produtos.txt', 'a') as digit:
                digit.write(add_produto + '\n')
            print('Produto adicionado com sucesso. Volte ao menu')
            start.menu()
        else:
            print('\t\tDigite apenas numeros inteiros. Tente novamente\n')
            start.adicionarPro()

    def addProduto(self):
        addEstoque = input('Qual produto vai adicionar?\nR: ')
        addEstoqueTXT = addEstoque.replace(' ', '').lower() + '.txt'
        if os.path.exists(addEstoqueTXT):
            with open (addEstoqueTXT, 'r') as arquivo1:
                arquivo = arquivo1.read()
            addEstoque1 = input('Qual quantidade vai adicionar?\nR: ')
            if addEstoque1.isdigit():
                total = int(arquivo) + int(addEstoque1)
                with open(addEstoqueTXT, 'w') as digit:
                    digit.write(str(total))
                print('Quantidade adicionada com sucesso, a nova quantidade é', total, '. Volte ao menu')
                start.menu()
            else:
                print('Digite apenas numeros inteiros. Tente novamente')
                start.addProduto()
        else:
            print('Produto não encontrado. Tente novamente')
            start.addProduto()

    def retirarProduto(self):
        retirarEstoque = input('Qual produto vai retirar?\nR: ')
        retirarEstoqueTXT = retirarEstoque.replace(' ', '').lower() + '.txt'
        if os.path.exists(retirarEstoqueTXT):
            with open (retirarEstoqueTXT, 'r') as arquivo1:
                arquivo = arquivo1.read()
            retirarEstoque1 = input('Qual quantidade vai retirar?\nR: ')
            if retirarEstoque1.isdigit():
                total = int(arquivo) - int(retirarEstoque1)
                with open(retirarEstoqueTXT, 'w') as digit:
                    digit.write(str(total))
                print('Quantidade adicionada com sucesso, a nova quantidade é', total, '. Volte ao menu')
                start.menu()
            else:
                print('Digite apenas numeros inteiros. Tente novamente')
                start.retirarProduto()
        else:
            print('Produto não encontrado. Tente novamente')
            start.retirarProduto()
    def menu(self):
        options = input('\nOpções do estoque:\n\tDigite 1 = adicionar um novo produto ao estoque\n\tDigite 2 = adicionar quantidade de produto existente\n\tDigite 3 = retirar quantidade de produto existente\n\tDigite 4 = Verificar produto no estoque\n\tDigite 5 = Verificar todo o estoque\n\tDigite "sair" para fechar o programa.\nR: ')
        if options == '1':
            start.adicionarPro()
        elif options == '2':
            start.addProduto()
        elif options == '3':
            start.retirarProduto()
        elif options == '4':
            start.verification()
        elif options == '5':
            start.verificationT()
        elif options == 'sair':
            exit()
        else:
            print('Opção invalidade. Tente novamente')
            start.menu()
start = estoque()
start.menu()