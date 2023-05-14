import json
import os
from glob import glob

class JsonHandler():
    """Luokka joka vastaa tallentamisesta ja latauksesta.
    """
    def __init__(self):
        """Luokan konstruktori, joka alustaa uuden datakirjaston."""
        self.data = {}

    def add_data(self, data):
        """Tyhjentää ensin nykyisen data-kirjaston ja hakee canvasilta 
        kaikki 'shape' tyypin objektit ja 'tallentaa' ne uuteen kirjastoon.
        """
        self.data.clear()
        self.data = data

    def save_exists(self, filename):
        """Luo/Avaa tiedostonimen mukaisen json-tiedoston 
        ja tallentaa data-kirjaston sisällön sinne.

        Args:
            filename: tiedoston nimi johon tallennetaan.

        Returns:
            True, jos samannimistä tiedostoa on olemassa,
            False, jos ei ole.
        """
        try:
            with open(f"{filename}.json", "r", encoding="utf-8") as file:
                file.close()
                return True

        except FileNotFoundError:
            return False

    def save(self, filename):

        with open(f"{filename}.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)
            return True

    def load(self, filename):
        """Avaa tiedostonimen mukaisen json-tiedoston 
        ja hakee sieltä objektien tiedot data-kirjastoon.

        Args:
            filename: tiedoston nimi johon tallennetaan.

        Returns:
            True, jos lataus onnistuu, muuten False. 
        """
        try:
            with open(f"{filename}.json", "r", encoding="utf-8") as file:
                self.data = json.load(file)
            return self.data

        except FileNotFoundError:
            return False

    def delete_data(self, filename):
        """Hakee tiedostonimen mukaisen tiedoston ja jos se on olemassa, poistaa sen.

        Args:
            filename: tiedoston nimi joka poistetaan.

        Returns: 
            True, jos tiedosto löytyy ja poisto onnistuu, muuten False.
        """
        if os.path.exists(f"{filename}.json"):
            os.remove(f"{filename}.json")
            return True

        return False

    def get_all_file_names(self):
        content = []

        json_pattern = "*.json"
        file_list = glob(json_pattern)
        for file in file_list:
            content.append((file))
        if not content:
            return None
        return content
