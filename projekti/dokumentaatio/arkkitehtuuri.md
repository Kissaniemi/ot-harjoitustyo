# Arkkitehtuurikuvaus

## Sovelluksen rakenne

Sovelluksen rakenne koostuu viidestä src-kansion alaisesta kansiosta.

![pakkauskaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Kaaviot/pakkausrakenne.png)

Ui ja popups-kansioissa on sovelluksen käyttöliittymästä vastaavat luokat ja logic_handler- kansiossa sovelluksen logiikasta vastaavat luokat. File_handler luokka vastaa sovelluksen pysyvän tiedon tallentamisesta json-tiedostoon ja SQL-tietokantaan. Shapes-kansiossa on sovelluksen käsittelemien muoto-objektien luokka.

## Käyttöliittymä-luokat

Käyttöliittymässä on kolme eri pääasiallista näkymää ja niistä vastaavaa luokkaa, Muodon luominen (MainView), Muodon muuttaminen (ChangeView) ja Canvas-alueen näkymä (CanvasView). Canvas-alueen näkymä on koko ajan näkyvillä ikkunan oikeassa reunassa ja sitä kautta vaihdetaan ikkunan vasemman reunan näkymää "Muodon luonti" ja "Muodon muutos" näkymien välillä nappia painamalla. 

Canvas-näkymä kutsuu näkymää vaihtaakseen UI-luokan funktioita "show_main_view" ja "show_change_view". "Muodon muutos" näkymä kutsuu vain sovelluslogiikasta vastaavan CanvasHandler-luokan funktioita. "Muodon luonti" näkymä kutsuu CanvasHandler luokan lisäksi kahta eri talletukseen liittyvää luokkaa JsonpopUps ja SqlPopUps, joista kumpikin ovat käyttöliittymä luokkia, jotka kutsuvat sovelluslogiikan DataHandler- ja JsonHandler- tai SqlHandler-luokkia.

## Sovelluslogiikka-luokat

Sovelluslogiikka on pyritty eriyttämään käyttöliittymästä mahdollisimman hyvin, sekä jakamaan pienempiin luokkiin.
Pääasiallisesti sovelluslogiikasta vastaa CanvasHandler-luokka ja sen funktioita on jaettu kahteen "apuluokkaan" ShapeHandler ja CoordHandler. 

CanvasHandler vastaa canvasilla olevien objektien liikuttelusta, pyörittelystä ja suurimmasta osasta objekteihin liittyvistä funktioista. ShapeHandler-luokka sisältää objektien luonnista canvasille vastaavia funktioita, CoordHandler taas sisältää canvasilla olevien objektien koordinaattien muutoksista vastaavat funktiot. Funktioita voisi jakaa vielä paremmin muihin luokkiin.

Näiden lisäksi on DataHandler, joka vastaa datan keräämisestä canvasilta sopivaan muotoon, joko json-tiedostoon tai SQL-tietokantaan tallennettavaksi.

Shape-luokka vastaa canvasin objektien tietojen ylläpidosta ja siihen sisältyy funktioita, joilla olion attribuutteja voi muuttaa. Näitä funktioita kutsutaan CanvasHandler-luokan kautta.

![luokkakaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Kaaviot/Luokkakaavio.png)


## Tietojen tallennus

Sovelluksen tietojen pysysväistalletuksesta vastaavat JsonHandler- ja SqlHandler-luokat. JsonHandler tallentaa tiedot
json-tiedostoon ja SqlHandler SQLite-tietokantaan. 
Käyttäjä itse päättää mmillä nimellä canvasin näkymä tallennetaan ja mistä näkymä ladataan. Käyttäjällä on lisäksi mahdollisuus poistaa sekä json-tiedosto, että SQLite-tietokannan talletus tiedoston nimen perusteella. Käyttäjä voi myös hakea kaikkien löytyven json-tiedostojen ja SQLite-tietokannan talletusten nimet.

