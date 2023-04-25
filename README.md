# Ohjelmistotekniikka, harjoitustyö

## **Room Planner**

Sovelluksella pystyy luomaan yksinkertaisia huone- ja huonekaluobjekteja vastaavia muotoja,
kuten suorakulmioita ja ovaaleja, antamalla niille mitat/nimen. Luotujen objektien nimiä ja
kokoa pystyy muuttamaan tuplaklikkauksella ja huonenäkymän voi tallentaa ja ladata. Sovelluksella ei ole 
käyttäjätilejä ja tällä hetkellä vain yhden tallennuksen tekeminen on mahdollista 

Kyseessä on tekijän ensimmäinen sovellusprojekti.  

### **Dokumentaatio** 

- [vaatimusmaarittely.md](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/vaatimusmaarittely.md)
- [tyoaikakirjanpito.md](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/tyoaikakirjanpito.md)
- [changelog.md](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/changelog.md)
- [arkkitehtuurikuvaus](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/luokkakaavio.jpg)
- [koodilähteet](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/dokumentaatio/koodin_lahteet_ideat.md)

# Tähän linkki releaseen

## Ohjelman käynnistys

 Asenna ensin ohjelman riippuvuudet:

poetry install

 Suorita alustustoimenpiteet:

poetry run invoke build

Käynnistä ohjelma:

poetry run invoke start

## Ohjelman testaus

poetry run invoke test

## Testikattavuusraportti

poetry run invoke coverage-report

## Pylint-tarkistus

poetry run invoke lint
