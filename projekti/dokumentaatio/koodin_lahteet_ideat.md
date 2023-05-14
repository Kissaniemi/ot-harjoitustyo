## Projektin koodin idea/koodilähteet

Aikaisemmin Tkinteriä käyttämättömänä suuri apu projektin alkuun pääsemisessa on ollut Youtubesta Codemy.com käyttäjän videosarja [Python GUI's With Tkinter](https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV) jonka oppien yhdistelmiin lähes kaikki viikko 3:n mennessä luotu koodi perustuu, varsinkin UI:n kohdalla. 
Aluksi hyödynnetty myös kurssin ohjelmistotekniikka [TkInter ja graafisen käyttöliittymän toteutus](https://ohjelmistotekniikka-hy.github.io/python/tkinter) sivua alkuun pääsemiseen (ikkunan avaus, graafiset komponentit ja niiden asettelu, tapahtumakäsittelijät).

Yleisesti koodia tehdessä käytetty apuna [tkinter - Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html#module-tkinter) sekä erityisesti [TkDocs- Tutorial](https://tkdocs.com/tutorial/index.html) sivustoa yksittäisten tkinterin toimintojen opetteluun ja hyödyntämiseen.

Koodin kansiorakenteessa ja docstring nimissä otettu mallia kurssin [referenssisovelluksesta.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/tree/master)

## Koodin rakenteen mukaisessa aakkosjärjestyksessä ylimmästä kansiosta alimpaan, tarkistettu viimeksi 14.5.2023 ja käytetty sitä ennen:

### src:
#### build.py: 
täysin sama kuin kurssin referenssisovelluksen [build.py.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/build.py)

#### database_connection.py: 
perustuu kurssin referenssisovelluksen [database_connection.py.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/database_connection.py)

#### initialize_database.py:

##### def drop_table: 
täysin sama kuin kurssin referenssisovelluksen [initialize_database.py.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/initialize_database.py)

##### def create_table: 
perustuu kurssin referenssisovelluksen [initialize_database.py.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/initialize_database.py)

##### def create_table: 
täysin sama kuin kurssin referenssisovelluksen [initialize_database.py.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/initialize_database.py)

##### main.py : 
täysin sama kuin kurssin referenssisovelluksen [index.py.](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/index.py)

### file_handler:
#### json_handler.py:
##### def get_all_file_names: 
Idea kaikkien json tiedostojen etsintä: [Stackoverflow](https://stackoverflow.com/questions/30539679/python-read-several-json-files-from-a-folder)

##### def delete_data:
Idea json-tiedoston etsintä os-moduulia käyttäen: [W3schools](https://www.w3schools.com/python/python_file_remove.asp)

##### Idea datalistan luomiseen:
[Ohjelmoinnin perusteet kurssi](https://ohjelmointi-22.mooc.fi/osa-7/4-datan-kasittely)

[Corey Schafer](https://www.youtube.com/watch?v=9N6a-VLBa2I&t=1059s)

[Stackoverflow](https://stackoverflow.com/questions/63025797/how-to-python-tkinter-saving-canvas-object-by-dump-all-canvas-object)

#### sql_handler.py: 
perustuu kurssin referenssisovelluksen [todo_repository.py](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/repositories/todo_repository.py)

sekä erityisesti Codemy:n Database videotutoriaaleihin 19-23
([19](https://www.youtube.com/watch?v=YR3h2CY21-U&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=19)
[20](https://www.youtube.com/watch?v=AK1J8xF4fuk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=20)
[21](https://www.youtube.com/watch?v=c9_gcIeAru0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=21)
[22](https://www.youtube.com/watch?v=EAs3gr9mC9g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=22)
[23](https://www.youtube.com/watch?v=0Ms0-68IgTY&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=23))

### logic_handler:
#### canvas_handler.py:
##### yleisesti:
Tagien käytön idea:
TkDocs [Canvas](https://tkdocs.com/tutorial/canvas.html)

TkDocs [Text](https://tkdocs.com/tutorial/text.html)

##### Kuinka saada valitun objektin tagit:
Idea [Stackoverflow](https://stackoverflow.com/questions/66831149/tkinter-how-to-get-tag-name-from-clicking-on-rectangle)

##### Canvas objektien hakemisen idea: 
Idea [Stackoverflow](https://stackoverflow.com/questions/34944935/python-tkinter-how-to-get-the-handle-of-all-canvas-objects-using-their-ids-or)

##### def initiliaze.py: 
Idea [Stackoverflow](https://stackoverflow.com/questions/15738617/how-to-select-multiple-objects-with-mouse-in-tkinter-python-gui)

##### def select_object: 
Päällimäisen suorakulmion löytämisen idea: 
[Stackoverflow](https://stackoverflow.com/questions/63442273/detecting-when-two-objects-are-overlapping-each-other-in-tkinter)

##### Valitun objektin reunan värin vaihtaminen punaiseksi:
[Tutorialspoint](https://www.tutorialspoint.com/how-to-change-the-color-of-a-tkinter-rectangle-on-clicking)

##### def object_move:
 Alkuperäinen idea ja jatkoidea liikutteluun: 
[Codemy](https://www.youtube.com/watch?v=Z4zePg2M5H8)
[Stackoverflow](https://stackoverflow.com/questions/15738617/how-to-select-multiple-objects-with-mouse-in-tkinter-python-gui)

##### def lower_shape/lift_shape:
Eteen ja taakse vieminen:
[Stackoverflow](https://stackoverflow.com/questions/35365828/python-tkinter-canvas-lift-and-canvas-lower-on-overlapping-buttons-does-not-w)

#### shape_handler.py:
##### Idea muoto-objektien luontiin: 
[Codemy](https://www.youtube.com/watch?v=HrK9Kmz3_9A&t=346s)

### ui:
##### yleisesti:
Popup-ikkunoiden käytön idea:
[Codemy](https://www.youtube.com/watch?v=KRuUtNxOb_k&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=138)
[Codemy](https://www.youtube.com/watch?v=tpwu5Zb64lQ)

##### Kuinka liittää napin painallukseen useamman funktio kutsu:
[Stackoverflow](https://stackoverflow.com/questions/51279570/python-tkinter-lambda-multiple-variable)

#### canvas_view.py: 
##### canvaksen käyttö ja ominaisuudet yleisesti:
[TkDocs](https://tkdocs.com/tutorial/canvas.html)

##### canvaksen luominen kehykseen:
[Codemy](https://stackoverflow.com/questions/51279570/python-tkinter-lambda-multiple-variable)

#### change_view.py:
##### def validate_input:
##### Validointi yleisesti:
[Codemy](https://www.youtube.com/watch?v=IbpInH4q4Sg)

##### Idea input validointiin exceptioneilla:
[PythonGUIS](https://www.youtube.com/watch?v=IbpInH4q4Sg)

##### Idea integer-validointiin:
[Codemy](https://www.youtube.com/watch?v=IbpInH4q4Sg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=68)

#### main_view.py:
##### checkboxit: 
Idea: 
[Codemy](https://www.youtube.com/watch?v=4IsLwwb_yDs)
[TkDocs](https://tkdocs.com/tutorial/widgets.html#checkbutton)
[Stackoverflow](https://stackoverflow.com/questions/53499669/how-to-hide-and-show-canvas-items-on-tkinter)

#### ui.py: 
perustuu referenssisovelluksen [ui.py](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/ui.py)

### popups:
#### json_pop_ups.py/sql_pop_ups.py: 

##### Messageboxien käytön idea: 
[Codemy](https://www.youtube.com/watch?v=S3AaSwpb5GE)
[Tutorialspoint](https://www.tutorialspoint.com/how-to-get-an-entry-box-within-a-messagebox-in-tkinter)

### Testejä tehdessä käytetty apuna:
[Stackoverflow](https://www.tutorialspoint.com/how-to-get-an-entry-box-within-a-messagebox-in-tkinter)
