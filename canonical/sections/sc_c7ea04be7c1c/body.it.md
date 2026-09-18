Un antico detto tra radioamatori recita che il miglior *amplificatore ad alta frequenza* è l'*antenna*. Nei primi anni della tecnologia radio, essa era l’unico "amplificatore" disponibile, poiché non esistevano ancora componenti elettronici amplificatori. Nel 1907 arrivò la valvola termoionica: un componente molto efficace, ma piuttosto ingombrante e poco efficiente. Già dagli anni Venti, la scienza sognava componenti con funzioni simili, ma con tutto il processo che avveniva all’interno di un solido (semiconduttore) e non nel vuoto. Il primo componente in cui ciò riuscì fu, nel 1947/1948, il *transistor bipolare*, che è anche oggetto di domande d’esame.

[question:EC602]

<indepth>
Il *transistor bipolare* in inglese è chiamato anche BJT (*Bipolar Junction Transistor*), in tedesco *bipolarer Sperrschicht-Transistor*.
</indepth>

La funzione ideale di tutti i tipi di transistor, inclusa la valvola termoionica, è quella di una *sorgente di corrente controllata in tensione*: con una piccola variazione di tensione all’ingresso si deve ottenere una grande variazione di corrente all’uscita.

Il transistor bipolare ha tre terminali, chiamati emettitore, base e collettore. L’emettitore emette portatori di carica nella base: nel transistor NPN si tratta di *elettroni*, nel transistor PNP di lacune (**Löcher** in tedesco). La fisica alla base di questi concetti verrà discussa solo durante il corso per la classe A. Questi portatori attraversano la base e vengono raccolti dal collettore.

---

La figura [ref:e_npn_pnp_symbol] mostra i simboli di circuito dei transistor NPN e PNP. L’elettrodo di emettitore è riconoscibile grazie a una freccia: nel transistor PNP è diretta verso la base, mentre nel transistor NPN è diretta lontano dalla base.

<margin>
[picture:864:e_npn_pnp_symbol:Simboli di circuito NPN e PNP]
</margin>

[question:EC605]
[question:EC606]
[question:EC607]
[question:EC608]
[question:EC609]

---

I transistor bipolari sono composti da due diodi: il diodo emettitore-base e il diodo base-collettore. 
Durante il funzionamento attivo, il diodo emettitore-base è sempre polarizzato in direzione di conduzione. Nel transistor NPN il potenziale della base deve essere positivo rispetto a quello dell’emettitore, mentre nel transistor PNP deve essere negativo. Il diodo base-collettore è invece polarizzato in *polarizzazione inversa*. Per questo, nel transistor NPN il potenziale del collettore deve essere positivo rispetto alla base, mentre nel transistor PNP deve essere negativo.

<tip>
La funzione del transistor si attiva solo se la zona di base tra emettitore e collettore è larga al massimo pochi micrometri. Quindi non è possibile costruire un transistor semplicemente saldando due diodi separati.
</tip>

La tensione minima al giunto emettitore-base dipende dal semiconduttore utilizzato. In un transistor NPN al silicio, la base deve essere circa $\qty{0,6}{\volt}$ più positiva dell’emettitore, mentre nel transistor PNP al silicio deve essere circa $\qty{0,6}{\volt}$ più negativa. Questa tensione è chiamata tensione base-emettitore $U_\mathrm{BE}$.

[question:EC610]
[question:EC612]
[question:EC613]
[question:EC614]
[question:EC615]

---

<margin>
[picture:863:e_npn_i_u:Correnti e tensioni in un transistor NPN]
</margin>

---

Le correnti e le tensioni in un transistor NPN sono illustrate nella figura [ref:e_npn_i_u]. Abbiamo già incontrato la tensione base-emettitore $U_\mathrm{BE}$. Esistono anche la tensione collettore-base $U_\mathrm{CB}$ e la tensione collettore-emettitore $U_\mathrm{CE}$. La corrente di collettore $I_\mathrm{C}$ dipende esponenzialmente dalla tensione base-emettitore:


$I_\mathrm{C} = I_\mathrm{S}\ e^{\frac{U_\mathrm{BE}}{U_\mathrm{T}}}$


A *temperatura ambiente*, $U_\mathrm{T}$ è circa $\qty{26}{\milli\volt}$.


<indepth>
$I_\mathrm{S}$ indica la cosiddetta corrente di saturazione inversa di un transistor bipolare. È un parametro caratteristico del componente e dipende strettamente dal diodo emettitore-base. Si tratta di una corrente di perdita molto piccola che fluisce attraverso il transistor anche quando il giunto base-emettitore non è in conduzione.
</indepth>

La corrente di base $I_\mathrm{B}$ ha, in ampi intervalli di funzionamento, la stessa dipendenza dalla tensione della corrente di collettore, per cui il rapporto tra corrente di collettore e corrente di base è costante:


$\frac{I_\mathrm{C}}{I_\mathrm{B}} = B$


*$B$* è il *rapporto* di corrente (più precisamente, il rapporto di corrente nella *configurazione a emettitore comune*). Spesso è più pratico considerare il transistor come un componente controllato in corrente, anche se fisicamente non è così. Il rapporto di corrente nei transistor pratici è compreso tra $50$ e $350$.

<tip>
Per il controllo in corrente del transistor bipolare esiste un’analogia molto antica, che paragona un grande e un piccolo canale d’acqua, una diga nel canale grande e una valvola di controllo. Forse i più anziani tra noi la ricordano ancora dal "Piccolo radiomane" della casa editrice Kosmos...

[picture:835:e_transistor_wehr_geschlossen:Il canale di controllo chiude completamente la diga]


Inizialmente non scorre acqua nel piccolo canale. La diga nel canale grande è chiusa, quindi non scorre acqua nemmeno lì.


[picture:837:e_transistor_wehr_halb_offen:Il canale di controllo apre la diga a metà]


Poi inizia a scorrere acqua nel piccolo canale, il canale di controllo. L’acqua solleva la valvola, che a sua volta aziona la diga: anche nel canale principale inizia a scorrere acqua.


[picture:836:e_transistor_wehr_geoeffnet:Il canale di controllo apre completamente la diga]


Ora scorre più acqua nel canale di controllo, la valvola si solleva ulteriormente e la diga nel canale principale si apre completamente.
</tip>

[question:EC603]


La corrente di emettitore $I_\mathrm{E}$ è la somma della corrente di collettore e della corrente di base:


$I_\mathrm{E} = I_\mathrm{C} + I_\mathrm{B}$


[question:EC611]


Il punto di lavoro in tensione dei transistor viene solitamente indicato tramite la tensione collettore-emettitore:


$U_\mathrm{CE} = U_\mathrm{CB} + U_\mathrm{BE}$


Oltre ai transistor bipolari, trattati prevalentemente qui, esistono soprattutto i *transistor a effetto di campo*, che funzionano fisicamente in modo diverso ma che, all’esterno, hanno la stessa funzione di base (sorgente di corrente controllata in tensione). Sotto forma di MOSFET, dominano la nostra elettronica, poiché sono presenti in milioni o miliardi nei circuiti integrati dell’elettronica digitale.

<indepth>
MOSFET sta per *metal-oxide-semiconductor field effect transistor*, in tedesco *Metall-Oxid-Halbleiter-Feldeffekttransistor*.
</indepth>

[question:EC604]


I transistor possono essere utilizzati non solo come *amplificatori*, ma anche come *interruttori* (corrente acceso/spento) o, con piccole tensioni in uscita, come *resistenza* controllabile. Quest’ultima funzione è implementata soprattutto con i transistor a effetto di campo.

[question:EC601]