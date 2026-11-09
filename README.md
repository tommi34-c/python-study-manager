# Python Study Manager

[Suomi](README.md) | [English](README_EN.md)

**Kehitysvaihe:** v1.2 – seitsemän päivän ja joustavan seurannan toteutus testattu (10.11.2026).  
**Tila:** aktiivinen oppimisprojekti; syötteiden validointi on seuraava kehityskohde.

## Projektin tarkoitus

Python Study Manager on Pythonilla toteutettava komentorivisovellus (CLI), jonka avulla harjoittelen ohjelmoinnin perusteita ja ohjelmistokehityksen työprosesseja. Sovellus seuraa ohjelmointikielten opiskelua, opiskelutunteja ja päivittäistä edistymistä. Myöhemmissä versioissa tavoitteena on lisätä tiedostotallennus, oppimistavoitteet ja raportointi.

Projektia kehitetään vaiheittain: opiskelen käsitteet, kirjoitan koodin itse, korjaan virheet, testaan toiminnallisuuden ja tallennan hyväksytyt muutokset Gitiin.

## Nykyiset ominaisuudet

| Nro | Ominaisuus | Toteutus | Tila |
|---|---|---|---|
| 1 | Käynnistys komentoriviltä | `python study_manager.py` | Testattu |
| 2 | Opiskelijan nimen kysyminen | `input()` | Testattu |
| 3 | Ohjelmointikielen kysyminen | `input()` | Testattu |
| 4 | Päivittäisen opiskelutuntimäärän kysyminen | `int(input())` | Testattu kelvollisella syötteellä |
| 5 | Viikkotuntien arvio yhdestä päivästä | `study_hours * 7` | Testattu |
| 6 | Opiskelijan tietojen näyttäminen | `print()`, f-merkkijonot | Testattu |
| 7 | Opiskelupäivän palaute | `if`, `elif`, `else` | Testattu |
| 8 | Seurantatilan valinta | `choice`, `if` ja `elif` | Testattu vaihtoehdoilla 1 ja 2 |
| 9 | Kiinteä seitsemän päivän seuranta | `for`, `range(1, 8)` | Testattu |
| 10 | Joustava opiskelupäivien kirjaaminen | `while` ja jatkamiskysymys `k/e` | Testattu |
| 11 | Opiskelutuntien yhteenlasku | `total_hours += daily_hours` | Testattu |
| 12 | Kirjattujen opiskelupäivien laskeminen | `day_count += 1` | Testattu |
| 13 | Päivittäisen keskiarvon laskeminen | `total_hours / 7` tai `/ day_count` | Testattu |
| 14 | Yhteenvetoraportti | `print()` | Testattu molemmissa tiloissa |
| 15 | Keskiarvon muotoilu | `:.2f` | Testattu |
| 16 | Versiohallinta | Git `status`, `add`, `commit`, `log` | Käytössä |

### Opiskelupäivän palaute

| Päivän opiskelutunnit | Palaute |
|---|---|
| 0–1 | Jatka harjoittelua! |
| 2–3 | Hyvää edistymistä! |
| 4 tai enemmän | Erinomainen opiskelupäivä! |

Palaute perustuu ensimmäiseen päivän tuntikysymykseen. Samassa kohdassa esitettävä `study_hours * 7` on **ennuste**, ei myöhemmin kirjattujen päivien toteutunut tuntisumma.

## Käyttö

Avaa projektikansio ja käynnistä ohjelma:

```bash
cd /mnt/projektit/github/python-study-manager
python study_manager.py
```

Ohjelma kysyy ensin nimen, ohjelmointikielen ja tämän päivän opiskelutunnit. Sen jälkeen valitaan seurantatila:

- **1 – Seitsemän päivän seuranta:** kysyy seitsemän päivän tunnit, laskee summan ja päivän keskiarvon.
- **2 – Joustava seuranta:** kysyy tunnit niin monelta päivältä kuin halutaan. Vastauksella `k` jatketaan ja `e` lopetetaan. Lopuksi tulostetaan summa, päiväkohtainen määrä ja keskiarvo.

