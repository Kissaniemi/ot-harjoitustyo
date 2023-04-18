import tkinter as tk
import unittest

from room_planner import UI
from handler.event_handler import EventHandler
from rectangle.rectangle import Rectangle


class TestHandler(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.UI = UI(self.root)
        self.canvas = self.UI.canvas
        self.event_handler = EventHandler(self.UI, self.canvas)

    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_create_rectangle(self):
        # Valid inputs
        self.UI.name_entry.insert(0, "test")
        self.UI.width_entry.insert(0, "50")
        self.UI.height_entry.insert(0, "100")
        self.event_handler.create_rectangle()
        rectangles = self.canvas.find_withtag("rectangle")
        self.assertEqual(len(rectangles), 1)

        # Invalid width
        self.UI.name_entry.insert(0, "test")
        self.UI.width_entry.insert(0, "test")
        self.UI.height_entry.insert(0, "100")
        self.event_handler.create_rectangle()
        error_text = self.UI.error_label.cget("text")
        self.assertEqual(error_text, "Width and height must be a number!")

        # Invalid height
        self.UI.name_entry.insert(0, "test")
        self.UI.width_entry.insert(0, "50")
        self.UI.height_entry.insert(0, "test")
        self.event_handler.create_rectangle()
        error_text = self.UI.error_label.cget("text")
        self.assertEqual(error_text, "Width and height must be a number!")

    def test_names_on_off(self):
        self.canvas.create_text(50, 50, text="test", tags="text")
        self.UI.checkbox_var.set(1)
        self.event_handler.names_on_off()
        self.assertEqual(self.UI.canvas.itemcget("text", "state"), "hidden")

        self.UI.checkbox_var.set(0)
        self.event_handler.names_on_off()
        self.assertEqual(self.UI.canvas.itemcget("text", "state"), "normal")

    def test_release_move(self):
        self.UI.name_entry.insert(0, "test")
        self.UI.width_entry.insert(0, "50")
        self.UI.height_entry.insert(0, "100")
        self.event_handler.selected_rectangle = self.event_handler.create_rectangle()
        self.event_handler.release_move()
        self.assertEqual(self.event_handler.selected_rectangle, None)
        self.assertEqual(self.event_handler.selected_text, None)

    def test_exit(self):
        self.event_handler.exit()


if __name__ == "__main__":
    unittest.main()
