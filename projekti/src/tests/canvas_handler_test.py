import unittest
import tkinter as tk

from logic_handler.canvas_handler import CanvasHandler
from logic_handler.coord_handler import CoordHandler

class TestControl(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(width=800, height=600, bg="white")
        self.canvas_handler = CanvasHandler(
            self.canvas)
        self.coord_handler = CoordHandler(
            self.canvas)

    def test_clear_canvas(self):
        self.canvas_handler.create_shape(100, 50, "test", "oval")
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        self.canvas_handler.create_shape(100, 50, "test", "room")
        objects = self.canvas.find_withtag("shape")
        self.assertEqual(objects, (1, 5, 9))
        self.assertEqual(3, len(objects))

    def test_create_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        object = self.canvas.find_withtag("shape")
        self.canvas_handler.selected_shape = object[0]
        self.assertEqual(1, object[0])

    def test_create_text(self):
        self.canvas_handler.create_texts(100, 50, "test")
        objects = self.canvas.find_withtag("text")
        self.canvas_handler.selected_shape = objects[0]
        self.assertEqual(1, objects[0])

        objects = self.canvas.find_withtag("text")
        self.canvas_handler.selected_shape = objects[1]
        self.assertEqual(2, objects[1])

        objects = self.canvas.find_withtag("text")
        self.assertEqual((1, 2, 3), objects)

    def test_get_object_color(self):
        color, linecolor = self.canvas_handler.get_object_color(True, "room")
        self.assertEqual("#104E8B", color)
        self.assertEqual("white", linecolor)

        color, linecolor = self.canvas_handler.get_object_color(False, "room")
        self.assertEqual("white", color)
        self.assertEqual("black", linecolor)

        color, linecolor = self.canvas_handler.get_object_color(
            False, "rectangle")
        self.assertEqual("lightgray", color)
        self.assertEqual("black", linecolor)

        color, linecolor = self.canvas_handler.get_object_color(
            True, "rectangle")
        self.assertEqual("#104E8B", color)
        self.assertEqual("white", linecolor)

    def test_current_color(self):
        ask = self.canvas_handler.get_current_color()
        self.assertEqual(False, ask)

        self.canvas.configure(bg="#104E8B")
        ask = self.canvas_handler.get_current_color()
        self.assertEqual(True, ask)

    def test_current_text_state(self):
        ask = self.canvas_handler.get_current_text_state()
        self.assertEqual(False, ask)

        self.canvas_handler.create_texts(100, 50, "test")
        self.canvas.itemconfigure("text", state="hidden")
        ask = self.canvas_handler.get_current_text_state()
        self.assertEqual(True, ask)

        self.canvas.itemconfigure("text", state="normal")
        ask = self.canvas_handler.get_current_text_state()
        self.assertEqual(False, ask)

    def test_delete_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        shapes = self.canvas_handler.shapes
        self.assertEqual(4, len(shapes))

        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.canvas_handler.delete_shape()
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual((), objects)

    def test_dont_delete_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(1, len(objects))

        self.canvas_handler.delete_shape()
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(1, len(objects))

    def test_change_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.assertEqual(1, objects[0])

        self.canvas_handler.change_shape(300, 400, "tuoli")
        shape = self.canvas_handler.shapes[0]
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(300, shape.width)
        self.assertEqual(400, shape.height)
        self.assertEqual("tuoli", shape.text)

    def test_dont_change_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(1, objects[0])

        self.canvas_handler.change_shape(300, 400, "tuoli")
        shape = self.canvas_handler.shapes[0]
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(100, shape.width)
        self.assertEqual(50, shape.height)
        self.assertEqual("test", shape.text)

    def test_change_text(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.canvas_handler.change_texts(300, 400, "tuoli")
        texts = self.canvas_handler.shapes[1]
        self.assertEqual(200, texts.top_left_x)
        self.assertEqual(460, texts.top_left_y)

        texts = self.canvas_handler.shapes[2]
        self.assertEqual(367, texts.top_left_x)
        self.assertEqual(250, texts.top_left_y)

        texts = self.canvas_handler.shapes[3]
        self.assertEqual(200, texts.top_left_x)
        self.assertEqual(40, texts.top_left_y)

    def test_dont_change_text(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        self.canvas_handler.change_texts(300, 400, "tuoli")
        texts = self.canvas_handler.shapes[1]
        self.assertEqual(50, texts.top_left_x)
        self.assertEqual(50, texts.top_left_y)

        texts = self.canvas_handler.shapes[2]
        self.assertEqual(50, texts.top_left_x)
        self.assertEqual(50, texts.top_left_y)

        texts = self.canvas_handler.shapes[3]
        self.assertEqual(50, texts.top_left_x)
        self.assertEqual(50, texts.top_left_y)

    def test_get_all(self):
        ask = self.canvas_handler.get_all()
        self.assertEqual(None, ask)

        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        text, x_1, y_1, x_2, y_2 = self.canvas_handler.get_all()
        self.assertEqual("test", text)
        self.assertEqual((50, 50, 150, 100), (x_1, y_1, x_2, y_2))

    def test_lower_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("", state)

        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        state2 = self.canvas.itemcget(5, "state")
        self.assertEqual("", state2)

        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.canvas_handler.lower_shape()
        state3 = self.canvas.itemcget(2, "state")
        self.assertEqual("normal", state3)

        state4 = self.canvas.itemcget(1, "state")
        self.assertEqual("", state4)

    def test_dont_lower_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("", state)

        self.canvas_handler.lower_shape()
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("", state)

    def test_lift_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("", state)

        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        state2 = self.canvas.itemcget(5, "state")
        self.assertEqual("", state2)

        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[1]
        self.canvas_handler.lift_shape()
        state3 = self.canvas.itemcget(2, "state")
        self.assertEqual("normal", state3)

    def test_dont_lift_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("", state)

        self.canvas_handler.lift_shape()
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("", state)

    def test_copy_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.copy_shape()
        self.assertEqual(1, len(objects))

        self.canvas_handler.selected_shape = objects[0]
        self.canvas_handler.copy_shape()
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(2, len(objects))

    def test_texts_on_off(self):
        self.canvas_handler.create_texts(100, 50, "test")
        state = self.canvas.itemcget(1, "state")
        self.assertEqual("normal", state)

        self.canvas_handler.texts_on_off(True)
        state1 = self.canvas.itemcget(1, "state")
        self.assertEqual("hidden", state1)

        self.canvas_handler.texts_on_off(False)
        state2 = self.canvas.itemcget(1, "state")
        self.assertEqual("normal", state2)

    def test_dark_mode(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        bgcolor = self.canvas.cget("bg")
        self.assertEqual("white", bgcolor)

        rectcolor = self.canvas.itemcget(1, "fill")
        rectlinecolor = self.canvas.itemcget(1, "outline")
        self.assertEqual("lightgray", rectcolor)
        self.assertEqual("black", rectlinecolor)

        textcolor = self.canvas.itemcget(2, "fill")
        self.assertEqual("black", textcolor)

        self.canvas_handler.dark_mode(True)
        bgcolorchange = self.canvas.cget("bg")
        self.assertEqual("#104E8B", bgcolorchange)

        rectcolorchange = self.canvas.itemcget(1, "fill")
        rectlinecolorchange = self.canvas.itemcget(1, "outline")
        self.assertEqual("#104E8B", rectcolorchange)
        self.assertEqual("white", rectlinecolorchange)

        textcolorchange = self.canvas.itemcget(2, "fill")
        self.assertEqual("white", textcolorchange)

    def test_dont_create_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "test")
        objects = self.canvas.find_withtag("shape")
        self.assertEqual(0, len(objects))

        shapes = self.canvas_handler.shapes
        self.assertEqual(0, len(shapes))

    def test_release_move(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.assertEqual(1, objects[0])

        self.canvas_handler.release_move()
        ask = self.canvas_handler.selected_shape
        self.assertEqual(None, ask)
