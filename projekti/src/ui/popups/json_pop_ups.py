from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

from file_handler.json_handler import JsonHandler
from logic_handler.data_handler import DataHandler


class JsonPopUps:
    """Luokka, joka vastaa popup ikkunoista.
    """

    def __init__(self, master, canvas_handler):
        """Luokan konstruktori. Alustaa kutsuttavat luokat.

        Args:
            master: juuri, jonka sisään käyttöliittymä-luokka luodaan.
            canvas_handler: canvasin logiikasta vastaava luokka
        """
        self._root = master
        self._canvas_handler = canvas_handler
        self._data_handler = DataHandler(self._canvas_handler)
        self._save_handler = JsonHandler()

    def save_popup(self):
        """Tallennus popup"""
        filename = askstring("", "Enter filename to save to")
        if filename == "":
            self.save_popup()
        elif filename == None:
            return
        else:
            self.save_confirm(filename)

    def save_confirm(self, filename):
        """Tallennuksen tiedostonimen tarkistus"""
        data = self._data_handler.get_json_data()
        ask = self._save_handler.save_exists(filename)
        if ask == False:
            self._save_handler.add_data(data)
            self._save_handler.save(filename)
            messagebox.showinfo(
                "Save", f"The file has been saved to '{filename}'.")
        else:
            response = messagebox.askyesno(
                "", f"File already exists, do you want to overwrite file '{filename}'?")
            if response == 1:
                self._save_handler.add_data(data)
                self._save_handler.save(filename)
                messagebox.showinfo(
                    "Save", f"The file has been saved to '{filename}'.")
            else:
                return

    def load_popup(self):
        """Latauksen popup"""
        filename = askstring("", "Enter filename to load from")
        if filename == "":
            self.load_popup()
        elif filename == None:
            return
        else:
            self.load_confirm(filename)

    def load_confirm(self, filename):
        """Latauksen tiedostonimen tarkistus"""
        ask = self._save_handler.load(filename)
        if ask == False:
            messagebox.showerror("Error", f"Filename '{filename}' not found.")

        else:
            ask = self._data_handler.unload_json_data(ask)
            if ask == True:
                messagebox.showinfo(
                    "", f"Filename '{filename}' loaded successfully.")
            else:
                messagebox.showerror(
                    "", f"Filename '{filename}' could not be loaded")

    def delete_file_popup(self):
        """Tiedoston poisto popup"""
        filename = askstring("", "Enter filename to delete")
        if filename == "":
            self.delete_file_popup()
        elif filename == None:
            return
        else:
            self.delete_confirm(filename)

    def delete_confirm(self, filename):
        """Tiedoston poiston tarkistus"""
        ask = self._save_handler.delete_data(filename)
        if ask == True:
            messagebox.showinfo("", f"Filename '{filename}' has been deleted.")
        if ask == False:
            messagebox.showerror("Error", f"Filename '{filename}' not found")

    def exit_popup(self):
        """Ohjelmasta poistuminen"""
        response = messagebox.askyesno(
            "", "Are you sure you want to exit the program?")
        if response == 1:
            self._root.quit()
        else:
            return

    def show_all(self):
        files = self._save_handler.get_all_file_names()
        if files is None:
            messagebox.showinfo(
                "JSON Saves", "No savefiles found.")
            return
        files = str(files)
        files = files.replace("[", "").replace("]", "")
        messagebox.showinfo(
            "JSON Saves", f"{files}.")
