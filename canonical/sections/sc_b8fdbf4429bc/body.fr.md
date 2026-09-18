Dans le radioamateurisme, de nombreuses méthodes de transmission digitales sont utilisées. Nous en avons déjà abordé une très simple. En télégraphie Morse avec une onde entretenue (CW), une porteuse est allumée et éteinte selon un rythme précis. Il n’y a donc que deux niveaux, $\qty{0}{\percent}$ et $\qty{100}{\percent}$ de l’amplitude maximale. La transmission est donc numérique.

La télégraphie Morse est la plus ancienne méthode de transmission utilisée en radio. Les premiers émetteurs radio ne connaissaient pas d’autre procédé. La seule façon de transmettre des informations consistait à allumer et éteindre brièvement l’émetteur à l’aide d’une touche. À la réception, cela se traduit par un son qui s’allume et s’éteint selon le rythme donné.

Pour transmettre différents caractères, c’est-à-dire des lettres, des chiffres et des signes de ponctuation, on utilise le code Morse. Chaque caractère est défini par une séquence précise de sons courts et longs. Les tableaux [ref:n_morsetelegrafie_morsecode_buchstaben], [ref:n_morsetelegrafie_morsecode_ziffern_satzzeichen] et [ref:n_morsetelegrafie_morsecode_spezial] présentent une partie du code Morse. Un point ([morse:e]) (prononcé « dit ») représente un son court et un trait ([morse:t]) (prononcé « dah ») un son long. Le décodage, c’est-à-dire la traduction des sons en caractères à la réception, se fait à l’oreille et avec le cerveau – ou, de nos jours, également avec un ordinateur.

**Le Morse est une manipulation temporellement définie d’une porteuse. L’information ne provient pas seulement des points et des traits, mais aussi des pauses strictement définies.**

Les rapports de temps entre point, trait et pauses sont définis comme suit :

* Point = 1 unité de temps
* Trait = 3 unités de temps
* Pause entre les éléments d’un même caractère = 1 unité de temps
* Pause entre deux caractères = 3 unités de temps
* Pause entre deux mots = 7 unités de temps

La « vitesse » est exprimée en mots par minute [WPM] (Words Per Minute), le mot de référence international étant PARIS.

<webmargin>
| c: | l: | c: | l: | c: | l: |
|  |  |  |  |  |  |
| A | [morse:a] | K | [morse:k] | U | [morse:u] |
| B | [morse:b] | L | [morse:l] | V | [morse:v] |
| C | [morse:c] | M | [morse:m] | W | [morse:w] |
| D | [morse:d] | N | [morse:n] | X | [morse:x] |
| E | [morse:e] | O | [morse:o] | Y | [morse:y] |
| F | [morse:f] | P | [morse:p] | Z | [morse:z] |
| G | [morse:g] | Q | [morse:q] | Ä | [morse:ä] |
| H | [morse:h] | R | [morse:r] | Ö | [morse:ö] |
| I | [morse:i] | S | [morse:s] | Ü | [morse:ü] |
| J | [morse:j] | T | [morse:t] |  |  |
[table:n_morsetelegrafie_morsecode_buchstaben:Code Morse (lettres)]
</webmargin>

<webmargin>
| c: | l: | c: | l: | c: | l: | 
|  |  |  |  |  |  | 
| 0 | [morse:0] | 5 | [morse:5] | / | [morse:/] |
| 1 | [morse:1] | 6 | [morse:6] | . | [morse:.] |
| 2 | [morse:2] | 7 | [morse:7] | , | [morse:,] |
| 3 | [morse:3] | 8 | [morse:8] | ? | [morse:?] |
| 4 | [morse:4] | 9 | [morse:9] | - | [morse:-] |
|  |  |  |  | @ | [morse:@] |
[table:n_morsetelegrafie_morsecode_ziffern_satzzeichen:Code Morse (chiffres et signes de ponctuation)]
</webmargin>

% TODO ARK: Les prosignaux bk, sk et irrung ne fonctionnent pas encore sans l’espace gênant. Le programme morse.py dans le générateur doit être remplacé par le programme morse.py indiqué dans l’issue xxx.

<webmargin>
| l: | l: |
|  |  |
| Interruption (BK) | [morse:bk] |
| Séparation dans un même passage (BT,=) | [morse:=] |
| Fin du passage (AR) | [morse:ar] |
| Fin de l’émission (SK) | [morse:sk] |
| Erreur, rectification | [morse:correction] |
[table:n_morsetelegrafie_morsecode_spezial:Code Morse (signes particuliers, sélection)]
</webmargin>

Pendant longtemps, il était obligatoire dans le monde entier que chaque radioamateur réussisse l’examen de Morse avant de pouvoir émettre sur ondes courtes. Depuis les années 1990, chaque pays peut décider s’il exige un examen de Morse. Dans la plupart des pays, dont la Suisse, aucun examen de Morse n’est requis. Bien que des méthodes de transmission pour la voix, les images et même la vidéo aient été inventées, la télégraphie Morse est toujours pratiquée dans le radioamateurisme. Elle conserve un charme particulier : communiquer à l’échelle mondiale avec des moyens des plus simples.

[question:VA304]

Il existe une particularité à prendre en compte lors des échanges en télégraphie Morse : le choix d’une vitesse adaptée. Les signaux Morse peuvent être envoyés à différentes vitesses. Cependant, il faut beaucoup d’entraînement pour pouvoir capter des signaux Morse envoyés rapidement. Il est donc important de veiller à ne pas surcharger la station correspondante avec une vitesse trop élevée. Une bonne règle empirique consiste à ne pas envoyer plus vite que l’autre station et à ne pas dépasser la vitesse à laquelle on est capable de recevoir soi-même. Ainsi, tout le monde suit sans difficulté.

<indepth>
Ce n’est pas un hasard si les lettres fréquentes (n, t, i, etc.) sont associées à des signaux Morse courts et les lettres rares (x, y, etc.) à des signaux longs. Cela permet d’économiser du temps lors de la transmission d’un message. On parle aussi de compression de données à la source.
</indepth>

[question:BE117]
[question:BE118]
