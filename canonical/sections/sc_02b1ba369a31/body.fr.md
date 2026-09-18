Les mesures importantes pour le radioamateur sur les émetteurs concernent les mesures de puissances de sortie des émetteurs ou la mesure des tensions HF dans les circuits HF. Lors de la mesure des puissances de sortie des émetteurs, l'émetteur doit être terminé par une impédance définie, adaptée à l'impédance de sortie de l'émetteur. En radioamateurisme, l'impédance habituelle (terminaison de l'émetteur) est de $\qty{50}{\ohm}$. La terminaison peut également être intégrée directement dans le circuit de mesure, mais cela n'est pertinent que pour de faibles puissances.

La mesure des tensions HF s'effectue à l'aide d'une sonde HF par redressement à diode et lissage consécutif de la tension continue ainsi obtenue au moyen d'un condensateur placé en aval. La figure [ref:hf_messkopf_0] montre le principe d'une sonde HF avec redressement simple et lissage de la tension continue. La tension HF est terminée à l'entrée avec une impédance adaptée, soit par une résistance (ou une combinaison de résistances). Le redressement s'effectue ensuite au moyen d'une diode, dont la tension de sortie se calcule comme la valeur de crête moins la tension directe de la diode et est tamponnée dans le condensateur placé en aval. La figure [ref:hf_messkopf_1] montre une sonde HF artisanale, la figure [ref:hf_messkopf_2] son schéma électrique.

<margin>
[picture:576:hf_messkopf_0:Principe d'une sonde HF avec redressement simple et lissage de la tension continue]
[photo:338:hf_messkopf_1:Sonde HF artisanale de DL3JOP]
[photo:339:hf_messkopf_2:Schéma électrique de la sonde HF de DL3JOP]
</margin>

[question:AI608]

Pour des puissances HF plus élevées, il est nécessaire de placer en amont un atténuateur capable de supporter la charge, qui absorbe une grande partie de la puissance de sortie de l'émetteur à mesurer. L'atténuateur doit être pris en compte dans le calcul de la puissance.

[question:AI609]

---

Pour une mesure aussi précise que possible des tensions et puissances HF, le circuit de mesure utilisé doit d'abord être étalonné. Pour cela, des signaux de référence connus sont injectés et les écarts entre la valeur réelle et la valeur mesurée sont déterminés. À partir de ces écarts, des valeurs de correction dépendant de la fréquence et du niveau peuvent être déterminées et, par exemple, enregistrées dans un tableau comme celui de la [ref:a_frequenzgang_messwerte].

Lors d'une mesure ultérieure, la valeur mesurée affichée est corrigée à l'aide de la valeur de correction correspondante. Si les valeurs mesurées sont indiquées en $\unit{\dBm}$, l'écart déterminé lors de l'étalonnage pour la fréquence correspondante peut, par exemple, être ajouté à la valeur mesurée en $\unit{\dB}$ comme valeur de correction.

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

[question:AI612]

Examinons maintenant en détail le calcul des circuits. Dans le cas des sondes HF à une seule diode, la tension de crête du signal HF appliqué, moins la tension directe de la diode utilisée et éventuellement d'un diviseur de tension placé en amont, est mesurable à la sortie de la mesure. Une sonde HF avec redressement simple et lissage consécutif se calcule comme suit :

Le signal d'entrée HF est terminé à l'entrée avec une impédance adaptée, soit par une résistance (ou une combinaison de résistances). Dans le circuit représenté (cf. figure [ref:hf_messkopf_0]), la tension HF est divisée par deux par le diviseur de tension placé en aval (qui agit également sur l'impédance). Le redressement de la valeur de crête s'effectue ensuite au moyen d'une diode, dont la tension de sortie se calcule comme la valeur de crête moins la tension directe de la diode et est tamponnée dans le condensateur placé en aval.

---

[question:AI610]

<tip>
Pour tous les circuits utilisant des sondes HF, on peut partir du principe que la résistance d'entrée est de $\qty{50}{\ohm}$. Il n'est pas nécessaire de la recalculer, cette étape peut être ignorée pour les questions d'examen.
</tip>

Inversement, la puissance appliquée au circuit peut être calculée à partir de la tension continue mesurée. Essayez de trouver la solution par vous-même !

[question:AI611]

Outre les sondes HF à une seule diode, il existe des circuits à deux diodes. Leur avantage réside dans le fait que les valeurs de crête positive et négative du signal HF sont détectées. Il en résulte une tension de mesure environ double par rapport à un redressement simple de la valeur de crête. Cela est particulièrement utile pour mesurer de faibles tensions HF avec un ampèremètre placé en aval.

[question:AI605]
[question:AI604]

Les valeurs de crête positive et négative du signal HF sont détectées séparément et stockées dans des condensateurs. Les deux tensions s'additionnent à la sortie. Idéalement, la tension de sortie correspond ainsi à la tension crête-à-crête du signal HF :

$U_\mathrm{A} \approx U_\mathrm{SS} = 2\hat U$

Dans un circuit réel, il faut également tenir compte des tensions de passage des deux diodes. On obtient donc approximativement :

$U_\mathrm{A} \approx 2\hat U - 2U_\mathrm{F}$

Si l'on souhaite déduire la tension HF à partir de la tension de sortie mesurée, on obtient :

$\hat{U} \approx \frac{U_\mathrm{A}+2U_\mathrm{F}}{2}$

À partir de la valeur de crête, on peut ensuite calculer la valeur efficace et, connaissant la résistance, la puissance HF.

[question:AI607]
[question:AI606]

Pour indiquer qu'un émetteur rayonne de la puissance via son antenne, on peut utiliser un indicateur d'intensité de champ. Dans ce cas, la HF reçue est appliquée à une diode via une antenne de mesure et redressée. La tension redressée est ensuite transmise à un condensateur via des selfs HF, qui tamponne la tension redressée. L'affichage se fait au moyen d'un ampèremètre sensible. Plus l'aiguille de l'instrument de mesure dévie, plus l'intensité de champ HF mesurée à l'antenne est élevée. Pour effectuer des mesures précises, il est nécessaire d'étalonner à la fois l'antenne de mesure et l'indicateur d'intensité de champ.

[question:AI613]