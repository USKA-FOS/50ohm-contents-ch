* Stabilisation d'un oscillateur variable et potentiellement instable (par exemple, VCO) à l'aide d'un oscillateur de référence stable
* Comparaison de phase entre les deux signaux
* La fréquence de sortie correspond à la fréquence de référence ou à un multiple et reste stable

--- style="font-size: smaller;"
[picture:45:a_oszillator_pll_pll:Schéma d'une boucle à verrouillage de phase (PLL)]

* Le *comparateur de phase* compare les phases du VCO et de l'oscillateur de référence
* Le *filtre passe-bas* convertit les impulsions du comparateur de phase en tension continue
* Le *VCO* génère la fréquence de sortie en fonction de la tension continue issue du filtre passe-bas
* Le *diviseur de fréquence* (optionnel) synchronise la fréquence du VCO sur un multiple de la fréquence de référence

<note>
Le comparateur de phase émet des impulsions en cas d'écart de phase, qui sont lissées en une tension continue par le filtre passe-bas. La modification de la fréquence du VCO réduit progressivement la différence de phase.
</note>

---
[question:AD701]
---
[question:AD702]
---
### Précision et stabilité

* Dépend de la qualité de l'oscillateur de référence
* Souvent un oscillateur à quartz

---
[question:AD705]
---
### Division de fréquence et accordabilité

* Le diviseur de fréquence permet de régler la PLL sur différentes fréquences
* La fréquence de sortie est un multiple entier de la fréquence de référence
* La plus petite fréquence sélectionnable correspond à celle de l'oscillateur de référence

---
[question:AD703]
---
[question:AD704]
--- style="font-size: 0.7em;"
#### Démarche
* donné : $f_\text{Osc} = \qty{12,5}{\kilo\hertz}$
* donné : $f_\text{Out,low} = \qty{12,000}{\mega\hertz}$
* donné : $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$
* recherché : $n$

<fragment>
Pour $f_{Out,low} = \qty{12,000}{\mega\hertz}$ :
$n = \frac{f_\text{Out,low}}{f_\text{Osc}} = \frac{\qty{12,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 960$
</fragment>
<fragment>
Pour $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$ :
$n = \frac{f_\text{Out,high}}{f_\text{Osc}} = \frac{\qty{14,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 1120$
</fragment>