Une "balise" (en anglais : beacon) est une installation d'émission radioamateur fonctionnant automatiquement, qui émet en continu ou à intervalles réguliers des signaux définis. Elle sert notamment à observer les conditions de propagation, à évaluer la recevabilité et pour des mesures techniques. Les balises existent également à bord de satellites radioamateurs. Dans le cas des satellites radioamateurs, les balises remplissent souvent une fonction importante pour l'identification et la surveillance du [sec:satellites] ainsi que pour la transmission de télémesures.

Les balises émettent généralement sur une fréquence fixe et peuvent être exploitées à des emplacements fixes ou sur des plateformes mobiles, par exemple des satellites. Comme leur recevabilité dépend fortement des conditions de propagation changeantes de la bande radio concernée, une balise peut servir d'indicateur des conditions de propagation actuelles sur le trajet entre la balise et le lieu de réception.

Par exemple, si l'on peut bien recevoir une balise en ondes courtes depuis l'Amérique du Sud, cela indique que les conditions de propagation pour les liaisons radio dans cette direction peuvent être favorables.

Les balises aurores dans la bande VHF peuvent indiquer si une propagation aurorale est actuellement présente et si des liaisons DX en direction de la Scandinavie sont possibles. Avec des balises connues sur les bandes VHF, UHF et SHF, on peut par exemple vérifier l'installation de réception et déterminer si une antenne directionnelle est correctement orientée. Les balises servent également à vérifier la sensibilité du récepteur, le niveau du signal et la précision de la fréquence.

<indepth>
Autres possibilités d'observer les conditions de propagation

En plus des balises, il existe aujourd'hui d'autres systèmes permettant d'observer les conditions de propagation actuelles. Parmi ceux-ci figurent par exemple :

- [PSK Reporter](https://pskreporter.info/pskmap.html) et le

- [Reverse Beacon Network](https://www.reversebeacon.net/).

Ces systèmes ne sont pas des balises. Ils collectent automatiquement des rapports de réception ou des informations sur les émissions détectées de stations radioamateurs et les affichent presque en temps réel sur une carte géographique.

[WSPR](https://www.wsprnet.org/) est également souvent utilisé pour étudier les conditions de propagation. Dans ce cas, des signaux très faibles et standardisés sont émis, qui sont reçus et analysés par de nombreuses stations de réception fonctionnant automatiquement.

Une description détaillée de ces systèmes dépasserait le cadre de ce chapitre. Cependant, ils constituent des compléments utiles pour observer les conditions de propagation actuelles dans la pratique radio.
</indepth>

<tip>
Où trouver les *balises VHF, UHF et SHF* ?

Pour la Suisse, l'USKA propose une [vue d'ensemble des fréquences des balises](https://uska.ch/wp-content/uploads/2026/03/251116-Baken-Schweiz.pdf).
</tip>

[question:BE409]

---

Le projet international de balises [IBP](https://www.ncdxf.org/beacon/) comprend un grand nombre de balises réparties dans plusieurs pays sur tous les continents. Les différentes balises émettent successivement selon un cycle défini sur les cinq fréquences de balises IBP, chaque fréquence étant utilisée pendant environ 10 secondes. Cela permet d'évaluer rapidement la qualité des conditions de propagation actuelles sur la bande respective.

Dans les plans de bandes de l'IARU, des bandes de fréquences spécifiques sont prévues pour les balises. Ces bandes de fréquences de balises ne doivent pas être utilisées pour le trafic radio normal. Le tableau [ref:n_baken_frequenzbereiche] présente les bandes de fréquences de balises des bandes ondes courtes prévues dans le plan de bande de l'IARU Région 1.

<margin>
*Bandes de fréquences des balises des bandes ondes courtes*

| l: Bande | X: Bande de fréquences | Fréquence IBP |
| $\qty{10}{\meter}$ | $\qtyrange{28190}{28225}{\kilo\hertz}$ | $\qty{28.200}{\mega\hertz}$ |
| $\qty{12}{\meter}$ | $\qtyrange{24929}{24931}{\kilo\hertz}$ | $\qty{24.930}{\mega\hertz}$ |
| $\qty{15}{\meter}$ | $\qtyrange{21149}{21151}{\kilo\hertz}$ | $\qty{21.150}{\mega\hertz}$ |
| $\qty{17}{\meter}$ | $\qtyrange{18109}{18111}{\kilo\hertz}$ | $\qty{18.110}{\mega\hertz}$ |
| $\qty{20}{\meter}$ | $\qtyrange{14099}{14101}{\kilo\hertz}$ | $\qty{14.100}{\mega\hertz}$ |
[table:n_baken_frequenzbereiche:Bandes de fréquences des balises selon le plan de bande de l'IARU et fréquences IBP]
</margin>

% [question:BE410]
% [question:VD119]

% Modifications lors de la révision
% Corrections d'erreurs et précisions
% Approfondissement du Reverse Beacon Network, pskreporter et WSPR