Json-tiedostot tallentuvat sovelluksen juureen ja SQLite talletukset projekti-tiedoston juuresta löytyvään data-kansion tietokantatauluun saves.db.

Tiedot tallennetaan SQLite-tietokantaan muodossa: 
            save_name text,
            width integer,
            height integer,
            text_input text,
            x_coord integer,
            y_coord integer,
            shape_type text

Tiedot tallennetaan json tiedostoon muodossa:
```{
  "shapes": [
    {
      "width": 150.0,
      "height": 60.0,
      "name": "sohva",
      "x": 86.0,
      "y": 77.0,
      "shape": "rectangle"
    }]}

## Päätoiminnallisuus

Sovelluksen päätoiminnallisuudet ovat muoto-objektien luominen, niiden muuttaminen ja talletus. Tarkastellaan seuraavaksi sekvenssikaavio esimerkkejä näistä toiminnoista.

### Muoto-objektin luominen

Käyttäjä kirjoittaa MainView näkymän syötekenttään objektin leveyden, pituuden ja nimen (esim. width=100, height=50, text=tuoli)
ja klikkaa "create rectangle" nappia. Sitä ennen sovelluksen käynnistyksen yhteydessä UI-luokka on luonut CanvasView-, CanvasHandler- ja Mainview-luokat. CanvasView luokassa on alkuperäinen canvas, jolle luotu muoto lopulta ilmestyy.

![luomuoto](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Kaaviot/Create%20Rectangle%20object.png)

Napin painallus hakee kenttien tiedot ja lisää siihen nappiin liitetyn muoto-tiedon "rectangle" ja kutsuu validate_input-funktiota. Funktio tarkistaa, että annetut leveys- ja pituus-syöttee ovat sopivia parametrejä.

Sen jälkeen validate_input kutsuu CanvasHandler-luokan funktiota create_shape(100, 50, "tuoli", "rectangle"). Create_shape funktio tarkistaa ensin kutsumalla get_current_color funktiota, mikä värimaailmaa canvasilla on sillä hetkellä asetettuna. Sen jälkeen se alustaa Shape-luokan objektin shape = Shape(100, 50, "tuoli", "rectangle") ja sitten erikseen kutsuu ShapeHandler-luokan create_shape("rectangle", "black", "white") funktiota, aikaisemmin saaduilla värimaailma tiedoilla.  Tämä luo canvasille halutun muodon. 

Samalla CanvasHandler-luokan funktio create_shape kutsuu luokan create_texts(100, 50, "tuoli", "black", 50, 50)funktiota, joka create_shape funktion lailla ensin alustaa teksti-objektin Shape-luokkaan ja sitten kutsuu ShapeHandler luokan funktiota luomaan tekstit canvasille. Tämä toistuu kolme kertaa, että sekä "nimi"teksti, "leveys"teksti että "pituus"teksti saadaan luotua canvasille.

### Muoto-objektin muuttaminen

Käyttäjä kirjoittaa ChangeView näkymän syötekentään objektin uuden leveyden, pituuden ja nimen (esim. width=200, height=70, text=pöytä)
ja klikkaa "Change" nappia. 

![muutamuoto](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Kaaviot/Change%20Shape.png)

Napin painallus hakee kenttien tiedotja kutsuu validate_input-funktiota. Funktio tarkistaa, että annetut leveys- ja pituus-syöttee ovat sopivia parametrejä.
Sen jälkeen validate_input kutsuu CanvasHandler-luokan funktiota change_shape(200, 70, "pöytä"). Change_Shape muuttaa muoto-objektin näkymää canvasilla.
CanvasHandler kutsuu samalla valitun muodon Shape-luokan funktioita change_width(200), change_height(70), change_text("pöytä") ja muuttaa tiedot luokkaan.

### Tallennus json-tiedostoon

![talletus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Kaaviot/Load%20Json%20save%20.png)









