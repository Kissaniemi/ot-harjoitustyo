import unittest

from shapes.shape import Shape


class TestShape(unittest.TestCase):

    def test_rectangle(self):
        rectangle = Shape(100, 50, "test", "rectangle")
        self.assertEqual(rectangle.width, 100)
        self.assertEqual(rectangle.height, 50)
        self.assertEqual(rectangle.text, "test")
        self.assertEqual(rectangle.shape, "rectangle")

    def test_oval(self):
        oval = Shape(100, 50, "test", "oval")
        self.assertEqual(oval.width, 100)
        self.assertEqual(oval.height, 50)
        self.assertEqual(oval.text, "test")
        self.assertEqual(oval.shape, "oval")

    def test_room(self):
        room = Shape(100, 50, "test", "room")
        self.assertEqual(room.width, 100)
        self.assertEqual(room.height, 50)
        self.assertEqual(room.text, "test")
        self.assertEqual(room.shape, "room")

    def test_change_text(self):
        rectangle = Shape(100, 50, "test", "rectangle")
        rectangle.change_text("newtext")
        self.assertEqual(rectangle.text, "newtext")

    def test_change_width(self):
        rectangle = Shape(100, 50, "test", "rectangle")
        rectangle.change_width(200)
        self.assertEqual(rectangle.width, 200)

    def test_change_height(self):
        rectangle = Shape(100, 50, "test", "rectangle")
        rectangle.change_height(200)
        self.assertEqual(rectangle.height, 200)

    def test_change_coordinates(self):
        rectangle = Shape(100, 150, "test", "rectangle")
        rectangle.change_coordinates(400, 100)
        self.assertEqual(rectangle.top_left_x, 400)
        self.assertEqual(rectangle.top_left_y, 100)

    def test_change_all(self):
        rectangle = Shape(100, 150, "test", "rectangle")
        rectangle.change_all(200, 300, "new_test",)
        self.assertEqual(rectangle.width, 200)
        self.assertEqual(rectangle.height, 300)
        self.assertEqual(rectangle.text, "new_test")
