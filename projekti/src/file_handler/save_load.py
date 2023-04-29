from tkinter import messagebox
import json

from shapes.shape_class import Shape

class SaveHandler():
    """ 
Luokka joka vastaa tallentamisesta ja latauksesta
"""

    def __init__(self):
        self.data = {"shapes": []}

    def save(self, canvas, filename):

        shapes = canvas.find_withtag("shape")

        for rect in shapes:
            top_left_x, top_left_y, bottom_right_x, bottom_right_y = canvas.coords(
                rect)
            width, height = bottom_right_x - top_left_x, bottom_right_y - top_left_y
            text_item = canvas.find_withtag(rect+1)[0]
            name = canvas.itemcget(text_item, "text")
            tags = canvas.gettags(rect)
            shape = tags
            self.data["shapes"].append({
                "width": width,
                "height": height,
                "name": name,
                "x": top_left_x,
                "y": top_left_y,
                "shape": shape[0]
            })

        with open(filename+".json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

        messagebox.showinfo("Save", "The state has been saved.")

    def load(self, canvas, filename):

        try:
            with open(filename+".json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for state in data["shapes"]:
                shape = Shape(canvas, state["width"], state["height"], state["name"],
                    state["shape"], state["x"], state["y"])
                Shape.create_shape(shape, state["shape"])


        except FileNotFoundError:
            messagebox.showerror("Error", "No saved data found.")
