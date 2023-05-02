# Arkkitehtuurikuvaus

Koodin rakenne on vielä niin kesken, että alla olevat tiedot eivät ole lopullisia, vaan alustavia.

Ajatus oli, että ui-tiedosto sisältäisi vain käyttöliittymästä vastaavan koodin, mutta siinä on vielä esim. ui_control.py ja sen Control-luokka, jonka idea oli vastata ikkunan oikealla olevalla canvas-alueen näkymästä ja ehkä myös pääasiassa sovelluslogiikasta. Ui_view.py:n View-luokan oli tarkoitus vastata ikkunan vasemmalla puolella olevasta "syöte, nappulat, jne"-näkymästä. Käyttöliittymän ja sovelluslogiikan erottelu on näiden osalta vielä siis kesken.

View-luokassa on myös tällä hetkellä joukko message-popup- funktioita, jotka on tarkoitus siirtää erilliseen omaan luokkaansa tai
ui-tiedostossa olevaan pop_up_window.py:hyn, jossa on jo yksittäinen PopUp-luokka custom ikkunalle. 

## Sovelluslogiikka

shape-tiedostosta löytyy shape_class.py:n Shape-luokka, jonka tarkoitus on vastata canvasille ilmestyvien muoto-objektien attribuuttien tiedoista ja muutoksista. Näiden muotojen kontrollointi canvasilla tapahtuu ui_control.py:n Control-luokan kautta.


## Tietojen tallennus

file_handler-tiedoston save_load.pyn: SaveHandler-luokka vastaa sovelluksen tallennuksesta ja latauksesta sovelluksen ulkopuoliseen json-tiedostoon. 
Käyttäjä itse päättää minkä nimiseen json-tiedostoon canvasin näkymä tallennetaan ja mistä ladataan. Käyttäjällä on lisäksi mahdollisuus poistaa json-tiedosto tiedoston nimen perusteella.

Tiedot tallennetaan json tiedostoon seuraavassa muodossa:

´´{
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
´´´

## Vanhentunut/Alustava pakkausrakenne

![kaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/pakkasukaavio.png)

## Vanhentunut/Alustava luokkakaavio

![kaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/luokkakaavio.png)

## Vanhentunut/Alustava sekvenssikaavio

![kaavio](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/sekvenssikaavio.png)



