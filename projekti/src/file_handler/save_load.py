import json
import os

from shapes.shape_class import Shape


class SaveHandler():
    """Luokka joka vastaa tallentamisesta ja latauksesta.

    Attributes:
        data: Canvasin objektien keräämiseen tarkoitettu kirjasto.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden kirjaston."""
        self.data = {}

    def get_data(self, canvas):
        """Tyhjentää ensin nykyisen data-kirjaston ja hakee canvasilta 
        kaikki 'shape' tyypin objektit ja 'tallentaa' ne uuteen kirjastoon.

        Args: 
            canvas: canvas, josta tiedot haetaan.
        """
        self.data.clear()
        self.data = {"shapes": []}

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

    def save(self, filename):
        """Luo/Avaa tiedostonimen mukaisen json-tiedoston 
        ja tallentaa data-kirjaston sisällön sinne.

        Args:
            filename: tiedoston nimi johon tallennetaan.

        Returns:
            True. 
        """
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
            return True

        except FileNotFoundError:
            return False

    def unload_data(self, canvas):
        """Hakee data-kirjastosta tiedot ja luo Shape-luokan 
        create_shape funktiolla objektit canvasille.

        Args: 
            canvas: canvas, jolle objektit luodaan.
        """
        for state in self.data["shapes"]:
            shape = Shape(canvas, state["width"], state["height"], state["name"],
                          state["shape"], state["x"], state["y"])
            shape.create_shape(state["shape"])

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
