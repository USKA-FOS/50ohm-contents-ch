Contrairement à la transmission vocale, de nombreux modes de transmission numériques (digimodes) n’utilisent qu’une bande passante très faible. Alors que les signaux vocaux en SSB occupent généralement une largeur de bande d’environ $\qty{2,4}{\kilo\hertz}$, les digimodes se contentent de plages de fréquences bien plus étroites. Par exemple, le BPSK31 n’a besoin que d’environ $\qty{31,25}{\hertz}$ de bande passante, tandis que le FT8 utilise environ $\qty{50}{\hertz}$. Les signaux générés par les digimodes sont également modulés en SSB sur ondes courtes. La largeur de bande HF du signal émis correspond alors exactement à la largeur de bande BF du digimode.

[question:EE402]
[question:EE403]

Dans la largeur de bande de réception SSB habituelle d’environ $\qty{2,4}{\kilo\hertz}$, plusieurs de ces signaux de digimodes à bande étroite peuvent être reçus simultanément.

<margin>
[picture:718:e_digimode_ssb_empfang_mehrerer_digimodes:Diagramme en cascade de la réception de plusieurs signaux de digimodes dans la largeur de bande SSB de 2,4 kHz. Chaque colonne représente la transmission d’un signal différent]
</margin>

[question:EE404]

D’un point de vue purement théorique, il est possible d’intégrer jusqu’à 48 signaux FT8 ($\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$) ou même jusqu’à 76 signaux BPSK31 ($\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$) dans une largeur de bande SSB de $\qty{2,4}{\kilo\hertz}$. Sur un ordinateur, il est ensuite possible de sélectionner un signal de digimode spécifique ou, selon le logiciel, de décoder simultanément un grand nombre de ces signaux. C’est précisément cette efficacité spectrale élevée qui rend les digimodes à bande étroite particulièrement attrayants pour le radioamateurisme.

---

La télévision à balayage lent (SSTV) désigne la transmission d’images fixes à l’aide de données d’image numérisées. Les images sont transmises ligne par ligne, ce qui permet une vitesse de transmission relativement faible. Il existe différents procédés SSTV qui se distinguent notamment par leur résolution, leur profondeur de couleur et leur durée de transmission. Un avantage majeur de la SSTV est sa faible largeur de bande requise : elle est généralement inférieure à $\qty{3}{\kilo\hertz}$ et correspond ainsi à peu près à la largeur de bande d’un signal vocal en SSB. Cela permet d’utiliser la SSTV sur les bandes HF et de réaliser des transmissions d’images à l’échelle mondiale dans le cadre du radioamateurisme. La figure [ref:e_digimode_ssb_sstv] montre une image SSTV typique.

À l’inverse, la télévision amateur (ATV) transmet des images animées, c’est-à-dire de la télévision proprement dite. En raison de la quantité d’informations bien plus importante, l’ATV nécessite une largeur de bande bien plus grande, typiquement de plusieurs mégahertz, souvent $\qty{6}{\mega\hertz}$ ou plus. C’est pourquoi l’ATV n’est pas réalisable sur les bandes HF et n’est utilisé qu’à des fréquences plus élevées, généralement à partir de la bande de $\qty{70}{\centi\meter}$ ou, par exemple, dans la gamme des $\unit{\giga\hertz}$ via QO-100. C’est là que des plages de fréquences suffisamment larges sont disponibles pour fournir la largeur de bande nécessaire aux transmissions d’images animées.

[question:EE415]

<margin>
[photo:84:e_digimode_ssb_sstv:Confirmation d’une liaison SSTV avec F1BIB depuis ON1GA avec un RST 575 et en plus l’image reçue à l’origine]
</margin>