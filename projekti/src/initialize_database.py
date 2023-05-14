from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulut.
    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists saves;
    """)

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.
    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE saves (
            save_name text,
            width integer,
            height integer,
            text_input text,
            x_coord integer,
            y_coord integer,
            shape_type text
            )""")

    connection.commit()

    # Close Connection
    connection.close()


def initialize_database():
    """Alustaa tietokantataulut."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
