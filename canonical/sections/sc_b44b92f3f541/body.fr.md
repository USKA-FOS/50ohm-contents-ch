Examinons d'abord comment est construit un récepteur. Dans la figure [ref:aufbau_empfaenger_blockdiagramm], nous ne descendons pas au niveau des composants individuels pour simplifier, mais nous considérons des blocs qui ont une fonction particulière. Cette représentation s'appelle un diagramme en blocs. Elle sert en électricité à représenter des appareils complexes dans une vue d'ensemble simplifiée. Pour ce faire, on omet les détails qui ne sont pas nécessaires à la compréhension de l'ensemble de l'appareil.

<margin>
[picture:736:aufbau_empfaenger_blockdiagramm:diagramme en blocs d'un récepteur simple]
</margin>

<indepth>
Le récepteur représenté ici est appelé récepteur direct. Le nom vient du fait que le signal capté par l'antenne n'est pas modifié en fréquence jusqu'au démodulateur.
</indepth>

---

Examinons les différents blocs du récepteur de gauche à droite en détail:

1. Antenne: L'antenne capte une multitude d'ondes radio et les transmet sous forme d'oscillations électriques.
2. Filtre passe-bande: Pour filtrer le signal souhaité, suit un filtre passe-bande. Celui-ci ne laisse passer que la bande de fréquences souhaitée et bloque toutes les autres fréquences indésirables.
3. Amplificateur HF: Ensuite, suit un amplificateur qui amplifie le signal filtré. Il s'agit ici d'un amplificateur haute fréquence (amplificateur HF), car le signal présente une fréquence élevée, par exemple $\qty{144,3}{\mega\hertz}$.
4. Démodulateur: Le signal amplifié est ensuite traité par le démodulateur. La démodulation est l'inverse de la modulation. Alors que lors de la modulation, un signal (par exemple un signal vocal) est modulé sur une porteuse haute fréquence, lors de la démodulation, l'inverse se produit: le signal d'origine est récupéré à partir de la porteuse haute fréquence modulée. Nous avons alors par exemple à nouveau le signal vocal qui a été parlé dans le microphone à l'émetteur. On parle aussi de signal basse fréquence, en abrégé signal BF, car il présente des fréquences relativement basses, par exemple des fréquences inférieures à $\qty{20}{\kilo\hertz}$ pour un signal vocal.
5. Amplificateur BF: Le signal démodulé est ensuite amplifié. Il s'agit ici d'un amplificateur basse fréquence (amplificateur BF) pour amplifier le signal pour le haut-parleur. Le symbole de l'amplificateur BF est le même que celui de l'amplificateur haute fréquence.
6. Haut-parleur: Le signal est maintenant converti par le haut-parleur d'une oscillation électrique en une onde sonore et ainsi rendu à nouveau audible.

<indepth>
Dans le *filtre passe-bande*, les deux ondes barrées symbolisent que les fréquences au-dessus et en dessous de la bande de fréquences souhaitée sont bloquées. L'onde centrale indique que la bande de fréquences souhaitée est laissée passer.
</indepth>

<indepth>
Le *démodulateur* est représenté par le symbole de circuit de la diode, qui est le composant le plus important de nombreux démodulateurs. Le fonctionnement d'une diode sera expliqué plus tard dans le chapitre "Composants et circuits".
</indepth>

[question:NF201]

Selon la manière dont un récepteur est construit, il a différentes propriétés. Une propriété importante est la sensibilité. C'est ainsi que l'on désigne la capacité du récepteur à recevoir des signaux faibles. Plus un récepteur est sensible, plus il peut recevoir des signaux faibles.

[question:NF303]
