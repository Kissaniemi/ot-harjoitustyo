# Vaatimusmäärittely

## Sovelluksen idea

Sovelluksen perusidea on voida luoda huonepohjia ja sijoittaa erilaisia huonekaluobjekteja
luotuun huoneeseen.

![malli](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/Ohje/avausruutu.png)

## Sovelluksen perustoiminnallisuus

- Käyttäjä voi luoda valkopohjaisia suorakulmio “huone”-objekteja, sekä harmaapohjaisia suorakulmio ja ovaali “huonekalu”-objekteja canvas-alueelle
- Canvas-alue laajenee ikkunan koon mukaan
- Objekteille annetaan kirjalliset mitat ja teksti ja objektin mittoja ja tekstiä voi muuttaa sen luomisen jälkeen
- Objektien koolla on rajat ja niiden pitää olla isompia kuin 4 pikseliä ja pienempiä kuin 2001 pikseliä
- Luotuja objekteja voi kopioida ja kääntää
- Luotuja objekteja voi poistaa
- Ohjelma luo automaattisesti tekstin ja mittojen perusteella teksti-objektit muoto-objektin sivuille, jotka päivittyvät jos objektin mittoja/tekstiä muuttaa
- Käyttäjä voi piilottaa canvasilla näkyvät tekstit 
- Käyttäjä voi muuttaa canvasin värimaailmaa “blueprint” väreihin
- Canvas-näkymän objektit pystyy tallentemaan sekä json-tiedostoon, että sql-tietokantaan 
- Tallennetun canvas-näkymän objektit pystyy lataamaan sekä json-tiedostosta, että sql-tietokannasta
- Tallennetun json-tiedoston ja sql-tietokannan tallennukseen liittyvät rivit pystyy poistamaan

## Sovelluksen jatkokehitys

- käyttäjä voi luoda  muunkin muotoisia objekteja kuten L-muotoja
- käyttäjä voi zoomata ja/tai scrollata canvasia ja asettaa sen koon 
- käyttäjä voi päättää ja vaihtaa objektien värejä 
- Käyttäjä voisi skaalata oikeita cm:jä ja mittayksiköitä voisi vaihtaa senttien ja tuumien välillä


