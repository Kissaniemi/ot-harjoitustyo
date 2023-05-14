import tkinter as tk


class CanvasView:
    """Oikean kehyksen näkymä, jossa alustetaan canvas
    muiden luokkien käyttöön. Sisältää napin joka
    vastaa vasemman kehyksen näkymän vaihtumisesta.
    """

    def __init__(self, master, show_main, show_change):
        """Luokan konstruktori, joka luo uuden käyttöliittymänäkymän.

        Args:
            master: juuri, jonka sisään käyttöliittymä-luokka luodaan.
            show_main: vaihtaa vasemman kehyksen päänäkymäksi.
            show_change: vaihtaa vasemman kehyksen "muutos"näkymäksi.
        """
        self._root = master

        self._canvas_frame = tk.Frame(self._root, width=1000, height=800)
        self._canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self._canvas_frame.pack_propagate(0)

        self._canvas = tk.Canvas(master=self._canvas_frame,
                                 bg="white")

        self.show_main_view = show_main
        self.show_change_view = show_change
        self.change_button = None
        self.shapes = []
        self.data = {"shapes": []}

    def _forget_frame(self):
        """Unohdetaan kehysnäkymän pakkaus."""
        if self._canvas_frame != None:
            self._canvas_frame.pack_forget()

    def _initiliaze(self):
        """Alustetan näkymä."""
        self._canvas.pack(side=tk.RIGHT, fill=tk.BOTH,
                          expand=True)

        self.change_button = tk.Button(self._canvas, text="Change view",
                                       command=lambda: (self.show_change_view(), self.change_buttons()), bg="lightgray")
        self.change_button.pack(side=tk.TOP, padx=10, pady=10)

    def change_buttons(self):
        """Vaihdetaan vaihtonapin tekstiä ja komentoa 
        näkymää vaihdettaessa."""
        text = self.change_button.cget("text")
        if text == "Change view":
            self.change_button.configure(text="Create View", command=lambda: (
                self.show_main_view(), self.change_buttons()))
        else:
            self.change_button.configure(text="Change view", command=lambda: (
                self.show_change_view(), self.change_buttons()))
