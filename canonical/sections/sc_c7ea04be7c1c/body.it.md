Un vecchio detto dei radioamatori dice che il miglior amplificatore ad alta frequenza è l'antenna. Nei primi anni della tecnologia radio, questa era l'unica "amplificazione", non esisteva un'elettronica di amplificazione. Nel 1907 arrivò la valvola termoionica, un componente di grande successo, ma piuttosto grande e poco efficiente. Già dagli anni Venti, la scienza sognava componenti con una funzione simile, ma in cui tutto avvenisse all'interno di un corpo solido (semiconduttore), non nel vuoto. Il primo componente in cui ciò riuscì praticamente fu, nel 1947/1948, il *Transistor* bipolare, che è anche l'oggetto predominante delle domande d'esame per la patente di classe E.

[question:EC602]

<indepth>
Il *Transistor* bipolare è chiamato in inglese anche BJT: Bipolar Junction Transistor, in tedesco: bipolarer Sperrschicht-Transistor.
</indepth>

La funzione ideale di tutti i tipi di Transistor, e anche della valvola termoionica, è quella di una *sorgente di corrente controllata in tensione*: con una variazione di tensione il più piccola possibile all'ingresso, si deve ottenere una variazione di corrente il più grande possibile all'uscita.

Il Transistor bipolare ha tre terminali, chiamati Emettitore, Base e Collettore. L'Emettitore invia portatori di carica alla Base - nel Transistor bipolare npn si tratta di *elettroni*, nel Transistor bipolare pnp di difetti elettronici, chiamati anche *lacune*. La fisica alla base di questi termini la discuteremo solo nella formazione per la classe A. Questi portatori di carica attraversano la Base e vengono raccolti dal Collettore.

---

La figura [ref:e_npn_pnp_symbol] mostra i simboli di circuito dei Transistor NPN e PNP. Riconosciamo l'elettrodo dell'Emettitore da una freccia che, nel Transistor pnp, punta verso la Base e, nel Transistor npn, si allontana dalla Base.

<margin>
[picture:864:e_npn_pnp_symbol:Simboli Transistor NPN e PNP]
</margin>

[question:EC605]
[question:EC606]
[question:EC607]
[question:EC608]
[question:EC609]

---

I Transistor bipolari sono composti da due Diodi: la Diode Emettitore-Base e la Diode Base-Collettore.
In funzionamento attivo, la Diode Emettitore-Base è sempre polarizzata in direzione diretta. Nel Transistor NPN, il potenziale sulla Base deve essere più positivo di quello dell'Emettitore, nel Transistor PNP più negativo. La Diode Base-Collettore è polarizzata in direzione inversa. Per questo, nel Transistor NPN, il potenziale del Collettore deve essere scelto più positivo di quello della Base, nel Transistor PNP più negativo.

<tip>
La funzione del Transistor si verifica però solo se la zona della Base tra Emettitore e Collettore è larga al massimo pochi micrometri. Quindi non possiamo creare un Transistor saldando due Diodi separati.
</tip>

La tensione minima sulla giunzione Emettitore-Base dipende dal semiconduttore utilizzato. In un Transistor NPN al silicio, la Base deve essere circa $\qty{0,6}{\volt}$ più positiva dell'Emettitore, in un Transistor PNP al silicio circa $\qty{0,6}{\volt}$ più negativa.

[question:EC610]
[question:EC612]
[question:EC613]
[question:EC614]
[question:EC615]

---

<margin>
[picture:863:e_npn_i_u:Correnti e tensioni su un Transistor npn]
</margin>

---

Le correnti e le tensioni su un Transistor npn sono rappresentate nella figura [ref:e_npn_i_u]. La tensione Base-Emettitore $U_{BE}$ la conosciamo già, così come la tensione Collettore-Base $U_{CB}$. La corrente di Collettore $I_C$ dipende esponenzialmente dalla tensione Base-Emettitore:

$I_C = I_\text{S}\ e^{\frac{U_{BE}}{U_T}}$

$U_T$ è a temperatura ambiente circa $\qty{26}{\milli\volt}$.

<indepth>
$I_\text{S}$ indica la cosiddetta corrente di saturazione inversa di un Transistor bipolare. È un parametro caratteristico del componente ed è strettamente correlato alla Diode Emettitore-Base. Si tratta di una corrente di perdita molto piccola che attraversa il Transistor anche quando la linea Base-Emettitore non è conduttiva.
</indepth>

La corrente di Base $I_B$ ha, in ampi intervalli operativi, la stessa dipendenza dalla tensione della corrente di Collettore, in modo che il rapporto tra corrente di Collettore e corrente di Base sia costante:

$\frac{I_C}{I_B} = B$

*B* è l'amplificazione di corrente (più precisamente, l'amplificazione di corrente in configurazione Emettitore comune). È spesso più pratico considerare il Transistor come un componente controllato in corrente, anche se fisicamente non lo è. L'amplificazione di corrente nei Transistor pratici varia da $50$ a $350$.

<tip>
Per il controllo della corrente del Transistor bipolare esiste un'antica analogia, in cui giocano un ruolo un canale d'acqua grande e uno piccolo, una diga nel canale grande e una valvola di controllo. I più anziani tra noi forse la ricordano ancora dal "Kleiner Radiomann" della Kosmos-Verlag...
  
[picture:835:e_transistor_wehr_geschlossen:Canale di controllo chiude completamente la diga]
  
Inizialmente, nessun flusso d'acqua nel canale piccolo. La diga nel canale grande è chiusa, quindi nemmeno lì scorre acqua.
  
[picture:837:e_transistor_wehr_halb_offen:Canale di controllo apre parzialmente la diga]

Poi inizia a scorrere acqua nel canale piccolo, il canale di controllo. L'acqua solleva la valvola, che a sua volta aziona la diga - anche nel canale principale inizia a scorrere acqua.
  
[picture:836:e_transistor_wehr_geoeffnet:Canale di controllo apre completamente la diga]

Ora scorre più acqua nel canale di controllo, la valvola viene sollevata ulteriormente, la diga nel canale principale si apre completamente.
</tip>

[question:EC603]

La corrente di Emettitore $I_E$ è la somma della corrente di Collettore e della corrente di Base:

$I_E = I_C + I_B$

[question:EC611]

Il punto di funzionamento in tensione dei Transistor è solitamente indicato tramite la tensione Collettore-Emettitore:

$U_{CE} = U_{CB} + U_{BE}$

Oltre ai Transistor bipolari qui trattati prevalentemente, esistono soprattutto anche i *Transistor a effetto di campo*, che funzionano fisicamente in modo diverso, ma esternamente hanno la stessa funzione di base (sorgente di corrente controllata in tensione). Sotto forma di MOSFET, dominano la nostra elettronica, poiché sono presenti milioni o miliardi di volte nei circuiti integrati dell'elettronica digitale.

<indepth>
MOSFET sta per *metal-oxide-semiconductor field effect transistor*, in tedesco: Metall-Oxid-Halbleiter-Feldeffekttransistor.
</indepth>

[question:EC604]

I Transistor possono essere utilizzati non solo come amplificatori, ma anche come interruttori (corrente on/off) o anche, con piccole tensioni in uscita, come resistenze controllabili. Quest'ultima funzione viene realizzata principalmente con Transistor a effetto di campo.

[question:EC601]
