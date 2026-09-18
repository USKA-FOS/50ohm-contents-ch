Ogni impianto radioamatoriale fisso con una potenza isotropica equivalente irradiata (EIRP) pari o superiore a <span class="math inline">\qty{10}{\watt}</span> deve essere segnalato all’<span class="underline">BNetzA</span> ai sensi del § 9 della <span class="underline">BEMFV</span>, prima dell’inizio delle trasmissioni. Il radioamatore deve dimostrare il rispetto dei valori limite e aver determinato le distanze di sicurezza necessarie, che devono rientrare nell’area controllata. In gergo radioamatoriale, questa procedura è chiamata *autodichiarazione*.

L’autodichiarazione può essere omessa solo se la potenza isotropica equivalente irradiata (EIRP) è *inferiore* a <span class="math inline">\qty{10}{\watt}</span> EIRP — non <span class="math inline">\qty{10}{\watt}</span> di potenza di trasmissione, né <span class="math inline">\qty{10}{\watt}</span> ERP!

Anche senza un calcolo preciso, è evidente che la combinazione di <span class="math inline">\qty{6}{\watt}</span> di potenza di trasmissione e un guadagno d’antenna di <span class="math inline">\qty{13}{\dBd}</span> (fattore <span class="math inline">\num{20}</span>) supera chiaramente il valore limite di <span class="math inline">\qty{10}{\watt}</span> EIRP.

<indepth>
Per esercizio, possiamo comunque calcolarlo: Utilizziamo nuovamente la formula dalla raccolta di formule:

<span class="math display">P_\mathrm{EIRP} = P_\mathrm{trasmettitore} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{6}{\watt} \cdot 10^{\frac{\qty{13}{\dBd}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{197}{\watt}</span>

Anche questo calcolo può essere eseguito facilmente a mente suddividendo il guadagno totale in parti significative:

<span class="math display">\qty{13}{\dBd} + \qty{2,15}{\dB} = \qty{10}{\dBd} + \qty{3}{\dB} + \qty{2,15}{\dB}</span>

Quindi si ottiene:

<span class="math display">P_\mathrm{EIRP} = \qty{6}{\watt} \cdot 10 \cdot 2 \cdot 1,64 \approx \qty{197}{\watt}</span>
</indepth>

[question:EK104]

Nelle [istruzioni per la segnalazione di impianti radioamatoriali fissi secondo il §9 della BEMFV](https://50ohm.de/abemfv) è definito in modo preciso cosa si intende per distanza di sicurezza. La distanza di sicurezza legata al sito descrive la distanza necessaria tra l’antenna di riferimento e l’area in cui devono essere rispettati i valori limite applicabili. In questo contesto, vanno considerate anche le intensità di campo rilevanti delle installazioni radioamatoriali fisse circostanti.

È importante notare che la distanza di sicurezza non si riferisce a un singolo punto dell’antenna, ma all’intera struttura dell’antenna. In altre parole, per ogni punto dell’antenna deve essere garantito che al di fuori della distanza di sicurezza calcolata i valori limite siano rispettati.

[question:EK107]