import unittest
import tkinter as tk

from logic_handler.canvas_handler import CanvasHandler
from logic_handler.data_handler import DataHandler


class TestData(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(width=800, height=600, bg="white")
        self.canvas_handler = CanvasHandler(
            self.canvas)
        self.data_handler = DataHandler(self.canvas_handler)

    def test_get_json_data(self):
        self.canvas_handler.create_shape(100, 50, "test", "oval")
        data = self.data_handler.get_json_data()
        self.assertEqual(data, {
            "shapes": [
                {"width": 100,
                 "height": 50,
                 "text": "test",
                 "x": 50.0,
                 "y": 50.0,
                 "shape": "oval"
                 }]})

    def test_unload_json_data(self):
        data = {"shapes": [
            {"width": 100,
             "height": 50,
             "text": "test",
             "x": 50.0,
             "y": 50.0,
             "shape": "oval"
             }]}
        ask = self.data_handler.unload_json_data(data)
        self.assertEqual(True, ask)

        newdata = self.data_handler.get_json_data()
        self.assertEqual(newdata, {
            "shapes": [
                {"width": 100,
                 "height": 50,
                 "text": "test",
                 "x": 50.0,
                 "y": 50.0,
                 "shape": "oval"
                 }]})

    def test_dont_load_json_data(self):
        data = {}
        ask = self.data_handler.unload_json_data(data)
        self.assertEqual(False, ask)

        newdata = self.data_handler.get_json_data()
        self.assertEqual(newdata, {'shapes': []})

    def test_get_sql_data(self):
        self.canvas_handler.create_shape(100, 150, "test", "oval")
        data = self.data_handler.get_sql_data()
        self.assertEqual(data, [(100, 150, "test", 50.0, 50.0, "oval",)])

    def test_unload_sql_data(self):
        self.canvas_handler.create_shape(400, 50, "test", "rectangle")
        data = [(400, 50, "test", 50, 50, "rectangle")]
        self.data_handler.unload_sql_data(data)
        newdata = self.data_handler.get_sql_data()
        self.assertEqual(newdata, [(400, 50, "test", 50, 50, "rectangle",)])
