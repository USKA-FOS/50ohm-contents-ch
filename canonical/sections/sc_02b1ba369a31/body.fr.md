Les mesures importantes pour le radioamateur sur les émetteurs sont les mesures de puissances de sortie des émetteurs ou la mesure de tensions HF dans des parties de circuits HF. Lors de la mesure de puissances de sortie d'émetteur, l'émetteur doit être terminé par une impédance définie, qui correspond à l'impédance de sortie de l'émetteur. En radioamateurisme, l'impédance habituelle (terminaison de l'émetteur) est de $\qty{50}{\ohm}$. La terminaison peut également être réalisée directement dans le circuit de mesure, ce qui n'est cependant judicieux que pour de faibles puissances.

La mesure des tensions HF s'effectue à l'aide d'une sonde HF via une détection par diode et un lissage ultérieur de la tension continue résultante avec un condensateur en aval. La figure [ref:hf_messkopf_0] montre le principe d'une sonde HF avec détection simple et lissage de la tension continue. La tension HF est terminée de manière adaptée en impédance à l'entrée via une résistance (ou une combinaison de résistances). Ensuite, la détection est effectuée par une diode, dont la tension de sortie est calculée comme la valeur de crête moins la tension directe de la diode, et est mise en mémoire tampon dans le condensateur en aval. La figure [ref:hf_messkopf_1] montre une sonde HF construite soi-même, la figure [ref:hf_messkopf_2] montre le schéma électrique correspondant.

