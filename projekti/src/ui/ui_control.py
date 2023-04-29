from shapes.shape_class import Shape
from ui.pop_up_windows import PopUp


class Control():
    def __init__(self, ui, canvas, error_label):
        self.selected_shape = None
        self.selected_text = None
        self.offset_x = 0
        self.offset_y = 0

        self._ui = ui
        self._canvas = canvas
        self._error_label = error_label

        self._canvas.bind("<ButtonPress-1>",
                          self.click_move)
        self._canvas.bind("<B1-Motion>",
                          self.drag_move)
        self._canvas.bind("ButtonRelease-1",
                          self.release_move)
        self._canvas.bind("<Double-Button-1>",
                          self._double_click)

    def _double_click(self, event):
        popup = PopUp(self._ui, self._canvas, self)
        popup.initiliaze()

    def _exit(self):
        self._ui.quit()

    def _clear_canvas(self):
        self._canvas.delete("all")

    def click_move(self, event):
        clicked_shape = None
        overlapping_shapes = self._canvas.find_overlapping(
            event.x, event.y, event.x, event.y)
        if overlapping_shapes:
            clicked_shape = overlapping_shapes[-1]

        if clicked_shape:
            self.selected_shape = clicked_shape
            self.selected_text = self._canvas.find_withtag(clicked_shape+1)

            self.offset_x = event.x - self._canvas.coords(clicked_shape)[0]
            self.offset_y = event.y - self._canvas.coords(clicked_shape)[1]

    def drag_move(self, event):
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
        self.selected_shape = None
        self.selected_text = None

    def _validate_input(self, shape_type, text_type, width_type, height_type):
        try:
            text = text_type
            width = float(width_type)
            height = float(height_type)
            if width < 5 or height < 5:
                self._error_label.config(
                    text="Width and height must be larger than 5!", bg="lightgray")
                return
            if width > 2000 or height > 2000:
                self._error_label.config(
                    text="Width and height must be less than 2000!", bg="lightgray")
                return
            
            shape = Shape(self._canvas, width, height, text, shape_type)
            Shape.create_shape(shape, shape_type)

            self._error_label.config(text="", bg="gray")

        except ValueError:
            self._error_label.config(
                text="Width and height must be a number!", bg="lightgray")

    def change_shape(self, width, height, text):
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
        self._canvas.delete(self.selected_shape)
        self._canvas.delete(self.selected_text)

