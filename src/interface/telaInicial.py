import tkinter as tk
from tkinter import ttk
from tkinter import font
from src.control import formula
from src.interface import resultado
from src.control import distanciaMetros

def criarTela(lista_nomes, listaTodos, lista_coordenadas):
    janela = tk.Tk()
    janela.title("Sistema de monitoramento de objetos indoor")
    janela.geometry("450x200") 
    janela.configure(background="lightblue")

    fonte = font.Font(size=12, weight="bold")
    rotulo = tk.Label(janela, text="Selecione  o beacon: ", background="lightblue", font=fonte)
    rotulo.pack(pady=10, padx=20, anchor="center")

    combo = ttk.Combobox(janela, values=lista_nomes, width="30", state="readonly")
    combo.pack(pady=10, padx=20, anchor="center")

    botao = tk.Button(janela, text="Executar!", command=lambda: exibir_selecao(janela, combo, listaTodos, lista_coordenadas))
    botao.pack(pady=30, anchor="center")


    janela.mainloop()

def exibir_selecao(janela, combo, listaTodos, lista_coordenadas):
        selecionado = combo.get()
        print(selecionado)
        janela.destroy()

        lista_distancias = distanciaMetros.valores_metros(listaTodos, selecionado)
        print("Distancias: ", lista_distancias)
            
        coordenadas = formula.formulaGeral(lista_coordenadas, lista_distancias)
        resultado.criarResultado(selecionado, coordenadas)