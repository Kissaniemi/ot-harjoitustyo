from tkinter import messagebox
import json

from rectangle.rectangle import Rectangle


class EventHandler():
    def __init__(self, main_ui, canvas):
        # Variables to track the selected rectange and text
        self.selected_rectangle = None
        self.selected_text = None
        self.offset_x = 0
        self.offset_y = 0

        self._ui = main_ui
        self.canvas = canvas

    # function to toggle names on/off
    def names_on_off(self):
        if self._ui.checkbox_var.get() == 1:
            self.canvas.itemconfigure("text", state="hidden")
        else:
            self.canvas.itemconfigure("text", state="normal")

   # Find the clicked rectangle and text related to it
    def click_move(self, event):
        clicked_rectangle = None
        overlapping_rectangles = self.canvas.find_overlapping(
            event.x, event.y, event.x, event.y)
        if overlapping_rectangles:
            # Get the topmost rectangle if rectangles overlap
            clicked_rectangle = overlapping_rectangles[-1]

        # make the click rect the selected rect
        # and the associated text the selected text
        if clicked_rectangle:
            self.selected_rectangle = clicked_rectangle
            # +1 because the associated text object id is the rectangle id+1
            self.selected_text = self.canvas.find_withtag(clicked_rectangle+1)

            # event.x and event.y tracks the mouse position
            self.offset_x = event.x - self.canvas.coords(clicked_rectangle)[0]
            self.offset_y = event.y - self.canvas.coords(clicked_rectangle)[1]

    # Move the selected rectangle with the mouse
    def drag_move(self, event):
        if self.selected_rectangle:
            start_x1, start_y1, start_x2, start_y2 = self.canvas.coords(
                self.selected_rectangle)
            new_x1 = event.x - self.offset_x   # event.x and event.y tracks the mouse position
            new_y1 = event.y - self.offset_y
            new_x2 = new_x1 + (start_x2 - start_x1)
            new_y2 = new_y1 + (start_y2 - start_y1)

            # Changes the coordinates for the rectangle
            self.canvas.coords(self.selected_rectangle,
                               new_x1, new_y1, new_x2, new_y2)
            # Changes coordinates for the text
            self.canvas.move(self.selected_text,
                             new_x1 - start_x1, new_y1 - start_y1)

   # Deselect the rectangle and text when the mouse is released
    def release_move(self):
        self.selected_rectangle = None
        self.selected_text = None

    # Creates a rectangle from the inputs
    def create_rectangle(self):

        name = self._ui.name_entry.get()
        # checks that the width and height inputs are numbers
        try:
            width = float(self._ui.width_entry.get())
            height = float(self._ui.height_entry.get())

            # Calls the Rectangle class
            rectangle = Rectangle(width, height, name)
            rectangle.create(self.canvas)

            self._ui.error_label.config(text="", bg="gray")

        except ValueError:
            self._ui.error_label.config(
                text="Width and height must be a number!", bg="lightgray")

    # Deletes the last selected rectangle and text
    def delete_rectangle(self):
        self.canvas.delete(self.selected_rectangle)
        self.canvas.delete(self.selected_text)

    # Popup to confirm you want to save
    def save_popup(self):
        response = messagebox.askyesno("", "Do you want to save?")
        if response == 1:
            self.save()
        else:
            pass

    # Popup to confirm you want to load
    def load_popup(self):
        response = messagebox.askyesno("", "Do you want to load last save?")
        if response == 1:
            self.load()
        else:
            pass

    # Popup to confirm you want to exit
    def exit_popup(self):
        response = messagebox.askyesno(
            "", "Are you sure you want to exit program?")
        if response == 1:
            self.exit()
        else:
            pass

    # Save to json
    def save(self):
        data = {"rectangles": []}
        # Find all rectangle objects on the canvas
        rectangles = self.canvas.find_withtag("rectangle")
        # Create a data list of the rectangles to append to the json file
        for rect in rectangles:
            top_left_x, top_left_y, bottom_right_x, bottom_right_y = self.canvas.coords(
                rect)
            width = bottom_right_x - top_left_x
            height = bottom_right_y - top_left_y
            # Get the text item associated with the rectangle
            text_item = self.canvas.find_withtag(rect+1)[0]
            # Get the text from the text item
            name = self.canvas.itemcget(text_item, "text")
            data["rectangles"].append({
                "width": width,
                "height": height,
                "name": name,
                "x": top_left_x,
                "y": top_left_y,
            })

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        # Saved pop up
        messagebox.showinfo("Save", "The state has been saved.")

    # Load from json
    def load(self):
        # Clears the canvas
        self.canvas.delete("all")

        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for state in data["rectangles"]:
                rect = Rectangle(
                    state["width"], state["height"], state["name"], state["x"], state["y"])
                rect.create(self.canvas)

        except FileNotFoundError:
            messagebox.showerror("Error", "No saved data found.")

    def exit(self):
        self._ui.window.quit()
