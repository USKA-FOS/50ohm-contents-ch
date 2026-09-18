<margin>
[picture:735:aufbau_sender:Diagramma a blocchi di un semplice trasmettitore]
</margin>

Nella figura [ref:aufbau_sender] sono illustrate le componenti necessarie per costruire un trasmettitore AM. Alcuni dei blocchi li abbiamo già incontrati nel ricevitore, altri sono nuovi:
1. Microfono: il microfono converte le onde sonore della voce in oscillazioni elettriche a bassa frequenza. In alternativa, ad esempio per procedure di trasmissione digitale, si può utilizzare il segnale a bassa frequenza proveniente dall’uscita audio di un [computer](#).
2. Amplificatore a bassa frequenza: il segnale proveniente dal microfono o dal [computer](#) viene inizialmente amplificato.
3. [Mixer](#): il [mixer](#) combina la portante ad [alta frequenza](#) generata dall’[oscillatore](#) (4) con l’oscillazione a bassa frequenza proveniente dal microfono o dal [computer](#). Questo processo fa sì che la portante ad [alta frequenza](#) venga modulata in ampiezza dal segnale vocale o dati.
4. [Oscillatore](#): l’[oscillatore](#) genera l’oscillazione ad [alta frequenza](#) alla frequenza di trasmissione desiderata, ad esempio $\qty{29,5}{\mega\hertz}$.
5. [Filtro passa-banda](#): poiché il [mixer](#), a causa del suo funzionamento, genera oltre alle frequenze desiderate anche altre frequenze indesiderate, queste devono essere bloccate con un [filtro di banda](#).
6. Amplificatore ad [alta frequenza](#): il segnale ad [alta frequenza](#) viene ora amplificato per raggiungere la desiderata [potenza di trasmissione](#).
7. [Filtro passa-basso](#): poiché anche l’amplificazione può generare frequenze indesiderate, è necessario filtrare nuovamente.
8. [Antenna](#): il segnale ad [alta frequenza](#) viene inviato all’[antenna](#), che lo irradia come onda radio.

%[class:N]
<indepth>
Quando un [mixer](#) combina due segnali, matematicamente corrisponde a una moltiplicazione dei due segnali. Pertanto, anche nel simbolo a blocchi del [mixer](#) si trova il segno della moltiplicazione. Come funziona esattamente un [mixer](#) è oggetto del corso per la classe A.
</indepth>
%[/class]

[question:NF401]
[question:NF403]

Per la domanda seguente è importante ricordare che un trasmettitore necessita di un [oscillatore](#) e di un [mixer](#).


[question:NF402]


Un [impianto radioamatoriale](#) deve essere costruito e utilizzato secondo le regole tecniche generalmente riconosciute. Questo vale naturalmente anche, e in particolare, per i trasmettitori.


[question:VD106]