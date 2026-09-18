### Génération

<left>
[picture:951:a_frequenzmodulation_schaltung:Modulateur pour la génération de FM]
</left>
<right>
* La capacité d'un oscillateur est modifiée par le signal BF
* Par exemple, à l'aide d'une diode à capacité variable
* La fréquence de modulation détermine la fréquence de variation de la porteuse HF
</right>
<note>
Ce sujet sera abordé plus en détail dans le chapitre *Émetteurs*
</note>

---
[question:AE303]
---
[question:AE301]
---
### Sensibilité aux perturbations

* L'information à transmettre est contenue dans la variation du signal
* Les fluctuations d'amplitude n'ont pas d'incidence
* Un amplificateur limiteur est souvent utilisé en interne
* Insensible aux perturbations impulsionnelles causées par des étincelles d'allumage, des moteurs électriques, etc.

---
[question:AE302]
---
### Excursion

* Détermine de combien la fréquence de l'oscillateur varie en fonction de l'amplitude du signal modulé
* Amplitude plus élevée dans le signal BF $\leftrightarrow$ excursion plus grande dans la porteuse
* Excursion plus grande $\rightarrow$ volume plus élevé dans le signal démodulé

---
[question:AE305]
---
### Bande passante

<left>
[picture:910:a_bandbreite_fm:Bande passante en FM]
$BP \approx 2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}}\right)$
</left>
<right>
* Bande passante occupée : excursion et fréquence de modulation maximale
* Pour une excursion faible et une fréquence de modulation basse $\rightarrow$ *formule de Carson*
* Fréquence de modulation ou excursion plus élevée $\rightarrow$ bande passante plus grande
* Risque de perturbations de canaux adjacents
</right>

<note>
Environ 99 % de la puissance d'émission se trouvent dans la bande passante
</note>
---
[question:AE306]
---
[question:AE307]
---
[question:AE304]
---
[question:AE309]
---
#### Méthode de résolution
* donné : $f_{\textrm{mod max}} = \qty{2}{\kilo\hertz}$
* donné : $\Delta f_{\textrm{T}} = \qty{1,8}{\kilo\hertz}$
* recherché : $BP$

<fragment>
$\begin{split} BP &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ &= 2 \cdot (\qty{1,8}{\kilo\hertz} + \qty{2}{\kilo\hertz}) = \qty{7,6}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE308]
---
#### Méthode de résolution
* donné : $f_{\textrm{mod max}} = \qty{2,7}{\kilo\hertz}$
* donné : $\Delta f_{\textrm{T}} = \qty{2,5}{\kilo\hertz}$
* recherché : $BP$

<fragment>
$\begin{split} BP &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ &= 2 \cdot (\qty{2,5}{\kilo\hertz} + \qty{2,7}{\kilo\hertz}) = \qty{10,4}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE311]
---
#### Méthode de résolution
* donné : $BP = \qty{10}{\kilo\hertz}$
* donné : $\Delta f_{\textrm{T}} = \qty{2,5}{\kilo\hertz}$
* recherché : $f_{\textrm{mod max}}$

<fragment>
$\begin{split} BP &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ \Rightarrow f_{\textrm{mod max}} &= \frac{BP}{2} - \Delta f_T\\ &= \frac{\qty{10}{\kilo\hertz}}{2} - \qty{2,5}{\kilo\hertz} = \qty{2,5}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE312]
---
#### Méthode de résolution
* donné : $BP = \qty{10}{\kilo\hertz}$
* donné : $f_{\textrm{mod max}} = \qty{2,7}{\kilo\hertz}$
* recherché : $\Delta f_{\textrm{T}}$

<fragment>
$\begin{split} BP &\approx 2 \cdot (\Delta f_{\textrm{T}} + f_{\textrm{mod max}})\\ \Rightarrow \Delta f_T &= \frac{BP}{2} - f_{\textrm{mod max}}\\ &= \frac{\qty{10}{\kilo\hertz}}{2} - \qty{2,7}{\kilo\hertz} = \qty{2,3}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AE310]