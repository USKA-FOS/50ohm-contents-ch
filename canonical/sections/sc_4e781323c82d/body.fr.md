Lors de la conversion analogique-numérique (A/N) et numérique-analogique (N/A), le traitement des signaux analogiques et numériques est interconnecté. Des filtres analogiques sont nécessaires avant le convertisseur A/N ainsi qu'après le convertisseur N/A. L'illustration [ref:a_adc_dac_filter] montre l'ensemble de la chaîne de signal. Du côté de l'entrée, un *filtre anti-repliement* est placé avant le convertisseur A/N. Il limite la bande de fréquences du signal d'entrée analogique avant son échantillonnage. Après le traitement numérique du signal, le convertisseur N/A génère à nouveau un signal analogique. Un *filtre de reconstruction* en aval élimine alors les composantes haute fréquence indésirables. Nous expliquerons pourquoi ces deux filtres sont nécessaires dans la section suivante.

<margin>
[picture:1131:a_adc_dac_filter:Conversion A/N et N/A avec filtre anti-repliement et filtre de reconstruction]
</margin>

---

D'après la leçon sur le théorème d'échantillonnage, nous savons qu'un signal doit être échantillonné avec une fréquence d'échantillonnage suffisamment élevée. Pour un signal dont la fréquence maximale à capturer est $f_\mathrm{max}$, la fréquence d'échantillonnage doit être supérieure à $2\cdot f_\mathrm{max}$.

Cependant, une antenne reçoit généralement de nombreux signaux différents, y compris ceux dont les fréquences dépassent la bande de fréquences que nous souhaitons traiter. Si de telles composantes fréquentielles atteignent le convertisseur A/N alors que sa fréquence d'échantillonnage est insuffisante pour ces fréquences, elles peuvent apparaître dans le signal numérique sous forme d'autres fréquences, inexistantes en réalité. Ces fréquences sont appelées *replis* (ou *aliasing*).

Pour éviter cela, un *filtre anti-repliement* est placé avant l'entrée du convertisseur A/N. Selon l'application, il peut s'agir par exemple d'un passe-bas ou d'un filtre passe-bande. Un filtre passe-bande pourrait être utilisé, par exemple, pour la voix. Le filtre doit suffisamment atténuer les composantes indésirables qui pourraient provoquer un repliement lors de l'échantillonnage. En particulier, les composantes fréquentielles supérieures à la moitié de la fréquence d'échantillonnage ne doivent pas atteindre le convertisseur A/N sans atténuation.

[question:AF622]
[question:AF623]

<indepth>
Un exemple concret de *repliement* se rencontre également dans la vie quotidienne avec les images numériques. Si l'on photographie avec un appareil des structures très fines et régulièrement répétées, par exemple une grille serrée, un tissu à fines rayures ou une moustiquaire, des motifs plus grands, inexistants dans l'original, peuvent apparaître sur l'image. Ces motifs sont appelés *effets de moiré*.

La cause est similaire à celle de l'échantillonnage d'un signal électrique. Un capteur d'image ne peut pas capturer une image en un nombre arbitrairement élevé de points, mais possède un nombre fini de pixels. Si une structure est plus fine que la résolution spatiale du capteur, elle n'est plus échantillonnée de manière univoque. Une structure fine peut ainsi donner l'impression d'une autre structure plus grossière qui n'existait pas à l'origine.

Avec le convertisseur A/N, le même principe s'applique sur l'axe temporel : si une fréquence de signal trop élevée est échantillonnée avec une fréquence d'échantillonnage trop basse, une fréquence plus basse, inexistante à l'origine, apparaît dans le signal numérisé.

Un effet de moiré peut donc être considéré comme un exemple visible de la manière dont une échantillonnage insuffisant crée de nouvelles structures apparentes.

% TODO: Bild besorgen
%<margin>
%[picture:XXXX:a_moire:Effet de moiré comme exemple de repliement spatial]
%</margin>
</indepth>

---

Le convertisseur A/N nécessite également un générateur d'horloge, aussi appelé générateur d'horloge d'échantillonnage. Celui-ci détermine les instants auxquels le signal d'entrée est échantillonné et fixe ainsi la fréquence d'échantillonnage. La fréquence d'échantillonnage peut être réglée de manière fixe ou contrôlée, par exemple, par un microcontrôleur.

<margin>
[picture:1132:a_anit_alias:Filtre anti-repliement, convertisseur A/N et générateur d'horloge]
</margin>

[question:AF620]

---

De l'autre côté du traitement numérique du signal, le convertisseur N/A effectue l'opération inverse. Il convertit les échantillons numériques en valeurs de tension analogiques. Comme les valeurs ne sont émises qu'à intervalles de temps discrets, le signal de sortie du convertisseur N/A ne présente pas immédiatement une évolution idéale et lisse.

En raison de l'émission discrète dans le temps, des composantes haute fréquence indésirables (par exemple, dans l'illustration [ref:a_adc_4bit], les transitions rapides entre les valeurs discrètes du signal de sortie contiennent des composantes haute fréquence) apparaissent en plus du signal utile souhaité. Pour les supprimer, un *filtre de reconstruction* est placé après le convertisseur N/A. Selon l'application, on peut utiliser par exemple un passe-bas ou un filtre passe-bande.

Le filtre de reconstruction laisse passer la bande de fréquences utile souhaitée et atténue les composantes haute fréquence indésirables du convertisseur N/A. Cela permet d'obtenir à la sortie un signal analogique aussi propre que possible (cf. illustration [ref:a_adc_12bit], le filtre de reconstruction lisse le signal).

[question:AF624]
[question:AF625]

<margin>
[picture:300:a_adc_4bit:Signal avant le filtre de reconstruction]
[picture:299:a_adc_12bit:Signal après le filtre de reconstruction]
</margin>