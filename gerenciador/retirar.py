from tkinter import *
import os
import nameArq

def retirarPro():
    janela4 = Tk()
    janela4.title("Retirar")
    janela4.geometry("370x170")
    janela4.configure(background="#001")
    janela4.wm_resizable(width=False, height=False)
    namePro = Label(janela4, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    namePro.place(x=10,y=10)
    name = Entry(janela4)
    name.place(x=10,y=35, width=300, height=20)
    amountPro = Label(janela4, text='Quantidade', background="#001",foreground="#dde", anchor=W)
    amountPro.place(x=10,y=60)
    amount = Entry(janela4)
    amount.place(x=10,y=85,width=300,height=20)
    def retirar():
        if os.path.exists(f"produtos/{nameArq.nomeArquivoTratado(name.get())}"):
            with open(f"produtos/{nameArq.nomeArquivoTratado(name.get())}", 'r') as arquivo1:
                arquivo = arquivo1.read()
            if amount.get().isdigit():
                total = int(arquivo) - int(amount.get())
                if total >= 0:
                    with open(f"produtos/{nameArq.nomeArquivoTratado(name.get())}", 'w') as digit:
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