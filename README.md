# Ohjelmistotekniikka, harjoitustyö

## **Room Planner**

Sovelluksella pystyy luomaan yksinkertaisia huone- ja huonekaluobjekteja vastaavia muotoja,
kuten suorakulmioita ja ovaaleja, antamalla niille mitat/nimen. Luotujen objektien nimiä ja
kokoa pystyy muuttamaan tuplaklikkauksella ja huonenäkymän voi tallentaa ja ladata. Sovelluksella ei ole 
käyttäjätilejä ja tällä hetkellä vain yhden tallennuksen tekeminen on mahdollista 

Kyseessä on tekijän ensimmäinen sovellusprojekti.  

### **Dokumentaatio** 

- [arkkitehtuurikuvaus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/arkkitehtuuri.md)
- [changelog](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/changelog.md)
- [koodilähteet](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/koodin_lahteet_ideat.md)
- [käyttöohje](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/kayttoohje.md)
- [tyoaikakirjanpito](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/tyoaikakirjanpito.md)
- [vaatimusmaarittely](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/vaatimusmaarittely.md)

## Ohjelman releaset

- [viimeisin release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko6)
  
- [vanhempi 1.release](https://github.com/Kissaniemi/ot-harjoitustyo/releases/tag/viikko5)

## Ohjelman käynnistys

### Asenna ensin ohjelman riippuvuudet:

poetry install

poetry run invoke build

### Käynnistä ohjelma:

poetry run invoke start

## Ohjelman testaus

poetry run invoke test

## Testikattavuusraportti

poetry run invoke coverage-report

## Pylint-tarkistus

poetry run invoke lint
