class Field:
    def __init__(self):
        self.coords_borr = {}

    def add_borr(self, borr, coord):
        self.coords_borr[borr] = coord

    def move_borr(self, borr):
        delta_x, delta_y = borr.camina()
        current_coord = self.coords_borr[borr]
        new_coord = current_coord.move(delta_x, delta_y)

        self.coords_borr[borr] = new_coord
    
    def get_coords(self, borr):
        return self.coords_borr[borr]
