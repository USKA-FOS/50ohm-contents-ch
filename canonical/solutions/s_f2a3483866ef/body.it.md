# Dati
Potenza d’uscita del trasmettitore: $p_\text{trasmettitore, uscita} = \qty{1}{\watt}$  
Guadagno: $g_\text{stadio finale} = \qty{10}{\dezibel}$  

# Procedimento
Utilizziamo la formula in $\unit{\dBm}$ dalla raccolta di formule (livelli, livelli di potenza e tensione):  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$ 
e calcoliamo così il livello d’ingresso nello stadio finale:
$ p_\text{stadio finale, ingresso} = 10 \cdot \log_{10}\left(\frac{p_\text{trasmettitore, uscita}}{\qty{1}{\milli\watt}}\right)\unit{\dBm}= 10 \cdot \log_{10}\left(\frac{\qty{1}{\watt}}{\qty{10^{-3}}{\watt}}\right)\unit{\dBm} \\ = 10 \cdot \log_{10}\left(10^{3}\right)\unit{\dBm}= 10 \cdot \qty{3}{\dBm}\\ = \qty{30}{\dBm}$ 
Il livello d’uscita si ottiene quindi semplicemente sommando:
$ p_\text{uscita} = p_\text{ingresso} + g_\text{guadagno} = \qty{30}{\dBm} + \qty{10}{\dB} = \qty{40}{\dBm}$

# Abbreviazione
Chi ha familiarità con i logaritmi e la tabella degli strumenti può risolvere il problema a mente.  
$\qty{1}{\watt}$ corrisponde a $\qty{1000}{\milli\watt}$, che corrisponde a $\qty{30}{\dBm}$; aggiungendo il guadagno di $\qty{10}{\dezibel}$ si ottiene $\qty{40}{\dBm}$. 