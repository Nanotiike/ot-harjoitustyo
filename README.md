# Sudoku -peli

Pelissä pelaajat voivat ratkaista sudoku ruudukon. Sudoku ruudukko generoidaan pelaajalle valmiiksi ja he voivat yrittää ratkaista sitä kunnes onnistuvat tai sulkevat ohjelman.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Release](https://github.com/Nanotiike/ot-harjoitustyo/releases)

## Asennus

1. Asenna riippuvuudet komennolla:
```
poetry install
```
2. Käynnistä sovellus komennolla:
```
poetry run invoke start
```

## Komentorivi

#### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:
```
poetry run invoke start
```
#### Testaus
Testit suoritetaan komennolla:
```
poetry run invoke test
```
#### Testikattavuus
Testikattavuuden voi generoida:
```
poetry run invoke coverage-report
```
Raportti generoituu htmlcov-hakemistoon.
#### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```
