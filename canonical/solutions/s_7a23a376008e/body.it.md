# Dati
Guadagno: $g = \qty{16}{\dezibel}$  
Potenza in ingresso: $P_1 = \qty{1}{\watt}$

# Procedimento di soluzione 1
Utilizziamo la formula dalla *raccolta di formule* (livello, guadagno, potenza):  
$ g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$  
e risolviamo per $P_2$:
$P_2 = P_1 \cdot 10^{\frac{g}{\qty{10}{\dB}}}$  
Con i valori numerici del quesito:
$P_2 = \qty{1}{\watt} \cdot 10^{\frac{\qty{16}{\dB}}{\qty{10}{\dB}}} = \qty{39.81}{\watt}$

# Procedimento di soluzione 2
Utilizziamo la tabella nella *raccolta di formule* e la conoscenza delle proprietà dei logaritmi:  
Il logaritmo di un prodotto corrisponde alla somma dei logaritmi dei fattori:

$\log\left(a\right)+\log\left(b\right) = \log\left(a \cdot b\right)$

Con i valori del quesito e la tabella otteniamo per il fattore di guadagno:

$\qty{16}{\dB} = \qty{6}{\dB} + \qty{10}{\dB} \rightarrow  4 \cdot 10 = 40$

E quindi:

$P_2 = \qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$