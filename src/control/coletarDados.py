from src.input import conexaoMQTT

def agruparDados(topico):
    resultados = {}
    #dados = conexaoMQTT.dadosMQTT(topico)
    dados = topico
    pares = dados.split("; ")

    for par in pares:
        valores = par.strip().split(", ")
        if len(valores) == 2:
            nome, frequencia = valores
            if nome in resultados:
                resultados[nome].append(frequencia)
            else:
                resultados[nome] = [frequencia]
    print(f"valore: {resultados}")

    return resultados


def beaconsExistente(lista_topico1, lista_topico2, lista_topico3, lista_topico4):
    nomes1 = set(lista_topico1.keys())
    nomes2 = set(lista_topico2.keys())
    nomes3 = set(lista_topico3.keys())
    nomes4 = set(lista_topico4.keys())

    nomes_comuns = list(nomes1.intersection(nomes2, nomes3, nomes4))
    
    return nomes_comuns


def lista(lista_topico1, lista_topico2, lista_topico3, lista_topico4):
    lista_todos = []

    for dispositivo in lista_topico1:
        frequencias = [lista_topico1[dispositivo], lista_topico2[dispositivo],
                    lista_topico3[dispositivo], lista_topico4[dispositivo]]
        lista_todos.append((dispositivo, frequencias))

    return lista_todos



