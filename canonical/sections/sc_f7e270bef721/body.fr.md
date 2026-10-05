Dans la section [sec:dummy_load_1], nous avons déjà fait connaissance avec la *charge fictive*. Une charge fictive est une résistance de charge qui convertit la puissance HF délivrée par l'émetteur en chaleur. Elle permet, par exemple, de tester un émetteur ou de déterminer sa puissance de sortie sans qu'un signal ne soit rayonné par une antenne. Dans cette section, nous examinons maintenant plus en détail comment une telle charge fictive peut être construite.

Une charge fictive pour la gamme HF est souvent composée de plusieurs résistances individuelles. Cela permet de répartir la puissance dissipée sur plusieurs composants et d'atteindre une capacité de charge totale correspondante élevée. Les résistances peuvent être connectées en parallèle, en série ou dans une combinaison de connexions en série et en parallèle. Si des résistances identiques avec la même capacité de charge sont utilisées et que le circuit est construit symétriquement, la puissance dissipée se répartit uniformément sur les résistances individuelles. Le nombre requis et la connexion des résistances peuvent être déterminés à l'aide des règles connues pour les connexions en série et en parallèle. Pour une charge fictive HF, il est également important que le circuit corresponde, même à haute fréquence, autant que possible à une résistance purement ohmique de $\qty{50}{\ohm}$. C'est pourquoi des résistances appropriées, aussi peu inductives que possible, sont utilisées et les conducteurs de connexion sont réalisés aussi courts que possible.

La figure [ref:dummy_load_aufbau1] montre une charge fictive finie de 50ohm.de. Ici, par exemple, $\num{20}$ résistances de $\qty{1}{\kilo\ohm}$ chacune sont connectées en parallèle. Pour $n$ résistances identiques connectées en parallèle, on a :

$R_\mathrm{ges} = \frac{R}{n}$

Ainsi, on obtient :

$R_\mathrm{ges} = \frac{\qty{1}{\kilo\ohm}}{20} = \qty{50}{\ohm}$

<warning>
La puissance dissipée maximale possible de la charge fictive entière est approximativement égale à la somme des capacités de charge de toutes les résistances, à condition que la puissance soit répartie uniformément entre elles. Comme la charge fictive 50ohm.de ne dispose pas de refroidissement et n'est pas blindée, elle ne doit être utilisée que pour les émetteurs QRP avec une faible puissance de sortie. Pour des puissances plus élevées, une charge fictive avec refroidissement et blindage est nécessaire, qui convient également pour un fonctionnement continu !
</warning>

La charge fictive 50ohm.de possède en plus un redresseur de valeur de crête composé d'une diode et d'un condensateur. Cela permet de générer une tension continue à partir de la tension HF appliquée, qui peut par exemple être mesurée avec un multimètre. En tenant compte du diviseur de tension et de la tension directe de la diode, la puissance de sortie HF de l'émetteur peut être déterminée à partir de celle-ci.

[question:AI602]

<margin>
[photo:340:dummy_load_aufbau1:La charge fictive 50ohm.de finie]
[photo:341:dummy_load_aufbau2:Structure de la charge fictive 50ohm.de]

*Affichage :* Tu veux aussi construire une super charge fictive QRP 50ohm.de ? Alors tu peux la commander en kit chez [DARC-Verlag](https://darcverlag.de/50Ohm-Dummy-Load-DIY-Kit-Bausatz).
</margin>

% ARK: Cette référence au DARC a été délibérément laissée.
% Cela devrait éventuellement être discuté au sein de l'équipe ou de la direction du projet.

Dans la question d'examen suivante, la charge fictive est constituée d'une combinaison de connexions en série et en parallèle. Si dans chaque branche $N_\mathrm{S}$ résistances identiques sont connectées en série et ensuite $N_\mathrm{P}$ de ces branches sont connectées en parallèle, la résistance totale est :

$R_\mathrm{ges} = \frac{N_\mathrm{S}}{N_\mathrm{P}} \cdot R$

Le nombre total de résistances utilisées est alors :

$n = N_\mathrm{S} \cdot N_\mathrm{P}$

Si toutes les résistances sont également chargées, leurs puissances dissipées admissibles s'additionnent. Cela permet de construire une charge fictive avec la résistance souhaitée et simultanément une capacité de charge élevée.

[question:AI601]

Une autre possibilité pour déterminer la puissance de sortie HF consiste à équiper la charge fictive d'une prise intermédiaire de son réseau de résistances. Si cette prise intermédiaire se trouve par exemple près de la connexion de masse, seule une partie de la tension HF totale y est présente.

Les résistances forment alors un diviseur de tension. Si son rapport de division est connu, la tension totale sur la charge fictive peut être recalculée à partir de la tension HF mesurée à la prise intermédiaire. La tension partielle peut par exemple être mesurée avec une sonde HF et un multimètre numérique. À partir de la tension totale ainsi déterminée, la puissance HF peut ensuite être calculée.

[question:AI603]
