import math

def calcularDistancia(rssi):
    A = -65
    n = 4 
    distancia = 10 ** ((A - rssi) / (10 * n))
    return distancia

def valores_metros(lista_rssi, beacon):
    distancias = []

    for dispositivo, frequencias_restantes in lista_rssi:
        if dispositivo == beacon:
            for lista_frequencias in frequencias_restantes:
                for frequencia in lista_frequencias:
                    metros = calcularDistancia(float(frequencia))
                    distancias.append(metros)

    return distancias