from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.get_coord(borracho)
    x_arreglo = [0]
    y_arreglo = [0]

    for _ in range(pasos):
        campo.move_drunk(borracho)
        x, y = campo.get_coord_x_y(borracho)
        x_arreglo.append(x)
        y_arreglo.append(y)

    #Graficando los pasos que dio el borracho a lo largo de la caminata
    graficar_steps(x_arreglo, y_arreglo, colors = 'red', steps=pasos)
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

#Para graficar cada paso que da el borracho
def graficar_steps(x, y, colors, steps):
    grafica = figure(title=f'Steps: {steps}')
    grafica.circle([0],[0], size=10, )
    grafica.line(x, y, line_color = colors)

    grafica.circle(x[-1],y[-1], size=10, fill_color = 'yellow')
    grafica.line([0,x[-1]],[0,y[-1]], line_color='purple', line_width=5, line_dash='dashed')

    show(grafica)

#Para graficar las distancias promedio
def graficar(x, y, colors):
    grafica_2 = figure(title='Camino de borrachos', x_axis_label='pasos', y_axis_label='distancia')
    grafica_2.line(x, y, legend_label='distancia media', line_color = colors)

    show(grafica_2)

def main(distacias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = [0]

    for pasos in distacias_de_caminata:
        distancias = simular_caminata(
            pasos, numero_de_intentos, tipo_de_borracho)

        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_max}')
        print(f'Min = {distancia_min}')

    # Para graficar las distancias promedio
    #graficar(distacias_de_caminata, distancias_media_por_caminata, blue)


if __name__ == '__main__':
    distacias_de_caminata = [10000]
    numero_de_intentos = 1

    main(distacias_de_caminata, numero_de_intentos, BorrachoTradicional)

