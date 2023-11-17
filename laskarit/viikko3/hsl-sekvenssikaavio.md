## HSL-matkakortti sekvenssikaavio

```mermaid
  sequenceDiagram
    participant main
    participant HKLLaitehallinto
    create participant rautatietori
    main->>rautatietori Lataajalaite
    create participant ratikka6
    main->>ratikka6 Lukijalaite
    create participant bussi244
    main->>bussi244 Lukijalaite 
```
