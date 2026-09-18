[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]

1. Stadio RF con preselezione
2. Primo mixer con VFO
3. Primo amplificatore IF con filtro *Roofing*
4. Secondo mixer con oscillatore di conversione (CO)

--- data-transition="none"
[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]

5. Secondo amplificatore IF con filtro
6. Terzo mixer come rivelatore a prodotto o demodulatore, eventualmente con BFO
7. Amplificatore BF

--- data-transition="none"
[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]

* Utilizzo di due frequenze intermedie (IF)
* Prima IF elevata → buona soppressione della frequenza immagine
* Seconda IF bassa → alta selettività

---
* Dopo la prima IF è presente un filtro d’ingresso prima del secondo mixer
* La frequenza immagine può essere soppressa efficacemente grazie alla grande separazione in frequenza
* Dopo la seconda IF è presente un filtro ad alta qualità
* Tale filtro è realizzabile con facilità a basse frequenze
* La IF e la frequenza di ricezione desiderata devono essere ben distanziate → evita la ricezione diretta della IF
* La prima IF dovrebbe essere il doppio della frequenza di ricezione massima

---
[question:AF112]
---
[question:AF113]
---
[question:AF114]
---
### Filtro *Roofing*


* Dopo il primo mixer è presente un filtro stretto (*Roofing Filter*)
* Sintonizzato sulla prima IF
* La larghezza di banda deve essere almeno pari alla massima larghezza di banda di ricezione richiesta

---
[question:AF116]
---
[question:AF209]
---
[question:AF117]
---
### Frequenze dell’oscillatore
* Le frequenze dell’oscillatore sono poste sopra o sotto la frequenza d’ingresso desiderata
* Per ogni mixer esistono due possibili soluzioni

<fragment>
1. $f_\text{OSZ} = f_\text{IF}\,+\,f_\text{E}$
2. $f_\text{OSZ} = f_\text{IF}\,-\,f_\text{E}$
</fragment>

---
[question:AF210]
--- style="font-size: smaller;"
#### Procedimento
* Dati: $f_\text{E} = 3\dots\qty{30}{\mega\hertz}$
* Dati: $f_\text{IF1} = \qty{50}{\mega\hertz}$
* Ricercato: $f_\text{OSZ}$


<fragment>
$f_\text{IF} = |f_\text{E} − f_\text{OSZ}| \Rightarrow f_\text{OSZ} = f_\text{IF} \pm f_\text{E}$
</fragment>
<fragment>
<left>
1. Soluzione:
$\begin{split}f_\text{OSZ} &= f_\text{IF} \, + \, f_\text{E}\\ &= \qty{50}{\mega\hertz} \, + \, 3\dots\qty{30}{\mega\hertz}\\ &= 53\dots\qty{80}{\mega\hertz}\end{split}$
</left>
</fragment>
<fragment>
<right>
2. Soluzione:
$\begin{split}f_\text{OSZ} &= f_\text{IF} \, - \, f_\text{E}\\ &= \qty{50}{\mega\hertz} \, - \, 3\dots\qty{30}{\mega\hertz}\\ &= 47\dots\qty{20}{\mega\hertz}\end{split}$
</right>
</fragment>
---
[question:AF120]
--- style="font-size: smaller;"
### Procedimento
<left>
* Dati: $f_\text{E} = \qty{3,65}{\mega\hertz}$
* Dati: $f_\text{IF1} = \qty{50}{\mega\hertz}$
</left>
<right>
* Dati: $f_\text{IF2} = \qty{9}{\mega\hertz}$
* Dati: $f_\text{BF} = \qty{455}{\kilo\hertz}$
</right>
* Ricercato: $f_\text{OSZ}$ per $f_\text{VFO}$, $f_\text{CO1}$, $f_\text{CO2}$


