from src.interface import telaInicial
from src.control import coletarDados

def main() -> int:
        
        #lista_topico1 = coletarDados.agruparDados("dispositivo1")
        #lista_topico2 = coletarDados.agruparDados("dispositivo2")
        #lista_topico3 = coletarDados.agruparDados("dispositivo3")
        #lista_topico4 = coletarDados.agruparDados("dispositivo4")

        #nomes = coletarDados.beaconsExistente(lista_topico1, lista_topico2, lista_topico3, lista_topico4)
        #listatodos = coletarDados.lista(lista_topico1, lista_topico2, lista_topico3, lista_topico4)

        lista_topico1 = coletarDados.agruparDados("segundoBeacon, -66; primeiroBeacon, -68; ")
        lista_topico2 = coletarDados.agruparDados("segundoBeacon, -68; primeiroBeacon, -78; ")
        lista_topico3 = coletarDados.agruparDados("segundoBeacon, -56; primeiroBeacon, -56; ")
        lista_topico4 = coletarDados.agruparDados("segundoBeacon, -63; primeiroBeacon, -67; ")

        nomes = coletarDados.beaconsExistente(lista_topico1, lista_topico2, lista_topico3, lista_topico4)
        listaTodos = coletarDados.lista(lista_topico1, lista_topico2, lista_topico3, lista_topico4)
        print(listaTodos)
        telaInicial.criarTela(nomes, listaTodos)

        return 0

if __name__ == "__main__":
        exit(main())