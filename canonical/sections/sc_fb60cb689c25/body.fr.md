---

De nombreux appareils radio disposent d’un port dit **DATA**, souvent marqué *DATA* ou *$\qty{9600}{\baud}$*, comme illustré dans la figure [ref:e_9600_port]. Ce port a été conçu à l’origine pour les applications Packet-Radio, aujourd’hui largement remplacées par HAMNET. Toutefois, il peut aussi servir à d’autres usages, par exemple pour le mode de transmission numérique de la voix M17. Dans ce cas, on y raccorde un modem adapté, souvent appelé TNC, comme montré dans la figure [ref:m17_tnc].

<margin>
[photo:303:e_9600_port:Appareil radio avec port DATA]
[photo:185:m17_tnc:Module M17, un TNC pour le mode de transmission M17]
</margin>

Le port $\qty{9600}{\baud}$ offre une connexion directe au modulateur et au démodulateur de l’émetteur-récepteur, permettant de traiter les signaux avec une grande précision et de faibles distorsions. Pour des débits plus élevés, comme ceux utilisés dans le Packet-Radio $\qty{9600}{\baud}$ (protocole AX.25), il est nécessaire de contourner l’ensemble de la voie audio, avec sa réponse en fréquence limitée et ses filtres (par exemple, le filtre micro et le préamplificateur). La voie audio d’un émetteur-récepteur est généralement accordée pour les signaux vocaux et présente une bande passante restreinte, souvent comprise entre $\qty{300}{\hertz}$ et $\qty{3000}{\hertz}$. Cette bande passante ne suffit pas pour transmettre de manière fiable $\qty{9600}{\baud}$, car un tel débit nécessite une largeur de signal plus importante. Par le port DATA, les signaux sont transmis sans les filtres, le traitement DSP et le processus de désaccentuation présents dans la voie audio. Cela réduit les distorsions et les latences, ce qui est crucial pour les transmissions numériques afin de minimiser le taux d’erreur.

En résumé, le port $\qty{9600}{\baud}$ est spécialement conçu pour traiter les données numériques directement, sans les contraintes de la voie audio, ce qui est indispensable pour une transmission de données rapide et efficace.


---

Dans les questions suivantes, un émetteur-récepteur FM est utilisé. Pour l’émission, le port DATA doit être connecté avant le modulateur FM, et pour la réception, après le démodulateur FM.

[question:EF309]
[question:EF219]

<indepth>
Pourquoi $\qty{9600}{\baud}$ ?


$\qty{9600}{\baud}$ ($\qty{9,6}{\kilo\bit\par\seconde}$ si une modulation à un bit par symbole est utilisée) est une vitesse courante pour les communications numériques en radioamateurisme, notamment en Packet-Radio. Ce débit représente un compromis entre la vitesse atteignable et la faisabilité technique dans la bande VHF/UHF, où opèrent la plupart des émetteurs-récepteurs FM.
</indepth>