---

### Symbole
* Un *symbole* est un état de signal identifiable.
* Les symboles peuvent différer, par exemple, par l’**amplitude**, la **fréquence** ou la **phase**.
* Plus il y a de symboles possibles, plus le nombre de **bits par symbole** est élevé.

---

### Débit de symboles
* Le *débit de symboles* indique le nombre de symboles transmis par seconde. L’unité du débit de symboles est le *baud*.
* Le **débit de transmission de données** et le débit de symboles ne sont donc pas toujours identiques.
* Si seulement deux symboles sont utilisés et que chaque **bit** est envoyé individuellement, le débit de symboles en baud correspond au débit de données en $\unit{\bit\per\second}$.
* En revanche, si davantage de symboles sont utilisés et que plusieurs **bits** sont transmis simultanément, le débit de transmission de données est supérieur au débit de symboles.

---

**Exemples**

* 2 symboles → 1 **bit**/symbole
* 4 symboles → 2 **bits**/symbole
* 8 symboles → 3 **bits**/symbole

---

* La formule $R_\mathrm{D} = R_\mathrm{S} \cdot N$ exprime la relation :

<fragment>
* $R_\mathrm{D}$ → **débit de transmission de données** en $\unit{\bit\per\second}$
* $R_\mathrm{S}$ → débit de symboles en $\unit{\baud}$
* $N$ → taille des symboles en $\unit{\bit\per\text{symbole}}$
</fragment>

---

[question:AA104]

---

Exemples :

<fragment>
*RTTY* : Commutation entre deux fréquences de symbole, permettant de transmettre un **bit** par symbole ($\num{0}$ ou $\num{1}$).
→ Débit de transmission de données = débit de symboles
</fragment>

<fragment>
*FT4* : Commutation entre quatre fréquences de symbole, permettant de transmettre deux **bits** par symbole ($\num{00}$, $\num{01}$, $\num{10}$ ou $\num{11}$).
→ Débit de transmission de données = 2 × débit de symboles
</fragment>

---

[question:AE405]

---

#### Méthode de résolution
* donné : $R_S = \qty{45,45}{\baud}$
* donné : $N=\qty{1}{\bit\per\text{symbole}}$
* recherché : $R_\mathrm{D}$

<fragment>
$R_\mathrm{D} = R_\mathrm{S} \cdot N = \qty{45,45}{\baud} \cdot \qty{1}{\bit\per\text{symbole}} = \qty{45,45}{\bit\per\second}$
</fragment>

---

[question:AE406]

---

#### Méthode de résolution
* donné : $R_S = \qty{23,4}{\baud}$
* donné : $N=\qty{2}{\bit\per\text{symbole}}$
* recherché : $R_\mathrm{D}$

<fragment>
$R_\mathrm{D} = R_\mathrm{S} \cdot N = \qty{23,4}{\baud} \cdot \qty{2}{\bit\per\text{symbole}} = \qty{46,8}{\bit\per\second}$
</fragment>