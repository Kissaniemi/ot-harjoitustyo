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
- [Koodilähteet](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/koodin_lahteet_ideat.md)
- [Käyttöohje](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/kayttoohje.md)
- [Työaikakirjanpito](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/tyoaikakirjanpito.md)
- [Vaatimusmaarittely](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/vaatimusmaarittely.md)

## Ohjelman releaset

- [viimeisin release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko6)
  
- [vanhempi 1.release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko5)

## Ohjelman käynnistys

### Asenna ensin ohjelman riippuvuudet:

poetry install

### Ja alusta ohjelman tietokanta:

poetry run invoke build

### Käynnistä ohjelma:

poetry run invoke start

## Ohjelman testaus

poetry run invoke test

## Testikattavuusraportti

poetry run invoke coverage-report

## Pylint-tarkistus

poetry run invoke lint
