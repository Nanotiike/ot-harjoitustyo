# Sudoku -peli

Pelissä pelaajat voivat ratkaista sudoku ruudukon.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/Nanotiike/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

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
poetry run invoke coverage_report
```
Raportti generoituu htmlcov-hakemistoon.
#### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```
