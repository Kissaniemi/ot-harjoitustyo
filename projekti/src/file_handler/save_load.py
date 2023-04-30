from tkinter import messagebox
import json
import os

from shapes.shape_class import Shape

class SaveHandler():
    """ 
Luokka joka vastaa tallentamisesta ja latauksesta
"""

    def __init__(self):
        self.data = {"shapes": []}

    def get_data(self, canvas):
        self.data = {"shapes": []}

        shapes = canvas.find_withtag("shape")

        for rect in shapes:
            top_left_x, top_left_y, bottom_right_x, bottom_right_y = canvas.coords(
                rect)
            width, height = bottom_right_x - top_left_x, bottom_right_y - top_left_y
            text_item = canvas.find_withtag(rect+1)[0]
            name = canvas.itemcget(text_item, "text")
            tags = canvas.gettags(rect)
            self.data["shapes"].append({
                "width": width,
                "height": height,
                "name": name,
                "x": top_left_x,
                "y": top_left_y,
                "shape": tags[0]
            })

    def save(self, filename):

        with open(f"{filename}.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

        return True

    def load(self, filename):
        try:
            with open(f"{filename}.json", "r", encoding="utf-8") as file:
                self.data = json.load(file)
            return True

        except FileNotFoundError:
            return False

    def unload_data(self, canvas):
        for state in self.data["shapes"]:
            shape = Shape(canvas, state["width"], state["height"], state["name"],
                    state["shape"], state["x"], state["y"])
            shape.create_shape(state["shape"])

    def delete_data(self, filename):
        if os.path.exists(f"{filename}.json"):
            os.remove(f"{filename}.json")
            return True
        else:
            return False

