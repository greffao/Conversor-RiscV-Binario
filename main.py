import tkinter as tk
from tkinter import messagebox

from Instrucao import Instrucao
from TipoR import TipoR

def informacao():
    messagebox.showinfo("Info", "Operações aceitas:\n" +
                        "Tipo R: add, sub e and\n" +
                        "Tipo I: addi\n" +
                        "Tipo S: sw e lw\n" +
                        "\n")
def converter():
    # Obter o valor digitado na caixa de texto
    texto = entry.get()


    print("Texto recebido: " + texto)

    tipo_R = ['add', 'sub', 'and']
    tipo_I = ['addi']
    tipo_S = ['sw', 'lw']


    if texto[:3] in tipo_R:
        instrucao = TipoR(texto)
    else:
        messagebox.showinfo("Conversor RISC-V para Binário",
                            "Instrução Inválida!")
        return

    codigo_binario = instrucao.converter()
    messagebox.showinfo("Conversor RISC-V para Binário",
                        "Código em Binário:\n\n" + codigo_binario)

# Criação da janela principal
window = tk.Tk()
window.title("Conversor RISC-V para Binário")

# Define a largura e altura da janela
largura = 500
altura = 300

# Calcula a posição x e y para centralizar a janela na tela
pos_x = (window.winfo_screenwidth() // 2) - (largura // 2)
pos_y = (window.winfo_screenheight() // 2) - (altura // 2)

# Define a geometria da janela
window.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Rótulo de título
title_label = tk.Label(window, text="Conversor RISC-V para Binário", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Rótulo
label = tk.Label(window, text="Digite a instrução RISC-V:", anchor="center")
label.pack()

# Campo de entrada de texto
entry = tk.Entry(window, justify="center")
entry.pack()

# Botão de conversão
button = tk.Button(window, text="Converter", command=converter)
button.pack()

# Botão "Info"
info_button = tk.Button(window, text="Info", command=informacao)
info_button.pack()

# Rótulo com o nome dos integrantes do grupo
integrantes_label = tk.Label(window, text="Integrantes do grupo:\n"
                                          "Lucas Greff Meneses - 13671615\n"
                                          "Henrique Souza Marques - 11815722\n"
                                          "Eduardo Neves Gomes da Silva - 13822710\n"
                                          "Vinicius Carneiro Macedo - 11915752", anchor="se")
integrantes_label.pack(side="bottom", padx=10, pady=10, anchor="se")

# Executa o loop principal da janela
window.mainloop()