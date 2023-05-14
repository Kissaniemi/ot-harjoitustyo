import tkinter as tk
from tkinter import constants

from ui.popups.json_pop_ups import JsonPopUps
from ui.popups.sql_pop_ups import SqlPopUps

class MainView():
    """
    Vasemman kehyksen päänäkymä. 

    Sisältä napit objektien luonnille, tallennusten käsittelyille
    ja ohjelmasta poistumiselle, sekä checkboxit canvasin tekstien
    ja värimaailman muuttamiselle.
    """

    def __init__(self, master, canvas_handler):
        """Luokan konstruktori, joka luo uuden käyttöliittymänäkymän.

        Args:
            master: juuri, jonka sisään käyttöliittymä-luokka luodaan.
            canvas_handler: canvasin logiikasta vastaava luokka.
        """
        self._root = master
        self._canvas_handler = canvas_handler
        self._left_frame = None
        self._width_entry = None
        self._height_entry = None
        self._text_entry = None
        self._error_label = None

    def _forget_frame(self):
        """Unohdetaan kehysnäkymän pakkaus."""
        if self._left_frame != None:
            self._left_frame.pack_forget()

    def _initialize(self):
        """Alustetaan luokan näkymä ja siihen
        liittyvä popup-luokka."""
        self._left_frame = tk.Frame(
            master=self._root, bg="gray", width=450, height=600)
        self._left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self._left_frame.pack_propagate(0)
        self._left_frame.pack(fill=constants.X)

        self._json_pop_ups = JsonPopUps(self._root, self._canvas_handler)
        self._sql_pop_ups = SqlPopUps(self._root, self._canvas_handler)

        self._initiliaze_input_fields_labels()
        self._initiliaze_buttons()

    def _initiliaze_buttons(self):
        """Alustetaan napit."""
        create_room_button = tk.Button(
            master=self._left_frame,
            text="Create Room",
            command=lambda: (self.validate_input("room")))

        create_rectangle_button = tk.Button(
            master=self._left_frame,
            text="Create Rectangle",
            command=lambda: (self.validate_input("rectangle")))

        create_oval_button = tk.Button(
            master=self._left_frame,
            text="Create Oval",
            command=lambda: (self.validate_input("oval")))

        create_room_button.pack(side=tk.TOP, padx=10, pady=10)
        create_rectangle_button.pack(side=tk.TOP, padx=10, pady=10)
        create_oval_button.pack(side=tk.TOP, padx=10, pady=10)

        save_button = tk.Button(master=self._left_frame,
                                text="Save File")
        save_button.pack(side=tk.RIGHT, padx=10, pady=10)
        save_button.config(command=self.choose_save)

        load_button = tk.Button(master=self._left_frame,
                                text="Load File")
        load_button.pack(side=tk.RIGHT, padx=10, pady=10)
        load_button.config(command=self.choose_load)

        delete_save_button = tk.Button(master=self._left_frame,
                                       text="Delete File")
        delete_save_button.pack(side=tk.RIGHT, padx=10, pady=10)
        delete_save_button.config(command=self.choose_delete)

        exit_button = tk.Button(master=self._left_frame,
                                text="Exit")
        exit_button.pack(side=tk.LEFT, padx=20, pady=10)
        exit_button.config(command=self._json_pop_ups.exit_popup)

    def _initiliaze_input_fields_labels(self):
        """Alustettavat syötekentät, checkboxit ja muu teksti."""
        create_label = tk.Label(master=self._left_frame,
                                text="CREATE SHAPE",
                                font=("Arial", 20),
                                bg="gray")
        create_label.pack(side=tk.TOP, padx=10, pady=5)

        self._error_label = tk.Label(master=self._left_frame,
                                     fg="red", bg="gray")
        self._error_label.pack(side=tk.TOP, padx=10, pady=10)

        width_label = tk.Label(master=self._left_frame,
                               text="Width (cm):")
        width_label.pack(side=tk.TOP, padx=10, pady=5)
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

        self._checkbox_var = tk.BooleanVar(value=False)
        checkbox = tk.Checkbutton(master=self._left_frame,
                                  text="texts on/off",
                                  variable=self._checkbox_var)
        checkbox.pack(side=tk.TOP, padx=10, pady=10)
        checkbox.config(command=lambda: (
            self._canvas_handler.texts_on_off(self._checkbox_var.get())))

        self._checkbox_var_2 = tk.BooleanVar(value=False)
        checkbox_mode = tk.Checkbutton(master=self._left_frame,
                                       text="blueprint mode on/off",
                                       variable=self._checkbox_var_2)
        checkbox_mode.pack(side=tk.TOP, padx=10, pady=10)
        checkbox_mode.config(command=lambda: (
            self._canvas_handler.dark_mode(self._checkbox_var_2.get())))

    def _check_state(self):
        """Tarkistaa mikä canvasin tilanne on
        ja asettaa checkboxit sen mukaisesti"""
        state = self._canvas_handler.get_current_text_state()
        self._checkbox_var.set(state)

        state2 = self._canvas_handler.get_current_color()
        self._checkbox_var_2.set(state2)

    def choose_save(self):
        """Valitse tallennustavan tyyppi (json, sql)."""
        top = tk.Toplevel(self._root)
        top.geometry("850x100")
        top.title("")
        text_label = tk.Label(master=top,
                              text="Do you want to save to a json file or to SQL database?")
        text_label.pack(side=tk.TOP, padx=10, pady=5)

        exit_button = tk.Button(master=top,
                                text="Cancel")
        exit_button.pack(side=tk.LEFT, padx=10, pady=10)
        exit_button.config(command=lambda: (
            top.destroy()))

        json_save_button = tk.Button(master=top,
                                     text="Save to json")
        json_save_button.pack(side=tk.LEFT, padx=10, pady=10)
        json_save_button.config(command=lambda: (
            top.destroy(), self._json_pop_ups.save_popup()))

        sql_save_button = tk.Button(master=top,
                                    text="Save to SQL")
        sql_save_button.pack(side=tk.LEFT, padx=10, pady=10)
        sql_save_button.config(command=lambda: (
            top.destroy(), self._sql_pop_ups.save_popup()))

        all_json_button = tk.Button(master=top,
                                    text="Show all json save names")
        all_json_button.pack(side=tk.RIGHT, padx=10, pady=10)
        all_json_button.config(command=lambda: (
            top.destroy(), self._json_pop_ups.show_all()))

        all_sql_button = tk.Button(master=top,
                                   text="Show all SQL save names")
        all_sql_button.pack(side=tk.RIGHT, padx=10, pady=10)
        all_sql_button.config(command=lambda: (
            top.destroy(), self._sql_pop_ups.show_all()))

    def choose_load(self):
        """Valitse ladattavan tiedoston tyyppi (json, sql)."""
        top = tk.Toplevel(self._root)
        top.geometry("850x100")
        top.title("")
        text_label = tk.Label(master=top,
                              text="Do you want to load a json file or a SQL record?")
        text_label.pack(side=tk.TOP, padx=10, pady=5)

        exit_button = tk.Button(master=top,
                                text="Cancel")
        exit_button.pack(side=tk.LEFT, padx=10, pady=10)
        exit_button.config(command=lambda: (
            top.destroy()))

        json_load_button = tk.Button(master=top,
                                     text="Load json file")
        json_load_button.pack(side=tk.LEFT, padx=10, pady=10)
        json_load_button.config(command=lambda: (
            top.destroy(), self._json_pop_ups.load_popup()))

        sql_load_button = tk.Button(master=top,
                                    text="Load SQL save")
        sql_load_button.pack(side=tk.LEFT, padx=10, pady=10)
        sql_load_button.config(command=lambda: (
            top.destroy(), self._sql_pop_ups.load_record_popup()))

        all_json_button = tk.Button(master=top,
                                    text="Show all json save names")
        all_json_button.pack(side=tk.RIGHT, padx=10, pady=10)
        all_json_button.config(command=lambda: (
            top.destroy(), self._json_pop_ups.show_all()))

        all_sql_button = tk.Button(master=top,
                                   text="Show all SQL save names")
        all_sql_button.pack(side=tk.RIGHT, padx=10, pady=10)
        all_sql_button.config(command=lambda: (
            top.destroy(), self._sql_pop_ups.show_all()))

    def choose_delete(self):
        """Valitse poistettavan tiedoston tyyppi, (json, sql)."""
        top = tk.Toplevel(self._root)
        top.geometry("850x100")
        top.title("Choose savemethod")
        text_label = tk.Label(master=top,
                              text="Do you want to delete a json file or from the SQL record?")
        text_label.pack(side=tk.TOP, padx=10, pady=5)

        exit_button = tk.Button(master=top,
                                text="Cancel")
        exit_button.pack(side=tk.LEFT, padx=10, pady=10)
        exit_button.config(command=lambda: (
            top.destroy()))

        json_delete_button = tk.Button(master=top,
                                       text="Delete json file")
        json_delete_button.pack(side=tk.LEFT, padx=10, pady=10)
        json_delete_button.config(command=lambda: (
            top.destroy(), self._json_pop_ups.delete_file_popup()))

        sql_delete_button = tk.Button(master=top,
                                      text="Delete from SQL record")
        sql_delete_button.pack(side=tk.LEFT, padx=10, pady=10)
        sql_delete_button.config(command=lambda: (
            top.destroy(), self._sql_pop_ups.delete_record_popup()))

        all_json_button = tk.Button(master=top,
                                    text="Show all json save names")
        all_json_button.pack(side=tk.RIGHT, padx=10, pady=10)
        all_json_button.config(command=lambda: (
            top.destroy(), self._json_pop_ups.show_all()))

        all_sql_button = tk.Button(master=top,
                                   text="Show all SQL save names")
        all_sql_button.pack(side=tk.RIGHT, padx=10, pady=10)
        all_sql_button.config(command=lambda: (
            top.destroy(), self._sql_pop_ups.show_all()))

    def validate_input(self, shape_type):
        """Validoi, ovatko syötekentistä saadut
         tiedot halutun mukaisia.

        Args:
            shape_type: muoto-attribuutti.

        Returns:
            True, jos oikeanlaisia,
            False, jos ei.
        """
        text = self._text_entry.get()
        width = self._width_entry.get()
        height = self._height_entry.get()
        if width and height:
            try:
                if int(width) in range(5, 2001) and int(height) in range(5, 2001):
                    self._canvas_handler.create_shape(
                        int(width), int(height), text, shape_type)
                    self._error_label.config(text="", bg="gray")
                    return True
                else:
                    self._error_label.config(
                        text="Width and height must be a whole number between 5 and 2000",
                        bg="lightgray")
                    return False

            except ValueError:
                self._error_label.config(
                    text="Width and height must be a whole number between 5 and 2000",
                    bg="lightgray")
                return False
        else:
            self._error_label.config(
                text="Width and height must be a whole number between 5 and 2000",
                bg="lightgray")
            return False
