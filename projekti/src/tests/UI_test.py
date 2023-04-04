import tkinter as tk
from tkinter import Entry
from RoomPlanner import UI, Rectangle
import unittest
from unittest import main


class TestUI(unittest.TestCase):

    def setUp(self):
        self.UI = UI()
        self.UI.width_entry = Entry()
        self.UI.height_entry = Entry()

    # Tests the UI class inputs and checks if it has created a rectangle
    def test_rectangle_input_valid(self):
        self.UI.width_entry.insert(0, "50")
        self.UI.height_entry.insert(0, "100")
        self.UI.create_rectangle()
        self.assertEqual(len(self.UI.rectangles), 1)
    
    # Tests the UI class inputs and that it has not created a rectangle
    def test_rectangle_input_not_valid(self):
        self.UI.width_entry.insert(0, "testi")
        self.UI.height_entry.insert(0, "10")
        self.UI.create_rectangle()
        self.assertEqual(len(self.UI.rectangles), 0)


        
        
