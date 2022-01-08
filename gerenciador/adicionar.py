from tkinter import *
import os
import nameArq

def addProduto():
    janela3 = Tk()
    janela3.title("Adicionar")
    janela3.geometry("370x170")
    janela3.configure(background="#001")
    janela3.wm_resizable(width=False, height=False)
    namePro = Label(janela3, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    namePro.place(x=10,y=10)
    name = Entry(janela3)
    name.place(x=10,y=35, width=300, height=20)
    amountPro = Label(janela3, text='Quantidade', background="#001",foreground="#dde", anchor=W)
    amountPro.place(x=10,y=60)
    amount = Entry(janela3)
    amount.place(x=10,y=85,width=300,height=20)
    def produtoAdd():
        if os.path.exists(f"produtos/{nameArq.nomeArquivoTratado(name.get())}"):
            with open(f"produtos/{nameArq.nomeArquivoTratado(name.get())}", 'r') as arquivo1:
                arquivo = arquivo1.read()
            if amount.get().isdigit():
                total = int(arquivo) + int(amount.get())
                with open(f"produtos/{nameArq.nomeArquivoTratado(name.get())}", 'w') as digit:
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