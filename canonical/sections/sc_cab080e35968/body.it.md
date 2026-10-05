In questo capitolo vengono trattate le basi sui collegamenti radio permanenti e le relative normative per il funzionamento. Un trattamento esteso degli aspetti tecnici avviene nel capitolo [sec:paketvermittelte_netzwerke].

Un collegamento radio permanente è un collegamento radio stabilito in modo fisso, che serve per interconnettere stazioni radioamatoriali, ad esempio relè, digipeater o nodi HAMNET. I collegamenti radio permanenti possono far parte di impianti radioamatoriali non presidiati. L'esercizio di tali impianti deve essere comunicato all'UFCOM secondo le [normative](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) vigenti. Per un impianto radioamatoriale non presidiato è necessario un nominativo radioamatoriale della categoria HB9. Il responsabile tecnico deve essere permanentemente raggiungibile durante il funzionamento. L'immagine [ref:n_linkstrecken_HB9AK-14] mostra un sistema di antenne sul Titlis a 2992 metri sul livello del mare. In località come nell'immagine [ref:n_linkstrecken_HB9AK] prevalgono condizioni meteorologiche impegnative. Un allineamento preciso e stabile verso la stazione corrispondente da raggiungere viene preparato nell'immagine [ref:n_linkstrecken_HB9].

<margin>
%[photo:127:n_linkstrecken_db0fc:Operazioni di manutenzione al nodo HAMNET DB0FC, in primo piano l'antenna direzionale %per il collegamento radio permanente verso DB0BWL]
%
[photo:1001:n_linkstrecken_HB9AK-14:Sede Titlis impianto della SWISS-ARTG, esperimenti con antenne da 10 m; sopra Peter HB9PAE, sotto Martin HB9AUR]

[photo:1002:n_linkstrecken_HB9AK:Impianti in alta montagna devono resistere a condizioni ambientali severe]

[photo:1003:n_linkstrecken_HB9:Sede Titlis impianto della SWISS-ARTG, Dieter HB9CJD durante la configurazione del collegamento HAMNET verso HB9BA (Weissenstein), uno specchio di 85 cm per 5 GHz]
</margin>

%TODO ARK: nel testo fare riferimento alle immagini!
%TODO ARK: Nell'immagine del Titlis, 1001, tagliare il bordo nero sinistro!
%TODO ARK: Spostare una delle immagini nella sezione 16.11 Reti a commutazione di pacchetto!

<law>
- Le "Spiegazioni dettagliate sul servizio di radioamatore" si trovano nel [Manuale del radioamatore](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) dell'UFCOM.

- Link diretto per la comunicazione delle cosiddette "Utilizzazioni speciali di frequenza" all'UFCOM in [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail)

</law>

I collegamenti radio permanenti possono trasmettere dati digitali o fungere da ponte analogico tra relè. I collegamenti radio permanenti operano frequentemente nella banda dei $\unit{\giga\hertz}$ dello spettro radioamatoriale. Più collegamenti radio permanenti interconnessi possono ad esempio costituire l'HAMNET (Highspeed Amateurradio Multimedia NETwork), una rete IP dati gestita da radioamatori.

[question:NE405]

<indepth>
*Calcolo del collegamento*

Con un [tool di calcolo del collegamento](http://ham.remote-area.net/linktool/index.php) è possibile valutare se un collegamento radio direzionale tra due sedi è tecnicamente possibile. Considera, tra l'altro, frequenza, distanza, potenza di trasmissione, guadagni delle antenne, perdite del cavo e il *profilo del terreno* tra le sedi. Il tool calcola, tra l'altro, l'attenuazione nello spazio libero, la potenza di ricezione e la riserva del collegamento, supportando così la pianificazione di collegamenti radio direzionali e HAMNET.

Per un collegamento radio direzionale affidabile, oltre alla linea di vista diretta, è importante anche una zona di Fresnel il più possibile libera. La zona di Fresnel indica un'area spaziale attorno alla linea di collegamento diretta, in cui ostacoli possono compromettere la trasmissione radio per diffrazione e attenuazione aggiuntiva.
</indepth>

% Modifiche
% Echolink rimosso, appartiene ai relè.
% Descrizioni dei collegamenti create o integrate
% Tool di calcolo del collegamento descritto, a cosa serve.