from tkinter import *

janela = Tk()

# Label (Rotulo)
label = Label(janela, text='isso e um rótulo', font=('Arial', 12), fg='#6A5ACD')
label.pack()

label2 = Label(janela, text='SEJA BEM VINDO', font=('Arial', 12), fg='#6A5ACD')
label2.pack()

# button (botão)
def button_click():
    label.config(text='botão clicado!')

button = Button(janela, text='Clique em mim!', command=button_click)
button.pack()

#gb é para mudar o backgroud color do campo de entrada

entry_text = StringVar()
entry = Entry(janela, textvariable=entry_text, bg='red')
entry.pack()


# text (caixa de texto)
text = Text(janela, height=5, width=30, wrap='word')
text.pack()

text.insert(END, 'este é um exemplo de caixa de texto.')

#Frame (Quadro)

frame = Tk.Frame(janela, relief=Tk. RAISED, borderwidth=2)
frame.pack








janela.mainloop()