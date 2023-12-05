# Arkkitehtuuri

## Käyttöliittymä

Käyttöliittymä on tehty pygamella ja siinä on yksi näkymä. Näkymä toimii main luokassa ja sen funktionaalisuus tulee sudoku luokasta. Näkymä muuttuu sen mukaan mitä käyttäjä valitsee ruudukosta ja lisää numeroita ruudukkoon.

## Päätoiminnallisuus

Kuvataan seuraavaksi sekvenssikaaviolla päätoiminnallisuudet.

Numeron lisääminen:
```mermaid
sequenceDiagram
  actor User
  participant main
  participant Sudoku
  User ->> main: muose click(x,y)
  main -> main: draw_backround()
  User ->> main: press 1-9
  main ->> Sudoku: make_move(x,y,number)
  Sudoku --> main: 0
  Sudoku -> Sudoku: player_board.append(x,y,number)
  main -> main: draw_backround()
```
