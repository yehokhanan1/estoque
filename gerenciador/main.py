from tkinter import *
import os
import delet
import newPro
import verificar
import adicionar
import retirar

janela = Tk()
janela.title("Estoque")
janela.geometry("280x300")
janela.configure(background="#001")
janela.wm_resizable(width=False, height=False)

adProduto = Button(janela, text="Adicionar novo produto ", background="#003", foreground="#dde",command=newPro.adicionarPro).place(x=15,y=30, width=250, height=25)

verProduto = Button(janela, text="Verficar produtos ", background="#003", foreground="#dde", command=verificar.verificarPro).place(x=15, y=70, width=250, height=25)

addProdutos = Button(janela, text="Adicionar produto existente", background="#003", foreground="#dde", command=adicionar.addProduto).place(x=15, y=110, width=250, height=25)

retirarPro = Button(janela, text="Retirar produto existente", background="#003", foreground="#dde", command=retirar.retirarPro).place(x=15, y=150, width=250, height=25)

excluirPro = Button(janela, text="Excluir produto existente", background="#003", foreground="#dde", command=delet.deletPro).place(x=15, y=190, width=250, height=25)

janela.mainloop()
