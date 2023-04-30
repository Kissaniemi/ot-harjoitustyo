import tkinter as tk
import unittest

from shapes.shape_class import Shape

class TestShape(unittest.TestCase):
    def setUp(self):
        self.canvas = tk.Canvas(width=800, height=600, bg="white")

    def test_create_rectangle(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle")
        self.assertEqual(rectangle.width, 100)
        self.assertEqual(rectangle.height, 50)
        self.assertEqual(rectangle.text, "test")
        self.assertEqual(rectangle.shape, "rectangle")

    def test_create_oval(self):
        oval = Shape(self.canvas, 100, 50, "test", "oval")
        self.assertEqual(oval.width, 100)
        self.assertEqual(oval.height, 50)
        self.assertEqual(oval.text, "test")
        self.assertEqual(oval.shape, "oval")

    def test_create_room(self):
        room = Shape(self.canvas, 100, 50, "test", "room")
        self.assertEqual(room.width, 100)
        self.assertEqual(room.height, 50)
        self.assertEqual(room.text, "test")
        self.assertEqual(room.shape, "room")
