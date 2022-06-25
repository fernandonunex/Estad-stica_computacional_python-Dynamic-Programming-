from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    inicio = campo.get_coord(borracho)

    for _ in range(pasos):
        campo.move_drunk(borracho)

    return inicio.distance(campo.get_coord(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(name='Fernando')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.add_drunk(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def main(distacias_de_caminata, numero_de_intentos, tipo_de_borracho):

    for pasos in distacias_de_caminata:
        distancias = simular_caminata(
            pasos, numero_de_intentos, tipo_de_borracho)

        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_max}')
        print(f'Min = {distancia_min}')



if __name__ == '__main__':
    distacias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distacias_de_caminata, numero_de_intentos, BorrachoTradicional)
