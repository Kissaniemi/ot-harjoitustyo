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

    def get_data(self, canvas, filename):

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

        self.save(filename)

    def save(self, filename):

        with open(f"{filename}.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

        messagebox.showinfo("Save", f"The file has been saved to '{filename}'.")

    def load(self, canvas, filename):
        try:
            with open(f"{filename}.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                self.unload_data(canvas, data)

        except FileNotFoundError:
            messagebox.showerror("Error", f"Filename '{filename}' not found.")

    def unload_data(self, canvas, data):
        for state in data["shapes"]:
                shape = Shape(canvas, state["width"], state["height"], state["name"],
                    state["shape"], state["x"], state["y"])
                Shape.create_shape(shape, state["shape"])

    def delete_data(self, filename):
        if os.path.exists(f"{filename}.json"):
            os.remove(f"{filename}.json")
            messagebox.showinfo("", f"Filename '{filename}' has been deleted.")
        else:
            messagebox.showerror("Error", f"Filename '{filename}' not found")
