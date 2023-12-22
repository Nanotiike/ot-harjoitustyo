# Testaus

Ohjelmaa on testattu automatisoiduin yksikkötestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sudoku ruudukosta vastaavaa `Sudoku`-luokkaa testataan [TestSudoku]()-testiluokalla. Sudoku ruudukon generoinnista vastaavaa `Generate_sudoku`-luokkaa testataan [TestSudokuGenerator]()-testiluokalla.

### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 33%

![]()

Testaamatta jäivät build.py, clock.py, renderer.py, ja game_loop.py. 

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen]() kuvaamalla tavalla Linux-ympäristöön. 

### Toiminnallisuudet

Kaikki [määrittelydokumentin]() ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi. Kaikkien toiminnallisuuksien yhteydessä on yritetty myös toimia tahallaan virheellisesti.
