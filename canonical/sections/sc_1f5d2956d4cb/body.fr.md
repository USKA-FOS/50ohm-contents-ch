Dans la section [sec:oszilloskop_1], nous avons appris qu'un oscilloscope représente l'évolution temporelle des tensions. Nous pouvons donc vérifier les formes d'onde des signaux avec un oscilloscope.

[question:AI301]

<margin>
[picture:1005:a_impulsbreite:Détermination de la largeur d'impulsion d'un signal rectangulaire non idéal]
</margin>

---

Outre les tensions alternatives sinusoïdales, les tensions rectangulaires apparaissent également en raison de la technologie numérique. Cependant, une évolution de tension parfaitement rectangulaire n'est pas possible. Les bords sont toujours un peu inclinés ou déformés. Le temps entre la montée et la descente d'un rectangle, appelé largeur d'impulsion ou durée d'impulsion, est donc toujours mesuré à mi-hauteur, c'est-à-dire à 50% de la tension. Cela garantit que pour le même signal, tout le monde obtient le même résultat de mesure.

<indepth>
La raison de ces déformations réside dans les capacités et inductances inévitables dans les câbles et les composants, qui agissent comme des filtres et atténuent les composantes haute fréquence d'un signal rectangulaire.
</indepth>

[question:AI303]
[question:EI303]

% TODO La question EI303 n'existe pas. Veuillez consulter l'issue #52.

Les oscilloscopes peuvent représenter des signaux avec des fréquences et des formes d'onde très variées. Pour que ces signaux apparaissent de manière stable sur l'écran, les oscilloscopes possèdent un dispositif de déclenchement (anglais : trigger = "déclencher"). L'appareil surveille continuellement le signal d'entrée et démarre l'acquisition exactement lorsqu'une condition préalablement définie est remplie – par exemple, lorsque le signal dépasse une certaine tension, appelée tension de déclenchement. À partir de ce moment, l'échantillonnage et le stockage des valeurs mesurées commencent, qui sont ensuite affichées sous forme de courbe sur l'écran.

Grâce à cette procédure, chaque affichage commence toujours au même état du signal, de sorte que les signaux périodiques comme les oscillations sinusoïdales ou les impulsions rectangulaires semblent figés et clairement reconnaissables. Les oscilloscopes numériques peuvent en outre afficher des images uniques, c'est-à-dire "figer" l'écran. Cela facilite l'analyse des signaux non périodiques. La touche prévue à cet effet est généralement étiquetée SINGLE. De plus, plusieurs mesures peuvent être superposées pour rendre visibles, par exemple, les fluctuations temporelles d'un signal (anglais : jitter).

[question:AI302]

%<indepth>
%La figure [ref:a_oszilloskop_einzelbild] montre une image unique de l'enregistrement musical de la figure [ref:a_oszilloskop_ueberlagerung]. Elle a été photographiée sur un ancien oscilloscope fonctionnant principalement de manière analogique et possédant en plus une petite mémoire numérique.
%[photo:222:a_oszilloskop_einzelbild:Image unique d'un enregistrement musical]
%</indepth>

Tous les câbles ne conviennent pas aux signaux haute fréquence – cela vaut également pour la connexion entre l'objet de mesure et l'oscilloscope. Pour cela, on utilise généralement des sondes. Elles établissent la connexion et veillent à ce que le signal soit transmis aussi fidèlement que possible, sans trop charger le circuit. Pour ce faire, elles réduisent la tension de signal (par exemple dans un rapport 10:1), adaptent la résistance et la capacité et contiennent souvent une compensation pour les hautes fréquences.

Une sonde se compose d'un boîtier en forme de poignée, comparable à un stylo à bille. À son extrémité, différents crochets ou aiguilles peuvent être fixés pour contacter le point de mesure. La connexion de masse se fait via une pince crocodile (voir figure [ref:a_oszilloskop_messung]). La figure [ref:a_oszilloskop_tastkoepfe] montre trois exemples de telles sondes. Les modèles haut de gamme sont donc chers, car ils doivent offrir une large bande passante, une distorsion minimale du signal et une mécanique précise.

<margin>
[photo:224:a_oszilloskop_messung:Mesure avec une sonde. La pointe de test est visible entre les diodes D1 et D2 et plus à gauche la pince crocodile pour la connexion de masse.]
</margin>

<margin>
[photo:223:a_oszilloskop_tastkoepfe:Sondes avec différentes pointes de test. Les pinces crocodiles ont été retirées pour cette prise de vue.]
</margin>

Les sondes les plus simples connectent directement la pointe de test à l'entrée de mesure. On parle de sondes 1:1, car la tension présente à la pointe arrive inchangée à l'oscilloscope. Les sondes pour hautes fréquences sont construites de manière plus élaborée. Elles divisent la tension d'entrée en une valeur plus petite, souvent un dixième. Lorsqu'on mesure une tension de 10 volts avec une telle sonde 10:1, 1 volt est affiché à l'écran.

<indepth>
Sur certains oscilloscopes, on peut régler le rapport de division de la sonde. La tension réelle est alors affichée à l'écran. Les sondes passives 10:1 contiennent entre autres une résistance de $\qty{9}{\mega\ohm}$ qui se trouve dans le chemin du signal. Les oscilloscopes ont généralement une résistance interne de $\qty{1}{\mega\ohm}$. Cela forme un diviseur de tension 10:1. De plus, un petit condensateur variable est présent dans la sonde ou dans le connecteur. Il sert à adapter la capacité de la sonde et du câble à l'entrée de mesure et est réglé de manière à ce qu'un signal rectangulaire apparaisse aussi fidèlement que possible sur l'écran. Outre les sondes passives décrites ici, il existe plusieurs autres variantes. Il y a par exemple des sondes avec un câble coaxial adapté de $\qty{50}{\ohm}$. Elles sont particulièrement adaptées aux très hautes fréquences, mais n'ont qu'une résistance interne relativement faible. Les versions actives résolvent ce problème en amplifiant le signal directement dans la sonde.
</indepth>
