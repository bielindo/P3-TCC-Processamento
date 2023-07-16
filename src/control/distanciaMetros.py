import math

"""
Calcula a distância estimada em metros com base no RSSI (Received Signal Strength Indication).

:param rssi: O valor RSSI recebido.
:return: A distância estimada em metros.
"""
def calcularDistancia(rssi):
    A = -65
    n = 4
    distancia = 10 ** ((A - rssi) / (10 * n))
    return distancia


"""
Calcula as distâncias estimadas em metros para um dispositivo específico (beacon) com base nos valores de RSSI.

:param lista_rssi: Uma lista contendo tuplas no formato (dispositivo, frequencias_restantes), onde
                       "dispositivo" é o nome do dispositivo e "frequencias_restantes" é uma lista de listas
                       contendo os valores de frequência (RSSI) do dispositivo para diferentes medições.
:param beacon: O nome do dispositivo específico (beacon) para o qual se deseja calcular as distâncias.
:return: Uma lista contendo as distâncias estimadas em metros para o dispositivo específico (beacon).
"""
def valores_metros(lista_rssi, beacon):
    distancias = []

    for dispositivo, frequencias_restantes in lista_rssi:
        if dispositivo == beacon:
            for lista_frequencias in frequencias_restantes:
                for frequencia in lista_frequencias:
                    metros = calcularDistancia(float(frequencia))
                    distancias.append(metros)

    return distancias