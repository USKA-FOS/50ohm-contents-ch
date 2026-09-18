Dans la classe E, nous avons déjà fait connaissance avec la *charge fictive* (dummy load). Une charge fictive est une résistance de charge qui convertit en chaleur la puissance HF émise par l'émetteur. Elle permet par exemple de tester un émetteur ou de déterminer sa puissance de sortie sans émettre de signal via une antenne. Dans la classe A, nous examinons maintenant plus en détail comment construire une telle charge fictive.

Une charge fictive pour la gamme HF est souvent composée de plusieurs résistances individuelles. Cela permet de répartir la puissance dissipée sur plusieurs composants et d'atteindre une capacité de charge globale plus élevée. Les résistances peuvent être connectées en parallèle, en série ou selon une combinaison de montages série et parallèle. Si l'on utilise des résistances identiques de même capacité de charge et que le circuit est symétrique, la puissance dissipée se répartit uniformément entre les résistances. Le nombre et le câblage des résistances nécessaires peuvent être déterminés à l'aide des règles connues pour les montages série et parallèle. Pour une charge fictive HF, il est également important que le circuit se comporte, même à haute fréquence, comme une résistance pure de $\qty{50}{\ohm}$. C'est pourquoi on utilise des résistances aussi peu inductives que possible et que les liaisons sont aussi courtes que possible.

La figure [ref:dummy_load_aufbau1] montre une charge fictive de 50 ohms finie, disponible sur 50ohm.de. Dans cet exemple, $\num{20}$ résistances de $\qty{1}{\kilo\ohm}$ chacune sont connectées en parallèle. Pour $n$ résistances identiques connectées en parallèle, on a :


$R_\mathrm{ges} = \frac{R}{n}$

Cela donne :

$R_\mathrm{ges} = \frac{\qty{1}{\kilo\ohm}}{20} = \qty{50}{\ohm}$


<warning>
La puissance dissipée maximale possible de l'ensemble de la charge fictive résulte approximativement de la somme des capacités de charge de toutes les résistances, à condition que la puissance se répartisse uniformément entre elles. Comme la charge fictive de 50ohm.de ne dispose ni de refroidissement ni de blindage, elle ne doit être utilisée que pour des émetteurs QRP de faible puissance de sortie. Pour des puissances plus élevées, une charge fictive avec refroidissement et blindage, adaptée au fonctionnement continu, est nécessaire !
</warning>

La charge fictive 50ohm.de possède en outre un redresseur de valeur de crête composé d'une diode et d'un condensateur. Cela permet de générer, à partir de la tension HF appliquée, une tension continue qui peut être mesurée par exemple avec un multimètre. En tenant compte du diviseur de tension et de la tension directe de la diode, on peut en déduire la puissance HF de sortie de l'émetteur.

[question:AI602]


<margin>
[photo:340:dummy_load_aufbau1:La charge fictive 50ohm.de finie]
[photo:341:dummy_load_aufbau2:Structure de la charge fictive 50ohm.de]


*Affichage* : Vous souhaitez également construire une charge fictive QRP 50ohm.de ? Vous pouvez alors vous la procurer en kit chez [DARC-Verlag](https://darcverlag.de/50Ohm-Dummy-Load-DIY-Kit-Bausatz).
</margin>

Dans la question d'examen suivante, la charge fictive est composée d'une combinaison de montages série et parallèle. Si l'on connecte $N_\mathrm{S}$ résistances identiques en série dans chaque branche, puis $N_\mathrm{P}$ de ces branches en parallèle, la résistance totale est donnée par :


$R_\mathrm{ges} = \frac{N_\mathrm{S}}{N_\mathrm{P}} \cdot R$


Le nombre total de résistances utilisées est alors :

$n = N_\mathrm{S} \cdot N_\mathrm{P}$


Si toutes les résistances sont chargées de manière égale, leurs puissances dissipées admissibles s'additionnent. Il est ainsi possible de construire une charge fictive avec la résistance souhaitée et une capacité de charge élevée.

[question:AI601]


Une autre méthode pour déterminer la puissance HF de sortie consiste à équiper la charge fictive d'une prise intermédiaire sur son réseau de résistances. Si cette prise est par exemple proche de la masse, seule une partie de la tension HF totale y est présente.

Les résistances forment alors un diviseur de tension. Si son rapport de division est connu, on peut, à partir de la tension HF mesurée à la prise intermédiaire, remonter à la tension totale aux bornes de la charge fictive. La tension partielle peut par exemple être mesurée avec une sonde HF et un multimètre numérique. Une fois la tension totale déterminée, on peut calculer la puissance HF.