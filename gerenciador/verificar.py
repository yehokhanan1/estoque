from tkinter import *
import os
import nameArq

def verificarPro():
    janela2 = Tk()
    janela2.title("Verificar")
    janela2.geometry("320x120")
    janela2.configure(background="#001")
    janela2.wm_resizable(width=False, height=False)
    verificarPro = Label(janela2, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    verificarPro.place(x=10,y=10)
    verificar = Entry(janela2)
    verificar.place(x=10,y=35, width=300, height=20)
    def verification():
        if os.path.exists(f"produtos/{nameArq.nomeArquivoTratado(verificar.get())}"):
            with open(f"produtos/{nameArq.nomeArquivoTratado(verificar.get())}", 'r') as arquivo1:
                arquivo = arquivo1.read()
                sucess = Label(janela2, text="Produto encontrado, " + arquivo + " em estoque.", background='green', foreground='#dde')
                sucess.place(x=10,y=95, width=250, height=20)
        else:
            fail = Label(janela2, text="Produto não encontrado. Tente novamente", background='red', foreground='#dde')
            fail.place(x=10,y=95, width=250, height=20)
    verificar2 = Button(janela2, text="Verificar", background="#003", foreground="#dde", command=verification)
    verificar2.place(x=10,y=60, width=100, height=25)