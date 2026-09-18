* *Circuit intégré (CI)* : Circuits intégrés
* Circuit complexe sur un substrat semi-conducteur
* Facilitent la construction de circuits électroniques

---
[question:AC601]
---
## Circuit intégré monolithique hyperfréquence (MMIC)

* Amplificateur large bande avec peu de composants
* Impédance d’entrée et de sortie typiquement de $\qty{50}{\ohm}$
* Intègre des composants actifs et passifs

---
[question:AC602]
---
[question:AC603]
---
[question:AC604]
---
### Montage d’un MMIC

<left>
[picture:773:a_mmic:Montage MMIC]
</left>
<right>
* Le point de fonctionnement est réglé via $R_{\textrm{BIAS}}$
* Les condensateurs isolent la tension continue
* Les broches 2 et 4 sont reliées à la masse par rapport à $U_{\textrm{CC}}$
* La broche 1 est ouverte
* $U_{\textrm{CC}}$ chute aux bornes de $R_{\textrm{BIAS}}$ et du MMIC
</right>
<note>
</note>

---
[question:AF425]
---
#### Méthode de résolution
* donné : $U_{\textrm{D}} = \qty{4}{\volt}$
* donné : $U_{\textrm{CC}} = \qty{13,5}{\volt}$
* donné : $I_{\textrm{D}} = \qty{10}{\milli\ampere}$
* recherché : $R_{\textrm{BIAS}}$

<fragment>
$R_{\textrm{BIAS}} = \frac{U_{\textrm{CC}} - U_{\textrm{D}}}{I_{\textrm{D}}} = \frac{\qty{13,5}{\volt} - \qty{4}{\volt}}{\qty{10}{\milli\ampere}} = \qty{950}{\ohm}$
</fragment>

---
[question:AF426]
---
#### Méthode de résolution
* donné : $U_{\textrm{D}} = \qty{4}{\volt}$
* donné : $U_{\textrm{CC}} = \qty{13,8}{\volt}$
* donné : $I_{\textrm{D}} = \qty{15}{\milli\ampere}$
* recherché : $R_{\textrm{BIAS}}$

<fragment>
$R_{\textrm{BIAS}} = \frac{U_{\textrm{CC}} - U_{\textrm{D}}}{I_{\textrm{D}}} = \frac{\qty{13,8}{\volt} - \qty{4}{\volt}}{\qty{15}{\milli\ampere}} = \qty{653,3}{\ohm} \rightarrow \qty{680}{\ohm}$
</fragment>

---
[question:AF427]
---
#### Méthode de résolution
* donné : $U = \qty{9}{\volt}$
* donné : $R_{\textrm{BIAS}} = \qty{470}{\ohm}$
* donné : $U_{\textrm{D}} = \qty{4}{\volt}$
* recherché : $P$
* Approche : le courant traversant $R_{\textrm{BIAS}}$ est le même partout, car aucun autre consommateur résistif n’est présent dans le circuit

<fragment>
$I_{\textrm{D}} = \frac{U_{\textrm{BIAS}}}{R_{\textrm{BIAS}}} = \frac{U-U_{\textrm{D}}}{R_{\textrm{BIAS}}} = \frac{\qty{9}{\volt}-\qty{4}{\volt}}{\qty{470}{\ohm}} = \qty{10,64}{\milli\ampere}$
</fragment>
<fragment>
$P = U_{\textrm{D}} \cdot I_{\textrm{D}} = \qty{4}{\volt} \cdot \qty{10,64}{\milli\ampere} \approx \qty{43}{\milli\watt}$
</fragment>
