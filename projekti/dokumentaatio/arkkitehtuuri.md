# Arkkitehtuurikuvaus

Koodin rakenne on vielä niin kesken, että alla olevat tiedot eivät ole lopullisia, vaan alustavia.

## Käyttöliittymä

Ajatus oli, että ui-tiedosto sisältäisi vain käyttöliittymästä vastaavan koodin, mutta siinä on vielä esim. ui_control.py ja sen Control-luokka, jonka idea oli vastata ikkunan oikealla olevalla canvas-alueen näkymästä ja ehkä myös pääasiassa sovelluslogiikasta. Ui_view.py:n View-luokan oli tarkoitus vastata ikkunan vasemmalla puolella olevasta "syöte, nappulat, jne"-näkymästä. Käyttöliittymän ja sovelluslogiikan erottelu on näiden osalta vielä siis kesken.

View-luokassa on myös tällä hetkellä joukko message-popup- funktioita, jotka on tarkoitus siirtää erilliseen omaan luokkaansa tai
ui-tiedostossa olevaan pop_up_window.py:hyn, jossa on jo yksittäinen PopUp-luokka custom ikkunalle. 

## Sovelluslogiikka

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

## Vanhentunut/Alustava pakkausrakenne

![kaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/pakkasukaavio.png)

## Vanhentunut/Alustava luokkakaavio

![kaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/luokkakaavio.png)

## Vanhentunut/Alustava sekvenssikaavio

![kaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/sekvenssikaavio.png)



