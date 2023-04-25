import tkinter as tk


class PopUp():
    """
    Custom PopUp ikkunan luokka
    """

    def __init__(self, parent, canvas, event_handler):
        self.pop = tk.Toplevel(parent)
        self.pop.title("")
        self.pop.geometry("350x300")
        self.pop.config(bg="white")
        self.canvas = canvas
        self.eventhandler = event_handler

    def initiliaze(self):
        self.shape = self.canvas.find_withtag("current")
        if not self.shape:
            self.pop.destroy()
            return

        change_label = tk.Label(
            self.pop, text="Change object text, size or delete object")
        change_label.pack(side=tk.TOP, padx=10, pady=5)

        shape_id = self.shape[0]
        text_item = self.canvas.find_withtag(shape_id+1)
        name = self.canvas.itemcget(text_item, "text")
        x_1, y_1, x_2, y_2 = self.canvas.coords(shape_id)

        new_width_label = tk.Label(self.pop, text="Width (cm):")
        new_width_label.pack(side=tk.TOP, padx=10, pady=5)
        self.new_width_entry = tk.Entry(self.pop)
        self.new_width_entry.insert(0, x_2 - x_1)
        self.new_width_entry.pack(side=tk.TOP, padx=10, pady=5)

        new_height_label = tk.Label(self.pop, text="Height (cm):")
        new_height_label.pack(side=tk.TOP, padx=10, pady=5)
        self.new_height_entry = tk.Entry(self.pop)
        self.new_height_entry.insert(0, y_2 - y_1)
        self.new_height_entry.pack(side=tk.TOP, padx=10, pady=5)

        new_name_label = tk.Label(self.pop, text="Name")
        new_name_label.pack(side=tk.TOP, padx=10, pady=5)
        self.new_name_entry = tk.Entry(self.pop)
        self.new_name_entry.insert(0, name)
        self.new_name_entry.pack(side=tk.TOP, padx=10, pady=5)

        change_button = tk.Button(self.pop, text="OK",
                                  command=lambda: (self.eventhandler.change_shape(
                                      float(self.new_width_entry.get()),
                                      float(self.new_height_entry.get()),
                                      self.new_name_entry.get()),
                                      self.pop.destroy()), bg="lightgray")
        change_button.pack(side=tk.RIGHT, padx=20, pady=10)

        cancel_button = tk.Button(self.pop, text="Delete Object",
                                  command=lambda: (self.eventhandler.delete_shape(),
                                                   self.pop.destroy()), bg="lightgray")
        cancel_button.pack(side=tk.LEFT, padx=20, pady=10)