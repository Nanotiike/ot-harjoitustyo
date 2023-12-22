# Vaatimusmäärittely harjoitustyölle

## Tarkoitus

Harjoitustyö tulee olemaan sudoku peli. Sudoku on perinteisesti 9x9 ruudukko joka koostuu yhdeksästä 3x3 ruudukosta. Koko 9x9 ruudukkoon tulee asettaa numerot 1-9 siten että samalla rivillä, sarakkeella tai 3x3 ruudukossa ei ole kahta samaa numeroa.

## Käyttäjät

Sovelluksell on vain yksi käyttäjä, eli sen pelaaja.

## Käyttöliittymäluonnos

Sovellus koostuu yhdestä näkymästä. Tässä näkymässä on sudoku ruudukko, jossa peli tapahtuu. Ruudukon yläpuolella on ajastin ja virheiden laskuri. Ruudukon alapuolella on lyhyet ohjeet kuinka pelata peliä.

## Perusversion toiminnallisuus

- Pelaaja näkee 9x9 sudoku ruudukon, jossa on osa numeroista täytetty. Sovellus luo täysin uuden ruudukon joka kerta kun sovellus avataan
- Pelaaja voi klikata ruutua ja painamalla numero näppäintä lisätä numeron ruutuun
  - Jos numero on väärin, peli ilmoittaa siitä pelaajalle eikä lisää nuemroa ruutuun
    - Peli pitää kirjaa tehdyistä virheistä
  - Jos pelaaja yrittää lisätä numeron ruutuun joka on jo täytetty niin peli ilmoittaa asiasta pelaajalle, mutta ei kuitenkaan lisää virheiden määrää
  - Jos pelaaja täyttää kaikki ruudut oikein, pelaaja voittaa pelin ja sovellus näyttää voittoruudun, jossa pelaaja näkee kuinka monta virhettä hän teki ja kuinka pitkään sudokun ratkaisemisessa kesti

#### Jatkokehitys ideoita

- Pelaaja voi luoda tunnuksen
- Sovellus pitää kirjaa pelien tuloksista ja tallentaa nämä tiedostoon, josta pelaaja voi omalla tunnuksellaan ne nähdä.
- Sovellus voi luoda useamman tason sudokuja
- Sovellukseen voi luoda omia sudoku haasteita
- Pelaaja voi numeroiden lisäämisen sijaan tehdä merkintöjä ruutuun, pitäen kirjaa siitä mitkä numerot voisivat mahdollisesti sopia siihen ruutuun
