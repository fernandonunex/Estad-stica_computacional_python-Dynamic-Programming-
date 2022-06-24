""" Location in a field (x,y)
"""

class Coordenada:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distance(self, other_coord):
        delta_x = self.x - other_coord.x
        delta_y = self.y - other_coord.y

        return (delta_x**2 + delta_y**2)**0.5
