# Ohjelmistotekniikka, harjoitustyö

## **Room Planner**

Sovelluksella pystyy luomaan yksinkertaisia huone- ja huonekaluobjekteja vastaavia muotoja,
kuten suorakulmioita ja ovaaleja, antamalla niille mitat/nimen. Luotujen objektien nimiä ja
kokoa pystyy muuttamaan ja canvas-näkymän voi tallentaa ja ladata joko json-tiedostoon tai SQL-tietokantaan.

Kyseessä on tekijän ensimmäinen sovellusprojekti.  

Ohjelman käyttö on testattu Python versiolla 3.10.6

### **Dokumentaatio** 

- [Arkkitehtuurikuvaus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/changelog.md)
- [Koodilähteet](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/lahdekoodi.md)
- [Käyttöohje](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/kayttoohje.md)
- [Työaikakirjanpito](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/tyoaikakirjanpito.md)
- [Vaatimusmäärittely](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/vaatimusmaarittely.md)

## Ohjelman releaset

- [viimeisin release - loppupalautus](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/loppupalautus)

- [vanhempi 2.release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko6)
  
- [vanhempi 1.release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko5)

## Ohjelman käynnistys

### Asenna ensin sovelluksen riippuvuudet:

poetry install

### Lisää projekti-kansioon tyhjä "data" niminen kansio (huom! Sovelluksen alustus ei toimi ilman tätä):

mkdir data

### Ja alusta sovelluksen tietokanta (huom! Sovellus, eivätkä sen testit, toimi ennen tätä):

poetry run invoke build

### Käynnistä sovellus:

poetry run invoke start

## Ohjelman testaus

poetry run invoke test

## Testikattavuusraportti

poetry run invoke coverage-report

## Pylint-tarkistus

poetry run invoke lint
