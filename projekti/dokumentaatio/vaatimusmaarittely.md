# Alustava vaatimusmäärittely

## Sovelluksen idea

Sovelluksen perusidea on voida luoda huonepohjia ja sijoittaa erilaisia huonekaluobjekteja
luotuun huoneeseen.

Alustavasti sovelluksella ei ole erillisiä käyttäjätilejä, mutta jatkoideana olisi
pystyä luomaan myös käyttäjätili ja tallentamaan huoneita käyttäjätilille.

![esimerkkikuva](https://github.com/Kissaniemi/ot-harjoitustyo/blob/main/projekti/kuvat/esimerkkikuva.png)

<sub>Karkea esimerkkikuva ideasta</sub>

## Sovelluksen perustoiminnallisuus


Tehty merkinnät sillä huomautuksella että sovelluksen huonepohjien ja huonekalujen luomista ei ole vielä eritelty omikseen,
vaan tapahtuvat saman "Create Rectangle" napin kautta. Tarkoitus vielä eriyttää niin että huonepohjat pysyvät aina 
huonekalujen takana canvasilla.
### Käyttäjä voi luoda huonepohjia 
Tehty  - Alustavasti luotu huone voi olla vain suorakulmion mallinen
Tehty  - Huoneelle joko annetaan kirjallisesti mitat ja/tai huoneen kokoa pystyy muuttamaan vetämällä
Tehty  - Huoneen voi nimetä
Tehty  - Huoneen voi tallentaa
Tehty  - Tallennetun huoneen voi hakea
  - Tallennetun huoneen voi poistaa  
  - Luodun huoneen koolla on rajat
  
### Käyttäjä voi lisätä huonepohjaan huonekaluja
 
Tehty  - Alustavasti luotu huonekalu on vain suorakulmion mallinen
Tehty  - Huonekalulle joko annetaan kirjallisesti mitat ja/tai huonekalun kokoa pystyy muuttamaan vetämällä
Tehty  - Huonekalun voi nimetä
Tehty  - Huonekalua voi liikuttaa
Tehty  - Huonekalun voi tallentaa huoneen tallennuksen yhteydessä
  - Luodun huonekalun koolla on rajat
 
## Sovelluksen jatkokehitys
  
 Perustoiminnan jälkeen täydennettäviä ominaisuuksia 
 
   - Luotu huonekalu voi olla ympyrän tai L-muotoinen
   - Luotua huonekalua voi kiertää (L-muotoinen huonekalu)  
   - Luotuja huoneita voi yhdistää isommaksi huoneiden kokonaisuudeksi (ns. koko asunnon pohja)
   - Luodaan valmiita huonekaluobjekteja joita voidaan käyttää   
   - Zoomaus in/out 
   - Käyttäjätili
