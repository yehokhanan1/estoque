preto = []
pretoCafe = []
verde = []
print("--------------------------------------------------------------------------------------")
print("\t\t\t\tBem Vindo ao Estoque KASSAI")
print("--------------------------------------------------------------------------------------")
class estoqueKassai():
# verificação se tem algo no txt se ja tiver adicionar na lista
    def __init__(self):
        with open('relogio_preto.txt', 'r') as arquivo1:
            arquivo = arquivo1.read()
            if arquivo == '':
                relogio_black = input("Informe a quantidade de Relogio preto em estoque\nR: ")
                if relogio_black.isdigit():
                    preto.append(relogio_black)
                    with open('relogio_preto.txt', 'w') as digit:
                        digit.write(str(preto[-1]))
                    print('Estoque adicionado com Sucesso!')
                else:
                    with open('relogio_preto.txt', 'w') as digit:
                        digit.write('')
                    print('ERRO: Digite apenas numeros inteiros. Refaça novamente.')
                    estoqueKassai()
            else:
                with open('relogio_preto.txt', 'r') as arquivo1:
                    arquivo = arquivo1.read()
                    preto.append(arquivo)

        with open('relogio_preto_cafe.txt', 'r') as arquivo1:
            arquivo = arquivo1.read()
            if arquivo == '':
                relogio_black_coffe = input("Informe a quantidade de Relogio preto cafe em estoque\nR: ")
                if relogio_black_coffe.isdigit():
                    pretoCafe.append(relogio_black_coffe)
                    with open('relogio_preto_cafe.txt', 'w') as digit:
                        digit.write(str(pretoCafe[-1]))
                    print('Estoque adicionado com Sucesso!')
                else:
                    with open('relogio_preto_cafe.txt', 'w') as digit:
                        digit.write('')
                    print('ERRO: Digite apenas numeros inteiros. Refaça novamente.')
                    estoqueKassai()
            else:
                with open('relogio_preto_cafe.txt', 'r') as arquivo1:
                    arquivo = arquivo1.read()
                    pretoCafe.append(arquivo)

        with open('relogio_verde.txt', 'r') as arquivo1:
            arquivo = arquivo1.read()
            if arquivo == '':
                relogio_green = input("Informe a quantidade de Relogio verde em estoque\nR: ")
                if relogio_green.isdigit():
                    verde.append(relogio_green)
                    with open('relogio_verde.txt', 'w') as digit:
                        digit.write(str(verde[-1]))
                    print('Estoque adicionado com Sucesso!')
                else:
                    with open('relogio_verde.txt', 'w') as digit:
                        digit.write('')
                    print('ERRO: Digite apenas numeros inteiros. Refaça novamente.')
                    estoqueKassai()
            else:
                with open('relogio_verde.txt', 'r') as arquivo1:
                    arquivo = arquivo1.read()
                    verde.append(arquivo)
# escrever no arquivo txt         
    def preto(self,preto1):
        with open('relogio_preto.txt', 'w') as digit:
            digit.write(str(preto1))
    def verde(self,verde1):
        with open('relogio_verde.txt', 'w') as digit:
            digit.write(str(verde1))
    def pretoCafe(self,pretoCafe1):
        with open('relogio_preto_cafe.txt', 'w') as digit:
            digit.write(str(pretoCafe1))
    def menu(self):
        menuBack = str(input("Deseja volta para o menu? se sim digite 'menu'. Deseja sair digite 'sair'\nR: "))
        if menuBack == 'menu':
            start.estoque()
        elif menuBack == 'sair':
            exit()
        else:
            print("\n\t\tOpção invalida! Digite novamente\n")
            start.menu()
# alternativas estoque            
    def estoque(self):
        while True:
            menu = input("O que deseja fazer?\n\tDigite 1 = Verificar estoque\n\tDigite 2 = Adicionar estoque\n\tDigite 3 = Retirar estoque\n\tDigite 'sair' para fechar o programa\nR: ")
# verificar estoque            
            if menu == '1':
                print("--------------------------------------------------------------------------------------")
                total = int(preto[-1]) + int(verde[-1]) + int(pretoCafe[-1])
                print("\tRelogios preto", preto[-1],"\n\tRelogios preto cafe", pretoCafe[-1],"\n\tRelogios verde", verde[-1],"\n\tTotal de itens =", total)
                start.menu()
# adicionar estoque
            elif menu == '2':
                print("--------------------------------------------------------------------------------------")
                add_estoque = input("Qual relogio vai adicionar?\n\tDigite 1 = relogio preto\n\tDigite 2 = relogio preto cafe\n\tDigite 3 = relogio verde\nR: ")
                if add_estoque == '1':
                    adicionar = int(input("Qual quantidade vai adicionar?\nR: "))
                    preto1 = int(preto[-1]) + adicionar
                    preto.append(preto1)
                    start.preto(preto1)
                    print("\tEstoque alterado com sucesso\n\tA nova quantidade de relogio preto é", preto[-1])
                    start.menu()

                elif add_estoque == '2':
                    adicionar = int(input("Qual quantidade vai adicionar?\nR: "))
                    pretoCafe1 = int(pretoCafe[-1]) + adicionar
                    pretoCafe.append(pretoCafe1)
                    start.pretoCafe(pretoCafe1)
                    print("\tEstoque alterado com sucesso\n\tA nova quantidade de relogio preto cafe é", pretoCafe[-1])
                    start.menu()

                elif add_estoque == '3':
                    adicionar = int(input("Qual quantidade vai adicionar?\nR: "))
                    verde1 = int(verde[-1]) + adicionar
                    verde.append(verde1)
                    start.verde(verde1)
                    print("\tEstoque alterado com sucesso\n\tA nova quantidade de relogio verde é", verde[-1])
                    start.menu()
                else:
                    print("\n\t\tOpção invalida! Volte ao menu\n")
                    start.estoque()
# retirada estoque
            elif menu == '3':
                print("--------------------------------------------------------------------------------------")
                baixa_estoque = input("Qual relogio vai retirar?\n\tDigite 1 = relogio preto\n\tDigite 2 = relogio preto cafe\n\tDigite 3 = relogio verde\nR: ")
                if baixa_estoque == '1':
                    retirada = int(input("Qual quantidade vai retirar?\nR: "))
                    preto1 = int(preto[-1]) - retirada
                    preto.append(preto1)
                    start.preto(preto1)
                    print("\tEstoque alterado com sucesso\n\tA nova quantidade de relogio preto é", preto[-1])
                    start.menu()

                elif baixa_estoque == '2':
                    retirada = int(input("Qual quantidade vai retirar?\nR: "))
                    pretoCafe1 = int(pretoCafe[-1]) - retirada
                    pretoCafe.append(pretoCafe1)
                    start.pretoCafe(pretoCafe1)
                    print("\tEstoque alterado com sucesso\n\tA nova quantidade de relogio preto cafe é", pretoCafe[-1])
                    start.menu()

                elif baixa_estoque == '3':
                    retirada = int(input("Qual quantidade vai retirar?\nR: "))
                    verde1 = int(verde[-1]) - retirada
                    verde.append(verde1)
                    start.verde(verde1)
                    print("\tEstoque alterado com sucesso\n\tA nova quantidade de relogio verde é", verde[-1])
                    start.menu()
                else:
                    print("\n\t\tOpção invalida! Volte ao menu\n")
                    start.estoque()
            elif menu == 'sair':
                exit()
            else:
                print("\n\t\tOpção invalida! Volte ao menu\n")
                start.estoque()
start = estoqueKassai()
start.estoque()
