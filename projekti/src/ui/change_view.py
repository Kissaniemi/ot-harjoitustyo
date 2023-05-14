import tkinter as tk


class ChangeView():
    """Vasemman kehyksen näkymä, johon syötetään shape-objektin 
    muutettavat tiedot (koko, nimi).

    Sisältää myös napit objektin poistolle (delete), objektin 
    kierrolle (rotate) ja koko canvasin tyhjentämiselle (clear all).
    """

    def __init__(self, master, canvas_handler):
        """Luokan konstruktori, joka luo pohjan uudelle ikkunalle

        Args:
            parent: pääikkuna, jonka päälle tulee
            canvas: canvas, josta tietoa haetaan
            event_handler: EventHandler luokka, jota kutsutaan muutosten tekemiseen
        """
        self._root = master
        self._canvas_handler = canvas_handler
        self._left_frame = None
        self.selected_shape = None

    def _forget_frame(self):
        if self._left_frame != None:
            self._left_frame.pack_forget()

    def _initiliaze(self):
        """Alustetaan näkymän sisältö"""

        self._left_frame = tk.Frame(
            master=self._root, bg="gray", width=450, height=600)
        self._left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self._left_frame.pack_propagate(0)

        top_text_label = tk.Label(self._left_frame, text="CHANGE SHAPE",
                                  font=("Arial", 20),
                                  bg="gray")
        top_text_label.pack(side=tk.TOP, padx=10, pady=5)

        self._error_label = tk.Label(master=self._left_frame,
                                     fg="red", bg="gray")
        self._error_label.pack(side=tk.TOP, padx=10, pady=10)

        new_width_label = tk.Label(self._left_frame, text="Width (cm):")
        new_width_label.pack(side=tk.TOP, padx=10, pady=5)
        self.new_width_entry = tk.Entry(self._left_frame)
        self.new_width_entry.pack(side=tk.TOP, padx=10, pady=5)

        new_height_label = tk.Label(self._left_frame, text="Height (cm):")
        new_height_label.pack(side=tk.TOP, padx=10, pady=5)
        self.new_height_entry = tk.Entry(self._left_frame)
        self.new_height_entry.pack(side=tk.TOP, padx=10, pady=5)

        new_text_label = tk.Label(self._left_frame, text="Text")
        new_text_label.pack(side=tk.TOP, padx=10, pady=5)
        self.new_text_entry = tk.Entry(self._left_frame)
        self.new_text_entry.pack(side=tk.TOP, padx=10, pady=5)

        change_button = tk.Button(self._left_frame, text="Change",
                                  command=lambda: (self.validate_input()), bg="lightgray")
        change_button.pack(side=tk.TOP, padx=10, pady=10)

        front_button = tk.Button(self._left_frame, text="Move front",
                                 command=self._canvas_handler.lift_shape)
        front_button.pack(side=tk.TOP, padx=20, pady=10)

        back_button = tk.Button(self._left_frame, text="Move back",
                                command=self._canvas_handler.lower_shape)
        back_button.pack(side=tk.TOP, padx=20, pady=10)

        copy_button = tk.Button(self._left_frame, text="Copy",
                                command=self._canvas_handler.copy_shape)
        copy_button.pack(side=tk.RIGHT, padx=10, pady=10)

        cancel_button = tk.Button(self._left_frame, text="Delete",
                                  command=lambda: (self._canvas_handler.delete_shape()), bg="lightgray")
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        copy_button = tk.Button(self._left_frame, text="Clear Canvas",
                                command=lambda: (self._canvas_handler.clear_canvas()))
        copy_button.pack(side=tk.LEFT, padx=10, pady=10)

    def validate_input(self):
        """Validoi, ovatko syötekentistä saadut
         tiedot halutun mukaisia.

        Returns:
            True, jos oikeanlaisia,
            False, jos ei.
        """
        self.selected_shape = self._canvas_handler.selected_shape
        if self.selected_shape is not None:
            text = self.new_text_entry.get()
            width = self.new_width_entry.get()
            height = self.new_height_entry.get()
            if width and height:
                try:
                    if int(width) in range(5, 2001) and int(height) in range(5, 2001):
                        self._canvas_handler.change_shape(
                            int(width), int(height), text)
                        self._canvas_handler.change_texts(
                            int(width), int(height), text)
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
