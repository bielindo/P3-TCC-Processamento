import tkinter as tk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fecharJanela(janela):
    janela.quit()
    janela.destroy()

def criarResultado(nome_beacon, coordenadas):
    janela = tk.Tk()
    janela.title("Sistema de monitoramento de objetos indoor")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ponto_x = coordenadas[0]
    ponto_y = coordenadas[1]
    ponto_z = coordenadas[2]
    nome_beacon_coordenada = f"{nome_beacon}({ponto_x:.2f}, {ponto_y:.2f}, {ponto_z:.2f})"
    print(coordenadas)
    ax.scatter(ponto_x, ponto_y, ponto_z, color='green', s=70)
    ax.text(ponto_x, ponto_y, ponto_z, nome_beacon_coordenada, fontsize=8)

    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

     # Definir o comportamento ao fechar a janela
    janela.protocol("WM_DELETE_WINDOW", lambda:fecharJanela(janela))

    janela.mainloop()