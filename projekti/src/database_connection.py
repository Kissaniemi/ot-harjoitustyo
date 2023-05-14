import os
import sqlite3


def get_database_connection():
    try:
        dirname = os.path.dirname(__file__)
        connection = sqlite3.connect(
            os.path.join(dirname, "..", "data", "saves.db"))
        return connection
    except FileNotFoundError:
        return None
