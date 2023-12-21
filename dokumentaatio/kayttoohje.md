# Käyttöohje

## Käynnistysohje

1. Asenna riippuvuudet komennolla:
```
poetry install
```
2. Käynnistä sovellus komennolla:
```
poetry run invoke start
```

## Pelin pelaaminen

Seuraava näkymä avautuu kun peli käynnistyy:

![]()

Numeron lisääminen ruutuun tapahtuu klikkaamalla ruutua ja sen jälkeen painamalla haluttua numeroa

Jos numero on väärä tulee ruudulle tekstiboksi joka sanoo näin. 

## Voittaminen

Jos pelaaja onnistuu täyttämään sudoku ruudukon kokonaan, avautuu hänelle seuraava näkymä:

![]()

Tästä näkymästä näkee kuinka monta virhettä teki pelin aikana ja kuinka pitkään ratkaisuun meni.
