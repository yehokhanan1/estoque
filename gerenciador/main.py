from tkinter import *
import os
import delet
import newPro
import verificar
import adicionar
import retirar

class windonws():
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Estoque")
        self.janela.geometry("280x300")
        self.janela.configure(background="#001")
        self.janela.wm_resizable(width=False, height=False)
    def buttons(self):
        adProduto = Button(self.janela, text="Adicionar novo produto ", background="#003", foreground="#dde",command=newPro.adicionarPro)
        adProduto.place(x=15,y=30, width=250, height=25)
        verProduto = Button(self.janela, text="Verficar produtos ", background="#003", foreground="#dde", command=verificar.verificarPro)
        verProduto.place(x=15, y=70, width=250, height=25)
        addProdutos = Button(self.janela, text="Adicionar produto existente", background="#003", foreground="#dde", command=adicionar.addProduto)
        addProdutos.place(x=15, y=110, width=250, height=25)
        retirarPro = Button(self.janela, text="Retirar produto existente", background="#003", foreground="#dde", command=retirar.retirarPro)
        retirarPro.place(x=15, y=150, width=250, height=25)
        excluirPro = Button(self.janela, text="Excluir produto existente", background="#003", foreground="#dde", command=delet.deletPro)
        excluirPro.place(x=15, y=190, width=250, height=25)
        self.janela.mainloop()
start = windonws()
start.buttons()
