L'idée fondamentale derrière la télégraphie Morse, qui consiste à transmettre des caractères individuels d'un texte, est appelée télégraphie et a été constamment développée. Une étape importante a été de connecter des téléimprimeurs au moyen d'un modem à des appareils radio. Ainsi, le téléimprimeur radio a été inventé pour envoyer et recevoir automatiquement des textes par radio. L'abréviation RTTY du terme anglais radio teletype se retrouve encore comme désignation. Aujourd'hui, la tâche du téléimprimeur radio est généralement assurée par l'ordinateur. Ainsi, en plus de la procédure classique RTTY, on peut utiliser de nombreux autres procédés de transmission numérique, également appelés Digimodes.

<indepth>
Un *téléimprimeur* est un appareil permettant de transmettre des messages sous forme de texte au moyen de signaux électriques.
</indepth>

<margin>
[photo:92:n_computersteuerung_funkfernschreiber:Téléimprimeur radio]
</margin>

---

Pour cela, il faut d'abord connecter un ordinateur approprié à l'appareil radio. La liaison peut, dans le cas le plus simple, s'effectuer directement via la prise audio ou l'interface USB. On a fondamentalement besoin d'une liaison audio ainsi que, le cas échéant, de signaux de commande. La figure [ref:n_computersteuerung_verbindungen] montre quelques variantes. Une prise souvent présente sur les émetteurs-récepteurs pour les signaux de commande est l'interface dite CAT. CAT signifie Computer Aided Tuning ou Computer Aided Transceiver. Via cette interface, tu peux commander l'émetteur-récepteur et interroger des valeurs, par exemple la fréquence, la puissance d'émission et l'état PTT.

<margin>
[picture:630:n_computersteuerung_verbindungen:Exemples de liaisons entre ordinateur et appareil radio]
</margin>

La liaison entre l'ordinateur et l'émetteur-récepteur peut cependant entraîner des perturbations des signaux transmis ou des réactions de l'appareil radio sur le PC. Diverses interfaces Digimode en tant que solution matérielle facilitent le raccordement et contiennent des mesures contre de tels problèmes. On peut également utiliser de telles interfaces pour d'autres objectifs, par exemple pour l'exploitation à distance ou pour enregistrer le trafic radio avec un logiciel approprié. Pour certains procédés, il existe également des modems matériels, dans lesquels la conversion entre les données et les signaux audio s'effectue dans un appareil séparé.

[question:NF114]
[question:NF116]

Il existe également d'autres effets involontaires. L'ordinateur pourrait passer en émission de manière inattendue ou émettre des sons de notification d'autres programmes en cours d'exécution. Parfois, on entend par exemple comment d'autres radioamateurs émettent accidentellement le son de démarrage du système d'exploitation. Si l'appareil radio émet de manière inattendue, des personnes pourraient être mises en danger, qui travaillent justement sur l'installation d'antenne ou se trouvent par hasard dans son environnement immédiat.

[question:NF117]

---

Pour certains procédés de transmission, la prise de microphone de l'appareil radio est inadaptée, car les étages amplificateurs et filtres suivants sont optimisés pour la parole et traitent différemment les tons plus ou moins élevés. C'est pourquoi les appareils radio disposent souvent d'une prise de données analogique séparée, qui est par exemple marquée DATA ou 9600. En utilisant cette prise spéciale, certains étages amplificateurs et filtres sont contournés et les signaux sont transmis aussi fidèlement que possible.

<indepth>
La désignation *9600* vient du fait que cette prise a été introduite pour le Packet-Radio beaucoup utilisé à l'époque, afin que les données puissent être transmises à $\qty{9600}{\baud}$. Aujourd'hui, la prise est utilisée par exemple pour la transmission vocale numérique et fonctionne parfois à une vitesse plus élevée.
</indepth>

[question:NF115]
