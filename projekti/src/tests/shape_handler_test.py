import unittest
import tkinter as tk

from entities.shape import Shape
from logic_handler.canvas_handler import ShapeHandler


class TestShapeControl(unittest.TestCase):

    def setUp(self):
        self.canvas = tk.Canvas(width=800, height=600, bg="white")
        self.shape_handler = ShapeHandler(self.canvas)

    def test_create_rect(self):
        rectangle = Shape(100, 50, "test", "rectangle")
        self.shape_handler.create_rectangle(rectangle)
        rectangles = self.canvas.find_withtag("rectangle")
        self.assertEqual(len(rectangles), 1)

    def test_create_oval(self):
        oval = Shape(100, 50, "test", "oval")
        self.shape_handler.create_oval(oval)
        ovals = self.canvas.find_withtag("oval")
        self.assertEqual(len(ovals), 1)

    def test_create_room(self):
        room = Shape(100, 50, "test", "room")
        self.shape_handler.create_room(room)
        rooms = self.canvas.find_withtag("room")
        self.assertEqual(len(rooms), 1)

    def test_create_text(self):
        text = Shape(100, 50, "test", "oval")
        self.shape_handler.create_text(text)
        texts = self.canvas.find_withtag("text")
        self.assertEqual(len(texts), 1)

    def test_create_width_text(self):
        texts = Shape(100, 50, "test", "rectangle")
        self.shape_handler.create_width_text(texts)
        canvas_text = self.canvas.find_withtag("text")
        self.assertEqual(len(canvas_text), 1)

    def test_create_height_text(self):
        texts = Shape(100, 50, "test", "rectangle")
        self.shape_handler.create_height_text(texts)
        canvas_text = self.canvas.find_withtag("text")
        self.assertEqual(len(canvas_text), 1)
