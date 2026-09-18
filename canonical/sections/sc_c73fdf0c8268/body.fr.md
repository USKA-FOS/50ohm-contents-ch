Les tensions alternatives sinusoïdales modifient en permanence leur valeur. Pour mieux les décrire, examinons trois grandeurs caractéristiques importantes dans ce qui suit :


1. $\hat{U}$ : la valeur de crête d'une tension alternative
2. $U_\text{SS}$ : la valeur crête-à-crête
3. $U_\text{eff}$ : la valeur efficace


<margin>
[picture:834:e_wechselspannung_kenngroessen:Les trois grandeurs caractéristiques d'une tension alternative]
</margin>

---

La *valeur de crête* d'une tension alternative $\hat{U}$ correspond à l'amplitude, que nous avons déjà abordée dans la classe N (cf. figure [ref:e_wechselspannung_kenngroessen]). Elle est notamment importante pour la tenue en tension des condensateurs. La figure [ref:e_spannungsfestigkeit_elkos] montre deux condensateurs électrolytiques traversants sur lesquels la tension maximale admissible est indiquée. La valeur de crête de la tension appliquée ne doit pas dépasser cette limite, sous peine de détruire le condensateur. On choisit souvent des composants avec une tenue en tension supérieure à celle requise – soit pour des raisons de sécurité, soit pour prolonger leur durée de vie.


<margin>
[photo:198:e_spannungsfestigkeit_elkos:Condensateurs électrolytiques avec les tenues en tension de 16 volts et 25 volts]
</margin>

Une autre grandeur caractéristique est la *valeur crête-à-crête*. Il s'agit de la différence entre l'excursion maximale et minimale. Pour les tensions alternatives sinusoïdales, on a :


$U_\text{SS} = 2\cdot \hat{U}$.

[question:EB406]
[question:EB407]


Lorsque ce n'est pas la tension, mais la puissance des appareils ou la charge thermique des composants et des conducteurs qui est au premier plan, la valeur de crête n'est pas pertinente. Dans ce cas, on a défini la *valeur efficace*. La valeur efficace d'une tension alternative correspond à la valeur d'une tension continue qui chaufferait une résistance ohmique de la même manière.


---

Pour les tensions sinusoïdales, la valeur de crête ou maximale est environ 1,4 fois plus grande que la valeur efficace (voir figure [ref:e_wechselspannung_kenngroessen]). Le calcul exact conduit à une formule simple :


$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ ou $\hat{U} = U_{eff} \cdot \sqrt{2}$


Lorsqu'une tension alternative est indiquée par la lettre $U$ seule, sans précision, il s'agit généralement de la valeur efficace. L'exemple le plus connu est notre tension secteur de $\qty{230}{\volt}$ – il s'agit également ici de la valeur efficace. La tension de crête est nettement plus élevée, à savoir


$\hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$.


<indepth>
La dérivation exacte de cette formule s'effectue à l'aide du calcul intégral et dépasse le cadre des connaissances requises pour l'examen de radioamateurisme. Ceux qui maîtrisent le calcul intégral et qui s'y intéressent peuvent consulter la dérivation ici : [Wikipedia](https://de.wikipedia.org/wiki/Effektivwert)
</indepth>

[question:EB401]


La valeur de $U_\text{SS}$ pour la tension secteur donne alors le double de la valeur de crête :


$ U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$


[question:EB402]


Le même principe s'applique aux deux questions suivantes :


[question:EB403]
[question:EB404]

---

% TODO référence au chapitre sur la puissance à insérer :


Pour la question suivante, on demande indirectement la valeur efficace de la tension. Si l'on sait que $\frac{1}{\sqrt{2}} \approx 0,7$, on peut lire directement les deux résultats.


<indepth>
Il est important de noter que la tension continue $\qty{0,7}{\volt}$ comme la tension continue $\qty{-0,7}{\volt}$ donnent le même résultat. Cela s'explique par le fait que, pour une tension négative, le signe du courant change également, ce qui conduit tout de même à la même puissance – car on a $P = U \cdot I$.
</indepth>

[question:EB405]


À noter : tout ce qui est écrit ici sur les tensions alternatives s'applique de la même manière aux courants alternatifs.