<margin>
[picture:576:hf_messkopf_0:Principe d'une sonde HF avec détection simple et lissage de la tension continue]
[photo:338:hf_messkopf_1:Sonde HF construite par DL3JOP]
[photo:339:hf_messkopf_2:Schéma électrique de la sonde HF de DL3JOP]
</margin>

[question:AI608]

Pour des puissances HF plus élevées, un atténuateur capable de supporter la charge correspondante doit être placé en amont, qui absorbe la majeure partie de la puissance de sortie de l'émetteur à mesurer. L'atténuateur doit être pris en compte dans le calcul de la puissance.

[question:AI609]

---

Pour une mesure aussi précise que possible des tensions et puissances HF, le circuit de mesure utilisé doit d'abord être étalonné. Pour cela, des signaux de référence connus sont injectés et les écarts entre la valeur réelle et la valeur mesurée sont déterminés. À partir de ces écarts, des valeurs de correction dépendantes de la fréquence et du niveau peuvent être déterminées et stockées, par exemple dans un tableau comme dans [ref:a_frequenzgang_messwerte].

Lors d'une mesure ultérieure, la valeur mesurée affichée est corrigée avec la valeur de correction correspondante. Si les valeurs mesurées sont indiquées en $\unit{\dBm}$, l'écart déterminé lors de l'étalonnage pour la fréquence correspondante peut par exemple être ajouté comme valeur de correction en $\unit{\dB}$ à la valeur mesurée.

<margin>
| c: Fréquence en MHz | c: Puissance d'émission $\qty{-40}{\dBm}$ | c: Puissance d'émission $\qty{-20}{\dBm}$ |
| 10   | $\qty{-40,24}{\dBm}$ | $\qty{-20}{\dBm}$    |
| 50   | $\qty{-40,24}{\dBm}$ | $\qty{-20}{\dBm}$    |
| 100  | $\qty{-40,26}{\dBm}$ | $\qty{-20,12}{\dBm}$ |
| 200  | $\qty{-40,26}{\dBm}$ | $\qty{-20,2}{\dBm}$  |
| 300  | $\qty{-40,51}{\dBm}$ | $\qty{-20,32}{\dBm}$ |
| 400  | $\qty{-40,46}{\dBm}$ | $\qty{-20,28}{\dBm}$ |
| 500  | $\qty{-40,84}{\dBm}$ | $\qty{-20,64}{\dBm}$ |
| 600  | $\qty{-40,7}{\dBm}$  | $\qty{-20,41}{\dBm}$ |
| 700  | $\qty{-40,7}{\dBm}$  | $\qty{-20,53}{\dBm}$ |
| 800  | $\qty{-40,8}{\dBm}$  | $\qty{-20,55}{\dBm}$ |
| 900  | $\qty{-40,37}{\dBm}$ | $\qty{-20,2}{\dBm}$  |
| 1000 | $\qty{-40,33}{\dBm}$ | $\qty{-20,09}{\dBm}$ |
| 1100 | $\qty{-40,12}{\dBm}$ | $\qty{-19,85}{\dBm}$ |
| 1200 | $\qty{-39,94}{\dBm}$ | $\qty{-19,62}{\dBm}$ |
| 1300 | $\qty{-39,69}{\dBm}$ | $\qty{-19,49}{\dBm}$ |
| 1400 | $\qty{-40,18}{\dBm}$ | $\qty{-19,79}{\dBm}$ |
| 1500 | $\qty{-40,13}{\dBm}$ | $\qty{-19,97}{\dBm}$ |
| 1600 | $\qty{-40,95}{\dBm}$ | $\qty{-20,62}{\dBm}$ |
| 1700 | $\qty{-41,55}{\dBm}$ | $\qty{-21,64}{\dBm}$ |
| 1800 | $\qty{-41,47}{\dBm}$ | $\qty{-20,92}{\dBm}$ |
| 1900 | $\qty{-43,1}{\dBm}$  | $\qty{-23,27}{\dBm}$ |
| 2000 | $\qty{-42,34}{\dBm}$ | $\qty{-21,89}{\dBm}$ |
[table:a_frequenzgang_messwerte:Niveaux mesurés en fonction de la fréquence pour la sonde HF de DL3JOP]
</margin>

% Remarque :
% Une indication précise au centième de décibel me semble quelque peu éloignée de la pratique. On peut difficilement
% mesurer avec une telle précision. Cela peut donner un point de discussion en cours.

[question:AI612]

Examinons maintenant le calcul des circuits en détail. Pour les sondes HF avec une seule diode, la tension de crête de la tension HF appliquée, moins la tension directe de la diode utilisée et d'un éventuel diviseur de tension en amont, est mesurable à la sortie de mesure. Une sonde HF avec détection simple et lissage ultérieur est calculée comme suit :

Le signal d'entrée HF est terminé de manière adaptée en impédance à l'entrée par la résistance présente (ou une combinaison de résistances individuelles). Dans le circuit représenté (cf. figure [ref:hf_messkopf_0]), la tension HF est divisée par deux par le diviseur de tension suivant (qui est également efficace en termes d'impédance). Ensuite, la détection de la valeur de crête est effectuée par une diode, dont la tension de sortie est calculée comme la valeur de crête moins la tension directe de la diode et est mise en mémoire tampon dans le condensateur en aval.

---

[question:AI610]

<tip>
Pour tous les circuits avec sondes de mesure HF, on peut généralement supposer que la résistance d'entrée est de $\qty{50}{\ohm}$. Il n'est pas nécessaire de la recalculer, et on peut sauter cette étape pour les questions d'examen.
</tip>

Inversement, la puissance fournie au circuit peut être calculée à partir de la tension continue mesurée. Essaie de trouver la solution !

[question:AI611]

Outre les sondes HF avec une seule diode, il existe des circuits avec deux diodes. Leur avantage est que la pointe positive et la pointe négative du signal HF sont captées. Ainsi, une tension de mesure environ deux fois plus grande est disponible à la sortie que pour une détection de valeur de crête simple. Ceci est particulièrement utile lorsque de petites tensions HF doivent être captées par un appareil de mesure de tension continue en aval.

[question:AI605]
[question:AI604]

La pointe positive et la pointe négative du signal HF sont captées séparément et stockées dans des condensateurs. Les deux tensions s'additionnent à la sortie. Idéalement, la tension de sortie correspond ainsi à la tension crête à crête du signal HF :

$U_\mathrm{A} \approx U_\mathrm{SS} = 2\hat U$

Dans le circuit réel, les tensions de seuil des deux diodes doivent également être prises en compte. En approximation, on a donc :

$U_\mathrm{A} \approx 2\hat U - 2U_\mathrm{F}$

Si l'on veut déduire à nouveau la tension HF à partir de la tension de sortie mesurée, on obtient :

$\hat{U} \approx \frac{U_\mathrm{A}+2U_\mathrm{F}}{2}$

À partir de la valeur de crête, on peut ensuite calculer la valeur efficace et, avec une résistance connue, la puissance HF.

[question:AI607]
[question:AI606]

Pour indiquer qu'un émetteur rayonne de la puissance via son antenne, un indicateur d'intensité de champ peut être utilisé. Ici, le HF reçu est fourni à la diode via une antenne de mesure et redressé par la diode. Ensuite, la tension redressée est fournie via des selfs HF à un condensateur, qui met en mémoire tampon la tension redressée. L'affichage se fait par un ampèremètre sensible. Plus la déviation de l'aiguille de l'instrument de mesure est grande, plus l'intensité de champ HF mesurée à l'antenne est élevée. Pour effectuer des mesures exactes, l'antenne de mesure ainsi que le mesureur d'intensité de champ doivent être étalonnés.

[question:AI613]