Tietoja ei vielä tallenneta pysyvästi: ne ovat käytettävissä vain ohjelman suorituksen ajan.

## Testaus

### Kiinteä seuranta – PY-SM-19.5

Syötteet: `3, 4, 2, 5, 3, 4, 2`.

```text
Viikon opiskelutunnit yhteensä: 23 tuntia
Päivittäinen keskiarvo: 3.29 tuntia
```

**Tulos:** hyväksytty käyttäjän terminaalitulosteen perusteella.

### Joustava seuranta – PY-SM-19.6

Syötteet: `2, 4, 6`; jatkovastaukset: `k, k, e`.

```text
Viikon opiskelutunnit yhteensä: 12 tuntia
Opiskelupäiviä: 3
Päivittäinen keskiarvo: 4.00 tuntia
```

**Tulos:** hyväksytty käyttäjän terminaalitulosteen perusteella.

Syntaksin voi tarkistaa komennolla:

```bash
python -m py_compile study_manager.py
```

Testatut tapaukset kattavat normaalin käytön, mutta eivät vielä virheellisiä syötteitä tai kaikkia reunatapauksia.

## Oppimislista

Toteutetut harjoitukset ja seuraavat oppimistavoitteet on koottu tiedostoon [OPPIMISLISTA.md](OPPIMISLISTA.md).

## Kehityssuunnitelma

| Kehitysvaihe | Sisältö | Tila |
|---|---|---|
| v1.0 | Opiskelijan perustiedot ja opiskelutuntien ennuste | Toteutettu |
| v1.1 | Ehtolauseet ja palaute | Toteutettu |
| v1.2.1 | `for`-silmukka ja seitsemän päivän seuranta | Toteutettu ja testattu |
| v1.2.2 | `while`-silmukan harjoittelu | Toteutettu |
| v1.2.3 | Valikko sekä kiinteä ja joustava seuranta | Toteutettu ja testattu |
| Seuraava | Syötteiden validointi: `try`, `except`, `ValueError` | Aloittamatta toteutuksessa |
| Suunniteltu | Virheellisten valikkovalintojen käsittely | Suunniteltu |
| Suunniteltu | Funktiot (`def`) ja koodin jäsentely | Suunniteltu |
| Suunniteltu | Opiskeluhistorian tallentaminen JSON- tai CSV-tiedostoon | Suunniteltu |
| Suunniteltu | Opiskelutavoitteet ja edistymisen seuranta | Suunniteltu |
| Myöhemmin | SQLite ja graafiset raportit | Idea |

Aiempien suunnitelmien versionumerointi voi tarkentua työn edetessä. Yllä oleva taulukko erottaa vahvistetut toteutukset suunnitelmista.

## Teknologiat

- **Ohjelmointikieli:** Python 3
- **Käyttöliittymä:** komentorivi (CLI)
- **Kehitysympäristö:** Fedora Linux KDE
- **Lähdekoodi:** `study_manager.py`
- **Versionhallinta:** Git ja GitHub
- **Tietojen säilytys:** ohjelman suoritusmuisti (ei vielä tiedostotallennusta)

## Versionhallinnan tilanne 10.11.2026

Paikallisesti vahvistettu commit:

```text
cdd8c4d feat: add fixed and flexible study hours tracking
```

GitHubiin julkaisemista ei ole vielä vahvistettu. Kaksi harjoitustiedostoa, `while_harjoitus.py` ja `while_opiskelutunnit.py`, olivat viimeisessä tarkistuksessa versionhallinnan ulkopuolella.

## Dokumentaation kielet

Tämä README on suomeksi. Englanninkielinen kuvaus on tiedostossa [README_EN.md](README_EN.md); sen sisältö on päivitettävä vastaamaan uusimpia ominaisuuksia.
