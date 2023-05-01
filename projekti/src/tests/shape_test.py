import tkinter as tk
import unittest

from shapes.shape_class import Shape


class TestShape(unittest.TestCase):
    def setUp(self):
        self.canvas = tk.Canvas(width=800, height=600, bg="white")

    def test_rectangle(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle")
        self.assertEqual(rectangle.width, 100)
        self.assertEqual(rectangle.height, 50)
        self.assertEqual(rectangle.text, "test")
        self.assertEqual(rectangle.shape, "rectangle")

    def test_oval(self):
        oval = Shape(self.canvas, 100, 50, "test", "oval")
        self.assertEqual(oval.width, 100)
        self.assertEqual(oval.height, 50)
        self.assertEqual(oval.text, "test")
        self.assertEqual(oval.shape, "oval")

    def test_room(self):
        room = Shape(self.canvas, 100, 50, "test", "room")
        self.assertEqual(room.width, 100)
        self.assertEqual(room.height, 50)
        self.assertEqual(room.text, "test")
        self.assertEqual(room.shape, "room")

    def test_create_rect(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle")
        rectangle.create_shape("rectangle")
        rectangles = self.canvas.find_withtag("rectangle")
        self.assertEqual(len(rectangles), 1)

    def test_create_oval(self):
        oval = Shape(self.canvas, 100, 50, "test", "oval")
        oval.create_shape("oval")
        ovals = self.canvas.find_withtag("oval")
        self.assertEqual(len(ovals), 1)

    def test_create_room(self):
        room = Shape(self.canvas, 100, 50, "test", "room")
        room.create_shape("")
        rooms = self.canvas.find_withtag("room")
        self.assertEqual(len(rooms), 1)

    def test_create_text(self):
        oval = Shape(self.canvas, 100, 50, "test", "oval")
        oval.create_shape("oval")
        texts = self.canvas.find_withtag("text")
        self.assertEqual(len(texts), 1)

    def test_change_text(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle")
        rectangle.change_text("newtext")
        self.assertEqual(rectangle.text, "newtext")

    def test_change_width(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle")
        rectangle.change_width(200)
        self.assertEqual(rectangle.width, 200)

    def test_change_height(self):
        rectangle = Shape(self.canvas, 100, 50, "test", "rectangle")
        rectangle.change_height(200)
        self.assertEqual(rectangle.height, 200)

    def test_change_coordinates(self):
        rectangle = Shape(self.canvas, 100, 150, "test", "rectangle")
        rectangle.change_coordinates(400, 100)
        self.assertEqual(rectangle.top_left_x, 400)
        self.assertEqual(rectangle.top_left_y, 100)
