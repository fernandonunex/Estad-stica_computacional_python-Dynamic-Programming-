import random
import collections

PALOS = ['espada', 'corazon', 'diamante', 'trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
        
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    # obtener las manos
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    # procesar los valores para encontrar pares
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
    # contando cuando encontramos un par
        counter = dict(collections.Counter(valores))
        #print(counter)
        for val in counter.values():
            if val == 2:
                pares += 1
                break
    
    # calculando las probabilidades
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es {probabilidad_par}')


if __name__ == "__main__":
    tamano_mano = int(input('Cuantas cartas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)


