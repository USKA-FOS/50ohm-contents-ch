<margin>
[picture:735:aufbau_sender:Diagramma a blocchi di un semplice trasmettitore]
</margin>

Nella figura [ref:aufbau_sender] viene mostrato da quali componenti si può costruire un trasmettitore AM. Alcuni dei blocchi li conosciamo già dal ricevitore, altri sono nuovi:
1. Microfono: Il microfono converte le onde sonore del parlato in oscillazioni elettriche a bassa frequenza. In alternativa, si può utilizzare il segnale a bassa frequenza dall'uscita audio di un computer, ad esempio per metodi di trasmissione digitale.
2. Amplificatore a bassa frequenza: Il segnale proveniente dal microfono o dal computer viene prima amplificato.
3. Mixer: Il mixer combina la portante ad alta frequenza generata dall'oscillatore (4) con l'oscillazione a bassa frequenza del microfono o del computer. Ciò fa sì che la portante ad alta frequenza venga modulata in ampiezza con il segnale vocale o dati.
4. Oscillatore: L'oscillatore genera l'oscillazione ad alta frequenza con la frequenza su cui si desidera trasmettere, ad esempio $\qty{29,5}{\mega\hertz}$.
5. Filtro passa-banda: Poiché il mixer, a causa del suo funzionamento, genera anche frequenze indesiderate oltre a quelle desiderate, queste devono essere bloccate con un filtro passa-banda.
6. Amplificatore ad alta frequenza: Il segnale ad alta frequenza viene ora amplificato in modo che disponga della potenza di trasmissione desiderata.
7. Filtro passa-basso: Poiché anche l'amplificazione può generare frequenze indesiderate, è necessario filtrare nuovamente.
8. Antenna: Il segnale ad alta frequenza viene quindi inviato all'antenna e da questa irradiato come onda radio.

%[class:N]
<indepth>
Quando un mixer combina due segnali, ciò corrisponde matematicamente a una moltiplicazione dei due segnali. Per questo motivo, nel simbolo a blocchi del mixer si ritrova anche la croce di moltiplicazione. Come funziona esattamente un mixer è contenuto nel corso per la classe A.
</indepth>
%[/class]

[question:NF401]
[question:NF403]

Per la seguente domanda è importante ricordare che un trasmettitore necessita di un oscillatore e di un mixer.

[question:NF402]

Un impianto radioamatoriale deve essere costruito e gestito secondo le regole universalmente riconosciute della tecnica. Ciò vale naturalmente anche in modo particolare per i trasmettitori.

[question:VD106]

