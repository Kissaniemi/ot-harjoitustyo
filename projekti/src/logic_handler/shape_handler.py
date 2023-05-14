
class ShapeHandler:
    def __init__(self, canvas):

        self._canvas = canvas

    def create_rectangle(self, shape, linecolor="black", color="lightgray",):
        """Luo suorakulmion"""
        self._canvas.create_rectangle(
            shape.top_left_x, shape.top_left_y,
            shape.width+shape.top_left_x,
            shape.height+shape.top_left_y,
            fill=color,
            outline=linecolor,
            tags=("rectangle", "shape"),
            width=2
        )

    def create_oval(self, shape, linecolor="black", color="lightgray"):
        """Luo ovaalin."""
        self._canvas.create_oval(
            shape.top_left_x, shape.top_left_y,
            shape.width+shape.top_left_x,
            shape.height+shape.top_left_y,
            fill=color,
            outline=linecolor,
            tags=("oval", "shape"),
            width=2
        )

    def create_room(self, shape, linecolor="black", color="white"):
        """Luo huone-suorakulmion."""
        self._canvas.create_rectangle(
            shape.top_left_x, shape.top_left_y,
            shape.width+shape.top_left_x,
            shape.height+shape.top_left_y,
            fill=color,
            outline=linecolor,
            tags=("room", "shape"),
            width=3
        )

    def create_text(self, shape, color="black"):
        """Luo tekstiobjektin"""
        self._canvas.create_text(
            shape.width/2+shape.top_left_x,
            shape.height+10+shape.top_left_y,
            text=shape.text,
            fill=color,
            font=("Arial"),
            tags="text"
        )

    def create_width_text(self, shape, color="black"):
        """Luo numerotekstiobjektin"""
        self._canvas.create_text(
            shape.width/2+shape.top_left_x,
            shape.top_left_y-10,
            text=shape.width,
            fill=color,
            font=("Arial"),
            tags="text"
        )

    def create_height_text(self, shape, color="black"):
        """Luo numerotekstiobjektin"""
        self._canvas.create_text(
            shape.width+shape.top_left_x+17,
            shape.top_left_y+shape.height/2,
            text=shape.height,
            fill=color,
            font=("Arial"),
            tags="text"
        )
