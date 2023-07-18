from src.input import conexaoMQTT


"""
Agrupa os dados recebidos de um tópico MQTT.

:param topico: O tópico MQTT do qual os dados serão agrupados.
:return: Um dicionário contendo os dados agrupados, onde as chaves são os nomes dos dispositivos e os valores são listas de frequências.
"""
def agruparDados(topico):
    resultados = {}
    dados = conexaoMQTT.dadosMQTT(topico)
    pares = dados.split("; ")

    for par in pares:
        valores = par.strip().split(", ")
        if len(valores) == 2:
            nome, potencia = valores
            if nome in resultados:
                resultados[nome].append(potencia)
            else:
                resultados[nome] = [potencia]

    return resultados

"""
Obtém os nomes comuns de dispositivos presentes em todas as listas.

:param receptores: Um objeto contendo as listas de dispositivos.
:return: Uma lista com os nomes comuns de dispositivos presentes em todas as listas.
"""
def beaconsExistente(receptores):
    # Cria uma lista de dicionários com os dados dos dispositivos
    lista_dados_dispositivos = [receptor.dados for receptor in receptores]

    # Inicializa o conjunto de nomes comuns com os tópicos do primeiro dispositivo
    nomes_comuns = set(lista_dados_dispositivos[0].keys())

    # Itera sobre os demais dispositivos e mantém apenas os tópicos em comum
    for dados_dispositivo in lista_dados_dispositivos[1:]:
        nomes_comuns.intersection_update(dados_dispositivo.keys())

    return list(nomes_comuns)

"""
Remove os valores de dispositivos que não estão presentes em todas as listas.

:param receptores: Um objeto contendo as listas de dispositivos.
:return: Uma lista de dicionários contendo as listas de dispositivos com os valores iguais entre elas.
"""
def removerValores(receptores):
    # Cria uma lista de dicionários com os dados dos dispositivos
    lista_dados_dispositivos = criar_lista_dados_dispositivos(receptores)

    # Inicializa o conjunto de chaves comuns com os tópicos do primeiro dispositivo
    chaves_comuns = set(lista_dados_dispositivos[0].keys())

    # Itera sobre os demais dispositivos e mantém apenas os tópicos em comum
    for dados_dispositivo in lista_dados_dispositivos[1:]:
        chaves_comuns.intersection_update(dados_dispositivo.keys())

    # Cria uma lista de dicionários com os valores em comum de todos os dispositivos
    listas_iguais = [{chave: dados_dispositivo[chave] for chave in chaves_comuns} for dados_dispositivo in lista_dados_dispositivos]

    return listas_iguais

"""
Cria uma lista com as frequências de dispositivos presentes nas listas.

:param listas_iguais: Uma lista de dicionários contendo as listas de dispositivos com valores iguais entre elas.
:return: Uma lista contendo as frequências de dispositivos presentes nas listas.
"""
def lista(listas_iguais):
    lista_todos = []

    dispositivos_comuns = listas_iguais[0].keys()

    for dispositivo in dispositivos_comuns:
        potencias = [lista[dispositivo] for lista in listas_iguais]
        lista_todos.append((dispositivo, potencias))

    return lista_todos

# Função para criar uma lista de dicionários com os dados dos dispositivos
def criar_lista_dados_dispositivos(receptores):
    return [receptor.dados for receptor in receptores]