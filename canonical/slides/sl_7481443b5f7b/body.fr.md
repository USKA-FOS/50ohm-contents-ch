* La tension d'entrée peut varier
* Par exemple, dans les appareils alimentés par batterie
* Des modules sensibles (par exemple, des oscillateurs) modifieraient la fréquence
* Solution : stabilisation de la tension

---
## Stabilisation avec une diode Zener
<left>
[picture:323:a_Stabilisierung mit Z-Diode:Stabilisation de la tension avec une diode Zener]
</left>
<right>
* Circuit très simple
* Peut maintenir la tension de sortie dans certaines limites
</right>
<note>
</note>
---
[question:AD321]
--- style="font-size: 0.7em;"
#### Méthode de résolution
* donné : $R_L = \qty{470}{\ohm}$
* donné : $I_L = \qty{10}{\milli\ampere}$
* donné : $I_Z = \qty{15}{\milli\ampere}$
* donné : $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* recherché : $\eta = \frac{P_L}{P_{\mathrm{in}}}$

<fragment>
$P_L = I_L^2 \cdot R_L = (\qty{10}{\milli\ampere})^2 \cdot \qty{470}{\ohm} = \qty{47}{\milli\watt}$
</fragment>
<fragment>
$P_{\mathrm{in}} = U_{\mathrm{in}} \cdot I_{\mathrm{in}} = U_{\mathrm{in}} \cdot (I_Z + I_L) = \qty{13,8}{\volt} \cdot (\qty{15}{\milli\ampere} + \qty{10}{\milli\ampere}) = \qty{345}{\milli\watt}$
</fragment>
<fragment>
$\eta = \frac{P_L}{P_{\mathrm{in}}} = \frac{\qty{47}{\milli\watt}}{\qty{345}{\milli\watt}} \approx \num{0,14}$
</fragment>
---
## Régulateur de tension linéaire

<left>
[picture:985:a_spannungsregler_linear:Schéma d'un régulateur de tension linéaire]
</left>
<right>
* Le transistor de puissance fonctionne comme une résistance variable
* Forme, avec la résistance de charge, un diviseur de tension
* Le rendement est souvent très faible
</right>

---
[question:AD315]
---
[question:AD319]
---
#### Méthode de résolution
* donné : $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* donné : $U_{\mathrm{out}} = \qty{9}{\volt}$
* donné : $I = \qty{900}{\milli\ampere}$
* recherché : $P_V$

<fragment>
$U_{IC1} = U_{\mathrm{in}} - U_{\mathrm{out}} = \qty{13,8}{\volt} - \qty{9}{\volt} = \qty{4,8}{\volt}$
</fragment>
<fragment>
$P_V = U_{IC1} \cdot I = \qty{4,8}{\volt} \cdot \qty{900}{\milli\ampere} = \qty{4,32}{\watt}$
</fragment>
---
[question:AD320]
---
#### Méthode de résolution
* donné : $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* donné : $U_{\mathrm{out}} = \qty{5}{\volt}$
* donné : $I_{\mathrm{in}} = \qty{455}{\milli\ampere}$
* donné : $I_{\mathrm{out}} = \qty{450}{\milli\ampere}$
* recherché : $\eta$

<fragment>
$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}} = \frac{\qty{5}{\volt} \cdot \qty{450}{\milli\ampere}}{\qty{13,8}{\volt} \cdot \qty{455}{\milli\ampere}} \approx \num{0,36}$
</fragment>
---
## Régulateur de tension fixe
<left>
[picture:200:a_Festspannungsregler:Régulateur de tension fixe]
</left>
<right>
* Conçu sous forme de circuit intégré
* Fonctionne comme un régulateur de tension linéaire avec une source de référence de tension très précise et une régulation électronique optimale
* Même en cas de forte fluctuation côté entrée, la sortie reste très stable
</right>

---
[question:AD317]
---
[question:AD316]
---
[question:AD318]