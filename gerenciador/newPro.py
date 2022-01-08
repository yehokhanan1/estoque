from tkinter import *
import os
import nameArq

def adicionarPro():
    janela1 = Tk()
    janela1.title("Adicionar")
    janela1.geometry("320x170")
    janela1.configure(background="#001")
    janela1.wm_resizable(width=False, height=False)
    namePro = Label(janela1, text='Nome do produto', background="#001",foreground="#dde", anchor=W)
    namePro.place(x=10,y=10)
    name = Entry(janela1)
    name.place(x=10,y=35,width=300,height=20)
    amountPro = Label(janela1, text='Quantidade', background="#001",foreground="#dde", anchor=W)
    amountPro.place(x=10,y=60)
    amount = Entry(janela1)
    amount.place(x=10,y=85,width=300,height=20)  
    def adicionar():
        if os.path.exists(f"produtos/{nameArq.nomeArquivoTratado(name.get())}"):
            fail1 = Label(janela1, text="ERRO: Produto em estoque", background='red',foreground='#dde')
            fail1.place(x=10,y=140, width=200)
        else:
            if amount.get().isdigit():
                with open(f"produtos/{nameArq.nomeArquivoTratado(name.get())}", 'w') as digit:
                    digit.write(amount.get())
                sucess = Label(janela1, text="Produto adicionado com sucesso!", background='green',foreground='#dde')
                sucess.place(x=10,y=140, width=200)
            else:
                fail = Label(janela1, text="ERRO: Digite apenas numeros inteiros", background='red',foreground='#dde')
                fail.place(x=10,y=140, width=200)
    adicionar1 = Button(janela1, text="Adicionar", background='#003', foreground="#dde", command=adicionar)
    adicionar1.place(x=10,y=110, width=100, height=25)