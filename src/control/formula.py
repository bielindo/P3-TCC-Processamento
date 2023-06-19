import numpy as np


def formulaGeral(lista_coordenadas, lista_distancias):
    A = calcular_A(lista_coordenadas)
    K = calcular_K(lista_coordenadas, lista_distancias)
    matrizCompleta = np.concatenate((A, K), axis=1)
    coeficientes = matrizCompleta[:, :-1]
    resultados = matrizCompleta[:, -1]
    print(matrizCompleta)
    coodenadas = np.linalg.lstsq(coeficientes, resultados, rcond=None)[0]

    return coodenadas

def calcular_K(lista_coordenadas, lista_distancias):
    resultados = []
    for i in range(len(lista_coordenadas)):
        coordenadas1 = lista_coordenadas[i]
        coordenadas2 = lista_coordenadas[(i + 1) % len(lista_coordenadas)]
        distancias1 = lista_distancias[i]
        distancias2 = lista_distancias[(i + 1) % len(lista_coordenadas)]
        x0, y0, z0 = coordenadas1
        d0 = distancias1
        x1, y1, z1 = coordenadas2
        d1 = distancias2
        k = (x0 ** 2 + y0 ** 2 + z0 ** 2 - d0 ** 2 - (x1 ** 2 + y1 ** 2 + z1 ** 2 - d1 ** 2)) / 2
        resultados.append([k])

    matriz_resultados = np.array(resultados)
    return matriz_resultados


def calcular_A(lista_coordenadas):
    resultados = []
    for i in range(len(lista_coordenadas)):
        coordenadas1 = lista_coordenadas[i]
        coordenadas2 = lista_coordenadas[(i + 1) % len(lista_coordenadas)]
        resultado_x = coordenadas1[0] - coordenadas2[0]
        resultado_y = coordenadas1[1] - coordenadas2[1]
        resultado_z = coordenadas1[2] - coordenadas2[2]
        resultados.append([resultado_x, resultado_y, resultado_z])
    
    matriz_resultados = np.array(resultados)
    return matriz_resultados