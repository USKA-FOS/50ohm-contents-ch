Dans la classe E, nous avons appris qu'un oscilloscope affiche l'évolution temporelle des tensions. Nous pouvons donc utiliser un oscilloscope pour vérifier les formes de signal. 

[question:AI301]

<margin>
[picture:1005:a_impulsbreite:Détermination de la durée d'impulsion d'un signal rectangulaire non idéal]
</margin>

---

Outre les tensions alternatives sinusoïdales, les tensions rectangulaires sont également présentes en raison de la technologie numérique. Cependant, une forme de tension strictement rectangulaire n'existe pas. Les fronts sont toujours légèrement inclinés ou déformés. Le temps entre la montée et la descente d'un rectangle, appelé largeur d'impulsion ou durée d'impulsion, est donc toujours mesuré à mi-hauteur, c'est-à-dire à 50 % de la tension. Cela garantit que tous obtiennent le même résultat de mesure pour le même signal.

<indepth>
La raison de ces déformations réside dans les capacités et inductances inévitables des câbles et composants, qui agissent comme des filtres et atténuent les composantes haute fréquence d'un signal rectangulaire.
</indepth>

[question:AI303]
[question:EI303]


Les oscilloscopes peuvent afficher des signaux de fréquences et de formes très variées. Pour que ces signaux apparaissent stables à l'écran, les oscilloscopes disposent d'un dispositif de déclenchement (en anglais *trigger*). L'appareil surveille en continu le signal d'entrée et commence l'enregistrement précisément lorsqu'une condition prédéfinie est remplie – par exemple, lorsque le signal dépasse une tension spécifique, appelée tension de déclenchement. À partir de ce moment, l'échantillonnage et l'enregistrement des valeurs de mesure commencent, puis sont affichés sous forme de courbe à l'écran.


Grâce à cette méthode, chaque affichage commence toujours au même état du signal, de sorte que les signaux périodiques comme les oscillations sinusoïdales ou les impulsions rectangulaires semblent figés et clairement reconnaissables. Les oscilloscopes numériques peuvent également afficher des images uniques, c'est-à-dire « geler » l'écran. Cela facilite l'analyse des signaux non périodiques. La touche dédiée est généralement étiquetée *SINGLE*. Il est également possible de superposer plusieurs mesures pour visualiser, par exemple, les variations temporelles d'un signal (appelées *jitter* en anglais).

[question:AI302]

%<indepth>
%La figure [ref:a_oszilloskop_einzelbild] montre une image unique d'un enregistrement musical issu de la figure [ref:a_oszilloskop_ueberlagerung]. Elle a été photographiée à partir d'un oscilloscope plus ancien, principalement analogique, doté d'une petite mémoire numérique.
%[photo:222:a_oszilloskop_einzelbild:Image unique d'un enregistrement musical]
%</indepth>

Tous les câbles ne conviennent pas aux signaux haute fréquence – cela s'applique également à la connexion entre l'objet de mesure et l'oscilloscope. Pour cela, on utilise généralement des sondes. Elles établissent la connexion et garantissent que le signal est transmis avec le moins de distorsion possible, sans trop charger le circuit. Pour ce faire, elles réduisent la tension du signal (par exemple dans un rapport 10:1), adaptent la résistance et la capacité, et intègrent souvent une compensation pour les hautes fréquences.

Une sonde se compose d'un boîtier en forme de stylo, comparable à un stylo à bille. À son extrémité, différents crochets ou pointes peuvent être fixés pour contacter le point de mesure. La connexion à la masse s'effectue via une pince crocodile (voir figure [ref:a_oszilloskop_messung]). La figure [ref:a_oszilloskop_tastkoepfe] montre trois exemples de telles sondes. Les modèles haut de gamme sont relativement coûteux, car ils doivent offrir une large bande passante, une distorsion minimale du signal et une mécanique précise.

<margin>
[photo:224:a_oszilloskop_messung:Mesure avec une sonde. Entre les diodes D1 et D2, on distingue la pointe de test, et plus à gauche, la pince crocodile pour la connexion à la masse.]
</margin>

<margin>
[photo:223:a_oszilloskop_tastkoepfe:Sondes avec différentes pointes de test. Les pinces crocodiles ont été retirées pour cette photo.]
</margin>

Les sondes les plus simples relient directement la pointe de test à l'entrée de mesure. On parle de sondes 1:1, car la tension appliquée à la pointe est transmise sans modification à l'oscilloscope. Les sondes pour hautes fréquences sont plus complexes. Elles divisent la tension d'entrée par une valeur plus petite, souvent un dixième. Si l'on mesure une tension de 10 volts avec une sonde 10:1, l'écran affichera 1 volt.

<indepth>
Sur certains oscilloscopes, il est possible de configurer le rapport de division de la sonde. Dans ce cas, la tension réelle est affichée à l'écran. Les sondes passives 10:1 contiennent notamment une résistance de $\qty{9}{\mega\ohm}$ dans le trajet du signal. Les oscilloscopes ont généralement une résistance interne de $\qty{1}{\mega\ohm}$. Cela forme un diviseur de tension 10:1. De plus, une petite capacité variable est présente dans la sonde ou la fiche. Elle sert à adapter la capacité de la sonde et du câble à l'entrée de mesure et est réglée de manière à ce qu'un signal rectangulaire apparaisse aussi peu déformé que possible à l'écran. Outre les sondes passives décrites ici, il existe plusieurs autres variantes. Il existe par exemple des sondes avec câble coaxial adapté à $\qty{50}{\ohm}$. Elles sont particulièrement adaptées aux très hautes fréquences, mais présentent une résistance interne relativement faible. Les versions actives résolvent ce problème en amplifiant directement le signal dans la sonde.
</indepth>
