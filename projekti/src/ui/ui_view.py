import tkinter as tk
from tkinter import messagebox, constants
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

from ui.ui_control import Control
from file_handler.save_load import SaveHandler
from shapes.shape_class import Shape


class View():
    """
    Ohjelman päänäkymä, joka on näkyvillä koko ajan.
    """

    def __init__(self, root):
        """Luokan konstruktori, joka luo uuden käyttöliittymäluokan.

        Args:
            root: juuri, jonka sisään käyttöliittymä-luokka luodaan.
        """
        self._root = root
        self._width_entry = None
        self._height_entry = None
        self._text_entry = None
        self._error_label = None
        self._left_frame = None
        self._right_frame = None
        self._canvas = None

    def pack(self):
        """Näkymän pakkaus."""
        self._left_frame.pack(fill=constants.X)

    def initialize(self):
        """Alustetaan framet,labelit, buttonit, muut luokat."""
        self._left_frame = tk.Frame(master=self._root, bg="gray")
        self._left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self._right_frame = tk.Frame(master=self._root, bg="gray")
        self._right_frame.pack(side=tk.LEFT, fill=tk.BOTH,
                               padx=10, pady=10, expand=True)

        self._canvas = tk.Canvas(master=self._right_frame,
                                 width=800, height=600, bg="white")
        self._canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.input()
        self.buttons_labels()

        self._event_handler = Control(
            self._root, self._canvas)
        self._event_handler.initiliaze()

        self._save_handler = SaveHandler()

    def buttons_labels(self):

        create_room_button = tk.Button(
            master=self._left_frame,
            text="Create Room",
            command=lambda: self.validate_input(
                "room",
                self._text_entry.get(),
                self._width_entry.get(),
                self._height_entry.get()))

        create_rectangle_button = tk.Button(
            master=self._left_frame,
            text="Create Rectangle",
            command=lambda: self.validate_input(
                "rectangle",
                self._text_entry.get(),
                self._width_entry.get(),
                self._height_entry.get()))

        create_oval_button = tk.Button(
            master=self._left_frame,
            text="Create Oval",
            command=lambda: self.validate_input(
                "oval",
                self._text_entry.get(),
                self._width_entry.get(),
                self._height_entry.get()))

        self.error_label = tk.Label(master=self._left_frame,
                                    fg="red", bg="gray")
        self.error_label.pack(side=tk.TOP, padx=10, pady=10)

        create_room_button.pack(side=tk.TOP, padx=10, pady=10)
        create_rectangle_button.pack(side=tk.TOP, padx=10, pady=10)
        create_oval_button.pack(side=tk.TOP, padx=10, pady=10)

        delete_save_button = tk.Button(master=self._left_frame,
                                       text="Delete File")
        delete_save_button.pack(side=tk.RIGHT, padx=10, pady=10)
        delete_save_button.config(command=self.delete_file_popup)

        load_button = tk.Button(master=self._left_frame,
                                text="Load File")
        load_button.pack(side=tk.RIGHT, padx=10, pady=10)
        load_button.config(command=self.load_popup)

        save_button = tk.Button(master=self._left_frame,
                                text="Save File")
        save_button.pack(side=tk.RIGHT, padx=20, pady=10)
        save_button.config(command=self.save_popup)

        exit_button = tk.Button(master=self._left_frame,
                                text="Exit")
        exit_button.pack(side=tk.LEFT, padx=20, pady=30)
        exit_button.config(command=self.exit_popup)

    def input(self):

        width_label = tk.Label(master=self._left_frame,
                               text="Width (cm):")
        width_label.pack(side=tk.TOP, padx=120, pady=5)
        self._width_entry = tk.Entry(master=self._left_frame)
        self._width_entry.pack(side=tk.TOP, padx=10, pady=5)

        height_label = tk.Label(master=self._left_frame,
                                text="Height (cm):")
        height_label.pack(side=tk.TOP, padx=10, pady=5)
        self._height_entry = tk.Entry(master=self._left_frame)
        self._height_entry.pack(side=tk.TOP, padx=10, pady=5)

        text_label = tk.Label(master=self._left_frame,
                              text="Text")
        text_label.pack(side=tk.TOP, padx=10, pady=5)
        self._text_entry = tk.Entry(master=self._left_frame)
        self._text_entry.pack(side=tk.TOP, padx=10, pady=5)

        self._checkbox_var = tk.IntVar()
        checkbox = tk.Checkbutton(master=self._left_frame,
                                  text="texts on/off",
                                  variable=self._checkbox_var)
        checkbox.pack(side=tk.TOP, padx=10, pady=10)
        checkbox.config(command=self.texts_on_off)

    def texts_on_off(self):
        """Piilottaa/näyttää tekstit canvasilla."""
        if self._checkbox_var.get() == 1:
            self._canvas.itemconfigure("text", state="hidden")
        else:
            self._canvas.itemconfigure("text", state="normal")

    def validate_input(self, shape_type, text_type, width_type, height_type):
        """Validoi, ovatko annetut syötteet halutun mukaisia.

        Args:
            shape_type: muodon syöte.
            text_type: tekstin syöte.
            width_type: leveyden syöte.
            height_type: pituuden syöte.
        """
        try:
            text = text_type
            width = float(width_type)
            height = float(height_type)
            if width < 5 or height < 5:
                self.change_error_label(1)
                return

            elif width > 2000 or height > 2000:
                self.change_error_label(2)
                return

            shape = Shape(self._canvas, width, height, text, shape_type)
            Shape.create_shape(shape, shape_type)

            self.change_error_label(3)

        except ValueError:
            self.change_error_label(4)

    def change_error_label(self, change_type):
        """Muuttaa error_labelin näkymää annetun argumentin mukaisesti.

        Args:
            change_type: tehtävä muutos.
        """
        if change_type == 1:
            self.error_label.config(
                text="Width and height must be larger than 5!", bg="lightgray")
        elif change_type == 2:
            self.error_label.config(
                text="Width and height must be less than 2000!", bg="lightgray")
        elif change_type == 3:
            self.error_label.config(text="", bg="gray")
        else:
            self.error_label.config(
                text="Width and height must be a number!", bg="lightgray")

    def save_popup(self):
        """Tallennus popup"""
        filename = askstring("", "Enter file name to save to")
        if filename == "":
            self.save_error()
        elif filename == None:
            return
        else:
            self.save_confirm(filename)

    def save_error(self):
        """Tallennus inputissa virhe, ei syötettä"""
        filename = askstring("", "Please enter file name to save to")
        if filename == "":
            self.save_error()
        elif filename == None:
            return
        else:
            self.save_confirm(filename)

    def save_confirm(self, filename):
        """Tallennuksen tiedostonimen tarkistus"""
        self._save_handler.get_data(self._canvas)
        ask = self._save_handler.save(filename)
        if ask == True:
            messagebox.showinfo(
                "Save", f"The file has been saved to '{filename}'.")
        else:
            messagebox.showinfo("Error", "Couldn't save to file.")

    def load_popup(self):
        """Latauksen popup"""
        filename = askstring("", "Enter file name to load from")
        if filename == "":
            self.load_error()
        elif filename == None:
            return
        else:
            self.load_confirm(filename)

    def load_error(self):
        """Latauksen inputissa virhe, ei syötettä"""
        filename = askstring("", "Please enter file name to load from")
        if filename == "":
            self.load_error()
        elif filename == None:
            return
        else:
            self.load_confirm(filename)

    def load_confirm(self, filename):
        """Latauksen tiedotonimen tarkistus"""
        ask = self._save_handler.load(filename)
        if ask == True:
            self._event_handler.clear_canvas()
            self._save_handler.unload_data(self._canvas)
        else:
            messagebox.showerror("Error", f"Filename '{filename}' not found.")

    def delete_file_popup(self):
        """Tiedoston poisto popup"""
        filename = askstring("", "Enter file name to delete")
        if filename == "":
            self.delete_file_error()
        elif filename == None:
            return
        else:
            self._save_handler.delete_data(filename)

    def delete_file_error(self):
        """Tiedoston poistossa virhe, ei syötettä"""
        filename = askstring("", "Please enter file name to delete")
        if filename == "":
            self.delete_file_error()
        elif filename == None:
            return
        else:
            self.delete_confirm(filename)

    def delete_confirm(self, filename):
        """Tiedoston poiston tarkistus"""
        ask = self._save_handler.delete_data(filename)
        if ask == True:
            messagebox.showinfo("", f"Filename '{filename}' has been deleted.")
        else:
            messagebox.showerror("Error", f"Filename '{filename}' not found")

    def exit_popup(self):
        """Ohjelmasta poistuminen"""
        response = messagebox.askyesno(
            "", "Are you sure you want to exit the program?")
        if response == 1:
            self._root.quit()
        else:
            return
