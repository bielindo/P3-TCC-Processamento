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
            nome, pontencia = valores
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
    nomes_comuns = set(receptores.listas[list(receptores.listas.keys())[0]].keys())
    for lista in list(receptores.listas.values())[1:]:
        nomes_comuns.intersection_update(lista.keys())

    return list(nomes_comuns)

"""
Remove os valores de dispositivos que não estão presentes em todas as listas.

:param receptores: Um objeto contendo as listas de dispositivos.
:return: Uma lista de dicionários contendo as listas de dispositivos com os valores iguais entre elas.
"""
def removerValores(receptores):
    chaves_comuns = set(receptores.listas[list(receptores.listas.keys())[0]].keys())
    for lista in list(receptores.listas.values())[1:]:
        chaves_comuns.intersection_update(lista.keys())

    listas_iguais = []
    for lista in receptores.listas.values():
        lista_igual = {chave: lista[chave] for chave in chaves_comuns}
        listas_iguais.append(lista_igual)

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
