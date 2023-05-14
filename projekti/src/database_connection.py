import os
import sqlite3


def get_database_connection():
    """Hakee save.db tietokannan data-kansiosta.

    Returns:
        connection, jos tietokanta löytyy.
        None, jos ei löydy.
    """
    try:
        dirname = os.path.dirname(__file__)
        connection = sqlite3.connect(
            os.path.join(dirname, "..", "data", "saves.db"))
        return connection
    except FileNotFoundError:
        return None
