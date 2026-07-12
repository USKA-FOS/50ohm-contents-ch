
% tu connais la représentation temporelle
% tu connais la représentation de fréquence
% fourier s'est occupé de la manière dont on passe de l'un à l'autre
% le signal temporel est analysé pour déterminer l'intensité de chaque fréquence sinusoïdale
% résumé : chaque signal peut être décomposé en une série d'oscillations sinusoïdales
% ne pas oublier la phase

Venons-en maintenant à un sujet passionnant qui semble plus compliqué qu'il ne l'est en réalité. On peut représenter les signaux de différentes manières. La représentation d'un signal dans le domaine temporel devrait être connue. Dans ce cas, l'axe des X représente le temps et l'axe des Y une valeur de tension ou de puissance.

Savais-tu que chaque signal peut être composé de sinusoïdes individuelles ? Cela semble fou, mais c'est ainsi. Chaque signal peut être décrit par une superposition de sinusoïdes pures ayant une amplitude et une phase déterminées.

La transformée de Fourier est une fonction mathématique complexe (que nous ne voulons pas expliquer plus en détail ici) qui analyse un signal présent dans le domaine temporel et représente ensuite les sinusoïdes individuelles dont le signal est composé. Cette information peut ensuite être représentée dans un diagramme dans le domaine des fréquences ou également dans le spectre de fréquences. Dans ce cas, l'axe des X décrit maintenant la fréquence et l'axe des Y la valeur de tension ou également la valeur de puissance de la fréquence contenue dans le signal de sortie. Un signal sinusoïdal pur d'une fréquence fixe représente ainsi, dans le spectre de fréquences, une ligne à sa fréquence.

La transformée de Fourier (également appelée transformée de Fourier discrète ou DFT) est, dans sa forme originale, une fonction mathématique complexe et coûteuse. Celle-ci ne peut être représentée que de manière très inefficace dans un logiciel. Au fil du temps, on a trouvé une méthode beaucoup plus efficace pour représenter cette fonction mathématique complexe de manière plus simple - la transformée de Fourier rapide ou également appelée FFT. Celle-ci simplifie considérablement le calcul, en particulier dans les logiciels et le matériel.



[question:AF630]

Nous nous souvenons que les signaux très anguleux et pointus contiennent des composantes de fréquence plus élevées (appelées harmoniques). Si l'on regarde un tel signal, par exemple un signal rectangulaire, dans le domaine des fréquences, on remarque qu'il est constitué d'un signal sinusoïdal fort à sa fréquence fondamentale ainsi que de plusieurs signaux sinusoïdaux de plus en plus faibles à des multiples impairs de la fréquence fondamentale. C'est d'ailleurs la raison pour laquelle on ne doit en aucun cas appliquer des signaux rectangulaires à une antenne avant qu'ils n'aient traversé un filtre passe-bas. Le filtre passe-bas sert dans ce cas à supprimer les composantes de signal plus élevées et à ne laisser sortir à sa sortie que la fondamentale sous forme de signal sinusoïdal. Si l'on appliquait directement le signal rectangulaire à l'antenne, une émission serait à recevoir sur tous les multiples impairs de la fréquence fondamentale et perturberait certainement de manière massive d'autres services radio.

[question:AB404]
[question:AB405]
[question:AB406]
[question:AB407]
