
class Shape():
    """Shape-luokka, jonka ylläpidetään muoto-objektin attribuutteja.
    Vastaa sekä muodon luonnista canvasille, että muodon attribuuttien muutoksista.
    """

    def __init__(self, canvas, width, height, text, shape_type, top_left_x=50, top_left_y=50):
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
        self.canvas = canvas
        self.width = width
        self.height = height
        self._id = None
        self.text = text
        self._text_id = None
        self.shape = shape_type
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y

    def create_shape(self, shape):
        """ Kutsuu eri create-funktiotia shape-tyypin mukaan.

        Args:
            shape: muodon tyyppi.
        """
        if shape == "rectangle":
            self.create_rectangle()

        elif shape == "oval":
            self.create_oval()

        else:
            self.create_room()

    def create_rectangle(self):
        """Luo suorakulmion ja kutsuu tekstinluonti-funktiota."""
        self._id = self.canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="lightgray",
            tags=("rectangle", "shape"),
            width=1
        )
        self.create_text()

    def create_oval(self):
        """Luo ovaalin ja kutsuu tekstinluonti-funktiota."""
        self._id = self.canvas.create_oval(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="lightgray",
            tags=("oval", "shape"),
            width=1
        )
        self.create_text()

    def create_room(self):
        """Luo huone-suorakulmion ja kutsuu tekstinluonti-funktiota.
        Vie huone-suorakulmion canvasin taaimmaisiksi.
        """
        self._id = self.canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="white",
            tags=("room", "shape"),
            width=2
        )
        self.create_text()

    def create_text(self):
        """Luo tekstiobjektin"""
        self._text_id = self.canvas.create_text(
            (self.width)/2+self.top_left_x,
            self.height+10+self.top_left_y,
            text=self.text,
            fill="black",
            font=("Arial"),
            tags="text"
        )

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
