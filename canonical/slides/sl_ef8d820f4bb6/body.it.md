[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]

1. Sezione HF con preselezione
2. Primo mixer con VFO
3. Primo amplificatore IF con filtro di copertura
4. Secondo mixer con CO

--- data-transition="none"
[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]

5. Secondo amplificatore IF con filtro
6. Terzo mixer come detettore di prodotto o demodulatore, eventualmente con BFO
7. Amplificatore AF

--- data-transition="none"
[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]

* Utilizzo di due frequenze intermedie
* IF 1ª alta $\rightarrow$ buona soppressione della frequenza immagine
* IF 2ª bassa $\rightarrow$ alta selettività

---
* Dopo la 1ª IF è presente un filtro di ingresso prima del 2º mixer
* La frequenza immagine può essere soppressa bene grazie a una grande distanza
* Dopo la 2ª IF filtro con alto fattore di qualità
* Può essere realizzato bene per basse frequenze
* Posizionare la frequenza intermedia e la frequenza di ricezione desiderata a distanza $\rightarrow$ evitare la ricezione diretta della frequenza intermedia
* La 1ª IF dovrebbe essere il doppio della massima frequenza di ricezione

---
[question:AF112]
---
[question:AF113]
---
[question:AF114]
---
### Filtro di copertura (Roofing Filter)

* Dopo il 1º mixer filtro stretto (*Filtro di copertura*)
* Sintonizzato sulla 1ª IF
* Larghezza di banda almeno pari alla massima larghezza di banda di ricezione necessaria

---
[question:AF116]
---
[question:AF209]
---
[question:AF117]
---
### Frequenze dell'oscillatore
* Le frequenze dell'oscillatore sono sempre sopra o sotto la frequenza di ingresso desiderata
* Esistono due possibili soluzioni per ogni mixer

<fragment>
1. $f_\text{OSZ} = f_\text{IF}\,+\,f_\text{E}$
2. $f_\text{OSZ} = f_\text{IF}\,-\,f_\text{E}$
</fragment>

---
[question:AF210]
--- style="font-size: smaller;"
#### Percorso di soluzione
* dato: $f_\text{E} = 3\dots\qty{30}{\mega\hertz}$
* dato: $f_\text{IF1} = \qty{50}{\mega\hertz}$
* cercato: $f_\text{OSZ}$

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
### Percorso di soluzione
<left>
* dato: $f_\text{E} = \qty{3,65}{\mega\hertz}$
* dato: $f_\text{IF1} = \qty{50}{\mega\hertz}$
</left>
<right>
* dato: $f_\text{IF2} = \qty{9}{\mega\hertz}$
* dato: $f_\text{AF} = \qty{455}{\kilo\hertz}$
</right>
* cercato: $f_\text{OSZ}$ per $f_\text{VFO}$, $f_\text{CO1}$, $f_\text{CO2}$

<fragment>
$f_\text{IF1} = \begin{cases}f_\text{E}\,+\,f_\text{OSZ}\\ f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{IF} \,-\,f_\text{E}\\ f_\text{E}\,+\,f_\text{IF}\\ f_\text{E}\,-\,f_\text{IF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = \begin{cases}f_\text{IF1}\,-\,f_\text{E} = \qty{50}{\mega\hertz}\,-\,\qty{3,65}{\mega\hertz} = \qty{46,35}{\mega\hertz}\\ f_\text{E}\,+\,f_\text{IF1} = \qty{3,65}{\mega\hertz}\,+\,\qty{50}{\mega\hertz} = \qty{53,64}{\mega\hertz}\\ f_\text{E}\,-\,f_\text{IF1} = \qty{3,65}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-46,35}{\mega\hertz}}\end{cases}$
</fragment>
--- style="font-size: smaller;"‚
<fragment>
$f_\text{CO1} = \begin{cases}f_\text{IF2}\,-\,f_\text{IF1} = \qty{9}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-41}{\mega\hertz}}\\ f_\text{IF1}\,+\,f_\text{IF2} = \qty{50}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{59}{\mega\hertz}\\ f_\text{IF1}\,-\,f_\text{IF2} = \qty{50}{\mega\hertz}\,-\,\qty{9}{\mega\hertz} = \qty{41}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
$f_\text{CO2} = \begin{cases}f_\text{AF}\,-\,f_\text{IF2} = \qty{455}{\kilo\hertz}\,-\,\qty{9}{\mega\hertz} = \cancel{\qty{-8,545}{\mega\hertz}}\\ f_\text{IF2}\,+\,f_\text{AF} = \qty{9}{\mega\hertz}\,+\,\qty{455}{\kilo\hertz} = \qty{9,455}{\mega\hertz}\\ f_\text{IF2}\,-\,f_\text{AF} = \qty{9}{\mega\hertz}\,-\,\qty{455}{\kilo\hertz} = \qty{8,545}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
VFO: $\bold{\qty{46,35}{\mega\hertz}} \And \qty{53,65}{\mega\hertz}$, CO1: $\bold{\qty{41}{\mega\hertz}} \And \qty{59}{\mega\hertz}$, CO2: $\qty{8,545}{\mega\hertz} \And \bold{\qty{9,455}{\mega\hertz}}$
</fragment>
---
[question:AF118]
--- style="font-size: smaller;"‚
#### Percorso di soluzione
<left>
* dato: $f_\text{E} = \qty{21,1}{\mega\hertz}$
* dato: $f_\text{IF1} = \qty{9}{\mega\hertz}$
</left>
<right>
* dato: $f_\text{IF2} = \qty{460}{\kilo\hertz}$
</right>
* cercato: $f_\text{VFO} \gt f_\text{E}$, $f_\text{CO} \lt f_\text{IF1}$

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
#### Percorso di soluzione
<left>
* dato: $f_\text{E} = \qty{28}{\mega\hertz}$
* dato: $f_\text{IF1} = \qty{10,7}{\mega\hertz}$
</left>
<right>
* dato: $f_\text{IF2} = \qty{460}{\kilo\hertz}$
</right>
* cercato: $f_\text{VFO} \gt f_\text{E}$, $f_\text{CO} \gt f_\text{IF1}$

<fragment>
$f_\text{IF} = \begin{cases}f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{E}\,+\,f_\text{IF}\\ f_\text{E}\,-\,f_\text{IF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{IF1} = \qty{28}{\mega\hertz}\,+\,\qty{10,7}{\mega\hertz} = \qty{38,70}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{IF1}\,+\,f_\text{IF2} = \qty{10,7}{\mega\hertz}\,+\,\qty{460}{\kilo\hertz} = \qty{11,16}{\mega\hertz}$
</fragment>
