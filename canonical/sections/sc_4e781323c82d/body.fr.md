Dans la conversion A/N et N/A, le traitement analogique et numérique du signal sont interconnectés. Des filtres analogiques sont nécessaires à la fois avant le convertisseur analogique et après le convertisseur numérique. La figure [ref:a_adc_dac_filter] montre la chaîne de signal complète. Du côté de l'entrée, un *filtre anti-repliement* est placé avant le convertisseur analogique. Il limite la bande de fréquences du signal d'entrée analogique avant son échantillonnage. Après le traitement numérique du signal, le convertisseur numérique génère à nouveau un signal analogique. Un *filtre de reconstruction* en aval élimine les composantes de signal haute fréquence indésirables. Nous examinerons pourquoi ces deux filtres sont nécessaires dans la section suivante.

<margin>
[picture:1131:a_adc_dac_filter:Conversion A/N et N/A avec filtre anti-repliement et filtre de reconstruction]
</margin>

---

De la leçon sur le théorème d'échantillonnage dans la section [sec:abtasttheorem], nous savons qu'un signal doit être échantillonné avec une fréquence d'échantillonnage suffisamment élevée. Pour un signal avec la fréquence maximale à capturer $f_\mathrm{max}$, la fréquence d'échantillonnage doit être supérieure à $2\cdot f_\mathrm{max}$.

Cependant, via une antenne, nous recevons généralement de nombreux signaux différents – y compris ceux avec des fréquences au-dessus de la bande de fréquences que nous souhaitons réellement traiter. Si ces composantes de signal atteignent le convertisseur analogique alors que sa fréquence d'échantillonnage n'est pas suffisante pour ces fréquences, elles peuvent apparaître dans le signal numérique comme d'autres fréquences, en réalité non présentes. Celles-ci sont appelées *repliements*.

Pour éviter cela, un *filtre anti-repliement* est utilisé avant l'entrée du convertisseur analogique. Selon l'application, il s'agit par exemple d'un filtre passe-bas ou passe-bande. Un filtre passe-bande pourrait par exemple être utilisé pour la parole. Le filtre doit suffisamment atténuer les composantes de signal indésirables qui pourraient provoquer un repliement lors de l'échantillonnage. En particulier, les composantes de fréquence au-dessus de la moitié de la fréquence d'échantillonnage ne doivent pas parvenir librement au convertisseur analogique.

[question:AF622]
[question:AF623]

<indepth>
Un exemple concret de *repliement* nous rencontre également dans la vie quotidienne avec les images numériques. Lorsqu'on photographie avec un appareil photo des structures très fines et régulièrement répétitives, par exemple une grille à mailles serrées, un tissu à fines rayures ou une moustiquaire, des motifs plus grands, absents de l'original, peuvent soudainement apparaître dans l'image. Ceux-ci sont appelés *motifs de moiré*.

La cause est similaire à l'échantillonnage d'un signal électrique. Un capteur d'appareil photo ne peut pas capturer une image à un nombre arbitraire de points, mais possède seulement un nombre fini de pixels. Si une structure est plus fine que la résolution spatiale du capteur, elle n'est plus échantillonnée de manière unique. À partir de la structure fine réellement présente, une autre structure, plus grossière, peut ainsi sembler apparaître.

Avec le convertisseur analogique, le même principe se produit sur l'axe temporel : si une fréquence de signal trop élevée est échantillonnée avec une fréquence d'échantillonnage trop basse, une autre fréquence, plus basse, qui n'était pas présente à l'origine, apparaît dans le signal numérisé.

Un motif de moiré peut donc être considéré comme un exemple visible de la façon dont, par un échantillonnage insuffisant, de nouvelles structures apparentes se forment.

% TODO: Image à obtenir
%<margin>
%[picture:XXXX:a_moire:Motif de moiré comme exemple de repliement spatial]
%</margin>
</indepth>

---

Le convertisseur analogique nécessite également un générateur d'horloge, également appelé générateur d'horloge d'échantillonnage. Celui-ci détermine aux quels instants le signal d'entrée est échantillonné et définit ainsi la fréquence d'échantillonnage. La fréquence d'échantillonnage peut être fixe ou être contrôlée, par exemple, par un microcontrôleur.

<margin>
[picture:1132:a_anit_alias:Filtre anti-repliement, convertisseur analogique et générateur d'horloge]
</margin>

[question:AF620]

---

De l'autre côté du traitement numérique du signal, le convertisseur numérique effectue l'opération inverse. Il reconvertit les échantillons numériques en valeurs de tension analogiques. Comme les valeurs individuelles ne sont émises qu'à des intervalles de temps fixes, il ne se forme pas initialement une évolution de signal idéalement lisse à la sortie du convertisseur numérique.

En raison de la sortie temporellement discrète, des composantes de signal haute fréquence indésirables apparaissent en plus du signal utile souhaité (par exemple dans la figure [ref:a_adc_4bit], les transitions rapides entre les valeurs discrètes du signal de sortie contiennent les composantes haute fréquence). Pour les atténuer, un *filtre de reconstruction* est utilisé après le convertisseur numérique. Ici aussi, selon l'application, un filtre passe-bas ou passe-bande peut par exemple être utilisé.

Le filtre de reconstruction laisse passer la bande de fréquences utile souhaitée et atténue les composantes de signal haute fréquence indésirables du convertisseur numérique. Il en résulte à la sortie un signal analogique aussi propre que possible (cf. figure [ref:a_adc_12bit], le filtre de reconstruction lisse le signal).

[question:AF624]
[question:AF625]

<margin>
[picture:300:a_adc_4bit:Signal avant le filtre de reconstruction]
[picture:299:a_adc_12bit:Signal après le filtre de reconstruction]
</margin>
