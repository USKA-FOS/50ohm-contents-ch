## Problema

* Comunicare la posizione, ad esempio per misurazioni di distanza
* Non sempre c'è una città nelle vicinanze
* Le coordinate GPS sono troppo lunghe
* Spesso è sufficiente una posizione approssimativa

---

## Locator Maidenhead

<left>
* La superficie terrestre viene suddivisa in $\num{18662400}$ quadrati
* In Germania, un quadrato corrisponde approssimativamente a una precisione di $\qty{5}{\kilo\meter}\times\qty{5}{\kilo\meter}$
* Questi quadrati vengono chiamati *Subsquares*
* A un livello superiore ci sono *Squares* e *Fields*
</left>
<right>
[photo:4:n_locator_welt:Locator Maidenhead a livello mondiale. Dati cartografici © OpenStreetMap contributors, SRTM. Rappresentazione cartografica © OpenTopoMap (CC-BY-SA)]
</right>

<note>
* Prende il nome dalla città di *Maidenhead*, situata a ovest di Londra nel Regno Unito.
* Nel 1980, in questa città si tenne una conferenza specialistica dell'IARU che riformò il precedente sistema di localizzazione QRA-Locator.
</note>

---
[photo:2:n_locator_jo:Il campo JO del sistema Maidenhead-Locator. Dati cartografici © OpenStreetMap contributors, SRTM. Rappresentazione cartografica © OpenTopoMap (CC-BY-SA)]

<note>
Vengono mostrati i *Squares* del campo JO
</note>

--- style="font-size: 0.7em;"
## Livelli del Maidenhead Locator

| X: Denominazione | l: Traduzione | l: Denominazione alternativa | c: | c: Esempio |
| Field | Campo | Campo principale | AA-RR | JO |
| Square | Quadrato | Campo grande | 00-99 | 41 |
| Subsquare | Sotto-quadrato | Campo piccolo | AA-XX | RG |
[table:n_locator_stufen:I singoli livelli del Maidenhead-Locator]

<fragment>
Da questo si ottiene, ad esempio, *JO41RG* per la sede del DARC a Baunatal, vicino a Kassel
</fragment>
<note>
* Sono possibili quadrati ancora più piccoli
* [Carta interattiva](https://f5len.org/tools/locator/)
</note>

---
[question:BE111]

