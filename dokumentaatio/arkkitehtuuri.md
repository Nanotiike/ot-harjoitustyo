# Arkkitehtuuri

## Käyttöliittymä

Käyttöliittymä on tehty pygamella ja siinä on yksi näkymä. Näkymä toimii main luokassa ja sen funktionaalisuus tulee sudoku luokasta. Näkymä muuttuu sen mukaan mitä käyttäjä valitsee ruudukosta ja lisää numeroita ruudukkoon.

## Päätoiminnallisuus

Numeron lisääminen:
```mermaid
sequenceDiagram
  actor User
  participant main
  participant Sudoku
  user ->> main: muose click(x,y)
  main -> main: draw_backround()
  user ->> main: press 1-9
  main ->> sudoku: make_move(x,y,number)
  sudoku --> main: 0
  sudoku -> sudoku: player_board.append(x,y,number)
  main -> main: draw_backround()
```
