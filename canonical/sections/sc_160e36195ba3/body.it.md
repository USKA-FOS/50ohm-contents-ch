Grazie al basso sforzo costruttivo, il raddrizzatore a ponte è uno dei circuiti raddrizzatori più utilizzati. Per realizzarlo, sono necessari un trasformatore e 4 diodi.

<latexonly>
Nella figura [ref:a_brueckenlgeichrichter] è rappresentato un tale raddrizzatore a ponte.

<margin>
[picture:965:a_brueckenlgeichrichter:Raddrizzatore a ponte]
</margin>
</latexonly>

<webonly>
Nel riquadro interattivo accanto è rappresentato un tale raddrizzatore a ponte. È possibile osservare la polarità della tensione del trasformatore $U_a$ o $U_s$ e seguire l'andamento della corrente di carico attraverso la resistenza di carico $R$, riconoscendo che questa scorre sempre nella stessa direzione attraverso la resistenza di carico.

<margin>
[include:applet_gleichrichter_2]
</margin>
</webonly>

<tip>
[picture:67:a_brueckenlgeichrichter_2:Disposizione dei diodi nel raddrizzatore a ponte]
Nel raddrizzatore a ponte, i diodi sono orientati con i catodi verso il polo positivo e gli anodi verso il polo negativo. Quindi si può ricordare: i "tratti" dei diodi si incontrano all'uscita positiva. Questa disposizione non deve essere confusa con un miscelatore ad anello di diodi, che impareremo a conoscere in seguito.
</tip>

[question:AD305]

---

Se dopo il raddrizzatore a ponte viene installato un condensatore di carica $C_L$ e un filtro LC (cfr. figura [ref:a_netzteil_Ucs]), si ottiene un'ampiezza minore nella tensione continua di uscita pulsante. In questo modo si ottiene un alimentatore convenzionale.

<margin>
[picture:66:a_netzteil_Ucs:Circuito raddrizzatore con filtro]
</margin>

Anche nel raddrizzatore a ponte, il condensatore si carica alla tensione di picco $\hat{U}$ della tensione secondaria $U_{\mathrm{sek}}$ del trasformatore.

$\hat{U}=U_{\mathrm{eff}}\cdot\sqrt{2}$

Inoltre, occorre considerare se il trasformatore presenta un rapporto di trasformazione $ü$. Con questa informazione, possiamo risolvere il seguente esercizio.

[question:AD306]

<indepth>
[photo:296: Forme costruttive del raddrizzatore a ponte: Forme costruttive di raddrizzatori a ponte]
Attenzione alla marcatura dei collegamenti.

1. Raddrizzatore a ponte ad alta corrente 26 MB 20 A ($\qty{200}{\volt}$, $\qty{25}{\ampere}$) in contenitore metallico per montaggio diretto su un dissipatore
2. B80 C 5000/3300 significa: tensione di servizio massima $\qty{80}{\volt}$, carico capacitivo massimo $\qty{2500}{\micro\farad}$ con resistenza di protezione $R = \qty{1}{\ohm}$, corrente di carico continua massima: $\qty{5000}{\milli\ampere}$ con dissipatore, $\qty{3300}{\milli\ampere}$ senza dissipatore
3. BY 225 Raddrizzatore a ponte - contenitore speciale
4. Forma costruttiva rotonda di un raddrizzatore a ponte B 80 C 1000
5. B40 C 1500 - attenzione alla sequenza modificata dei collegamenti
6. FPU 4M ($\qty{1000}{\volt}$, $\qty{4}{\ampere}$)
7. Sequenza dei collegamenti impressa nella plastica