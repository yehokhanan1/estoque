from tkinter import *
import os

janela = Tk()
janela.title("Estoque")
janela.geometry("280x300")
janela.configure(background="#001")
janela.wm_resizable(width=False, height=False)

def nomeArquivoTratado(nomeArquivo):
    return nomeArquivo.replace(" ", "").lower() + '.txt'

def adicionarPro():
    janela1 = Tk()
    janela1.title("Adicionar")
    janela1.geometry("320x170")
    janela1.configure(background="#001")
    namePro = Label(janela1, text='Nome do produto', background="#001",foreground="#dde", anchor=W)
    namePro.place(x=10,y=10)
    name = Entry(janela1)
    name.place(x=10,y=35,width=300,height=20)
    amountPro = Label(janela1, text='Quantidade', background="#001",foreground="#dde", anchor=W)
    amountPro.place(x=10,y=60)
    amount = Entry(janela1)
    amount.place(x=10,y=85,width=300,height=20)  
    def adicionar():
        if os.path.exists(f"produtos/{nomeArquivoTratado(name.get())}"):
            fail1 = Label(janela1, text="ERRO: Produto em estoque", background='red',foreground='#dde')
            fail1.place(x=10,y=140, width=200)
        else:
            if amount.get().isdigit():
                with open(f"produtos/{nomeArquivoTratado(name.get())}", 'w') as digit:
                    digit.write(amount.get())
                sucess = Label(janela1, text="Produto adicionado com sucesso!", background='green',foreground='#dde')
                sucess.place(x=10,y=140, width=200)
            else:
                fail = Label(janela1, text="ERRO: Digite apenas numeros inteiros", background='red',foreground='#dde')
                fail.place(x=10,y=140, width=200)
    adicionar1 = Button(janela1, text="Adicionar", background='#003', foreground="#dde", command=adicionar)
    adicionar1.place(x=10,y=110, width=100, height=25)

def verificarPro():
    janela2 = Tk()
    janela2.title("Verificar")
    janela2.geometry("320x120")
    janela2.configure(background="#001")
    verificarPro = Label(janela2, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    verificarPro.place(x=10,y=10)
    verificar = Entry(janela2)
    verificar.place(x=10,y=35, width=300, height=20)
    def verification():
        if os.path.exists(f"produtos/{nomeArquivoTratado(verificar.get())}"):
            with open(f"produtos/{nomeArquivoTratado(verificar.get())}", 'r') as arquivo1:
                arquivo = arquivo1.read()
                sucess = Label(janela2, text="Produto encontrado, " + arquivo + " em estoque.", background='green', foreground='#dde')
                sucess.place(x=10,y=95, width=250, height=20)
        else:
            fail = Label(janela2, text="Produto não encontrado. Tente novamente", background='red', foreground='#dde')
            fail.place(x=10,y=95, width=250, height=20)
    verificar2 = Button(janela2, text="Verificar", background="#003", foreground="#dde", command=verification)
    verificar2.place(x=10,y=60, width=100, height=25)

def addProduto():
    janela3 = Tk()
    janela3.title("Adicionar")
    janela3.geometry("370x170")
    janela3.configure(background="#001")
    namePro = Label(janela3, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    namePro.place(x=10,y=10)
    name = Entry(janela3)
    name.place(x=10,y=35, width=300, height=20)
    amountPro = Label(janela3, text='Quantidade', background="#001",foreground="#dde", anchor=W)
    amountPro.place(x=10,y=60)
    amount = Entry(janela3)
    amount.place(x=10,y=85,width=300,height=20)
    def produtoAdd():
        if os.path.exists(f"produtos/{nomeArquivoTratado(name.get())}"):
            with open(f"produtos/{nomeArquivoTratado(name.get())}", 'r') as arquivo1:
                arquivo = arquivo1.read()
            if amount.get().isdigit():
                total = int(arquivo) + int(amount.get())
                with open(f"produtos/{nomeArquivoTratado(name.get())}", 'w') as digit:
                    digit.write(str(total))
                sucess = Label(janela3, text="Quantidade adicionada com sucesso, a nova quantidade é " + str(total), background='green',foreground='#dde')
                sucess.place(x=10,y=140, width=350, height=20)
            else:
                fail = Label(janela3, text="Digite apenas numero inteiros. Tente novamente", background='red', foreground='#dde')
                fail.place(x=10,y=140, width=350, height=20)
        else:
            fail = Label(janela3, text="Produto não encontrado. Tente novamente", background='red', foreground='#dde')
            fail.place(x=10,y=140, width=350, height=20) 
    adicionar1 = Button(janela3, text="Adicionar", background='#003', foreground="#dde", command=produtoAdd)
    adicionar1.place(x=10,y=110, width=100, height=25)

def retirarPro():
    janela4 = Tk()
    janela4.title("Retirar")
    janela4.geometry("370x170")
    janela4.configure(background="#001")
    namePro = Label(janela4, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    namePro.place(x=10,y=10)
    name = Entry(janela4)
    name.place(x=10,y=35, width=300, height=20)
    amountPro = Label(janela4, text='Quantidade', background="#001",foreground="#dde", anchor=W)
    amountPro.place(x=10,y=60)
    amount = Entry(janela4)
    amount.place(x=10,y=85,width=300,height=20)
    def retirar():
        if os.path.exists(f"produtos/{nomeArquivoTratado(name.get())}"):
            with open(f"produtos/{nomeArquivoTratado(name.get())}", 'r') as arquivo1:
                arquivo = arquivo1.read()
            if amount.get().isdigit():
                total = int(arquivo) - int(amount.get())
                if total >= 0:
                    with open(f"produtos/{nomeArquivoTratado(name.get())}", 'w') as digit:
                        digit.write(str(total))
                    sucess = Label(janela4, text="Quantidade retirada com sucesso, a nova quantidade é " + str(total), background='green',foreground='#dde')
                    sucess.place(x=10,y=140, width=350, height=20)
                else:
                    fail = Label(janela4, text="ERRO: Retirada bloqueada. Estoque menor que 0 não permitido.", background='red', foreground='#dde')
                    fail.place(x=10,y=140, width=350, height=20)
            else:
                fail = Label(janela4, text="Digite apenas numero inteiros. Tente novamente", background='red', foreground='#dde')
                fail.place(x=10,y=140, width=350, height=20)
        else:
            fail = Label(janela4, text="Produto não encontrado. Tente novamente", background='red', foreground='#dde')
            fail.place(x=10,y=140, width=350, height=20) 
    retirar1 = Button(janela4, text="Retirar", background='#003', foreground="#dde", command=retirar)
    retirar1.place(x=10,y=110, width=100, height=25)   

adProduto = Button(janela, text="Adicionar novo produto ", background="#003", foreground="#dde",command=adicionarPro).place(x=15,y=30, width=250, height=25)

verProduto = Button(janela, text="Verficar produtos ", background="#003", foreground="#dde", command=verificarPro).place(x=15, y=70, width=250, height=25)

addProdutos = Button(janela, text="Adicionar produto existente", background="#003", foreground="#dde", command=addProduto).place(x=15, y=110, width=250, height=25)

retirarPro = Button(janela, text="Retirar produto existente", background="#003", foreground="#dde", command=retirarPro).place(x=15, y=150, width=250, height=25)

janela.mainloop()