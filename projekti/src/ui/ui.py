from ui.main_view import MainView
from ui.change_view import ChangeView
from ui.canvas_view import CanvasView
from logic_handler.canvas_handler import CanvasHandler


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka.
    """

    def __init__(self, root):
        """Luokan konstruktori. Alustetaan kehysten paikat ja canvas.
        Args:
            root:
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """
        self._root = root
        self._left_frame_view = None
        self._right_frame_view = None

        self._canvas_view = CanvasView(
            self._root,
            self._show_main_view,
            self._show_change_view)

        self._canvas = self._canvas_view._canvas

        self._canvas_control = CanvasHandler(
            self._canvas)

        self._change_view = ChangeView(
            self._root,
            self._canvas_control)

        self._main_view = MainView(
            self._root,
            self._canvas_control)

    def start(self):
        """Käynnistää käyttöliittymän päänäkymän.
        """
        self._show_main_view()
        self._show_canvas_view()

    def _show_main_view(self):
        """Käyttöliittymän päänäkymän käynnistys.
        """
        if self._left_frame_view == self._change_view:
            self._change_view._forget_frame()
        elif self._left_frame_view == self._main_view:
            return

        self._left_frame_view = self._main_view
        self._main_view._initialize()
        self._main_view._check_state()

    def _show_change_view(self):
        """Käyttöliittymän muutos-näkymän käynnistys,
        jos jo käynnisssä, hakee vain uudet syötteet.
        """
        if self._left_frame_view != self._change_view:
            self._left_frame_view = self._change_view
            self._main_view._forget_frame()
            self._change_view._initiliaze()

    def _show_canvas_view(self):
        """Käyttöliittymän canvas-näkymän käynnistys.
        """
        self._right_frame_view = self._canvas_view
        self._canvas_view._initiliaze()
        self._canvas_control._initiliaze()
