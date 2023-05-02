# Käyttöohje

Projektin viimeisin [release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko6)

## Ennen käynnistystä

### Asenna ensin ohjelman riippuvuudet:

poetry install

### Käynnistä ohjelma:

poetry run invoke start


## Ohjelman käyttö

Sovellus avautuu suoraan pääikkunaan.

![aloitus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/kayttokuva1.png)

### Objektin luonti

Pääikkunassa on vasemmalla puolella kentät joihin käyttäjä voi syöttää leveyden (width), pituuden (height) ja tekstin (text). Teksti-kentän täyttäminen ei ole pakollista. Leveys ja pituus syötteiden pitää olla isompia kuin 4 ja pienempiä kuin 2000, eivätkä ne myöskään voi olla tyhjiä.

Syötteiden täytön jälkeen käyttäjä voi painaa:
- "Create Room" nappia, joka luo valkotaustaisen paksumpireunaisen suorakulmion. 
- "Create Rectangle" nappia, joka luo harmaataustaisen ohuempireunaisen suorakulmion.
- "Create Oval" nappia, joka luo harmaataustaisen ohuempireunaisen ovaalin.
luodut muodot ilmestyvät oikealla puolella olevalle valkoiselle canvas-alueelle.

Canvasilla olevia muoto-objekteja voi liikuttaa klikkaamalla ja vetämällä niitä vasemmalla hiiren painikkeella.

Canvasilla näkyvät tekstit voi piilottaa "texts on/off" täpästä.

![tekstit](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/kayttokuva5.png)

### Jo luodun objektin muuttaminen ja/tai poistaminen

Canvasille jo luotua objektia voi muuttaa kaksoisklikkaamalla niitä vasemmalla hiiren panikkeella. Tällöin ikkunan päälle aukeaa popup-ikkuna, josta valitun objektin kokoa ja nimeä voi muuttaa. Ikkunasta pystyy myös poistamaan valitun objektin. 

Objektiapystyy myös tuomaan canvasilla eteen valitsemalla objekti ja klikkaamalla sitä oikealla hiiren painikkeella. 
Tuplaklikkaamalla oikeaa hiiren painiketta objektin saa vietyä taakse.

![muutos](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/kayttokuva3.png)

### Tallentaminen ja lataus

Canvas-näkymän voi tallentaa klikkaamalla "Save File" nappia, jolloin ilmestyy popup-ikkuna joka kysyy tiedoston nimeä johon tiedosto tallennetaan. Tiedostot tallentuvat json-tiedostoon, joten tiedoston nimeksi riittää antaa esim. "testi" jolloin nnäkymä tallentuu "testi.json" tiedostoon.

Canvas-näkymän lataus toimii samalla lailla "Load File" napista, haetun tiedoston nimeksi riittää antaa vain "testi" jolloin se löytää "testi.json" tiedoston, jos sellainen on olemassa

Ohjelmassa on lisäksi "Delete File" nappi, joka avaa tallennuksen/latauksen näköisen popup-ikkunan, nyt ohjelma poistaa syötetyn nime mukaisen json-tiedoston, jos sellainen löytyy.

![tallennus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/kayttokuva4.png)

Ohjelmasta voi poistua alhaalla olevasta "Exit" napista, joka vielä varmistaa haluatko poistua ohjelmasta.

