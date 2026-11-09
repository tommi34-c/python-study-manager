# Python Study Manager – Oppimislista

**Päivitetty:** 10.11.2026  
**Projekti:** `/mnt/projektit/github/python-study-manager`  
**Opiskelumenetelmä:** teoria → oma toteutus → koodikatselmointi → virheen korjaus → testi → Git-commit.

## Opitut asiat

- [x] Python-ohjelman suorittaminen terminaalissa (`python study_manager.py`)
- [x] Muuttujat ja tietotyypit (`str`, `int`, `float`)
- [x] Käyttäjän syötteet (`input`, `int(input(...))`)
- [x] Tulostaminen ja f-merkkijonot (`print`, `f"..."`)
- [x] Peruslaskutoimitukset ja sijoitusoperaattori (`=`, `*`, `/`, `+=`)
- [x] Ehtolauseet (`if`, `elif`, `else`)
- [x] Vertailuoperaattorit (`==`, `>=`)
- [x] `for`-silmukka ja `range(1, 8)`
- [x] `while`-silmukka ja silmukan lopetusehto
- [x] Laskurin käyttö (`day_count += 1`)
- [x] Summamuuttujan käyttö (`total_hours += daily_hours`)
- [x] Päivittäisen keskiarvon laskeminen
- [x] Liukulukujen muotoilu kahteen desimaaliin (`:.2f`)
- [x] Pythonin sisennysten ja suoritusjärjestyksen korjaaminen
- [x] Seitsemän päivän seurannan toteuttaminen
- [x] Joustavan seurannan toteuttaminen (`k/e`)
- [x] Toiminnallinen testaus ja regressiotestaus normaalisyötteillä
- [x] Gitin peruskomennot (`status`, `add`, `commit`, `log`)

## Hyväksytyt kehitysvaiheet

| Tunnus | Sisältö | Tulos |
|---|---|---|
| PY-SM-13–16 | `while`-silmukan harjoitukset, päivälaskuri ja keskiarvo | Hyväksytty |
| PY-SM-17 | Valikkovaihtoehto 1: seitsemän päivän seuranta | Hyväksytty |
| PY-SM-18 | Valikkovaihtoehto 2: joustava seuranta | Hyväksytty |
| PY-SM-19.1 | Joustavan seurannan testi (5 + 3 + 4) | 12 h / 3 päivää / 4,00 h; hyväksytty |
| PY-SM-19.5 | Kiinteän seurannan uusintatesti | 23 h / 7 päivää / 3,29 h; hyväksytty |
| PY-SM-19.6 | Joustavan seurannan regressiotesti (2 + 4 + 6) | 12 h / 3 päivää / 4,00 h; hyväksytty |
| PY-SM-20.1–20.3 | Git staging ja commit | `cdd8c4d`; hyväksytty |

## Seuraavaksi opiskeltavat asiat

- [ ] PY-SM-20.4A: tunnista, milloin `int()` aiheuttaa `ValueError`-poikkeuksen
- [ ] `try`–`except`-rakenteen teoria ja oma harjoitus
- [ ] Virheellisen tuntisyötteen käsittely ilman ohjelman kaatumista
- [ ] Negatiivisten ja epärealististen tuntimäärien validointi
- [ ] Valikkovalinnan `1/2` validointi
- [ ] Testit: tyhjä syöte, kirjaimet numerokentässä, virheellinen valikkovalinta
- [ ] Funktiot (`def`) ja ohjelman jäsentäminen pienempiin osiin
- [ ] Opiskelutietojen tallentaminen tiedostoon
- [ ] Automaattiset testit (myöhempi kehityskohde)
- [ ] README_EN.md:n päivittäminen uusinta ominaisuustilannetta vastaavaksi
- [ ] Muutosten julkaisu GitHubiin (`git push`), kun paikallinen tila on tarkistettu

## Avoimet huomiot

1. `study_hours * 7` on päivittäisestä syötteestä laskettu ennuste; se ei tarkoita toteutunutta viikkosummaa.
2. Kelpaamattomat numerosyötteet voivat keskeyttää ohjelman (`ValueError`), koska virheenkäsittely puuttuu.
3. Tietoja ei vielä tallenneta pysyvästi.
4. `while_harjoitus.py` ja `while_opiskelutunnit.py` ovat harjoitustiedostoja, eivät vielä Gitin seurannassa viimeisimmän tarkistuksen perusteella.
5. Testaus kattaa vahvistetut normaalikäytön tapaukset, ei vielä kaikkia poikkeustilanteita.

## Jatkamiskohta

**PY-SM-20.4A:** selitä omin sanoin, mitä tapahtuu, kun käyttäjä kirjoittaa `kolme` lausekkeen `int(input(...))` syötteeksi. Seuraavaksi opetellaan `try` ja `except` yksi rivi kerrallaan ilman valmista ohjelmaratkaisua.
