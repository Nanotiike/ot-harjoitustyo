# Vaatimusmäärittely harjoitustyölle

## Tarkoitus

Harjoitustyö tulee olemaan sudoku peli. Sudoku on perinteisesti 9x9 ruudukko joka koostuu yhdeksästä 3x3 ruudukosta. Koko 9x9 ruudukkoon tulee asettaa numerot 1-9 siten että samalla rivillä, sarakkeella tai 3x3 ruudukossa ei ole kahta samaa numeroa.

## Perusversion toiminnallisuus

- Yksinkertainen käyttöliittymä pygamella, jossa on sudoku ruudukko ja numero näppäimet. Pelaaja voi valita yhden ruudun ruudukosta ja oikeata numeroa painamalla asettaa numeron ruutuun.
- Peli luo automaattisesti uuden sudoku ruudukon ja näyttää sen pelaajalle niin että vain osa numeroista näkyy.
- Kun pelaaja saa numeron oikein, se lisätään ruudukkoon. Kun hän saa numeron väärin, sitä ei lisätä ruudukkoon vaan viesti tulee näytölle että numero oli väärä.

#### Jatkokehitys ideoita

- Pelaaja voi luoda tunnuksen
- Peli pitää kirjaa siitä kuinka monta virhettä pelaaja teki pelin aikana ja kuinka pitään sudokun ratkaisemiseen kesti, ja tallentaa nämä tiedostoon, josta pelaaja voi omalla tunnuksellaan ne nähdä.
- Peli voi luoda useamman tason sudokuja
- Peliin voi luoda omia sudoku haasteita
