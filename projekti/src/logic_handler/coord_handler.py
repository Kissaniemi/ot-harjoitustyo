
class CoordHandler:
    def __init__(self, canvas):
        self._canvas = canvas

    def rotate_change_coords(self, x_coord, y_coord, shape, width, height):

        self._canvas.coords(shape, x_coord, y_coord,
                            x_coord + height, y_coord + width)

        self._canvas.coords(shape+1,
                            x_coord + height/2,
                            y_coord + width + 10)

        self._canvas.coords(shape+2,
                            height/2+x_coord,
                            y_coord-10)

        self._canvas.coords(shape+3,
                            height+x_coord+17,
                            y_coord+width/2)

    def text_change_coords(self, x_coord, y_coord, shape, width, height):

        self._canvas.coords(shape+1,
                            x_coord + width/2,
                            y_coord + height + 10)

        self._canvas.coords(shape+2,
                            width+x_coord+17,
                            y_coord+height/2)

        self._canvas.coords(shape+3,
                            width/2+x_coord,
                            y_coord-10)
