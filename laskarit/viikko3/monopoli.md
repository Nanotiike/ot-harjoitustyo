## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitusruutu "1" -- "40" Ruutu
    Aloitusruutu "Sijainti" --> Monopolipeli
    Vankila "1" -- "40" Ruutu
    Vankila "Sijainti" --> Monopolipeli
    Sattuma ja yhteismaa -- "40" Ruutu
    Asemat ja laitokset -- "40" Ruutu
    Kadut -- "40" Ruutu
    Toiminnot -- "1" Ruutu
    Kortit -- Sattuma ja yhteismaa
    Toiminnot -- "1" Kortit
```
