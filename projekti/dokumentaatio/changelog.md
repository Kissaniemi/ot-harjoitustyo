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
- Vaatimusmäärittelyssä ei oltu asetettu tätä, mutta olisi kiva lisätä mahdollisuus muokata jo luodun suroakulmion kokoa/nimeä
