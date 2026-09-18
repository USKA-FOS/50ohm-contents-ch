Commençons par examiner la structure d'un récepteur. Dans l'illustration [ref:aufbau_empfaenger_blockdiagramm], nous simplifions volontairement l'analyse en ne nous intéressant pas aux composants individuels, mais en considérant des blocs ayant une fonction spécifique. Cette représentation est appelée *diagramme en blocs*. Elle sert en électrotechnique à présenter des appareils complexes sous forme de vue d'ensemble simplifiée. Pour cela, on omet les détails non nécessaires à la compréhension de l'appareil dans son ensemble.

<margin>
[picture:736:aufbau_empfaenger_blockdiagramm:Diagramme en blocs d'un récepteur simple]
</margin>

<indepth>
Le récepteur représenté ici est appelé *récepteur à amplification directe*. Ce nom vient du fait que le signal capté par l'antenne n'est pas modifié en fréquence jusqu'au démodulateur.
</indepth>

---

Examinons maintenant en détail les différents blocs du récepteur, de gauche à droite :

1. Antenne : L'antenne capte une multitude d'ondes radio et les transmet sous forme d'oscillations électriques.
2. Filtre passe-bande : Pour isoler le signal souhaité, un filtre passe-bande est utilisé. Il ne laisse passer que la bande de fréquences souhaitée et bloque toutes les autres fréquences indésirables.
3. Amplificateur HF : Vient ensuite un amplificateur qui renforce le signal filtré. Il s'agit d'un amplificateur haute fréquence (amplificateur HF), car le signal possède une fréquence élevée, par exemple $\qty{144,3}{\mega\hertz}$.
4. Démodulateur : Le signal amplifié est ensuite traité par le démodulateur. La démodulation est l'inverse de la modulation. Alors que lors de la modulation, un signal (par exemple un signal vocal) est superposé à une porteuse haute fréquence, la démodulation permet de récupérer le signal d'origine à partir de la porteuse modulée. On obtient alors, par exemple, à nouveau le signal vocal qui avait été parlé dans le microphone de l'émetteur. On parle aussi de signal basse fréquence (signal BF), car il présente des fréquences relativement basses, par exemple inférieures à $\qty{20}{\kilo\hertz}$ pour un signal vocal.
5. Amplificateur BF : Le signal démodulé est ensuite amplifié. Il s'agit cette fois d'un amplificateur basse fréquence (amplificateur BF) pour amplifier le signal destiné au haut-parleur. Le symbole de l'amplificateur BF est identique à celui de l'amplificateur haute fréquence.
6. Haut-parleur : Le signal est ensuite converti par le haut-parleur d'une oscillation électrique en une onde sonore, ce qui le rend à nouveau audible.

<indepth>
Pour le *filtre passe-bande*, les deux ondes barrées indiquent que les fréquences au-dessus et en dessous de la bande de fréquences souhaitée sont bloquées. L'onde centrale montre que la bande de fréquences souhaitée est transmise.
</indepth>

<indepth>
Le *démodulateur* est représenté par le symbole de circuit de la diode, qui est le composant principal de nombreux démodulateurs. Le fonctionnement d'une diode sera expliqué plus en détail dans le chapitre « Composants et circuits ».
</indepth>

[question:NF201]

Selon la structure exacte d'un récepteur, celui-ci présente différentes caractéristiques. Une propriété importante est la *sensibilité*. Elle désigne la capacité du récepteur à capter des signaux faibles. Plus un récepteur est sensible, plus il peut capter des signaux faibles.

[question:NF303]
