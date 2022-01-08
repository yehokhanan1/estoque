from tkinter import *
import os
import nameArq

def deletPro():
    janela5 = Tk()
    janela5.title("Excluir")
    janela5.geometry("320x120")
    janela5.configure(background="#001")
    janela5.wm_resizable(width=False, height=False)
    verificarPro = Label(janela5, text="Nome do produto", background="#001",foreground="#dde", anchor=W)
    verificarPro.place(x=10,y=10)
    verificar = Entry(janela5)
    verificar.place(x=10,y=35, width=300, height=20)
    def delet():
        if os.path.exists(f"produtos/{nameArq.nomeArquivoTratado(verificar.get())}"):
            os.remove(f"produtos/{nameArq.nomeArquivoTratado(verificar.get())}")
            sucess = Label(janela5, text="Produto excluido do estoque.", background='green', foreground='#dde')
            sucess.place(x=10,y=95, width=250, height=20)
        else:
            fail = Label(janela5, text="Produto não encontrado. Tente novamente", background='red', foreground='#dde')
            fail.place(x=10,y=95, width=250, height=20)
    verificar2 = Button(janela5, text="Excluir", background="#003", foreground="#dde", command=delet)
    verificar2.place(x=10,y=60, width=100, height=25)