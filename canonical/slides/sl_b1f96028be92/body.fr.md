<left>
[picture:342:daempfungsglied_pi:Atténuateur en configuration PI avec source et résistance de charge]
</left>
<right>
* Affaiblir le niveau du signal de manière définie
* Éviter la surmodulation ou l'endommagement des appareils de mesure
* Réduire le niveau d'entrée pour les amplificateurs et récepteurs à une valeur définie
</right>
<note>
Le nom de configuration PI provient de la structure des résistances en forme de &Pi;
</note>

---
<left>
[picture:342:daempfungsglied_pi:Atténuateur en configuration PI avec source et résistance de charge]
</left>
<right>
* Affaiblissement par les résistances et conversion en chaleur
* Pour les atténuateurs symétriques, les impédances d'entrée et de sortie sont identiques
* Généralement $\qty{50}{\ohm}$
</right>

---
<left>
[picture:341:daempfungsglied_t:Atténuateur en configuration T avec source et résistance de charge]
</left>
<right>
* L'affaiblissement est indiqué en $\unit{\dB}$
* Par exemple $\qty{20}{\dB}$ = facteur $\num{100}$
* $\qty{100}{\watt}$ de puissance d'entrée $\rightarrow\qty{1}{\watt}$ de puissance de sortie
</right>
<note>
Le nom de configuration T provient de la structure des résistances en forme de T
</note>

---
[question:AD806]
--- style="font-size: smaller;"
#### Méthode de résolution
* donné : $P_1 = \qty{100}{\watt}$
* donné : $a = \qty{20}{\dB}$
* recherché : $\Delta P = P_2 - P_1$

<fragment>
$\begin{split} a &= \qty{10 \cdot \log_{10}{\left(\frac{P_1}{P_2}\right)}}{\dB}\\ \Rightarrow \frac{a}{\qty{10}{\dB}} &= \log_{10}{\left(\frac{P_1}{P_2}\right)}\\ \Rightarrow 10^{\frac{a}{\qty{10}{\dB}}} &= \frac{P_1}{P_2}\\ \Rightarrow P_2 &= \frac{P_1}{10^{\frac{a}{\qty{10}{\dB}}}}\end{split}$
</fragment>
---
<fragment>
$P_2 = \frac{P_1}{10^{\frac{a}{10}}} = \frac{\qty{100}{\watt}}{10^{\frac{20}{10}}} = \qty{1}{\watt}$
</fragment>
<fragment>
$\Delta P = P_2 - P_1 = \qty{100}{\watt} - \qty{1}{\watt} = \qty{99}{\watt}$
</fragment>
---
[question:AD803]
---
#### Méthode de résolution

* $\qty{20}{\dB}$ correspondent à un affaiblissement de puissance d'un facteur $\num{100}$

---
[question:AD804]
---
#### Méthode de résolution

* $\qty{6}{\dB}$ correspondent à un affaiblissement de puissance d'un facteur $\num{4}$

---
[question:AD805]
---
#### Méthode de résolution

* L'impédance du circuit complet ne change pas – donc $\qty{50}{\ohm}$

---
[question:AD801]
---
[question:AD802]