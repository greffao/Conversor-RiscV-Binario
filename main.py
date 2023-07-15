import tkinter as tk
from tkinter import messagebox

from Instrucoes.TipoI import TipoI
from Instrucoes.TipoR import TipoR
from Instrucoes.TipoS import TipoS
from Instrucoes.TipoJ import TipoJ
from Instrucoes.TipoU import TipoU
from Instrucoes.TipoB import TipoB

instrucoes = { 
    "tipo_R": ['add', 'sub', 'sll', 'slt', 'sltu','xor', 'srl', 'sra', 'or',  'and'],
    "tipo_I": ['jalr', 'lb', 'lh', 'lw', 'lbu', 'lhu', 'addi', 'slti', 'sltiu', 'xori', 'ori', 'andi'],
    "tipo_S": ['sb', 'sh', 'sw'],
    "tipo_B": ['beq', 'bne', 'blt', 'bge', 'bltu','bgeu'],
    "tipo_J": ['jal'],
    "tipo_U": ['lui', 'auipc']
}

def informacao():
    messagebox.showinfo("Info", "Operações aceitas:\n" +
                        "Tipo R \n" +
                        "Tipo I \n" +
                        "Tipo S \n" +
                        "Tipo B \n" +
                        "Tipo U \n" +
                        "Tipo J \n" +
                        "\n")
    

def show_custom_message(title, message, width, height):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Cria uma janela personalizada
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry(f"{width}x{height}")

    # Adiciona um rótulo para exibir a mensagem
    label = tk.Label(dialog, text=message, wraplength=width-50)
    label.pack(padx=20, pady=20)

    # Centraliza a janela personalizada na tela
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    dialog.geometry(f"+{x}+{y}")

    # Executa a janela personalizada
    return dialog

def converter():
    # Obter o valor digitado na caixa de texto
    texto = entry.get()
    
    mneumonico = (texto.split(","))[0].split(" ")[0].lower()

    try:
        if mneumonico in instrucoes["tipo_R"]:
            instrucao = TipoR(texto)
        elif mneumonico in instrucoes["tipo_I"]:
            instrucao = TipoI(texto)
        elif mneumonico in instrucoes["tipo_S"]:
            instrucao = TipoS(texto)
        elif mneumonico in instrucoes["tipo_J"]:
            instrucao = TipoJ(texto)
        elif mneumonico in instrucoes["tipo_U"]:
            instrucao = TipoU(texto)
        elif mneumonico in instrucoes["tipo_B"]:
            instrucao = TipoB(texto)
        else:
            messagebox.showinfo("Conversor RISC-V para Binário",
                                "Instrução Inválida!")
            return
        
        codigo_binario = str(instrucao)
        dialog = show_custom_message("Conversor RISC-V para Binário", 
                                     f"Campos: \n\n{codigo_binario}", 
                                     width=400, 
                                     height=200)
        
        dialog.grab_set()  # Bloquear interação com a janela principal enquanto a janela personalizada estiver aberta
        
        # Loop para atualizar a janela principal e aguardar o fechamento da janela personalizada
        while dialog.winfo_exists():
            window.update()
    except TypeError:
        messagebox.showinfo("Conversor RISC-V para Binário",
                                "Formatação Inválida!")
    except ValueError:
        messagebox.showinfo("Conversor RISC-V para Binário",
                                "Imediato deve ser inteiro positivo!")

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
integrantes_label.place(relx=0.5, rely=1.0, anchor=tk.S)


def on_close():
    if messagebox.askokcancel("Sair", "Deseja sair do aplicativo?"):
        window.quit()

# Configura a função on_close para ser chamada quando a janela for fechada
window.protocol("WM_DELETE_WINDOW", on_close)

# Executa o loop principal da janela
window.mainloop()