from src.interface import telaInicial
from src.control import coletarDados

#Classe para representar as listas de tópicos de dispositivos.
class ListasTopicos:
#Construtor da classe ListasTopicos.
#:param listas: Dicionário com as listas de dispositivos, onde cada chave é o nome do tópico e o valor é uma lista de dispositivos.
    def __init__(self, **listas):
        self.listas = listas

def main() -> int:

    # Coleta dos dados para os tópicos de dispositivos
    lista_topico1 = coletarDados.agruparDados("dispositivo1")
    lista_topico2 = coletarDados.agruparDados("dispositivo2")
    lista_topico3 = coletarDados.agruparDados("dispositivo3")
    lista_topico4 = coletarDados.agruparDados("dispositivo4")

    # Criação do objeto receptores para armazenar as listas de dispositivos
    receptores = ListasTopicos(lista_topico1=lista_topico1, lista_topico2=lista_topico2, lista_topico3=lista_topico3, lista_topico4=lista_topico4)

    # Obtém os nomes comuns dos dispositivos presentes em todas as listas
    nomes = coletarDados.beaconsExistente(receptores)

    # Remove os dispositivos que não estão presentes em todas as listas
    listas_iguais = coletarDados.removerValores(receptores)

    # Cria a lista de frequências para cada dispositivo presente nas listas
    listaTodos = coletarDados.lista(listas_iguais)

    telaInicial.criarTela(nomes, listaTodos)

    return 0

if __name__ == "__main__":
    exit(main())