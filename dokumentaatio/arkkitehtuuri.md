# Arkkitehtuuri

## Käyttöliittymä

Käyttöliittymä on tehty pygamella ja siinä on yksi näkymä. Näkymä toimii main luokassa ja sen funktionaalisuus tulee sudoku luokasta. Näkymä muuttuu sen mukaan mitä käyttäjä valitsee ruudukosta ja lisää numeroita ruudukkoon.

## Päätoiminnallisuus

Kuvataan seuraavaksi sekvenssikaaviolla päätoiminnallisuudet.

Numeron lisääminen:
```mermaid
sequenceDiagram
  actor User
  participant Game_loop
  participant Renderer
  participant Sudoku
  User ->> Game_loop: muose click(x,y)
  Game_loop -> Renderer: render(x,y)
  User ->> Game_loop: press 1-9
  Game_loop ->> Sudoku: make_move(x,y,number)
  Sudoku --> Game_loop: 0
  Sudoku -> Sudoku: player_board.append(x,y,number)
  Game_loop -> Renderer: render(x,y)
```
