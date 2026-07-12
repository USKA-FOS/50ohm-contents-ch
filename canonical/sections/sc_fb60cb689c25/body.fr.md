---

De nombreux appareils radio disposent d'un port appelé DATA, souvent marqué *DATA* ou *$\qty{9600}{\baud}$*, comme illustré dans la figure [ref:e_9600_port]. Ce port a été initialement développé pour les applications Packet-Radio, qui ont été largement remplacées par HAMNET. Néanmoins, ce port peut également être utilisé pour d'autres procédés, comme le procédé de transmission vocale numérique M17. Dans ce cas, un modem approprié - souvent appelé TNC - est connecté, comme illustré dans la figure [ref:m17_tnc].

<margin>
[photo:303:e_9600_port:Appareil radio avec port DATA]
[photo:185:m17_tnc:Module M17 un TNC pour le procédé de transmission M17]
</margin>

Le port $\qty{9600}{\baud}$ offre une connexion directe au modulateur et au démodulateur de l'émetteur-récepteur pour traiter les signaux avec une grande précision et de faibles distorsions. Pour des débits de données plus élevés, tels que ceux utilisés dans le Packet-Radio $\qty{9600}{\baud}$ (protocole AX.25), il est nécessaire de contourner l'ensemble du chemin audio avec ses bandes passantes limitées et ses filtrages (par exemple, les filtres de microphone et les préamplificateurs). Le chemin audio d'un émetteur-récepteur est normalement adapté aux signaux vocaux et a une bande passante limitée, souvent comprise entre $\qty{300}{\hertz}$ et $\qty{3000}{\hertz}$. Cette bande passante n'est pas suffisante pour transmettre $\qty{9600}{\baud}$ de manière fiable, car un débit aussi élevé nécessite une plus grande largeur de signal. Les signaux sont transmis via le port de données sans les filtres, le traitement DSP et le processus de désaccentuation présents dans le chemin audio. Cela réduit les distorsions et les latences, ce qui est crucial pour les transmissions numériques afin de minimiser le taux d'erreur.

En résumé : le port $\qty{9600}{\baud}$ est spécialement conçu pour traiter les données numériques directement et sans les limitations du chemin audio, ce qui est nécessaire pour une transmission de données à haute vitesse fiable et efficace.


---

Dans les questions suivantes, un émetteur-récepteur FM est utilisé. Pour l'émission, le port DATA doit être connecté avant le modulateur FM et pour la réception après le démodulateur FM.

[question:EF309]
[question:EF219]

<indepth>
Pourquoi $\qty{9600}{\baud}$ ?

$\qty{9600}{\baud}$ ($\qty{9,6}{\kilo\bit\per\second}$, si une modulation avec un bit par symbole est utilisée) est une vitesse courante pour la communication numérique dans le radioamateur, en particulier dans le Packet-Radio. Ce débit de données représente un compromis entre la vitesse atteignable et la faisabilité technique dans la bande de fréquences VHF/UHF, où la plupart des émetteurs-récepteurs FM fonctionnent.
</indepth>