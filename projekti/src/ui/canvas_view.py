import tkinter as tk


class CanvasView:
    def __init__(self, master, show_main, show_change):
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

    def _initiliaze(self):
        self._canvas.pack(side=tk.RIGHT, fill=tk.BOTH,
                          expand=True)

        self.change_button = tk.Button(self._canvas, text="Change view",
                                       command=lambda: (self.show_change_view(), self.change_buttons()), bg="lightgray")
        self.change_button.pack(side=tk.TOP, padx=10, pady=10)

    def change_buttons(self):
        text = self.change_button.cget("text")
        if text == "Change view":
            self.change_button.configure(text="Create View", command=lambda: (
                self.show_main_view(), self.change_buttons()))
        else:
            self.change_button.configure(text="Change view", command=lambda: (
                self.show_change_view(), self.change_buttons()))
