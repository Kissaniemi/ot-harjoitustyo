# Arkkitehtuurikuvaus

## Sovelluksen rakenne

Sovelluksen rakenne koostuu viidestä src-kansion alaisesta kansiosta.

![pakkauskaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Kaaviot/pakkausrakenne.png)

Ui ja popups-kansioissa on sovelluksen käyttöliittymästä vastaavat luokat ja logic_handler- kansiossa sovelluksen logiikasta vastaavat luokat. File_handler luokka vastaa sovelluksen pysyvän tiedon tallentamisesta json-tiedostoon ja SQL-tietokantaan. Shapes-kansiossa on sovelluksen käsittelemien muoto-objektien luokka.

## Käyttöliittymä-luokat

Käyttöliittymässä on kolme eri pääasiallista näkymää ja niistä vastaavaa luokkaa, Muodon luominen (MainView), Muodon muuttaminen (ChangeView) ja Canvas-alueen näkymä (CanvasView). Canvas-alueen näkymä on koko ajan näkyvillä ikkunan oikeassa reunassa ja sitä kautta vaihdetaan ikkunan vasemman reunan näkymää "Muodon luonti" ja "Muodon muutos" näkymien välillä nappia painamalla. Canvas-näkymä kutsuu näkymää vaihtaakseen UI-luokan funktioita "show_main_view" ja "show_change_view". "Muodon muutos" näkymä kutsuu vain sovelluslogiikasta vastaavan CanvasHandler-luokan funktioita. "Muodon luonti" näkymä kutsuu CanvasHandler luokan lisäksi kahta eri talletukseen liittyvää luokkaa JsonpopUps ja SqlPopUps, joista kumpikin ovat käyttöliittymä luokkia, jotka kutsuvat sovelluslogiikan DataHandler- ja JsonHandler- tai SqlHandler-luokkia.

## Sovelluslogiikka-luokat

Sovelluslogiikka on pyritty eriyttämään käyttöliittymästä mahdollisimman hyvin.
Pääasiallisesti sovelluslogiikasta vastaa CanvasHandler-luokka 
shape-tiedostosta löytyy shape_class.py:n Shape-luokka, jonka tarkoitus on vastata canvasille ilmestyvien muoto-objektien attribuuttien tiedoista ja muutoksista. Näiden muotojen kontrollointi canvasilla tapahtuu ui_control.py:n Control-luokan kautta.


## Tietojen tallennus

file_handler-tiedoston save_load.pyn: SaveHandler-luokka vastaa sovelluksen tallennuksesta ja latauksesta sovelluksen ulkopuoliseen json-tiedostoon. 
Käyttäjä itse päättää minkä nimiseen json-tiedostoon canvasin näkymä tallennetaan ja mistä ladataan. Käyttäjällä on lisäksi mahdollisuus poistaa json-tiedosto tiedoston nimen perusteella.

Tiedot tallennetaan json tiedostoon seuraavassa muodossa:

```{
  "shapes": [
    {
      "width": 400.0,
      "height": 600.0,
      "name": "",
      "x": 50.0,
      "y": 50.0,
      "shape": "room"
    },
    {
      "width": 150.0,
      "height": 60.0,
      "name": "sohva",
      "x": 86.0,
      "y": 77.0,
      "shape": "rectangle"
    },
    {
      "width": 120.0,
      "height": 40.0,
      "name": "p\u00f6yt\u00e4",
      "x": 103.0,
      "y": 172.0,
      "shape": "oval"
    }
  ]
}
```

## Päätoiminnallisuus

Käyttäjä kirjoittaa pääikkunan syötekenttään objektin leveyden, pituuden ja nimen (esim. width=100, height=50, text=sohva)
ja klikkaa "create rectangle" nappia. 

Napin painallus hakee kenttien tiedot ja lisää siihen nappiin liitetyn muoto-tiedon "rectangle" ja kutsuu validate_input-funktiota (shape_type, text_type, width_type, height_type)-attribuuteilla eli tässä ("rectangle", "sohva", 100, 50). Funktio tarkistaa, että annetut leveys- ja pituus-syötteet/attribuutit ovat sopivia parametrejä.

Sen jälkeen validate_input alustaa Shape-luokan objektin shape = Shape(self._ canvas, width, height, text, shape_type) 
eli shape = Shape(self._ canvas, 100, 50, "sohva", "rectangle") ja sitten erikseen kutsuu Shape-luokan create_shape funktiota (shape, shape_type) eli (shape, "rectangle"), joka tarkistaa minkä tyyppinen muoto halutaan luoda. 

Create_shape funktio sitten kutsuu Shape-luokan create_rectangle-funktiota, joka luo canvasille suorakulmion aiemmin annettujen attribuuttien mukaan.
Lopuksi se kutsuu myös Shape-luokan create_text-funktiota, joka luo aiemmin annettujen attribuuttien mukaan teksti-objektin, joka ilmestyy canvasille suorakulmion alle.






