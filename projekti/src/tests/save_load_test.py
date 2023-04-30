import tkinter as tk
import unittest

from file_handler.save_load import SaveHandler
from shapes.shape_class import Shape

class TestSave(unittest.TestCase):

    def setUp(self):
        self.canvas = tk.Canvas(width=800, height=600, bg="white")
        self.handler = SaveHandler()

    def test_get_data(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle", 50, 50)
        rectangle.create_shape("rectangle")
        self.handler.get_data(self.canvas)
        data = {
        "shapes": [
            {
            "width": 100,
            "height": 50,
            "name": "test",
            "x": 50.0,
            "y": 50.0,
            "shape": "rectangle"
            }
        ]}
        self.assertEqual(self.handler.data, data)

    def test_unload_data(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle", 50, 50)
        rectangle.create_shape("rectangle")
        self.handler.get_data(self.canvas)
        self.canvas.delete("all")
        self.handler.unload_data(self.canvas)
        rectangles = self.canvas.find_withtag("shape")
        self.assertEqual(len(rectangles), 1) 

    def test_save_data(self):
        test = self.handler.save("test")
        self.assertEqual(test, True)
        self.handler.delete_data("test")

    def test_load_data(self):
        self.handler.save("test")
        test = self.handler.load("test_2")
        self.assertEqual(test, False)
        test = self.handler.load("test")
        self.assertEqual(test, True)
        self.handler.delete_data("test")

    def test_load_delete(self):
        self.handler.save("test")
        test = self.handler.delete_data("test")
        self.assertEqual(test, True)
        test = self.handler.delete_data("test_2")
        self.assertEqual(test, False)
