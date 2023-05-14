# Käyttöohje

Projektin viimeisin [release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko6)

## Ennen käynnistystä

### Asenna ensin ohjelman riippuvuudet:

poetry install

### Ja alusta sovelluksen tietokanta (huom! Sovellus eivätkä sen testit toimi ennen tätä):

poetry run invoke build

### Käynnistä ohjelma:

poetry run invoke start


## Ohjelman käyttö

Sovellus avautuu suoraan pääikkunaan.

![aloitus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/avausruutu.png)

### Objektin luonti

Pääikkunassa on vasemmalla puolella kentät joihin käyttäjä voi syöttää leveyden (width), pituuden (height) ja tekstin (text). Teksti-kentän täyttäminen ei ole pakollista. Leveys ja pituus syötteiden pitää olla isompia kuin 4 ja pienempiä kuin 2000, eivätkä ne myöskään voi olla tyhjiä.

Syötteiden täytön jälkeen käyttäjä voi painaa:
- "Create Room" nappia, joka luo valkotaustaisen paksumpireunaisen suorakulmion. 
- "Create Rectangle" nappia, joka luo harmaataustaisen ohuempireunaisen suorakulmion.
- "Create Oval" nappia, joka luo harmaataustaisen ohuempireunaisen ovaalin.

Luodut muodot ilmestyvät oikealla puolella olevalle valkoiselle canvas-alueelle.

![luomuoto](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/luotuobjekti.png)

Canvasilla olevia muoto-objekteja voi liikuttaa klikkaamalla ja vetämällä niitä vasemmalla hiiren painikkeella. Valittu liikuteltava objekti näkyy punaisella ääriviivalla.

![liiku](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/liikuttelu.png)

Canvasilla näkyvät tekstit voi piilottaa "texts on/off" täpästä.

![pois](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/tekstipois.png)

Canvasilla värimaailmaa voi muuttaa "blueprint" näkymäksi "blueprint mode on/off" täpästä.

![sini](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/blueprint.png)

### Jo luodun objektin muuttaminen ja/tai poistaminen

Canvasille jo luotua objektia voi muuttaa klikkaamalla canvasilla näkyvästä "Change view" napista, joka vaihtaa vasemmalla olevan "CREATE SHAPE" näkymän "CHANGE SHAPE" näkymäksi. Nyt uudessa näkymässä voit valita objektin ja syöttää kentiin halutut muutokset (tai pitää jotain samana ja muuttaa vain yhtä tietoa).

Näkymästä voi myös tuoda valittua objektia canvasilla eteen tai viedä taakse. Valitun objektin voi myös poistaa "Delete" napista tai kopioida "Copy" napista. "Clear Canvas" nappi tyhjentää koko canvas näkymän. 
Jos haluat takaisin muodon luomisnäkymään, klikkaa ylhäällä olevaa "Create view" nappia.

![muutos](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/muutos.png)

Valittua objektia voi myös kääntää klikkaamalla hiiren oikealla

![kierra](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/kaannos.png)

### Tallentaminen ja lataus

Canvas-näkymän voi tallentaa klikkaamalla "Save File" nappia, jolloin ilmestyy popup-ikkuna joka kysyy haluatko tallentaa json-tiedostoon vai SQL-tietokantaan. Voit myös klikata "Show all SQL save names" tai " Show all json save names" nappia, jolloin ruudulle ilmestyy ruutu joka kertaa kaikkien sen löytämien sen tyyppisten tallennusten nimet.

![talletus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/tallennus.png)

Jos klikkaat "Save to json" tai "Save to SQL" nappeja, saat uuden popupikkunan joka kysyy millä nimellä haluat tallentaa. Tiedoston nimeksi riittää antaa esim. "testi" jolloin näkymä tallentuu "testi.json" tiedostoon tai "testi" nimellä SQL-tietokantaan.

![muoto](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/nimimuoto.png)

Canvas-näkymän lataus toimii samalla lailla "Load File" napista, haetun tiedoston nimeksi riittää antaa vain "testi" jolloin se löytää tiedoston, jos sellainen on olemassa.

Ohjelmassa on lisäksi "Delete File" nappi, joka avaa tallennuksen/latauksen näköisen popup-ikkunan, nyt ohjelma poistaa syötetyn nimen mukaisen tiedoston, jos sellainen löytyy.

Ohjelmasta voi poistua alhaalla olevasta "Exit" napista, joka vielä varmistaa haluatko poistua ohjelmasta.

