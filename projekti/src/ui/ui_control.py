
from ui.pop_up_window import PopUp


class Control():
    """Luokka, joka vastaa hiiren sekä canvasin tapahtumista.

    Attributes:
        selected_shape: Tällä hetkellä valittu muoto.
        selected_text: Tällä hetkellä valittu teksti.
        offset_x: x-koordinaatin ero hiiren ja valitun objektin välillä.
        offset_y: y-koordinaatin ero hiiren ja valitun objektin välillä.
        self._parent = peritty ui_view luokka.
        self._canvas = canvas, jota käsitellään.
    """

    def __init__(self, parent, canvas):
        """Luo

        Args:
            parent: peritty ui_view luokka
            canvas: canvas, jota käsitellään.
        """
        self.selected_shape = None
        self.selected_text = None
        self.offset_x = 0
        self.offset_y = 0

        self._parent = parent
        self._canvas = canvas

    def initiliaze(self):
        """Bindataan hiiren klikkaukset/painallukset canvasiin."""
        self._canvas.bind("<ButtonPress-1>",
                          self.select_object)
        self._canvas.bind("<B1-Motion>",
                          self.object_move)
        self._canvas.bind("ButtonRelease-1",
                          self.release_move)
        self._canvas.bind("<Double-Button-1>",
                          self.double_click)
        self._canvas.bind("<Double-Button-3>",
                          self.lower_shape)
        self._canvas.bind("<ButtonPress-3>",
                          self.lift_shape)

    def double_click(self, event):
        """Kutsutaan PopUp-ikkunaa, jos tuplaklikkaus tapahtuu
        ja jokin muoto-objekti on valittuna.

        Args: 
            event: vasemman hiiren tuplaklikkaus.
        """
        if self.selected_shape != None:
            popup = PopUp(self._parent, self._canvas, self)
            popup.initiliaze()

    def clear_canvas(self):
        """Tyhjennetään canvas objekteista."""
        self._canvas.delete("all")

    def select_object(self, event):
        """Hakee päällimmäisen klikatun objektin ja asettaa
        sen valituksi objektiksi (värittää reunat punaiseksi).

        Args:
            event: vasemman hiiren klikkaus.
        """
        if self.selected_shape != None:
            clicked_shape = self.selected_shape
            self._canvas.itemconfig(clicked_shape, outline="black")

        clicked_shape = None
        overlapping_shapes = self._canvas.find_overlapping(
            event.x, event.y, event.x, event.y)
        if overlapping_shapes:
            clicked_shape = overlapping_shapes[-1]

        if clicked_shape:
            self.selected_shape = clicked_shape
            self._canvas.itemconfig(clicked_shape, outline="red")
            self.selected_text = self._canvas.find_withtag(clicked_shape+1)

            self.offset_x = event.x - self._canvas.coords(clicked_shape)[0]
            self.offset_y = event.y - self._canvas.coords(clicked_shape)[1]

    def object_move(self, event):
        """Objektin liikuttelu, muuttaa valitun objektin koordinaatteja.

        Args:
            event: vasen hiiren painallus pohjaan.
        """
        if self.selected_shape:
            start_x1, start_y1, start_x2, start_y2 = self._canvas.coords(
                self.selected_shape)
            new_x1 = event.x - self.offset_x
            new_y1 = event.y - self.offset_y
            new_x2 = new_x1 + (start_x2 - start_x1)
            new_y2 = new_y1 + (start_y2 - start_y1)

            self._canvas.coords(self.selected_shape,
                                new_x1, new_y1, new_x2, new_y2)

            self._canvas.move(self.selected_text,
                              new_x1 - start_x1, new_y1 - start_y1)

    def release_move(self):
        """Vapauttaa valitun objektin ja siihen linkitetyn tekstin, 
        kun hiiren klikkaus loppuu."""
        self.selected_shape = None
        self.selected_text = None

    def change_shape(self, width, height, text):
        """Muuttaa/päivittää valitun objektin koon/nimen.

        Args:
            width: uusi leveys.
            height: uusi pituus.
            text: uusi teksti.
        """
        shape_id = self.selected_shape
        start_x1 = self._canvas.coords(
            shape_id)[0]
        start_y1 = self._canvas.coords(
            shape_id)[1]
        self._canvas.coords(shape_id, start_x1, start_y1,
                            start_x1 + width, start_y1 + height)
        self._canvas.itemconfig(shape_id+1, text=text)
        self._canvas.coords(shape_id+1, start_x1 + width/2,
                            start_y1 + height + 10)

    def delete_shape(self):
        """Poistaa valitun objektin ja siihen liittyvän tekstin"""
        self._canvas.delete(self.selected_shape)
        self._canvas.delete(self.selected_text)

    def lower_shape(self, event):
        """Vie annetun objektin canvasilla taaimmaisiksi.

        Args:
            event: oikea hiiren kaksoisklikkaus
        """
        if self.selected_shape != None:
            self._canvas.lower(self.selected_shape)
            self._canvas.lower(self.selected_text)

    def lift_shape(self, event):
        """Vie annetun objektin canvasilla etummaisiksi.

        Args:
            event: oikea hiiren klikkaus
        """
        if self.selected_shape != None:
            self._canvas.lift(self.selected_shape)
            self._canvas.lift(self.selected_text)
