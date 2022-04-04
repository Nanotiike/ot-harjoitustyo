```mermaid
 classDiagram
      Pelaaja --> Pelaajia
      Ruutu -- Pelilauta
      Pelaaja "nappula" --> Pelilauta
      class Pelaajia{
          maara
	  min=2
	  max=8
      }
      class Pelilauta{
          ruutuja=40
      }
      class Ruutu{
          seuraava_ruutu 
      }
      class Pelaaja{
          pelinappula
	  pelinappulan_sijainti
      }
```
