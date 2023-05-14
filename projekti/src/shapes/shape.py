
class Shape():
    """Shape-luokka, joka ylläpitää muoto-objektin attribuutteja. 
    Vastaa muodon luonnista canvasille ja muodon attribuuttien muutoksista.
    """

    def __init__(self, width: int, height: int, text: str, shape_type: str, x_coord=50, y_coord=50):
        """Luokan konstruktori, joka alustaa muodosta ylläpidetyt tiedot.

        Args: 
            canvas: canvas, jolle muodot luodaan.
            width: muodon leveys.
            length: muodon pituus.
            text: muodon teksti.
            shape: muodon 'tyyppi'.
            top_left_x: muodon ylävasen x-koordinatti.
            top_left_y: muodon ylävasen y-koordinatti.
        """
        self.width = width
        self.height = height
        self.text = text
        self.shape = shape_type
        self.top_left_x = x_coord
        self.top_left_y = y_coord

    def change_text(self, text):
        """Muuttaa tekstiä.

        Args:
            test: uusi teksti.
        """
        self.text = text

    def change_width(self, width):
        """Muuttaa leveyttä.

        Args:
            width: uusi leveys.
        """
        self.width = width

    def change_height(self, height):
        """Muuttaa pituutta.

        Args:
            height: uusi pituus.
        """
        self.height = height

    def change_coordinates(self, new_x, new_y):
        """Muuttaa koordinaatteja.

        Args:
            new_x: uusi x-koordinaatti.
            new_y: uusi y-koordinaatti.
        """
        self.top_left_x = new_x
        self.top_left_y = new_y

    def change_all(self, width, height, text):
        """Muuttaa leveys-, pituus-, tekstiattribuutteja

        Args:
            width: uusi leveys
            height: uusi pituus
            text: uusi teksti
        """
        self.change_width(width)
        self.change_height(height)
        self.change_text(text)
