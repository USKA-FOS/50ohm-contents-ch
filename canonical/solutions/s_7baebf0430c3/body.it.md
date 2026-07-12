# Dati
Livelli: $\qty{0}{\dBm}$, $\qty{3}{\dBm}$, $\qty{20}{\dBm}$  

# Percorso di soluzione
Utilizziamo la formula $\unit{\dBm}$ dalla raccolta di formule (Livello, livelli di potenza e tensione):  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$ 
e risolviamo per $P$:
$P = \qty{1}{\milli\watt}\cdot 10^{\frac{p}{\qty{10}{\dBm}}}$
Inseriamo i valori dalla domanda e otteniamo:  

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{0}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{0}= \qty{1}{\milli\watt}$

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{3}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{0,3}= \qty{1,995}{\milli\watt}$

$P = \qty{1}{\milli\watt}\cdot 10^{\frac{\qty{20}{\dBm}}{\qty{10}{\dBm}}}= \qty{1}{\milli\watt}\cdot 10^{2}= \qty{100}{\milli\watt}$

# Abbreviazione
Chi ha lavorato un po' con i logaritmi e la tabella degli ausiliari, può arrivare rapidamente alla soluzione corretta per esclusione.  
$\qty{0}{\dBm} \rightarrow \qty{1}{\milli\watt}$ (rimangono solo due possibili risposte).  
$\qty{3}{\dB}$ corrispondono a un raddoppio. Quindi $\qty{3}{\dBm} \rightarrow  \qty{2}{\milli\watt}$ (rimane solo una risposta). 
