* Convertisseur d'une fréquence à une autre par multiplicateur de fréquence
* Si la fréquence de l'oscillateur est inférieure au signal utile, la fréquence plus élevée du signal utile peut être mélangée directement à la fréquence de sortie plus élevée du convertisseur/transverter
* Si la fréquence de l'oscillateur est inférieure, un signal SSB est inversé (USB $\rightarrow$ LSB et LSB $\rightarrow$ USB)

---
[question:AF501]
---
#### Solution
* donné : $\Delta f_\text{o} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{410}{\mega\hertz}$
* donné : $\Delta f_\text{u} = \qty{436}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$
* donné : $n = 9$
* recherché : $f_{\text{Osc},1}, f_{\text{Osc},2}$

<fragment>
$f_{\text{Osc},1} = \frac{\Delta f_\text{u}}{n} = \frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$
$f_{\text{Osc},2} = \frac{\Delta f_\text{o}}{n} = \frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$
</fragment>
---
[question:AF502]
---
#### Solution
* donné : $\Delta f_\text{o} = \qty{434}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{404}{\mega\hertz}$
* donné : $\Delta f_\text{u} = \qty{430}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{402}{\mega\hertz}$
* donné : $n = 9$
* recherché : $f_{\text{Osc},1}, f_{Osc,2}$

<fragment>
$f_{\text{Osc},1} = \frac{\Delta f_\text{u}}{n} = \frac{\qty{402}{\mega\hertz}}{9} = \qty{44,6667}{\mega\hertz}$
$f_{\text{Osc},2} = \frac{\Delta f_\text{o}}{n} = \frac{\qty{404}{\mega\hertz}}{9} = \qty{44,889}{\mega\hertz}$
</fragment>
---
La question suivante sera classée dans un autre chapitre, car elle ne convient pas au sujet des convertisseurs et des transverters.
---
[question:AF301]
