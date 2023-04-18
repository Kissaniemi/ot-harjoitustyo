import tkinter as tk
import unittest

from room_planner import UI
from handler.event_handler import EventHandler
from rectangle.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.UI = UI(self.root)
        self.canvas = self.UI.canvas
        self.event_handler = EventHandler(self.UI, self.canvas)

    def test_create_rectangle(self):
        rectangle = Rectangle(100, 50, "test")
        rectangle.create(self.canvas)
        self.assertIsNotNone(rectangle.id)
        self.assertEqual(self.canvas.type(rectangle.id), "rectangle")

    def test_create_text(self):
        rectangle = Rectangle(100, 50, "test")
        rectangle.create(self.canvas)
        self.assertIsNotNone(rectangle.text_id)
        self.assertEqual(self.canvas.type(rectangle.text_id), "text")
