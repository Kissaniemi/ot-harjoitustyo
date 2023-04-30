
class Shape:
    """
Shape-luokka johon talletetaan canvasilla olevien muotojen tiedot ja
joka vastaa muodon luonnista canvasille

 """
    def __init__(self, canvas, width, height, text, shape_type, top_left_x=50, top_left_y=50):
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
        if shape == "rectangle":
            self.create_rectangle()

        elif shape == "oval":
            self.create_oval()

        else:
            self.create_room()

    def create_rectangle(self):
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
        self._id = self.canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="white",
            tags=("room", "shape"),
            width=2
        )
        self.canvas.lower(self._id)
        self.create_text()

    def create_text(self):
        self._text_id = self.canvas.create_text(
            (self.width)/2+self.top_left_x,
            self.height+10+self.top_left_y,
            text=self.text,
            fill="black",
            font=("Arial"),
            tags="text"
        )

    def change_text(self, text):
        self.text = text

    def change_width(self, width):
        self.width = width

    def change_height(self, height):
        self.height = height

    def change_coordinates(self, new_x, new_y):
        self.top_left_x = new_x
        self.top_left_y = new_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_id(self):
        return self._id

    def get_text(self):
        return self.text

    def get_text_id(self):
        return self._text_id

    def get_shape(self):
        return self.shape

    def get_coordinates(self):
        return (self.top_left_x, self.top_left_y)
