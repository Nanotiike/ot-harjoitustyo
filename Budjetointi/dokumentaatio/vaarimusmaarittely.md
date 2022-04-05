# Vaatimusmäärittely

## Sovelluksen tarkoitus

Jokapäiväisten maksujen budjetointi sovellus, johon voi kirjata kuukauden tulot ja menot. Käyttöliittymästä voi sitten tarkastella tämän kuukauden ja edellisten kuukauksien tuloja ja menoja. Voi ehkä myös tehdä suunnitelmia tuleville kuukausille.

## Käyttäjät

Alussa vain normaali käyttäjä. En nää syytä lisätä muita käyttäjiä.

## Käyttöliittymäluonnos

Sovellus koostuu lähinnä kolmesta eri näkymästä. Ensimmäinen on kirjautumis sivu, jossa on vain mitä tarvitaan sivulta. Toinen on käyttäjän luontisivu, jossa on samoin vain se mitä tarvitaan. 
Viimeinen näkymä on varsinainen budjetointi sivu. Tässä näkymässä on taulukko, jossa on ylhäällä x-akselilla kuukauden päivät ja vasemmalla y-akselilla erillaisia tulo ja meno joukkoja kuten "ruokamenot". Käyttäjä voi itse tehdä näitä joukkoja ja sitten kirjoittaa menoja kunkin päivän kohdalle, jotka sitten yhdistetään taulukon oikealle puolelle.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen pitää olla uniikki ja tarpeeksi pitkä. Lisäksi pitää tehdä salasana
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasanan
  - Järjestelmä ilmoittaa jos käyttäjää ei olemassa, tai salasana ei täsmää

### Kirjautumisen jälkeen

- Käyttäjä voi luoda joukkoja joihin voi kirjata eri tuloja ja menoja.
- Käyttäjä voi kirjata erilliset tulot ja menot taulukkoon ja nähdä niiden summan.
  - Näihin voi myös tarvittaessa kirjata lisää tietoa, kuten kulutuksen nimi, yms.
- Käyttäjä voi myös katsella edellisten kuukauksien tuloja ja menoja.
- Käyttäjä voi myös nähdä yleiset tilastot omista kulutuksistaan.

## Jatkokehitysideoita

- Käyttäjä voisi tehdä myös suunnitelmia tulevien kuukauksien varalta
- Käyttäjä voisi myös nähdä suunnitelman vuosi kerrallaan, eikä vain kuukausi.
  - Tässä olisi kaikki samat funktionaalisuudet kuin kuukausissa, mutta vain suuremmassa mittakaavassa.

