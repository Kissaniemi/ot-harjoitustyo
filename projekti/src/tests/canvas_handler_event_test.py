import unittest
import tkinter as tk

from logic_handler.canvas_handler import CanvasHandler


class TestEvents(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.event = tk.Event()
        self.canvas = tk.Canvas(width=800, height=600, bg="white")
        self.canvas_handler = CanvasHandler(
            self.canvas)

    def test_select_object(self):
        self.event.x, self.event.y = 60, 60
        self.canvas_handler.select_object(self.event)
        self.canvas_handler.create_texts(100, 50, "test")
        self.canvas_handler.select_object(self.event)
        self.assertEqual(self.canvas_handler.selected_shape, None)

        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        self.canvas_handler.select_object(self.event)

        objects = self.canvas.find_withtag("shape")
        self.assertEqual(self.canvas_handler.selected_shape, objects[0])

        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        self.canvas_handler.select_object(self.event)
        objects = self.canvas.find_withtag("shape")
        self.assertEqual(self.canvas_handler.selected_shape, objects[1])

        self.event.x, self.event.y = 400, 500
        self.canvas_handler.select_object(self.event)
        self.assertEqual(self.canvas_handler.selected_shape, None)

    def test_dark_select_object(self):
        self.canvas.configure(bg="#104E8B")

        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        self.event.x, self.event.y = 60, 60
        self.canvas_handler.select_object(self.event)
        objects = self.canvas.find_withtag("shape")
        self.assertEqual(self.canvas_handler.selected_shape, objects[0])

    def test_object_move(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.event.x, self.event.y = 300, 400
        self.canvas_handler.object_move(self.event)
        new_coords = self.canvas_handler._canvas.coords(objects[0])
        self.assertEqual([300, 400, 400, 450], new_coords)

    def test_dont_move_object(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.assertEqual(1, len(objects))

        self.event.x, self.event.y = 300, 400
        self.canvas_handler.object_move(self.event)
        new_coords = self.canvas_handler._canvas.coords(objects[0])
        self.assertEqual([50, 50, 150, 100], new_coords)

    def test_rotate_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        self.event.x, self.event.y = 300, 400
        self.canvas_handler.rotate_shape(self.event)
        shape = self.canvas_handler.shapes[0]
        self.assertEqual((100, 50, "test"),
                         (shape.width, shape.height, shape.text))

    def test_dont_rotate_shape(self):
        self.canvas_handler.create_shape(100, 50, "test", "rectangle")
        objects = self.canvas.find_withtag("rectangle")
        self.canvas_handler.selected_shape = objects[0]
        self.event.x, self.event.y = 300, 400
        self.canvas_handler.rotate_shape(self.event)
        shape = self.canvas_handler.shapes[0]
        self.assertEqual((50, 100, "test"),
                         (shape.width, shape.height, shape.text))
