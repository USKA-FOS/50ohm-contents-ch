<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* Les circuits amplificateurs de transistors bipolaires sont nommés selon la connexion qui est parcourue par le signal d'entrée et de sortie
* Ou inversement : La connexion à laquelle ni l'entrée ni la sortie ne sont directement connectées
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* Signal d'entrée : source $\rightarrow$ base $\rightarrow$ collecteur $\rightarrow$ tension d'alimentation $\rightarrow$ source
* Signal de sortie : collecteur $\rightarrow$ charge $\rightarrow$ tension d'alimentation $\rightarrow$ collecteur
</right>
---
[question:AD401]
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* Le transistor nécessite un point de fonctionnement défini (BIAS)
* Il est déterminé par le diviseur de tension à la base
</right>
--- 
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* La résistance d'émetteur génère une tension lorsque le courant traverse le transistor.
* Le courant circule de l'émetteur à travers la résistance vers la masse.
* Plus le courant est important, plus la tension à l'émetteur est élevée.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* La tension d'émetteur freine le flux de courant et empêche de fortes fluctuations.
* Les variations de température influencent moins le transistor.
* $\rightarrow$ Le transistor reste fiable et fonctionne de manière uniforme.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* Couplage des signaux à la base et à l'émetteur via des *condensateurs de couplage*
* Maintiennent les composantes de tension continue à l'écart du étage amplificateur
* Le point de fonctionnement est stabilisé
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* Le condensateur de blocage dans la tension de service conduit les signaux HF et BF indésirables à la masse
* Les effets de rétroaction dans l'étage et sur la tension d'alimentation sont évités
* Le collecteur est mis à la masse $\rightarrow$ la sortie est au même potentiel que l'entrée
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificateur en circuit collecteur d'un transistor bipolaire]
</left>
<right>
* Le déphasage est de $\qty{0}{\degree}$
* L'impédance d'entrée est relativement élevée
* $\rightarrow$ L'amplification de tension est d'environ $\num{0,9}$ à $\num{0,98}$ (toujours un peu inférieure à $1$)
* L'impédance de sortie est très faible par rapport à l'impédance d'entrée
</right>

---
[question:AD405]
---
[question:AD402]
---
[question:AD403]
---
### Étage tampon

* Application fréquente comme étage tampon entre l'oscillateur et les autres parties du circuit
* Charge l'oscillateur de manière haute impédance
* $\rightarrow$ Moins de courant de l'oscillateur
* $\rightarrow$ Découplage
* $\rightarrow$ Meilleure stabilisation de la fréquence de l'oscillateur

---
[question:AD404]