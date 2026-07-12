## Calcul de la puissance rayonnée efficace (ERP)

* Ne prendre en compte que l'énergie qui arrive réellement à l'antenne – les pertes de câble sont soustraites
* L'ERP est calculée comme le produit de la puissance fournie et du gain d'antenne (par rapport à un dipôle demi-onde)

---
[question:AG501]
---

### Instructions de calcul pour l'ERP

* Les pertes sont soustraites de la puissance d'émission avant d'appliquer le facteur de gain ($G_{Antenne}$)
* La référence à un dipôle demi-onde doit être respectée lors du calcul

---
[question:AG502]
---

### ERP en radioamateur – Exemple pratique

* Le plan de fréquences pour la bande de $\qty{630}{\meter}$ prévoit une ERP maximale de $\qty{1}{\watt}$
* Un dipôle demi-onde aurait une longueur de $\qty{315}{\meter}$ à $\qty{630}{\meter}$ – souvent irréalisable, donc des antennes raccourcies sont utilisées
* Les antennes raccourcies ont un rendement inférieur, par exemple un gain d'antenne de $\qty{-20}{\dBd}$
* Rapport de puissance : $\qty{-20}{\dB}$ correspond à un facteur de $\num{0,01}$ ; Exemple : $\qty{50}{\watt} \cdot 0,01 = \qty{0,5}{\watt}$ ERP

--- style="font-size: 0.7em;"

### Rapports de puissance dans le recueil de formules

Ce tableau est inclus dans le recueil de formules et est disponible pendant l'examen.

| r:   | r: Rapport de puissance | r: Rapport de tension |
| $\qty{-20}{\dB}$ | $\num{0,01}$ | $\num{0,1}$ |
| $\qty{-10}{\dB}$ | $\num{0,1}$ | $\num{0,32}$ |
| $\qty{-6}{\dB}$ | $\num{0,25}$ | $\num{0,5}$ |
| $\qty{-3}{\dB}$ | $\num{0,5}$ | $\num{0,71}$ |
| $\qty{-1}{\dB}$ | $\num{0,79}$ | $\num{0,89}$ |
| $\qty{0}{\dB}$ | $\num{1}$ | $\num{1}$ |
| $\qty{1}{\dB}$ | $\num{1,26}$ | $\num{1,12}$ |
| $\qty{3}{\dB}$ | $\num{2}$ | $\num{1,41}$ |
| $\qty{6}{\dB}$ | $\num{4}$ | $\num{2}$ |
| $\qty{10}{\dB}$ | $\num{10}$  | $\num{3,16}$ |
| $\qty{20}{\dB}$ | $\num{100}$ | $\num{10}$ |
[table:Pegel_Verhältnis:Rapports de puissance et de tension pour des valeurs d'atténuation et d'amplification importantes]

---
[question:AG503]
---
#### Solution
* donné : $P_S = \qty{50}{\watt}$
* donné : $a \approx \qty{0}{\dB}$
* donné : $g_d = \qty{-20}{\dBd}$
* recherché : $P_{\textrm{ERP}}$

<fragment>
$\begin{split} P_{\textrm{ERP}} &= P_S \cdot 10^{\frac{g_d - a}{\qty{10}{\dB}}}\\ &= \qty{50}{\watt} \cdot 10^{\frac{\qty{-20}{\dBd} - \qty{0}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{50}{\watt} \cdot 10^{-2} = \qty{0,5}{\watt}\end{split}$
</fragment>
