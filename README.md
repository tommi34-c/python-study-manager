# Python Study Manager

**Versio: v1.2 - keskeneräinen**

## Projektin tarkoitus

Python Study Manager on Python-projektini,
josta kehitän täysimääräisen opiskeluhallinta sovelluksen (Study Management Application)

Sovelluksen tavoitteena on seurata ohjelmointi kielten opiskelua,
käytettyjä opiskelutunteja,
viikottaista edistymistä ja myöhemmin myös oppimistavoitteita.

Kehitämme ohjelmaa vaiheittain,
jossa opitaan Python perusteet ja ohjelmisto kehityksen työprosessin.

## Nykyiset ominaisuudet

| Nro | Ominaisuudet | Toteutus | Tila |
|---|---|---|---|
| 1 | Ohjelman käynnistys | `python study_manager.py` | Valmis |
| 2 | Opiskelijan nimen kysyminen | `input()` | Valmis |
| 3 | Ohjelmointikielen kysyminen | `input()` | Valmis |
| 4 | Päivittäisen opiskelutuntimäärän kysyminen | `int(input())` | Valmis |
| 5 | Viikoittaisen opiskelutuntimäärän ennuste | `study_hours * 7` | Valmis |
| 6 | Opiskelutietojen tulostaminen | `print()`  f-merkkijonot | Valmis |
| 7 | Opiskelupäivän arviointi | `if` `elif` `else` | Valmis |
| 8 | Seitsemän opiskelupäivän käsittely | `for` `range()` | Valmis |
| 9 | Jokaisen päivän tuntien kysely | `daily_hours` | Valmis |
| 10 | Opiskelutuntien yhteenlasku | `total_hours += daily_hours` | Valmis |
| 11 | Viikkotuntien näyttäminen | `print()` | Valmis |
| 12 | Päivittäisen keskiarvon laskeminen | `average_hours` | Työn alla |



    - ohjelma on keskeneräinen
    - 11 toimintoa on toteutettu
    - keskiarvolaskenta on vielä työn alla

Nykyinen opiskelupäivän arviointi
Päivittäiset tunnit	Palaute
0–1	Jatka harjoittelua!
2–3	Hyvää edistymistä!
4 tai enemmän	Erinomainen opiskelupäivä!

Toteutettu teknologia
- Ohjelmointikieli: Python 3
- Käyttöliittymä: komentorivi (CLI)
- Kehitysympäristö: Fedora Linux KDE
- Lähdekoodi: study_manager.py
- Tietojen käsittely: muuttujat ja laskutoimitukset keskusmuistissa
- Ohjausrakenteet: ehtolauseet ja for-silmukka

Seuraavat kehitys kohteet:
1. v1.2 viimeistely: keskiarvon laskeminen ja viikkoraportti
2. v1.3: funktiot (def) ja ohjelman modulaarinen rakenne
3. v1.4: virheellisten syötteiden käsittely (try, except)
4. v2.0: opiskelu historian tallennus JSON- ja CSV-tiedostoihin
5. v2.1: opiskelutavoitteet ja edistymisen seuranta
6. v3.0:SQLite-tietokanta ja graafiset raportit

Nykytila: 11 ominaisuutta toteutettu. Ohjelman testaus ja keskiarvolaskennan käyttöönotto ovat seuraavia kehitysvaiheita.

## Tulevat kehitysvaiheet

1. v1.0 - Opiskelutietojen kerääminen
    - Opiskelijan nimi
    - Ohjelmointi kieli
    - Opiskelu tunnit
    - Viikkotuntien arvio

2. v1.1 - Ehtolauseet
    - if, elif ja else
    - Ohjelma antaa palautetta opiskelu tunneista.

3.  v1.2.1 - Toistorakenteet
    - for-silmukka ja range() käytössä
    - Seitsemän opiskelupäivän tuntien seuranta
    - Päivittäisen keskiarvon laskeminen työn alla

4. v1.2.2 - while-silmukka (suunniteltu)
    - while-silmukan toimintaperiaate
    - Silmukan lopetusehdon harjoittelu
    - Käyttäjän syötteiden käsittely silmukassa

5. v1.3 - Funktiot
    - Ohjelman jakaminen uudelleen käyttäviin osiin def - rakenteella.

6. 2.0 - Tietojen tallentaminen
    - Opiskelu tietojen tallentaminen json tai csv.

7. 3.0 - Tietokanta ja raportointi
    - SQLite-tietokanta
    - Opiskeluhistoria
    - Edistymisen visuaalisointi
