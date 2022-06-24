"""Map or canvas where our drunk will walk
"""

class Campo:

    def __init__(self):
        self.coordenadas_of_drunks = {}

    def add_drunk(self, drunk, coord):
        self.coordenadas_of_drunks[drunk] = coord

    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        current_coord = self.coordenadas_of_drunks[drunk]
        new_coord = current_coord.move(delta_x, delta_y)

        self.coordenadas_of_drunks[drunk] = new_coord

    def get_coord(self, drunk):
        return self.coordenadas_of_drunks[drunk]
