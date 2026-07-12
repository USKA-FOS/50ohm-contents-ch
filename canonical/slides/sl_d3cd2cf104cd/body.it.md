<left>
[picture:489:a_frequenzvervielfacher_schaltung:Esempio di un circuito di un moltiplicatore di frequenza con amplificatore di classe C senza polarizzazione di base]
</left>
<right>
* Il segnale di ingresso viene alimentato a uno stadio di distorsione non lineare
* Ad esempio, amplificatore di classe C, tramite funzionamento senza polarizzazione di base
* Il segnale viene fortemente distorto
* Con un filtro viene selezionata la sovratono desiderata
</right>
<note>
Gli amplificatori verranno trattati più avanti nel capitolo.
</note>
---
<left>
[picture:489:a_frequenzvervielfacher_schaltung:Esempio di un circuito di un moltiplicatore di frequenza con amplificatore di classe C senza polarizzazione di base]
</left>
<right>
* Sono possibili solo multipli interi
* Di norma si utilizza la 2ª o 3ª armonica
* Moltiplicazione di frequenza più elevata con stadi collegati in serie
</right>
<note>
</note>
---
[question:AF312]
---
[question:AF311]
---
### Schermatura

* Vengono generate frequenze intermedie
* Queste spesso causano disturbi
* Tutti gli stadi devono essere ben schermati

---
[question:AF313]
---
### Più stadi moltiplicatori

* Le singole frequenze tra gli stadi moltiplicatori possono causare disturbi
* Seguire il percorso attraverso i singoli stadi e calcolare le singole frequenze
* L'ordine degli stadi è importante per determinare le frequenze di disturbo

---
[question:AF314]
---
#### Percorso di soluzione
* dato: $f_\text{trasmettitore} = \qty{432}{\mega\hertz}$
* dato: $f_\text{fondamentale} = \qty{12}{\mega\hertz}$
* dato: $f_\text{QRM} = \qty{144}{\mega\hertz}$
* cercato: combinazione di moltiplicazione

<fragment>
$n = \frac{f_\text{trasmettitore}}{f_\text{QRM}} = \frac{\qty{432}{\mega\hertz}}{\qty{144}{\mega\hertz}} = 3$
</fragment>
<fragment>
È possibile solo la combinazione da $\textrm{frequenza fondamentale}\,\cdot 2\cdot 2\cdot 3\cdot 3$, poiché quest'ultima effettua una triplicazione della frequenza.
</fragment>
---
Controprova:
$\begin{split}f_\text{trasmettitore} &= f_\text{fondamentale}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{12}{\mega\hertz}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{24}{\mega\hertz}\cdot 2\cdot 3\cdot 3\\ &= \qty{48}{\mega\hertz}\cdot 3\cdot 3\\ &= \bold{\qty{144}{\mega\hertz}}\cdot 3\\ &= \qty{432}{\mega\hertz}\end{split}$
