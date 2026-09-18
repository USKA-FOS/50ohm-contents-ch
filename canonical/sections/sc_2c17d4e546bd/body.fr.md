L'idée fondamentale derrière la télégraphie Morse, qui consiste à transmettre des caractères d'un texte, est appelée télégraphie et a été constamment développée. Une étape importante a été l'interconnexion de téléimprimeurs à des appareils radio via un modem. Ainsi, le téléimprimeur radio était né, permettant d'envoyer et de recevoir automatiquement des textes par radio. L'abréviation RTTY, issue de l'anglais *radio teletype*, est encore utilisée aujourd'hui. Aujourd'hui, c'est généralement l'ordinateur qui a pris en charge la tâche du téléimprimeur radio. Grâce à cela, on peut utiliser, en plus de la méthode classique RTTY, de nombreux autres procédés de transmission numérique, également appelés *Digimodes*.

<indepth>
Un *téléimprimeur* est un appareil permettant de transmettre des messages sous forme de texte au moyen de signaux électriques.
</indepth>

<margin>
[photo:92:n_computersteuerung_funkfernschreiber:Téléimprimeur radio]
</margin>

---

Pour cela, il faut d'abord relier un ordinateur adapté à l'appareil radio. La connexion peut se faire, dans le cas le plus simple, directement via la prise audio ou l'interface USB. Il faut généralement une connexion audio ainsi que, le cas échéant, des signaux de commande. Dans l'illustration [ref:n_computersteuerung_verbindungen], plusieurs variantes sont représentées. Une interface souvent présente sur les émetteurs-récepteurs pour les signaux de commande est l'interface dite CAT. CAT signifie *Computer Aided Tuning* ou *Computer Aided Transceiver*. Grâce à cette interface, vous pouvez contrôler l'émetteur-récepteur et interroger des valeurs, par exemple la fréquence, la puissance d'émission et l'état du PTT.

<margin>
[picture:630:n_computersteuerung_verbindungen:Exemples de connexions entre ordinateur et appareil radio]
</margin>

Cependant, la connexion entre l'ordinateur et l'émetteur-récepteur peut entraîner des perturbations des signaux transmis ou des rétroactions de l'appareil radio sur le PC. Diverses interfaces *Digimode* en tant que solution matérielle simplifient la connexion et intègrent des mesures contre de tels problèmes. Ces interfaces peuvent également être utilisées à d'autres fins, par exemple pour l'exploitation à distance ou pour enregistrer le trafic radio avec un logiciel adapté. Pour certaines méthodes, il existe également des modems matériels dans lesquels la conversion entre données et signaux audio est effectuée dans un appareil dédié.

[question:NF114]
[question:NF116]

Il existe également d'autres effets involontaires. L'ordinateur pourrait passer en émission de manière inattendue ou émettre des sons de notification d'autres programmes en cours d'exécution. Parfois, on entend par exemple d'autres radioamateurs émettre accidentellement le son de démarrage du système d'exploitation. Si l'appareil radio émet de manière inattendue, des personnes travaillant sur l'installation d'antenne ou se trouvant par hasard dans son environnement direct pourraient être mises en danger.

[question:NF117]

---

Pour certaines méthodes de transmission, la prise micro de l'appareil radio n'est pas adaptée, car les étages d'amplification et de filtrage suivants sont optimisés pour la parole et traitent différemment les tons aigus ou graves. C'est pourquoi les appareils radio disposent souvent d'une propre prise de données analogique, marquée par exemple par *DATA* ou *9600*. En utilisant cette prise spécifique, certains étages d'amplification et de filtrage sont contournés et les signaux sont transmis avec un minimum de distorsion.

<indepth>
La désignation *9600* vient du fait que cette prise a été introduite pour le Packet-Radio, largement utilisé auparavant, afin de transmettre des données à $\qty{9600}{\baud}$. Aujourd'hui, cette prise est par exemple utilisée pour la transmission numérique de la voix et peut également fonctionner à des vitesses plus élevées.
</indepth>

[question:NF115]
