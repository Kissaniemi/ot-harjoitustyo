"""
Shape-luokka johon talletetaan canvasilla olevien muotojen tiedot ja
joka vastaa muodon luonnista canvasille

 """

class Shape:
    def __init__(self, width, height, text, shape, top_left_x=50, top_left_y=50):
        self.width = width
        self.height = height
        self.id = None
        self.text = text
        self.text_id = None
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.shape = shape

    def create_shape(self, canvas):
        if self.shape == "rectangle":
            self.id = canvas.create_rectangle(
                self.top_left_x, self.top_left_y,
                self.width+self.top_left_x,
                self.height+self.top_left_y,
                fill="white",
                tags=("rectangle", "shape"),
                width=2
            )

        elif self.shape == "oval":
            self.id = canvas.create_oval(
                self.top_left_x, self.top_left_y,
                self.width+self.top_left_x,
                self.height+self.top_left_y,
                fill="white",
                tags=("oval", "shape"),
                width=2
            )

        else:
            self.id = canvas.create_rectangle(
                self.top_left_x, self.top_left_y,
                self.width+self.top_left_x,
                self.height+self.top_left_y,
                fill="white",
                tags=("room", "shape"),
                width=2
            )
            canvas.lower(self.id)

        self.text_id = canvas.create_text(
            (self.width)/2+self.top_left_x,
            self.height+10+self.top_left_y,
            text=self.text,
            fill="black",
            font=("Arial"),
            tags="text"
        )
