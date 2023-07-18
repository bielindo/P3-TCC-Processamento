# Importando módulos necessários
from src.interface import telaInicial
from src.control import coletarDados

"""
Classe para representar as listas de tópicos de dispositivos.

:param listas: Dicionário com as listas de dispositivos, onde cada chave é o nome do tópico e o valor é uma lista de dispositivos.
"""
class ListasTopicos:
    def __init__(self, **listas):
        self.dados = listas

"""
Lê os dados de dispositivos de um arquivo e retorna um dicionário com as informações.

:param dispositivos: Caminho do arquivo contendo os dados dos dispositivos.
:return: Dicionário com os dados dos dispositivos, onde cada chave é o nome do dispositivo e o valor é uma tupla de coordenadas.
"""
def lerDadosArquivo(dispositivos):
    with open(dispositivos, 'r') as arquivo:
        linhas = arquivo.readlines()

    dados_servidores = {}
    for linha in linhas:
        chave, valores = linha.strip().split(': ')
        dispositivo = chave.strip('"')
        valores = tuple(map(int, valores.strip('()\n').split(',')))
        dados_servidores[dispositivo] = valores

    return dados_servidores

def main() -> int:
    dispositivos = "src\config\dispositivos.txt"
    dados_servidores = lerDadosArquivo(dispositivos)

    lista_topicos = []
    lista_coordenada = []
    for dispositivo, valores in dados_servidores.items():
        lista_topico = coletarDados.agruparDados(dispositivo)
        lista_topicos.append(lista_topico)
        lista_coordenada.append(valores)

    # Convertendo a lista de tuplas para o formato desejado
    lista_coordenadas = [list(tupla) for tupla in lista_coordenada]  

    # Criando objetos Dispositivo com base nos dicionários
    receptores = [ListasTopicos(**d) for d in lista_topicos]
    
    # Obtém os nomes comuns dos dispositivos presentes em todas as listas
    nomes = coletarDados.beaconsExistente(receptores)
    # Remove os dispositivos que não estão presentes em todas as listas
    listas_iguais = coletarDados.removerValores(receptores)

    # Cria a lista de frequências para cada dispositivo presente nas listas
    listaTodos = coletarDados.lista(listas_iguais)

    # Cria e exibe a tela inicial com as informações coletadas
    telaInicial.criarTela(nomes, listaTodos, lista_coordenadas)

    return 0

if __name__ == "__main__":
    exit(main())