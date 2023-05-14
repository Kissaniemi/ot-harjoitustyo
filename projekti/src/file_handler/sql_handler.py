from database_connection import get_database_connection


class SqlHandler():
    """SQL tietokannasta shape tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa uuden datalistan."""
        self._connection = get_database_connection()
        self.data = []

    def _delete_all_tables(self):
        """Tyhjentää koko 'saves' tietokannan."""
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM saves")
        conn.commit()
        conn.close()

    def add_data(self, data):
        """Tyhjentää ensin nykyisen data-kirjaston ja hakee canvasilta 
        kaikki 'shape' tyypin objektit ja 'tallentaa' ne uuteen listaan.

        Args:
            data: käsiteltävä data.
        """
        self.data.clear()
        self.data = data

    def record_exists(self, filename):
        """Tarkistaa löytyyky annettu nimi 
        'saves' tietokannasta.

        Args:
            filename: tallennukselle annettu nimi.

        Returns:
            True, jos tietokannassa ei ole save_name sarakkeessa
            samannimistä talletusta.
            False, jos on.
        """
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(
            f"SELECT save_name FROM saves WHERE save_name='{filename}'")
        record = cur.fetchone()
        conn.commit()
        conn.close()

        if record is None:
            return True
        return False

    def save(self, filename):
        """Tallettaa datan annetulla talletusnimellä.
        Args:
            filename: tallennukselle annettu nimi.

        Returns:
            False, jos datataulu on tyhjä.
            True, jos talletus onnistuu.

        """
        if self.data == []:
            return False

        conn = get_database_connection()
        cur = conn.cursor()

        for _, item in enumerate(self.data):
            cur.execute("""INSERT INTO saves VALUES (:save_name, :width, :height,
            :text_input, :x_coord, :y_coord, :shape_type)""",
                        {
                            "save_name": filename,
                            "width": item[0],
                            "height": item[1],
                            "text_input": item[2],
                            "x_coord": item[3],
                            "y_coord": item[4],
                            "shape_type": item[5],
                        })

        conn.commit()
        conn.close()
        return True

    def load_record(self, filename):
        """Hakee tietokannasta annetun talletusnimen
        mukaiset rivit.

        Args:
            filename: tallennukselle annettu nimi.

        Returns:
            False, jos talletusnimen mukaisia
            rivejä ei löydy.
            record, johon on haettu rivien tiedot,
            jos rivejä löytyy.
        """
        conn = get_database_connection()
        cur = conn.cursor()

        cur.execute(f"SELECT width, height, text_input, x_coord, y_coord, \
                    shape_type FROM saves WHERE save_name='{filename}'")
        record = cur.fetchall()

        conn.commit()
        conn.close()
        if record == []:
            return False
        return record

    def get_all_save_files(self):
        """Hakee kaikkien tallennusten nimet.

        Returns:
            False, jos talletusnimen mukaisia
            rivejä ei löydy.
            record, johon on haettu kaikkien talletusten 
            tiedot, jos rivejä löytyy.
        """
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("SELECT save_name FROM saves")
        record = cur.fetchall()
        conn.commit()
        conn.close()
        if record == []:
            return False
        return record

    def delete_record(self, filename):
        """Poistaa tietokannasta annetun nimen talletukset.

        Args:
            filename: tallennukselle annettu nimi

        Returns:
            True, jos ei onnistu.
            False, jos onnistuu.
        """
        ask = self.record_exists(filename)
        if ask is False:
            conn = get_database_connection()
            cur = conn.cursor()
            cur.execute(f"DELETE FROM saves WHERE save_name='{filename}'")

            conn.commit()
            conn.close()
        return True
