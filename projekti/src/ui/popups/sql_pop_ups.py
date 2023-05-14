import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

from file_handler.sql_handler import SqlHandler
from logic_handler.data_handler import DataHandler


class SqlPopUps:
    """Luokka, joka vastaa popup ikkunoista.
    """

    def __init__(self, master, canvas_handler):
        """Luokan konstruktori. Alustaa kutsuttavat luokat.
        Args:
            master: juuri, jonka sisään käyttöliittymä-luokka luodaan.
            canvas_handler: canvasin logiikasta vastaava luokka.
        """
        self._root = master
        self._canvas_handler = canvas_handler
        self._data_handler = DataHandler(self._canvas_handler)
        self._save_handler = SqlHandler()

    def show_all_saves(self):
        top = tk.Toplevel(self._root)
        top.geometry("400x100")
        top.title("Save Files")
        files = self._save_handler.get_all_save_files()

        if files == False:
            text_label = tk.Label(master=top,
                                  text=f"No files found")
        else:
            text_label = tk.Label(master=top,
                                  text=f"{files}")
        text_label.pack(side=tk.TOP, padx=10, pady=5)

    def save_popup(self):
        """Tallennus popup"""
        filename = askstring("", "Enter file name to save to")
        if filename == "":
            self.save_popup()
        elif filename == None:
            return
        else:
            self.save_confirm(filename)

    def save_confirm(self, filename):
        """Tallennuksen tiedostonimen tarkistus"""
        ask = self._save_handler.record_exists(filename)
        if ask == True:
            data = self._data_handler.get_sql_data()
            self._save_handler.add_data(data)
            self._save_handler.save(filename)
            messagebox.showinfo(
                "Save", f"The file has been saved to '{filename}'.")
        else:
            response = messagebox.askyesno(
                "", f"File already exists, do you want to overwrite file '{filename}'?")
            if response == 1:
                self._save_handler.delete_record(filename)
                self._save_handler.save(filename)
                messagebox.showinfo(
                    "Save", f"The file has been saved to '{filename}'.")
            else:
                return

    def load_record_popup(self):
        """Latauksen popup"""
        filename = askstring("", "Enter file name to load from")
        if filename == "":
            self.load_record_popup()
        elif filename == None:
            return
        else:
            self.load_confirm(filename)

    def load_confirm(self, filename):
        """Latauksen tiedostonimen tarkistus"""
        ask = self._save_handler.load_record(filename)
        if ask == False:
            messagebox.showerror("Error", f"Filename '{filename}' not found.")
        self._data_handler.unload_sql_data(ask)

    def delete_record_popup(self):
        """Tiedoston poisto popup"""
        filename = askstring("", "Enter save name to delete")
        if filename == "":
            self.delete_record_popup()
        elif filename == None:
            return
        else:
            ask = self._save_handler.record_exists(filename)
            if ask == True:
                messagebox.showinfo(
                    "", f"'{filename}' save doesn't exist.")
            else:
                save = self._save_handler.delete_record(filename)
                if save == True:
                    messagebox.showinfo(
                        "", f"'{filename}' save has been deleted.")
                else:
                    messagebox.showinfo(
                        "", f"'Error happened.")

    def show_all(self):
        files = self._save_handler.get_all_save_files()
        if files is False:
            messagebox.showinfo(
                "SQL Saves", "No saves found.")
            return
        files = str(files)
        files = files.replace("[", "").replace(
            "]", "").replace("(", "").replace(")", "")
        messagebox.showinfo(
            "SQL Saves", f"{files}.")
