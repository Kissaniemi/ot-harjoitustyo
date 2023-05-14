
class DataHandler:
    def __init__(self, canvas_handler):
        self._handler = canvas_handler
        self._canvas = self._handler._canvas
        self.data = []

    def get_json_data(self):
        """Tyhjentää ensin nykyisen data-kirjaston ja hakee canvasilta 
        kaikki 'shape' tyypin objektit ja 'tallentaa' ne uuteen kirjastoon.

        Args: 
            canvas: canvas, josta tiedot haetaan.
        """
        self.data.clear()
        self.data = {"shapes": []}

        shapes = self._canvas.find_withtag("shape")

        for rect in shapes:
            top_left_x, top_left_y, bottom_right_x, bottom_right_y = self._canvas.coords(
                rect)
            width, height = bottom_right_x - top_left_x, bottom_right_y - top_left_y
            text_item = self._canvas.find_withtag(rect+1)[0]
            text = self._canvas.itemcget(text_item, "text")
            tags = self._canvas.gettags(rect)
            self.data["shapes"].append({
                "width": int(width),
                "height": int(height),
                "text": text,
                "x": top_left_x,
                "y": top_left_y,
                "shape": tags[0]
            })

        return self.data

    def unload_json_data(self, data):
        """Purkaa saadun datan canvasille

        Args:
            data: annettu data
        """
        if data == {}:
            return False

        self._handler.clear_canvas()
        for state in data["shapes"]:
            self._handler.create_shape(state["width"], state["height"], state["text"],
                                       state["shape"], state["x"], state["y"])
        return True

    def get_sql_data(self):
        """Tyhjentää ensin nykyisen data-kirjaston ja hakee canvasilta 
        kaikki 'shape' tyypin objektit ja 'tallentaa' ne uuteen kirjastoon.

        Args: 
            canvas: canvas, josta tiedot haetaan.
        """
        self.data.clear()
        self.data = []

        shapes = self._canvas.find_withtag("shape")

        for rect in shapes:
            top_left_x, top_left_y, bottom_right_x, bottom_right_y = self._canvas.coords(
                rect)
            width, height = bottom_right_x - top_left_x, bottom_right_y - top_left_y
            text_item = self._canvas.find_withtag(rect+1)[0]
            text = self._canvas.itemcget(text_item, "text")
            tags = self._canvas.gettags(rect)
            self.data.append((int(width), int(height), text,
                             top_left_x, top_left_y, tags[0]))

        return self.data

    def unload_sql_data(self, data):
        self._handler.clear_canvas()
        for _, item in enumerate(data):
            self._handler.create_shape(
                item[0], item[1], item[2], item[5], item[3], item[4])
