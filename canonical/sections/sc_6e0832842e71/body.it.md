Un segnale ideale puramente sinusoidale è composto solo dalla sua *onda fondamentale*, che viene anche chiamata *1ª armonica*. Non appena un segnale non corrisponde più alla forma sinusoidale e devia anche leggermente da essa, il segnale contiene *multipli interi* della sua frequenza fondamentale, che vengono anche chiamati *armoniche superiori* o semplicemente *armoniche*. È importante qui distinguere tra i due concetti di armoniche superiori e armoniche.

La figura [ref:zusammenhang_oberwellen_harmonische] e la tabella [ref:a_harmonische] mostrano la relazione tra armoniche superiori e armoniche, che è sufficiente memorizzare una volta per tutte. La 1ª armonica superiore corrisponde alla 2ª armonica della frequenza fondamentale e si trova alla frequenza doppia rispetto a quest'ultima. La 2ª armonica superiore corrisponde alla 3ª armonica della frequenza fondamentale e si trova alla frequenza tripla rispetto a quest'ultima. Secondo questo principio, tutte le armoniche e armoniche superiori vengono riferite alla frequenza fondamentale e numerate con un numero d'ordine $N$.

<margin>
[picture:869:zusammenhang_oberwellen_harmonische:Relazione tra armoniche superiori e armoniche]

| l: Multiplo della frequenza fondamentale | l: Armonica | l: Armonica superiore |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonische:Armoniche e armoniche superiori]
</margin>

<indepth>
A seconda del tipo di distorsione di un segnale, nel suo spettro di frequenza si generano più armoniche superiori pari o dispari. I segnali a forma d'onda rettangolare, che ad esempio si formano a causa della sovraeccitazione degli stadi amplificatori (in questo caso i picchi delle ampiezze vengono limitati e appiattiti), contengono armoniche dispari o armoniche superiori pari.

<webonly>
[include:applet_rectangle]

Nelle discontinuità, l'approssimazione di Fourier mostra il cosiddetto fenomeno di Gibbs: anche con molte armoniche, in corrispondenza di tali punti rimane una piccola oscillazione in eccesso e in difetto.
</webonly>

I segnali a forma d'onda a dente di sega contengono prevalentemente armoniche pari o armoniche superiori dispari.
</indepth>

[question:AB403]
[question:AB401]
[question:AB402]

Se è nota la frequenza fondamentale di un segnale, la frequenza della $N$-esima armonica si ottiene moltiplicando la frequenza fondamentale per il numero d'ordine $N$:

$f_N = N \cdot f_0$

Per la $N$-esima armonica superiore vale invece:

$f_\mathrm{armonica\ superiore,N} = (N+1)\cdot f_0$

[question:AJ201]
[question:AJ205]
[question:AJ202]
[question:AJ206]

Anche se un segnale appare inizialmente sinusoidale sull'oscilloscopio, può comunque contenere componenti significative di armoniche superiori (o armoniche della frequenza fondamentale). Per valutare quantitativamente e qualitativamente la componente di armoniche superiori di un segnale, è necessario un *analizzatore di spettro* che possa rappresentare il segnale nel dominio delle frequenze (Frequency-Domain) e mostrare i valori di ampiezza delle singole armoniche superiori in modo logaritmico, in modo da poter misurare le loro proporzioni rispetto al segnale complessivo.

[question:AI615]
[question:AI614]
