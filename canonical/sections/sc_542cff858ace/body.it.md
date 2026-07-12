Ogni impianto radioamatoriale fisso deve essere notificato alla BNetzA, ai sensi del § 9 BEMFV, se la potenza irradiata isotropa equivalente (EIRP) è pari o superiore a $\qty{10}{\watt}$. Ciò deve avvenire prima dell'inizio delle operazioni radio. L'operatore radioamatoriale deve fornire la prova di rispettare i limiti e di aver determinato le distanze di sicurezza necessarie, e che queste si trovino all'interno dell'area controllata. In termini colloquiali, questo viene definito dagli operatori radioamatoriali come *autodichiarazione*.

Si può rinunciare a un'autodichiarazione solo se la potenza irradiata isotropa equivalente (EIRP) è *inferiore* a $\qty{10}{\watt}$ EIRP - non $\qty{10}{\watt}$ di potenza di trasmissione, nemmeno $\qty{10}{\watt}$ di ERP!

Anche senza un calcolo preciso, diventa rapidamente evidente che la combinazione di $\qty{6}{\watt}$ di potenza di trasmissione e un guadagno d'antenna di $\qty{13}{\dBd}$ (fattore 20) supera di gran lunga il limite di $\qty{10}{\watt}$ EIRP nella domanda seguente.

<indepth>
Per esercizio, si può comunque calcolare: utilizziamo nuovamente la formula dalla raccolta di formule: 

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{6}{\watt} \cdot 10^{\frac{\qty{13}{dBd}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{197}{\watt}$

Anche questo calcolo può essere facilmente eseguito mentalmente, scomponendo il guadagno totale in singole parti significative:
  
$\qty{13}{\dBd} + \qty{2,15}{\dB} = \qty{10}{\dBd} + \qty{3}{\dB} + \qty{2,15}{\dB}$

Così si ottiene:

$P_\text{EIRP} = \qty{6}{\watt} \cdot 10 \cdot 2 \cdot 1,64 \approx \qty{197}{\watt}$
</indepth>

[question:EK104]
  
Nell'[istruzione per l'esecuzione della notifica degli impianti radioamatoriali fissi ai sensi del §9 della BEMFV](https://50ohm.de/abemfv) è definito esattamente cosa si intende per distanza di sicurezza. La distanza di sicurezza basata sulla località descrive la distanza richiesta tra l'antenna di riferimento e l'area in cui devono essere rispettati i limiti vigenti. Devono essere considerate anche le intensità di campo rilevanti degli impianti radio fissi circostanti.

È importante notare: la distanza di sicurezza non si riferisce a un singolo punto dell'antenna, ma all'intera struttura dell'antenna. In altre parole, per ogni punto dell'antenna deve essere garantito che i limiti siano rispettati al di fuori della distanza di sicurezza calcolata.

[question:EK107]
