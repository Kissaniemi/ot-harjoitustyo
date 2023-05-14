import unittest

from file_handler.sql_handler import SQLHandler


class TestSQL(unittest.TestCase):

    def setUp(self):
        self.handler = SQLHandler()
        self.handler._delete_all_tables()

    def tearDown(self):
        self.handler._delete_all_tables()

    def test_add_data(self):
        data = [(150, 100, "tuoli", 50, 50, "rectangle")]
        self.handler.add_data(data)

    def test_delete_record(self):
        data = [(150, 100, "test", 50, 50, "rectangle")]
        self.handler.add_data(data)
        self.handler.save("test")
        ask = self.handler.load_record("test")
        self.assertEqual([(150, 100, "test", 50, 50, "rectangle")], ask)

        self.handler.delete_record("test")
        ask = self.handler.load_record("test")
        self.assertEqual(False, ask)

    def test_record_exists(self):
        ask = self.handler.record_exists("test2")
        self.assertEqual(True, ask)

        data = [(150, 100, "test", 50, 50, "rectangle")]
        self.handler.add_data(data)
        self.handler.save("test2")
        ask = self.handler.record_exists("test2")
        self.assertEqual(False, ask)

    def test_dont_save(self):
        self.handler.add_data([])
        ask = self.handler.save("test3")
        self.assertEqual(False, ask)

    def test_save(self):
        data = [(150, 100, "test", 50, 50, "rectangle")]
        self.handler.add_data(data)
        ask = self.handler.save("test3.5")
        self.assertEqual(True, ask)

    def test_load_record(self):
        ask = self.handler.load_record("test4")
        self.assertEqual(False, ask)

        data = [(150, 100, "test", 50, 50, "rectangle")]
        self.handler.add_data(data)
        self.handler.save("test4")
        ask = self.handler.load_record("test4")
        self.assertEqual(data, ask)

    def test_get_all_save_files(self):
        ask = self.handler.get_all_save_files()
        self.assertEqual(False, ask)

        data = [(150, 100, "test", 50, 50, "rectangle")]
        self.handler.add_data(data)
        self.handler.save("test5")
        data = [(10, 10, "test", 100, 100, "room")]
        self.handler.add_data(data)
        self.handler.save("test5")
        ask = self.handler.get_all_save_files()
        self.assertEqual([("test5",), ("test5",)], ask)

    def test_delete_all(self):
        data = [(150, 100, "test", 50, 50, "rectangle")]
        self.handler.add_data(data)
        self.handler.save("test6")
        data = [(10, 10, "test", 100, 100, "room")]
        self.handler.add_data(data)
        self.handler.save("test7")
        self.handler._delete_all_tables()
        ask = self.handler.get_all_save_files()
        self.assertEqual(False, ask)
