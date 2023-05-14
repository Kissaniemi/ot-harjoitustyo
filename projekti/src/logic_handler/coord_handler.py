
class CoordHandler:
    """Canvasin objektien koordinaattien muuttamisesta vastaava luokka.
    """

    def __init__(self, canvas):
        """Luokan konstruktori.

        Args:
            canvas: canvas, jolla koordinaatteja muutetaan
        """
        self._canvas = canvas

    def rotate_change_coords(self, x_coord, y_coord, shape, width, height):
        """Muuttaa neljän 'linkitetyn' objektin koordinaatteja kierrettäessä.

        Args:
            x_coord: x-koordinaatti.
            y_coord: y-koordinaatti.
            shape: muoto-objektin id.
            width: leveys.
            height: pituus.
        """
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
        """Muuttaa kolmen 'linkitetyn' teksti-objektin koordinaatteja.

        Args:
            x_coord: x-koordinaatti.
            y_coord: y-koordinaatti.
            shape: muoto-objektin id.
            width: leveys.
            height: pituus.
        """
        self._canvas.coords(shape+1,
                            x_coord + width/2,
                            y_coord + height + 10)

        self._canvas.coords(shape+2,
                            width+x_coord+17,
                            y_coord+height/2)

        self._canvas.coords(shape+3,
                            width/2+x_coord,
                            y_coord-10)
