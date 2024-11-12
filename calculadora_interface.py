import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Solicitação dos dados necessários para o usuário.
        n1 = int(entry_n1.get())
        n2 = int(entry_n2.get())
        operacao = entry_op.get()

        # O código executará uma operação diferente para cada sinal digitado e mostrará um resultado personalizado para o usuário.
        if operacao == '+':
            resultado = n1 + n2
        elif operacao == '-':
            resultado = n1 - n2
        elif operacao == '*':
            resultado = n1 * n2
        elif operacao == '/':
            if n2 == 0: 
                messagebox.showerror('Erro', 'Operação inválida!') # Caso o usuário tente dividir por zero.
            else:
                resultado = round(n1 / n2, 2) # O comando 'round' arredondará o resultado para 2 casas decimais.
        else:
            messagebox.showerror('Erro', 'Operação inválida. Use apenas +, -, * ou /.') # Mensagem para operações não reconhecidas.

        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira números válidos.') # Mensagem de erro para entradas inválidas.

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Definindo uma fonte maior
fonte_padrao = ("Arial", 20)  # Família de fonte Arial, tamanho 14

# Componentes da interface
tk.Label(janela, text="Primeiro Número:", font=fonte_padrao).pack()
entry_n1 = tk.Entry(janela, font=fonte_padrao)
entry_n1.pack()

tk.Label(janela, text="Operação (+, -, * ou /):", font=fonte_padrao).pack()
entry_op = tk.Entry(janela, font=fonte_padrao)
entry_op.pack()

tk.Label(janela, text="Segundo Número:", font=fonte_padrao).pack()
entry_n2 = tk.Entry(janela, font=fonte_padrao)
entry_n2.pack()

btn_calcular = tk.Button(janela, text="Calcular", font=fonte_padrao, command=calcular)
btn_calcular.pack()

label_resultado = tk.Label(janela, text="Resultado:", font=fonte_padrao)
label_resultado.pack()

# Inicia a janela
janela.mainloop()