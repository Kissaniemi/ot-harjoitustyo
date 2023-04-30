import tkinter as tk
from tkinter import messagebox, constants
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

from ui.ui_control import Control
from file_handler.save_load import SaveHandler


class View():
    """
    Ohjelman päänäkymä, näkyvillä koko ajan
    """

    def __init__(self, root):
        self._root = root
        self._width_entry = None
        self._height_entry = None
        self._text_entry = None
        self._error_label = None
        self._left_frame = None
        self._right_frame = None
        self._canvas = None

    def pack(self):

        self._left_frame.pack(fill=constants.X)

    def initialize(self):

        self._left_frame = tk.Frame(master=self._root, bg="gray")
        self._left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self._right_frame = tk.Frame(master=self._root, bg="gray")
        self._right_frame.pack(side=tk.LEFT, fill=tk.BOTH,
                               padx=10, pady=10, expand=True)

        self._canvas = tk.Canvas(master=self._right_frame,
                                 width=800, height=600, bg="white")
        self._canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.input()
        self.checkbox()

        self._error_label = tk.Label(master=self._left_frame,
                                     fg="red", bg="gray")
        self._error_label.pack(side=tk.TOP, padx=10, pady=10)

        self._event_handler = Control(
            self._root, self._canvas, self._error_label)
        self._save_handler = SaveHandler()

        create_room_button = tk.Button(
            master=self._left_frame,
            text="Create Room",
            command=lambda: self._event_handler._validate_input(
                "room",
                self._text_entry.get(),
                self._width_entry.get(),
                self._height_entry.get()))

        create_rectangle_button = tk.Button(
            master=self._left_frame,
            text="Create Rectangle",
            command=lambda: self._event_handler._validate_input(
                "rectangle",
                self._text_entry.get(),
                self._width_entry.get(),
                self._height_entry.get()))

        create_oval_button = tk.Button(
            master=self._left_frame,
            text="Create Oval",
            command=lambda: self._event_handler._validate_input(
                "oval",
                self._text_entry.get(),
                self._width_entry.get(),
                self._height_entry.get()))

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

    def checkbox(self):
        self._checkbox_var = tk.IntVar()
        checkbox = tk.Checkbutton(master=self._left_frame,
                                  text="texts on/off",
                                  variable=self._checkbox_var)
        checkbox.pack(side=tk.TOP, padx=10, pady=10)
        checkbox.config(command=self.texts_on_off)

    def texts_on_off(self):
        if self._checkbox_var.get() == 1:
            self._canvas.itemconfigure("text", state="hidden")
        else:
            self._canvas.itemconfigure("text", state="normal")

    def save_popup(self):
        filename = askstring("", "Enter file name to save to")
        if filename == "":
            self.save_error()
        elif filename == None:
            return
        else:
            self._save_handler.get_data(self._canvas, filename)

    def save_error(self):     
        filename = askstring("", "Please enter file name to save to")
        if filename == "":
            self.save_error()
        elif filename == None:
            return
        else:
            self._save_handler.get_data(self._canvas, filename)   
    
    def load_popup(self):
        filename = askstring("", "Enter file name to load from")
        if filename == "":
            self.load_error()
        elif filename== None:
            return
        else:
            self._save_handler.load(self._canvas, filename) 

    def load_error(self):     
        filename = askstring("", "Please enter file name to load from")
        if filename == "":
            self.load_error()
        elif filename == None:
            return
        else:
            self._save_handler.load(self._canvas, filename)  

    def delete_file_popup(self):
        filename = askstring("", "Enter file name to delete")
        if filename == "":
            self.delete_file_error()
        elif filename == None:
            return
        else:
            self._save_handler.delete_data(filename)

    def delete_file_error(self):
        filename = askstring("", "Please enter file name to delete")
        if filename == "":
            self.delete_file_error()
        elif filename == None:
            return
        else:
            self._save_handler.delete_data(filename)
                                                   
    def exit_popup(self):
        response = messagebox.askyesno(
            "", "Are you sure you want to exit the program?")
        if response == 1:
            self._event_handler._exit()
        pass
