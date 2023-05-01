# Changelog

### Viikko 3

## Muutokset:

- Luotu UI ja Rectangle-luokat, UI:n tarkoitus on vastata sovelluksen graafisesta käyttöliittymästä ja Rectangle:n tarkoitus on säilyttää kaikkien eri luotujen suorakulmioiden tiedot
- Ui:hin lisätty:
- ruudun-jako kahtia, canvas-alue, input-kentät leveydelle, korkeudelle ja nimelle, napit suorakulmion luonnille ja poistolle sekä exit-nappi
- hiiren klikkaus/trackaus ja muuttujat jotka trackaavat mitä suorakulmiota on viimeksi klikattu ja muuttuja-alustukset joita käytettään
   liikuttamisen koordinaattien laskemiseen että suorakulmio ei teleporttaa esim. hiiren yläkulman kohdalle kun sitä yrittää liikuttaa
- lisätyt funktiot:
 click_move: "etsii" päällimmäisimmän suorakulmion klikatessa suorakulmiota ja muuttaa sen "selected" suorakulmioksi,
 drag_move: suorakulmion liikuttelu vetämällä
 release_move: "deselect" suorakulmion on hiiren klikkauksen vapauttaa
 create_rectangle: Luo suorakulmion canvasille ja samalla lisätty ValueError expection leveys ja korkeus input-kentistä saaduille arvoille, että syötetyt
 arvot ovat lukuja. Jos arvo on virheellinen input-kenttien nimien yläpuolelle ilmestuu error-viesti jota kutsutaan. Jos arvo on luku, kutsuu Rectangle-luokkaa 
 ja lisää sen tiedot listaan jota myöhemmin käytetään tallennuksen ja latauksen yhteydessä, nyt vain pitää yllä leveys ja korkeus tietoja. 
 delete_rectangle: Poistaa viimeksi klikatun suorakulmion canvasilta (mutta ei vielä poista sitä listalta)

## Testit:
- Lisätty kaksi testiä, ensimmäinen testaa Ui-luokan input_kenttiä ja luoko se suorakulmion kun annetut arvot ovat lukuja,
  toinen testaa että suorakulmiota ei luoda jos annetut arvot eivät ole lukuja

## Tämän hetkinen toiminnallisuus mitä toimintamäärittelyssä on asetettu:

- Käyttäjä voi luoda useita eri suorakulmioita annettujen mittojen mukaan
- Suorakulmioita voi liikutella
- Suorakulmioita voi poistaa

## Seuraavaksi to do-listalla:

- Nimien lisäys suorakulmioille
- Tallennus ja lataus
- Vaatimusmäärittelyssä ei oltu asetettu tätä, mutta olisi kiva lisätä mahdollisuus muokata jo luodun suorakulmion kokoa/nimeä

### Viikko 4

## Muutokset:

- Muutettu tkinterin import tapaa "from tkinter import *":sta  "import tkinter as tk" (ja muokattu koodia muutoksen mukaisesti)
- Korjattu/formatoitu koodia pylintin kehotusten mukaan 
- Lisätty teksti-objektin luominen suorakulmion luonnin yhteydessä
- Lisätty checkbox josta canvasilla näkyvät tekstit saa näkyviin ja pois näkyvistä
- Lisätty tallennus ja lataustoiminnot json:in avulla
- Lisätty clickmove, dragmove, releasemove ja deleterectangle funktioihin teksti-objektin käsittelyä suorakulmio-objektin rinnalla
- Poistettu self.rectangle-lista, koska sitä ei tarvitakaan
- Muutettu "createrectanglefunction" funktio "create_rectangle"ksi ja siirretty suorakulmion luonti Rectangle-luokan funktioon "create"
- Rectangle-luokkaan lisätyy: self.id = suorakulmion id, self.text = korvaa self.name:n, self.text_id = teksti-objektin id, self._x, self._y = suorakulmion kulman koordinaatti
- Otettu tag:it käyttöön suorakulmio-objektiin ja teksti-objektiin  
- Jaettu koodi kolmeen eri luokkaan ja tiedostoon, class UI, class Rectangle, class EventHandler

## Testit:
- Poistettu Ui-luokan testit, lisätty handler_test ja rectangle_test joista toinen testaa EventHandler-luokkaa ja toinen Rectangle-luokkaa
- EventHandler testit: create_rectangle (suorakulmion luonti valid/invalid inputeilla), names_on_off (saako tekstit näkyviin/pois näkyvistä),
 release_move (testataan että suorakulmion/tekstin "valinta" nollaantuu), exit (testaa ohjelmsta poistumisen)

## Tämän hetkinen toiminnallisuus mitä toimintamäärittelyssä on asetettu:

- Käyttäjä voi luoda useita eri suorakulmioita annettujen mittojen mukaan
- Suorakulmioita voi liikutella
- Suorakulmioita voi poistaa
- Suorakulmion voi nimetä
- Tallennus ja lataus onnistuu (tällä hetkellä tallennuksia voi olla vain yksi, uusi tallennus yliajaa aikaisemman)

## Seuraavaksi to do-listalla:
- Koodin jaottelu vielä paremmin (esim. EventHandler luokasta eriytetään lataus ja tallennus omaan luokkaansa)
- Useamman tallennuksen tekeminen
- Tallennuksen poistaminen
- Jo luodun suorakulmion koon/nimen muuttaminen


### Viikko 5

## Muutokset:

- Lisätty ovaalin muodon lisäys, eriytetty huoneen(menee aina canvasilla muiden
 objektien taaks ja suorakulmion lisäys ja muutettu Rectangle-luokka
 Shape-luokaksi kuvaamaan paremmin luokan toimintaa
- Lisätty tuplaklikkaus ja siihen liitetty popup ikkuna jonka kautta voi muuttaa 
 jo olemassa olevan objektin nimeä/kokoa
- Siirretty delete (rectangle) nappi kaksoisklikkauksen avaamaan ikkunaan
- Eriytetty koodia enemmän ja muutettu pakkausrakennetta ja samalla korjattu/muutettu 
poistettu yksittäisiä asioita ns. siistitty koodia
- Korjattu/poistettu testejä, koska eivät toimi 
- muutettu joidenkin funktioiden nimiä kuvaamaan paremmin niiden toimintaa
## Seuraavaksi to do-listalla
- Testien korjaus
- Koodin jäsentelyn korjaus
- Useamman tallennuksen tekeminen ja tallennuksen poistaminen
- Valmiin muoto-objektin kopiointi
- Muoto-objektin kääntö


### Viikko 6

## Muutokset:

- Lisätty mahdollisuus useamman tallennuksen luomiseen
- Lisätty tallennetun tiedoston poistaminen
- Lisätty Shape-luokkaan funktioita/jaettu pienempiin funktioihin
- Jaettu SaveHandler luokkaa paremmin pienempiin funktioihin
- Korjattu ja luotu uusia testejä
- Lisätty Docstring:t
- Siirretty kaikki tekstin luonti pois Control-luokasta View-luokkaan
- Lisätty valitun objektin reunan värin muuttuminen
- Lisätty objektin vienti taakse/eteen

## Seuraavaksi to do-listalla:

- Lisää ValueError testit myös PopUp luokkaan
- View-luokasta popup-funktioiden vienti muualle/uuteen luokkaan
- Valmiin muoto-objektin kopiointi
- Muoto-objektin kääntö
- Tallennukselle/Lataukselle oma ikkuna, josta näkee tämän hetkiset tiedostot
