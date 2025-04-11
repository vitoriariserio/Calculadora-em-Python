import tkinter as tk

def clicar_botao(valor):
    texto_atual = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, texto_atual + str(valor))

def calcular():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, resultado)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, 'erro')

def limpar():
    entry.delete(0, tk.END)

def apagar():
    texto_atual = entry.get()
    entry.delete(len(texto_atual)-1, tk.END)

janela = tk.Tk()  
janela.title('Calculadora')


entry = tk.Entry(janela, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('←', 5, 1)
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        b = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=calcular)
    elif texto == 'C':
        b = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=limpar)
    elif texto == '←':
        b = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=apagar)
    else:
        b = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=lambda valor=texto: clicar_botao(valor))
    b.grid(row=linha, column=coluna)

janela.mainloop()
