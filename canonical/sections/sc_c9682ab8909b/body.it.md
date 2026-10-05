Nella sezione [sec:oszillator_tcxo_ocxo] abbiamo visto che esistono diversi tipi di oscillatori con diversa stabilità e precisione di frequenza. Una stabilità particolarmente elevata è raggiunta dagli oscillatori al quarzo sotto forma di TCXO e soprattutto di OCXO. I moderni apparati radio, ad esempio con un TCXO, raggiungono una precisione di frequenza di $\pm\qty{0,5}{\ppm}$. Per una frequenza desiderata di $\qty{10}{\mega\hertz}$, la frequenza effettiva si trova quindi nell'intervallo da $\qtyrange{9,999995}{10,000005}{\mega\hertz}$, cioè al massimo $\pm\qty{5}{\hertz}$ rispetto alla frequenza nominale. Questa deviazione è piccola e per l'operatività in onde corte è generalmente più che sufficiente.

Tuttavia, se non operiamo a $\qty{10}{\mega\hertz}$, ma a $\qty{10}{\giga\hertz}$, la possibile deviazione aumenta a $\pm\qty{5000}{\hertz}$. Può quindi già essere maggiore della larghezza di banda di un filtro SSB tipico. In un collegamento radio su una frequenza concordata in anticipo, il segnale potrebbe quindi trovarsi al di fuori della gamma di ricezione. Per tali applicazioni, ad esempio nel satellite geostazionario QO-100 che trasmette a $\qty{10}{\giga\hertz}$, sono quindi necessari riferimenti di frequenza ancora più precisi.

<margin>
[picture:1081:a_gpsdo:Oscillatore disciplinato GPS (GPSDO) nel contesto di una stazione QO-100]
</margin>

Si potrebbe investire un grande sforzo per stabilizzare ulteriormente un OCXO, o utilizzare altri tipi di oscillatori come i campioni di frequenza al rubidio, che in particolare su periodi più lunghi raggiungono una stabilità maggiore degli oscillatori al quarzo. Tali campioni di frequenza hanno però spesso svantaggi come un maggiore assorbimento di corrente, dimensioni più grandi e un prezzo più elevato, poiché sono sviluppati principalmente per applicazioni professionali.

Fortunatamente esiste un'altra possibilità: i sistemi di navigazione satellitare, in inglese Global Navigation Satellite Systems (GNSS), come GPS o Galileo, necessitano di riferimenti temporali molto precisi. La posizione del ricevitore è determinata in base ai tempi di propagazione dei segnali che vengono trasmessi da più satelliti al ricevitore. Poiché ogni orologio preciso necessita di un oscillatore stabile come base temporale, possiamo utilizzare il riferimento temporale ottenuto dai segnali satellitari per stabilizzare il nostro TCXO o OCXO. Un tale oscillatore è chiamato oscillatore sincronizzato GPS o in inglese GPS-Disciplined Oscillator (GPSDO). Come funziona tecnicamente questa regolazione, lo esamineremo in un capitolo successivo sui loop ad aggancio di fase (PLL). Nella figura [ref:a_gpsdo] è mostrato un GPSDO nel contesto di una stazione QO-100, che fornisce al Software Defined Radio (SDR) una frequenza di riferimento stabile. Un modulo autocostruito è visibile nella figura [ref:a_gpsdo_homebrew].

---

Ora ci si potrebbe chiedere perché non utilizziamo direttamente il riferimento temporale fornito dal GPS come segnale dell'oscillatore. Il ricevitore GPS ricava dai deboli segnali satellitari modulati tipicamente un segnale temporale preciso, ad esempio un impulso al secondo. Tuttavia, l'istante esatto di questo impulso può fluttuare a breve termine a causa di rumore, propagazione per cammini multipli, influenze atmosferiche e ritardi nel ricevitore. Considerata su periodi più lunghi, la frequenza da esso derivata è invece molto precisa.

Un TCXO o OCXO possiede a sua volta una buona o molto buona stabilità a breve termine, ma a lungo termine può discostarsi lentamente dalla frequenza nominale a causa di influenze termiche residue e dell'invecchiamento dei suoi componenti. In un GPSDO, quindi, entrambe le proprietà vengono combinate: il TCXO o OCXO locale fornisce un segnale di uscita stabile a breve termine e a basso rumore, mentre un loop di regolazione lento corregge la sua deviazione a lungo termine utilizzando il riferimento temporale GPS. In questo modo, un GPSDO raggiunge sia un'ottima stabilità a breve termine sia un'elevata stabilità a lungo termine, oltre a un'elevata precisione di frequenza.

[question:AD606]

<margin>
[photo:335:a_gpsdo_homebrew:GPSDO autocostruito con TCXO]
</margin>
