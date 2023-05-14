import unittest

from file_handler.json_handler import SaveHandler


class TestJson(unittest.TestCase):

    def setUp(self):
        self.handler = SaveHandler()

    def test_get_data(self):
        data = {"shapes": [{"width": 100, "height": 50,
                            "text": "test", "x": 50, "y": 50, "shape": "rectangle"}]}
        self.handler.add_data(data)
        self.assertEqual(self.handler.data, data)

    def test_save_data(self):
        test = self.handler.save("test")
        self.assertEqual(test, True)
        self.handler.delete_data("test")

    def test_load_data(self):
        self.handler.save("test")
        test = self.handler.load("test2")
        self.assertEqual(test, False)
        self.handler.delete_data("test2")

    def test_load_false(self):
        self.handler.save("test3")
        test = self.handler.load("test3")
        self.assertEqual(test, {})
        self.handler.delete_data("test3")

    def test_load_delete(self):
        self.handler.save("test4")
        test = self.handler.delete_data("test4")
        self.assertEqual(test, True)
        self.handler.delete_data("test4")

    def test_delete_false(self):
        test = self.handler.delete_data("test5")
        self.assertEqual(test, False)

    def test_save_exist(self):
        self.handler.save("test6")
        test = self.handler.save_exists("test6")
        self.assertEqual(test, True)
        self.handler.delete_data("test6")

    def test_save_doesnt_exist(self):
        test = self.handler.save_exists("test")
        self.assertEqual(test, False)
