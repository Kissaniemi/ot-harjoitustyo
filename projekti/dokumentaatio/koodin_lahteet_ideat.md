## Projektin koodin idea/koodilähteet

Aikaisemmin Tkinteriä käyttämättömänä suuri apu projektia tehdessä on ollut Youtubesta Codemy.com käyttäjän videosarja [Python GUI's With Tkinter](https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV) jonka oppien yhdistelmiin lähes kaikki viikko 3:n mennessä luoto koodi perustuu, varsinkin UI:n kohdalla. 
Aluksi hyödynnetty myös kurssin ohjelmistotekniikka [TkInter ja graafisen käyttöliittymän toteutus](https://ohjelmistotekniikka-hy.github.io/python/tkinter) sivua alkuun pääsemiseen (ikkunan avaus, graafiset komponentit ja niiden asettelu, tapahtumakäsittelijät).

Yleisesti koodia tehdessä käytetty apuna [tkinter - Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html#module-tkinter) sekä erityisesti [TkDocs- Tutorial](https://tkdocs.com/tutorial/index.html) sivustoa yksittäisten tkinterin toimintojen opetteluun ja hyödyntämiseen.

## Tarkemmat tähän mennessä tehdyn koodin lähteet koodin mukaisessa järjestyksessä ylhäältä alas:

#### # Creates a canvas on top of the right_frame for the rectangles
Idea: Codemy [How to Draw Lines and Shapes With Canvas - Python Tkinter GUI Tutorial #68](https://www.youtube.com/watch?v=HrK9Kmz3_9A&t=346s)

#### #Binds the mouse events to the canvas
Idea: Stackoverflow [how to select multiple objects with mouse in tkinter python gui?](https://stackoverflow.com/questions/15738617/how-to-select-multiple-objects-with-mouse-in-tkinter-python-gui)

#### #checkbox to toggle names on/off
Idea: Codemy [Checkboxes With TKinter - Python Tkinter GUI Tutorial #17](https://www.youtube.com/watch?v=4IsLwwb_yDs)
 TkDocs [Basic Widgets - Checkbutton](https://tkdocs.com/tutorial/widgets.html#checkbutton)
 Stackoverflow [How to hide and show canvas items on tkinter?](https://stackoverflow.com/questions/53499669/how-to-hide-and-show-canvas-items-on-tkinter)

#### #Find the clicked rectangle and text related to it / # Move the selected rectangle with the mouse
Idea päällimäisen suorakulmion löytämiseen: Stackoverflow  [Detecting when two objects are overlapping each other in tkinter](https://stackoverflow.com/questions/63442273/detecting-when-two-objects-are-overlapping-each-other-in-tkinter)
Alkuperäinen idea ja jatkoidea liikutteluun: Codemy [Drag and Drop Images With The Mouse - Python Tkinter GUI Tutorial #71](https://www.youtube.com/watch?v=Z4zePg2M5H8)
Stackoverflow [how to select multiple objects with mouse in tkinter python gui?](https://stackoverflow.com/questions/15738617/how-to-select-multiple-objects-with-mouse-in-tkinter-python-gui)

#### # Save to json / # Load from json
##### # Find all rectangle objects on the canvas
Idea: Stackoverflow [ Python, Tkinter: How to get the handle of all canvas objects using their IDs or tags?](https://stackoverflow.com/questions/34944935/python-tkinter-how-to-get-the-handle-of-all-canvas-objects-using-their-ids-or)
##### # Create a data list of the rectangles to append to the json file
Idea: Ohjelmoinnin perusteet kurssi-[Osa 7 Datan käsittely, JSON-tiedoston lukeminen](https://ohjelmointi-22.mooc.fi/osa-7/4-datan-kasittely)
Corey Schafer [Python Tutorial: Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I&t=1059s)
Stackoverflow [How to Python Tkinter saving canvas object by dump all canvas object?](https://stackoverflow.com/questions/63025797/how-to-python-tkinter-saving-canvas-object-by-dump-all-canvas-object)
#### # Popup to confirm you want to save/load/exit/# Saved pop up
Idea: Codemy [Message Boxes with TKinter - Python Tkinter GUI Tutorial #13](https://www.youtube.com/watch?v=S3AaSwpb5GE)

#### # Function to create the rectangle and text object:
Idea suorakulmio-objektin luontiin luontiin: Codemy[How to Draw Lines and Shapes With Canvas - Python Tkinter GUI Tutorial #68](https://www.youtube.com/watch?v=HrK9Kmz3_9A&t=346s)
Idea teksti-objektin luontiin: TkDocs [Canvas- Item Types - Text](https://tkdocs.com/tutorial/canvas.html)

#### Tagien hyödyntäminen:
Idea:  TkDocs [Canvas - Tags](https://tkdocs.com/tutorial/canvas.html)
TkDocs [Text- Differences between Tags in Canvas and Text Widgets](https://tkdocs.com/tutorial/text.html)

