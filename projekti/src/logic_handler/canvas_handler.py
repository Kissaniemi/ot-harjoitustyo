from shapes.shape import Shape
from logic_handler.shape_handler import ShapeHandler
from logic_handler.coord_handler import CoordHandler


class CanvasHandler():
    """Pääasiallinen sovelluslogiikasta vastaava luokka."""

    def __init__(self, canvas):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            canvas: canvas, jota käsitellään.
        """
        self.selected_shape = None
        self._canvas = canvas
        self.offset_x = 0
        self.offset_y = 0
        self.shapes = []
        self._shape_handler = ShapeHandler(self._canvas)
        self._coord_handler = CoordHandler(self._canvas)

    def _initiliaze(self):
        """Bindataan hiiren klikkaukset/painallukset canvasiin."""

        self._canvas.bind("<ButtonPress-1>",
                          self.select_object)
        self._canvas.bind("<B1-Motion>",
                          self.object_move)
        self._canvas.bind("ButtonRelease-1",
                          self.release_move)
        self._canvas.bind("<ButtonPress-3>",
                          self.rotate_shape)
        self._canvas.bind("<Double-Button-3>",
                          self.rotate_shape)

    def uncheck_color(self):
        """Tarkistaa canvasin taustan värin ja 
        vaihtaa objektin reunaväriä sen mukaan.
        """
        color = self._canvas.itemcget(self.selected_shape, "fill")
        if color == "#104E8B":
            self._canvas.itemconfig(self.selected_shape, outline="white")
        else:
            self._canvas.itemconfig(self.selected_shape, outline="black")

    def change_texts(self, width, height, text):
        """Muuttaa valittuun muoto-objektiin
        liittyvien tekstiobjektien tekstit.

        Args:
            width: uusi leveys.
            height: uusi pituus.
            text: uusi teksti.
        """
        if self.selected_shape is None:
            return

        shape_id = self.selected_shape

        self._canvas.itemconfig(shape_id+1, text=text)
        self._canvas.itemconfig(shape_id+2, text=height)
        self._canvas.itemconfig(shape_id+3, text=width)

        x_coord = self._canvas.coords(
            shape_id)[0]
        y_coord = self._canvas.coords(
            shape_id)[1]

        texts = self.shapes[shape_id]
        texts.change_coordinates(x_coord + width/2, y_coord + height + 10)

        width_text = self.shapes[shape_id+1]
        width_text.change_coordinates(width+x_coord+17, y_coord+height/2)

        height_text = self.shapes[shape_id+2]
        height_text.change_coordinates(width/2+x_coord, y_coord-10)

        self._coord_handler.text_change_coords(x_coord, y_coord,
                                               shape_id, width, height)

    def rotate_shape(self, event):
        """Kääntää valitun objektin 
        (vaihtaa pituuden ja leveyden keskenään)
        """
        if self.selected_shape is not None:
            shape_id = self.selected_shape
            shape = self.shapes[shape_id-1]
            width = shape.width
            height = shape.height
            text = shape.text

            shape.change_all(height, width, text)
            new_width = shape.height
            new_height = shape.width

            texts = self.shapes[shape_id]
            texts.change_all(new_width, new_height, text)

            width_text = self.shapes[shape_id+1]
            width_text.change_all(new_width, new_height, new_height)

            height_text = self.shapes[shape_id+2]
            height_text.change_all(new_width, new_height, new_width)

            self._canvas.itemconfig(shape_id+2, text=new_height)
            self._canvas.itemconfig(shape_id+3, text=new_width)

            x_coord, y_coord = event.x, event.y

            self._coord_handler.rotate_change_coords(
                x_coord, y_coord, shape_id, new_width, new_height)

    def release_move(self):
        """Vapauttaa valitun objektin ja siihen linkitetyn tekstin, 
        kun hiiren klikkaus loppuu."""
        self.selected_shape = None

    def select_object(self, event):
        """Hakee päällimmäisen klikatun objektin ja asettaa
        sen valituksi objektiksi (muuttaa reunavärin punaiseksi).

        Args:
            event: vasemman hiiren klikkaus.
        """
        tags = self._canvas.gettags("current")
        if "text" in tags:
            self.uncheck_color()
            self.release_move()
            return

        if self.selected_shape is not None:
            self.uncheck_color()

        self.release_move()
        overlapping_shapes = self._canvas.find_overlapping(
            event.x, event.y, event.x, event.y)
        if overlapping_shapes:
            self.selected_shape = overlapping_shapes[-1]

        if self.selected_shape:
            self._canvas.itemconfig(self.selected_shape, outline="red")
            self.offset_x = event.x - \
                self._canvas.coords(self.selected_shape)[0]
            self.offset_y = event.y - \
                self._canvas.coords(self.selected_shape)[1]
        else:
            self.release_move()

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

            self._canvas.move(self.selected_shape+1,
                              new_x1 - start_x1, new_y1 - start_y1)

            self._canvas.move(self.selected_shape+2,
                              new_x1 - start_x1, new_y1 - start_y1)

            self._canvas.move(self.selected_shape+3,
                              new_x1 - start_x1, new_y1 - start_y1)

    def get_all(self):
        """Hakeee valitun objektin koordinaatit ja tekstin.

        Returns:
            Tekstin ja koordinaatit, jos objekti on valittu.
            None, jos objektia ei ole valittu.
        """
        if self.selected_shape is not None:
            shape_id = self.selected_shape
            text_item = self._canvas.find_withtag(shape_id+1)
            text = self._canvas.itemcget(text_item, "text")
            x_1, y_1, x_2, y_2 = self._canvas.coords(shape_id)
            return text, x_1, y_1, x_2, y_2
        return None

    def change_shape(self, width, height, text):
        """Muuttaa valitun objektin koon/tekstin.

        Args:
            width: uusi leveys.
            height: uusi pituus.
            text: uusi teksti.
        """
        if self.selected_shape is None:
            return

        shape_id = self.selected_shape
        start_x1 = self._canvas.coords(
            shape_id)[0]
        start_y1 = self._canvas.coords(
            shape_id)[1]

        self._canvas.coords(shape_id, start_x1, start_y1,
                            start_x1 + width, start_y1 + height)

        shape = self.shapes[shape_id-1]
        shape.change_width(width)
        shape.change_height(height)
        shape.change_text(text)

    def dark_mode(self, var):
        """Muuttaa canvasin värimaailman.

        Args: 
            var: checkboxin tila.
        """
        if var is True:
            self._canvas.itemconfigure("room", fill="#104E8B", outline="white")
            self._canvas.itemconfigure(
                "rectangle", fill="#104E8B", outline="white")
            self._canvas.itemconfigure("oval", fill="#104E8B", outline="white")
            self._canvas.itemconfigure("text", fill="white")

            self._canvas.configure(bg="#104E8B")

        else:
            self._canvas.itemconfigure("room", fill="white", outline="black")
            self._canvas.itemconfigure(
                "rectangle", fill="lightgray", outline="black")
            self._canvas.itemconfigure(
                "oval", fill="lightgray", outline="black")
            self._canvas.itemconfigure("text", fill="black")

            self._canvas.configure(bg="white")

    def texts_on_off(self, var):
        """Piilottaa/näyttää teksti-objektit canvasilla.

        Args: 
            var: checkboxin tila.
        """
        if var is True:
            self._canvas.itemconfigure("text", state="hidden")
        else:
            self._canvas.itemconfigure("text", state="normal")

    def copy_shape(self):
        """Kopioi valitun objektin"
        """
        if self.selected_shape is not None:
            shape_id = self.selected_shape
            shape = self.shapes[shape_id-1]
            width = shape.width
            height = shape.height
            text = shape.text
            shape = shape.shape
            self.create_shape(width, height, text, shape)

    def lower_shape(self):
        """Vie annetun objektin ja siihen liittyvät 
        tekstit canvasilla taaimmaisiksi.
        """
        if self.selected_shape is not None:
            for i in range(self.selected_shape, self.selected_shape+4):
                self._canvas.lower(i)

    def lift_shape(self):
        """Vie annetun objektin ja siihen liittyvät 
        tekstit canvasilla etummaisiksi.
        """
        if self.selected_shape is not None:
            for i in range(self.selected_shape, self.selected_shape+4):
                self._canvas.lift(i)

    def clear_canvas(self):
        """Tyhjennetään canvas objekteista."""
        self._canvas.delete("all")

    def create_shape(self, width, height, text, shape_type, x_coord=50, y_coord=50):
        """Kutsuu Shape-luokan create_shape fuktiota ja lisää luodun
        objektin id:n self.shapes listaan.

        Args:
            width: objektin leveys.
            height: objektin pituus.
            text: objektiin liitetty teksti.
            shape_type: objektin muodon tyyppi.
            x_coord : x-koordinaatti, Default 50.
            y_coord : y-koordinaatti, Default 50.
        """
        getcolor = self.get_current_color()
        color, linecolor = self.get_object_color(getcolor, shape_type)

        shape = Shape(width, height, text,
                      shape_type, x_coord, y_coord)

        if shape_type == "rectangle":
            self._shape_handler.create_rectangle(shape, linecolor, color)

        elif shape_type == "oval":
            self._shape_handler.create_oval(shape, linecolor, color)

        elif shape_type == "room":
            self._shape_handler.create_room(shape, linecolor, color)
        else:
            return

        self.shapes.append(shape)

        self.create_texts(width, height, text,
                          linecolor, x_coord, y_coord)

    def create_texts(self, width, height, text, linecolor="black", x_coord=50, y_coord=50):
        """Kutsuu Shape-luokan create_text fuktiota ja lisää luodun
        objektin id:n self.shapes listaan.

        Args:
            width: objektin leveys.
            height: objektin pituus.
            text: objektiin liitetty teksti.
            linecolor: tekstin väri, Default "black".
            x_coord : x-koordinaatti, Default 50.
            y_coord : y-koordinaatti, Default 50.
        """
        state = self.get_current_text_state()

        texts = Shape(width, height,
                      text, "text", x_coord, y_coord)
        self._shape_handler.create_text(texts, linecolor)

        widths = Shape(width, height,
                       text, "width", x_coord, y_coord)
        self._shape_handler.create_width_text(widths, linecolor)

        heights = Shape(width, height,
                        text, "height", x_coord, y_coord)
        self._shape_handler.create_height_text(heights, linecolor)

        self.shapes.append(texts)
        self.shapes.append(widths)
        self.shapes.append(heights)

        self.texts_on_off(state)

    def get_object_color(self, state, shape):
        """Tarkistaa ollaanko "normi" vai "blueprint"
        tilassa ja asetaan luotavan värin objektit sen mukaan.

        Args:
            state: tila-attribuutti .
            shape: muoto-objekti, jonka väri halutaan.

        Returns:
            Palauttaa täyttövärin "color" ja 
            reunojen värin "linecolor".
        """
        if state is True:
            color = "#104E8B"
            linecolor = "white"
        else:
            if shape == "room":
                color = "white"
                linecolor = "black"
            else:
                color = "lightgray"
                linecolor = "black"
        return color, linecolor

    def get_current_color(self):
        """Tarkistaa canvasin taustavärin.

        Returns:
            Palauttaa True, jos väri on "#104E8B"
            ja False, jos väri on jokin muu.
        """

        color = self._canvas.cget("bg")
        if color == "#104E8B":
            return True
        return False

    def get_current_text_state(self):
        """Tarkistaa onko canvasilla teksti näkyvissä.

        Returns:
            Palauttaa True, jos teksti on piilotettu
            ja palauttaa False jos canvasilla ei ole tekstiä
            tai jos tekstiä ei ole piilotettu.
        """
        texts = self._canvas.find_withtag("text")
        if not texts:
            return False
        state = all(self._canvas.itemcget(item, 'state') == 'hidden'
                    for item in self._canvas.find_withtag("text"))
        if state:
            return True
        return False

    def delete_shape(self):
        """Poistaa valitun objektin ja siihen liittyvät tekstit
        """
        if self.selected_shape is not None:
            for i in range(self.selected_shape, self.selected_shape+4):
                self._canvas.delete(i)
            self.selected_shape = None
