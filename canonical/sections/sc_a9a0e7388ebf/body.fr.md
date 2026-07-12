Contrairement à la transmission vocale, de nombreux procédés de transmission numériques (Digimodes) ne nécessitent qu'une bande passante très faible. Alors que les signaux vocaux en SSB occupent généralement une bande passante d'environ $\qty{2,4}{\kilo\hertz}$, les Digimodes se contentent de bandes de fréquences beaucoup plus étroites. Par exemple, BPSK31 ne nécessite qu'environ $\qty{31,25}{\hertz}$ de bande passante, tandis que FT8 se contente d'environ $\qty{50}{\hertz}$. Les signaux générés par les Digimodes sont également modulés en SSB sur les ondes courtes. La bande passante HF du signal émis correspond alors exactement à la bande passante NF du Digimode.

[question:EE402]
[question:EE403]

Dans la bande passante SSB d'environ $\qty{2,4}{\kilo\hertz}$ habituelle, plusieurs de ces signaux Digimode à bande étroite peuvent être reçus simultanément.

<margin>
[picture:718:e_digimode_ssb_empfang_mehrerer_digimodes:Diagramme en cascade de la réception de plusieurs signaux Digimode dans la largeur de bande SSB de 2,4 kHz. Chaque colonne est la transmission d'un autre signal]
</margin>

[question:EE404]

Théoriquement, jusqu'à 48 signaux FT8 ($\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$) ou même jusqu'à 76 signaux BPSK31 ($\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$) peuvent être logés dans une bande passante SSB de $\qty{2,4}{\kilo\hertz}$. Sur l'ordinateur, un seul signal Digimode peut ensuite être sélectionné de manière ciblée ou, selon le logiciel, une pluralité de ces signaux peut également être décodée simultanément. C'est précisément cette efficacité spectrale élevée qui rend les Digimodes à bande étroite particulièrement attractifs pour l'exploitation radioamateur.

---

La télévision à balayage lent (SSTV) désigne la transmission d'images fixes à l'aide de données d'image numérisées. Les images sont transmises ligne par ligne, ce qui permet une vitesse de transmission relativement faible. Il existe différents procédés SSTV qui se distinguent, entre autres, par leur résolution, leur profondeur de couleur et leur durée de transmission. Un avantage essentiel de la SSTV est la faible bande passante nécessaire : elle est typiquement inférieure à $\qty{3}{\kilo\hertz}$ et correspond ainsi environ à la bande passante d'un signal vocal SSB. Cela permet d'utiliser la SSTV également dans les bandes d'ondes courtes et elle est particulièrement adaptée aux transmissions d'images mondiales dans le domaine du radioamateur. La figure [ref:e_digimode_ssb_sstv] montre une image SSTV typique.

En revanche, la télévision amateur (ATV) permet de transmettre des images animées - donc de la télévision réelle. En raison de la quantité d'informations nettement plus élevée, l'ATV nécessite une bande passante beaucoup plus grande, typiquement plusieurs mégahertz, souvent $\qty{6}{\mega\hertz}$ ou plus. C'est pourquoi l'ATV n'est pas réalisable dans les bandes d'ondes courtes et n'est utilisée qu'à des fréquences plus élevées, généralement à partir de la bande des $\qty{70}{\centi\meter}$ ou par exemple dans la gamme des $\unit{\giga\hertz}$ via QO-100. Là, des bandes de fréquences suffisamment larges sont disponibles pour fournir la bande passante nécessaire aux transmissions d'images animées.

[question:EE415]

<margin>
[photo:84:e_digimode_ssb_sstv:Confirmation d'une connexion SSTV à F1BIB de ON1GA avec le RST 575 et en plus l'image reçue à l'origine]
</margin>