<fragment>
$f_\text{IF1} = \begin{cases}f_\text{E}\,+\,f_\text{OSZ}\\ f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{IF}\,-\,f_\text{E}\\ f_\text{E}\,+\,f_\text{IF}\\ f_\text{E}\,-\,f_\text{IF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = \begin{cases}f_\text{IF1}\,-\,f_\text{E} = \qty{50}{\mega\hertz}\,-\,\qty{3,65}{\mega\hertz} = \qty{46,35}{\mega\hertz}\\ f_\text{E}\,+\,f_\text{IF1} = \qty{3,65}{\mega\hertz}\,+\,\qty{50}{\mega\hertz} = \qty{53,64}{\mega\hertz}\\ f_\text{E}\,-\,f_\text{IF1} = \qty{3,65}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-46,35}{\mega\hertz}}\end{cases}$
</fragment>
--- style="font-size: smaller;"‚
<fragment>
$f_\text{CO1} = \begin{cases}f_\text{IF2}\,-\,f_\text{IF1} = \qty{9}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-41}{\mega\hertz}}\\ f_\text{IF1}\,+\,f_\text{IF2} = \qty{50}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{59}{\mega\hertz}\\ f_\text{IF1}\,-\,f_\text{IF2} = \qty{50}{\mega\hertz}\,-\,\qty{9}{\mega\hertz} = \qty{41}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
$f_\text{CO2} = \begin{cases}f_\text{BF}\,-\,f_\text{IF2} = \qty{455}{\kilo\hertz}\,-\,\qty{9}{\mega\hertz} = \cancel{\qty{-8,545}{\mega\hertz}}\\ f_\text{IF2}\,+\,f_\text{BF} = \qty{9}{\mega\hertz}\,+\,\qty{455}{\kilo\hertz} = \qty{9,455}{\mega\hertz}\\ f_\text{IF2}\,-\,f_\text{BF} = \qty{9}{\mega\hertz}\,-\,\qty{455}{\kilo\hertz} = \qty{8,545}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
VFO: $\bold{\qty{46,35}{\mega\hertz}} \And \qty{53,65}{\mega\hertz}$, CO1: $\bold{\qty{41}{\mega\hertz}} \And \qty{59}{\mega\hertz}$, CO2: $\qty{8,545}{\mega\hertz}} \And \bold{\qty{9,455}{\mega\hertz}}$
</fragment>
---
[question:AF118]
--- style="font-size: smaller;"‚
#### Procedimento
<left>
* Dati: $f_\text{E} = \qty{21,1}{\mega\hertz}$
* Dati: $f_\text{IF1} = \qty{9}{\mega\hertz}$
</left>
<right>
* Dati: $f_\text{IF2} = \qty{460}{\kilo\hertz}$
</right>
* Ricercato: $f_\text{VFO} > f_\text{E}$, $f_\text{CO} < f_\text{IF1}$

<fragment>
$f_\text{IF} = \begin{cases}f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{E}\,+\,f_\text{IF}\\ f_\text{E}\,-\,f_\text{IF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{IF1} = \qty{21,1}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{30,1}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{IF1}\,-\,f_\text{IF2} = \qty{9}{\mega\hertz}\,-\,\qty{460}{\kilo\hertz} = \qty{8,54}{\mega\hertz}$
</fragment>

---
[question:AF119]
--- style="font-size: smaller;"‚
#### Procedimento
<left>
* Dati: $f_\text{E} = \qty{28}{\mega\hertz}$
* Dati: $f_\text{IF1} = \qty{10,7}{\mega\hertz}$
</left>
<right>
* Dati: $f_\text{IF2} = \qty{460}{\kilo\hertz}$
</right>
* Ricercato: $f_\text{VFO} > f_\text{E}$, $f_\text{CO} > f_\text{IF1}$

<fragment>
$f_\text{IF} = \begin{cases}f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{E}\,+\,f_\text{IF}\\ f_\text{E}\,-\,f_\text{IF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{IF1} = \qty{28}{\mega\hertz}\,+\,\qty{10,7}{\mega\hertz} = \qty{38,70}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{IF1}\,+\,f_\text{IF2} = \qty{10,7}{\mega\hertz}\,+\,\qty{460}{\kilo\hertz} = \qty{11,16}{\mega\hertz}$
</fragment>