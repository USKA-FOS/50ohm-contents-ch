<margin>
[picture:735:aufbau_sender:Diagramme en blocs d'un émetteur simple]
</margin>

La figure [ref:aufbau_sender] montre les composants nécessaires pour construire un émetteur AM. Certains de ces blocs nous sont déjà connus du récepteur, d'autres sont nouveaux :
1. Microphone : Le microphone convertit les ondes sonores de la voix en oscillations électriques basse fréquence. On peut aussi utiliser, par exemple pour les procédés de transmission numériques, le signal basse fréquence issu de la sortie audio d'un ordinateur.
2. Amplificateur basse fréquence : Le signal provenant du microphone ou de l'ordinateur est d'abord amplifié.
3. Mélangeur : Le mélangeur combine l'oscillation haute fréquence générée par l'oscillateur (4) avec l'oscillation basse fréquence provenant du microphone ou de l'ordinateur. Cela permet de moduler en amplitude la porteuse haute fréquence avec le signal vocal ou de données.
4. Oscillateur : L'oscillateur génère l'oscillation haute fréquence à la fréquence d'émission souhaitée, par exemple $\qty{29,5}{\mega\hertz}$.
5. Filtre passe-bande : Comme le mélangeur, en raison de son fonctionnement, génère non seulement les fréquences souhaitées mais aussi d'autres fréquences indésirables, celles-ci doivent être bloquées par un filtre passe-bande.
6. Amplificateur haute fréquence : Le signal haute fréquence est ensuite amplifié pour disposer de la puissance d'émission souhaitée.
7. Filtre passe-bas : Comme l'amplification peut également générer des fréquences indésirables, un nouveau filtrage est nécessaire.
8. Antenne : Le signal haute fréquence est ensuite transmis à l'antenne qui l'émet sous forme d'onde radio.

%[class:N]
<indepth>
Lorsqu'un mélangeur combine deux signaux, cela correspond mathématiquement à une multiplication des deux signaux. C'est pourquoi le symbole du mélangeur en diagramme en blocs contient aussi une croix de multiplication. Le fonctionnement exact d'un mélangeur est abordé dans le cours de classe A.
</indepth>
%[/class]

[question:NF401]
[question:NF403]

Pour la question suivante, il est important de se rappeler qu'un émetteur nécessite un oscillateur et un mélangeur.

[question:NF402]

Une installation de radioamateur doit être construite et exploitée selon les règles techniques généralement reconnues. Cela s'applique bien sûr aussi tout particulièrement aux émetteurs.

[question:VD106]