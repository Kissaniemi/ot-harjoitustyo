## Projektin koodin idea/koodilähteet

Aikaisemmin Tkinteriä käyttämättömänä suuri apu projektin alkuun pääsemisessa on ollut Youtubesta Codemy.com käyttäjän videosarja [Python GUI's With Tkinter](https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV) jonka oppien yhdistelmiin lähes kaikki viikko 3:n mennessä luotu koodi perustuu, varsinkin UI:n kohdalla. 
Aluksi hyödynnetty myös kurssin ohjelmistotekniikka [TkInter ja graafisen käyttöliittymän toteutus](https://ohjelmistotekniikka-hy.github.io/python/tkinter) sivua alkuun pääsemiseen (ikkunan avaus, graafiset komponentit ja niiden asettelu, tapahtumakäsittelijät).

Yleisesti koodia tehdessä käytetty apuna [tkinter - Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html#module-tkinter) sekä erityisesti [TkDocs- Tutorial](https://tkdocs.com/tutorial/index.html) sivustoa yksittäisten tkinterin toimintojen opetteluun ja hyödyntämiseen.

Koodin kansiorakenteessa ja docstring nimissä otettu mallia kurssin [referenssisovelluksesta.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/tree/master)

## Koodin rakenteen mukaisessa aakkosjärjestyksessä ylimmästä kansiosta alimpaan, tarkistettu viimeksi 14.5.2023 ja käytetty sitä ennen:

src:
build.py: täysin sama kuin kurssin referenssisovelluksen build.py.
database_connection.py: perustuu kurssin referenssisovelluksen database_connection.py.
initialize_database.py:
def drop_table: täysin sama kuin kurssin referenssisovelluksen initialize_database.py.
def create_table: perustuu kurssin referenssisovelluksen initialize_database.py.
def create_table: täysin sama kuin kurssin referenssisovelluksen initialize_database.py.
main.py : täysin sama kuin referenssisovelluksen index.py.
file_handler:
json_handler.py:
def get_all_file_names: 
kaikkien json tiedostojen etsintä: https://stackoverflow.com/questions/30539679/python-read-several-json-files-from-a-folder.
def delete_data:
json-tiedoston etsintä os-moduulia käyttäen
https://www.w3schools.com/python/python_file_remove.asp
Idea datalistan luomiseen:
 Ohjelmoinnin perusteet kurssi-Osa 7 Datan käsittely, JSON-tiedoston lukeminen 
Corey Schafer Python Tutorial: Working with JSON Data using the json Module 
Stackoverflow How to Python Tkinter saving canvas object by dump all canvas object?

sql_handler.py: 
perustuu referenssisovelluksen todo_repository.py, sekä erityisesti Codemy:n Database videotutoriaaleihin #19-23.
logic_handler:
canvas_handler.py:
yleisesti:
Tagien käytön idea:
TkDocs Canvas - Tags T
kDocs Text- Differences between Tags in Canvas and Text Widgets
Kuinka saada valitun objektin tagit:
Stackoverflow https://stackoverflow.com/questions/66831149/tkinter-how-to-get-tag-name-from-clicking-on-rectangle
Canvas objektien hakemisen idea: 
Stackoverflow Python, Tkinter: How to get the handle of all canvas objects using their IDs or tags?
def _initiliaze.py: perustuu Stackoverflow how to select multiple objects with mouse in tkinter python gui?
def select_object: 
Päällimäisen suorakulmion löytämisen idea: Stackoverflow Detecting when two objects are overlapping each other in tkinter 
Valitun objektin reunan värin vaihtaminen punaiseksi:
https://www.tutorialspoint.com/how-to-change-the-color-of-a-tkinter-rectangle-on-clicking
def object_move:
 Alkuperäinen idea ja jatkoidea liikutteluun: 
Codemy Drag and Drop Images With The Mouse - Python Tkinter GUI Tutorial #71 
Stackoverflow how to select multiple objects with mouse in tkinter python gui?
def lower_shape/lift_shape:
Eteen ja taakse vieminen:
https://stackoverflow.com/questions/35365828/python-tkinter-canvas-lift-and-canvas-lower-on-overlapping-buttons-does-not-wng
shape_handler:
Idea muoto-objektien luontiin: 
Codemy How to Draw Lines and Shapes With Canvas - Python Tkinter GUI Tutorial #68 
Idea teksti-objektin luontiin: 
TkDocs Canvas- Item Types - Text
ui:
yleisesti:
Popup-ikkunoiden käytön idea:
Codemy, https://www.youtube.com/watch?v=KRuUtNxOb_k&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=138
Codemy, https://www.youtube.com/watch?v=tpwu5Zb64lQ

Kuinka liittää napin painallukseen useamman funktio kutsu:
https://stackoverflow.com/questions/51279570/python-tkinter-lambda-multiple-variable
canvas_view.py: 
canvaksen käyttö ja ominaisuudet yleisesti:
TkDocs https://tkdocs.com/tutorial/canvas.html
canvaksen luominen kehykseen:
Codemy How to Draw Lines and Shapes With Canvas - Python Tkinter GUI Tutorial #68
change_view.py:
def validate_input:
Validointi yleisesti:
Codemy https://www.youtube.com/watch?v=IbpInH4q4Sg

Idea input validointiin exceptioneilla:
https://www.pythonguis.com/tutorials/input-validation-tkinter/

Idea integer-validointiin:
Codemy https://www.youtube.com/watch?v=IbpInH4q4Sg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=68
main_view.py:
checkboxit: 
Idea: 
Codemy Checkboxes With TKinter - Python Tkinter GUI Tutorial #17 ,
TkDocs Basic Widgets - Checkbutton , 
Stackoverflow How to hide and show canvas items on tkinter?
ui.py: perustuu referenssisovelluksen ui.py
popups:
json_pop_ups.py/sql_pop_ups.py: 
Messageboxien käytön idea: 
Codemy Message Boxes with TKinter - Python Tkinter GUI Tutorial #13
Tutorialspoint https://www.tutorialspoint.com/how-to-get-an-entry-box-within-a-messagebox-in-tkinter
11:49

Testejä tehdessä käytetty apuna:
Stackoverflow https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app
