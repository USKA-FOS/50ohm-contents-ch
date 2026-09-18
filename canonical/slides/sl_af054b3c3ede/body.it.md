### Perché I/Q?

* I simboli possono differire per ampiezza, frequenza o fase.
* Per rappresentare ampiezza e fase in modo chiaro, si utilizza una rappresentazione specifica.
* Questa rappresentazione è chiamata *rappresentazione I/Q*.
* Essa mostra lo stato del segnale di un simbolo come un punto in un piano.

--- style="font-size: 0.7em;"

<left>
[include:applet_iq_zeiger]
</left>
<right>
### Simbolo come vettore

* Lunghezza del vettore: ampiezza $A$
* Angolo del vettore: fase $\varphi$

* Il vettore può essere scomposto in due componenti:

$I=A\cdot\cos(\varphi)$


$Q=A\cdot\cos(\varphi-\qty{90}{\degree})=A\cdot\sin(\varphi)$


* Il diagramma di costellazione mostra lo stato iniziale del vettore per ogni simbolo.
</right>


---


[question:AF633]


---


### Diagramma di costellazione

[picture:1060:a_konstellationsdiagramm:Diagramma di costellazione]


---


### Diagramma di costellazione

* Per rappresentare i simboli, non consideriamo la rotazione continua della portante.
* Invece, osserviamo lo stato del segnale associato a un simbolo.
* Ogni possibile stato del simbolo viene rappresentato come un punto nel piano I/Q.
* La distanza dall'origine: ampiezza
* L'angolo rispetto all'asse I: posizione di fase

---


### Perché ne abbiamo bisogno?

* I diagrammi di costellazione mostrano immediatamente i possibili simboli di un metodo di trasmissione digitale.
* Si può riconoscere se i simboli differiscono per ampiezza, fase o entrambi.
* Nei prossimi paragrafi utilizzeremo questa rappresentazione per il mapping, PSK e QAM.