Les tensions alternatives sinusoïdales changent continuellement de valeur. Pour mieux les décrire, nous voulons examiner trois caractéristiques importantes dans ce qui suit :

1. $\hat{U}$ : la valeur de crête d'une tension alternative
2. $U_\text{SS}$ : la valeur de crête à crête
3. $U_\text{eff}$ : la valeur efficace

<margin>
[picture:834:e_wechselspannung_kenngroessen:Les trois caractéristiques d'une tension alternative]
</margin>

---

La *valeur de crête* d'une tension alternative $\hat{U}$ correspond à l'amplitude que nous avons déjà apprise dans la classe N (cf. figure [ref:e_wechselspannung_kenngroessen]). Elle est entre autres importante pour la tension admissible des condensateurs. La figure [ref:e_spannungsfestigkeit_elkos] montre deux condensateurs électrolytiques filaires sur lesquels la tension admissible est imprimée. La valeur de crête de la tension appliquée ne doit pas dépasser cette valeur limite, sinon la destruction du condensateur est à craindre. Souvent, on choisit des composants avec une tension admissible plus élevée que nécessaire – soit pour des raisons de sécurité, soit pour prolonger la durée de vie.

<margin>
[photo:198:e_spannungsfestigkeit_elkos:Condensateurs électrolytiques avec des tensions admissibles de 16 volts et 25 volts]
</margin>

Une autre caractéristique est la *valeur de crête à crête*. Il s'agit de la différence entre la plus haute et la plus basse amplitude. Pour les tensions alternatives sinusoïdales, on a :

$U_\text{SS} = 2\cdot \hat{U}$.
 
[question:EB406]
[question:EB407]

Si ce n'est pas la tension, mais la puissance des appareils ou la charge thermique des composants et des conducteurs qui est au premier plan, la valeur de crête n'est pas utile. Dans ce cas, on a défini la *valeur efficace*. La valeur efficace d'une tension alternative correspond à la valeur d'une tension continue qui chaufferait une résistance ohmique de la même manière. 

---

Pour les tensions sinusoïdales, la valeur de crête ou de sommet est environ 1,4 fois plus grande que la valeur efficace (voir figure [ref:e_wechselspannung_kenngroessen]). Le calcul exact conduit à une formule simple :

$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ ou $\hat{U} = U_{eff} \cdot \sqrt{2}$

Si une tension alternative est indiquée uniquement par la lettre $U$ sans complément, il s'agit en règle générale de la valeur efficace. L'exemple le plus connu est notre tension secteur de $\qty{230}{\volt}$ – il s'agit également de la valeur efficace. La tension de crête est nettement plus élevée, à savoir

$\hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$.

<indepth>
La dérivation exacte de cette formule est effectuée à l'aide du calcul intégral et dépasse les connaissances requises pour l'examen du radioamateur. Celui qui est familier avec le calcul intégral et qui s'y intéresse peut lire la dérivation ici : [Wikipedia](https://50ohm.de/ew)
</indepth>

[question:EB401]

La valeur de $U_\text{SS}$ pour la tension secteur donne alors le double de la valeur de crête : 

$ U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$

[question:EB402]

Selon le même principe, les deux questions suivantes fonctionnent également : 

[question:EB403]
[question:EB404]

---

% TODO insérer une référence au chapitre sur la puissance :

Dans la question suivante, on demande indirectement la valeur efficace de la tension. Si l'on sait que $\frac{1}{\sqrt{2}} \approx 0,7$, on peut lire directement les deux résultats. 

<indepth>
Il est important que la tension continue $\qty{0,7}{\volt}$ ainsi que la tension continue $\qty{-0,7}{\volt}$ conduisent au même résultat. Cela est dû au fait que lors d'une tension négative, le signe du courant change également, ce qui conduit toutefois à la même puissance – car il s'applique $P = U \cdot I$.
</indepth>

[question:EB405]

D'ailleurs : Tout ce qui a été écrit ici sur les tensions alternatives s'applique de manière analogue aux courants alternatifs.