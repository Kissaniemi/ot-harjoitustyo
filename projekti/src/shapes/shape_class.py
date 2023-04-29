"""
Shape-luokka johon talletetaan canvasilla olevien muotojen tiedot ja
joka vastaa muodon luonnista canvasille

 """

class Shape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = None
        self.height = None
        self.id = None
        self.text = None
        self.text_id = None
        self.shape = None
        self.top_left_x = None
        self.top_left_y = None
           
    def create_shape(self, width, height, text, shape_type, top_left_x=50, top_left_y=50):
        self.width = width
        self.height = height
        self.text = text
        self.shape = shape_type
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y

        if self.shape == "rectangle":
            self.create_rectangle()

        elif self.shape == "oval":
            self.create_oval()

        else:
            self.create_room()
    
    def create_rectangle(self):
        self.id = self.canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="lightgray",
            tags=("rectangle", "shape"),
            width=1
        )
        self.create_text()

    def create_oval(self):
        self.id = self.canvas.create_oval(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="lightgray",
            tags=("oval", "shape"),
            width=1
        )
        self.create_text()

    def create_room(self):
        self.id = self.canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="white",
            tags=("room", "shape"),
            width=2
        )
        self.canvas.lower(self.id)
        self.create_text()

    def create_text(self):
        self.text_id = self.canvas.create_text(
            (self.width)/2+self.top_left_x,
            self.height+10+self.top_left_y,
            text=self.text,
            fill="black",
            font=("Arial"),
            tags="text"
        )
 
   
    def rotate_shape(self):
        self.width, self.height = self.height, self.width

    def duplicate_shape(self):
        pass


