# Rectangle class to store info of the rectangle
class Rectangle:
    def __init__(self, width, height, name, top_left_x=50, top_left_y=50):
        self.width = width
        self.height = height
        self.id = None
        self.text = name
        self.text_id = None
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y

    # Function to create the rectangle and text object
    def create(self, canvas):
        self.id = canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.width+self.top_left_x,
            self.height+self.top_left_y,
            fill="white",
            tags="rectangle",
        )

        self.text_id = canvas.create_text(
            (self.width)/2+self.top_left_x,
            self.height+10+self.top_left_y,
            text=self.text,
            fill="black",
            font=("Arial"),
            tags="text"
        )
