--- style="font-size: 0.7em;"
## Le décibel expliqué simplement

| l:Quoi | r:Puissance en $\unit{\milli\watt}$ |
| Puissance effective d'une station EME | 100 000 000 | 
| Émetteur-récepteur standard | 100 000 |
| Petite radio portative | 1 000 |
| Signal de haut-parleur (volume ambiant) | 100 |
| Signal d'écouteur | 1 |
| Signal OC fort | 0,000 001 |
| Signal OC faible (entrée antenne RX) | 0,000 000 000 001 |
[table:e_dezibel_leistungen_mw:Puissances en $\unit{\milli\watt}$]

Qui manipule ces chiffres commence automatiquement à compter les zéros.

--- style="font-size: 0.7em;"
Nous comptons les zéros (et appelons le résultat "bel")

| l:Quoi | r:Puissance en $\unit{\milli\watt}$ | r:Bel |
| Puissance effective d'une station EME | 100 000 000 | 8 |
| Émetteur-récepteur standard | 100 000 | 5 |
| Petite radio portative | 1 000 | 3 |
| Signal de haut-parleur (volume ambiant) | 100 | 2 |
| Signal d'écouteur | 1 | 0 |
| Signal OC fort | 0,000 001 | -6 |
| Signal OC faible (entrée antenne RX) | 0,000 000 000 001 | -12 |
[table:e_dezibel_leistungen_bel:Puissances en $\unit{\milli\watt}$ et bel]

<note>
D'après Alexander Graham Bell
</note>
--- style="font-size: 0.7em;"
$\unit{\dBm}$ = décibel par rapport à $\unit{\milli\watt}$

| l:Quoi | r:Puissance en $\unit{\milli\watt}$ | r:Bel | r:$\unit{\dBm}$ |
| Puissance effective d'une station EME | 100 000 000 | 8 | 80 |
| Émetteur-récepteur standard | 100 000 | 5 | 50 |
| Petite radio portative | 1 000 | 3 | 30 |
| Signal de haut-parleur (volume ambiant) | 100 | 2 | 20 |
| Signal d'écouteur | 1 | 0 | 0 |
| Signal OC fort | 0,000 001 | -6 | -60 |
| Signal OC faible (entrée antenne RX) | 0,000 000 000 001 | -12 | -120 |
[table:e_dezibel_leistungen_bel:Puissances en $\unit{\milli\watt}$ et bel]

<note>
* Facteur 10
* déci comme dans décimètre
</note>
---
### Gain de puissance

*Récepteur*
* Signal d'entrée : $\qty{0,000000000001}{\milli\watt}$
* Signal de sortie : $\qty{100}{\milli\watt}$
* Gain nécessaire : $\num{100000000000000}$
 
*Émetteur*
* Étage générateur de fréquence (oscillateur) : $\qty{10}{\milli\watt}$
* Signal de sortie : $\qty{100000}{\milli\watt}$
* Gain nécessaire : $\num{10000}$
 
---
### Gain de puissance avec dB
*Récepteur*
* Signal d'entrée : $\qty{0,000000000001}{\milli\watt} = \qty{-120}{\dBm}$
* Signal de sortie : $\qty{100}{\milli\watt} = \qty{20}{\dBm}$
* Gain nécessaire : $\num{100000000000000} = \qty{140}{\dB}$
 
*Émetteur*
* Étage générateur de fréquence (oscillateur) : $\qty{10}{\milli\watt} = \qty{10}{\dBm}$
* Signal de sortie : $\qty{100000}{\milli\watt} = \qty{50}{\dBm}$
* Gain nécessaire : $\num{10000} = \qty{40}{\dB}$

<note>
* La différence est le gain
* Le gain est un facteur et n'est pas rapporté au $\unit{mW}$, c'est pourquoi on utilise uniquement $\unit{\dB}$
</note>

--- style="font-size: 0.7em;"
## Facteurs de puissance importants

| c:$\unit{dB}$ | c:≈ Facteur de puissance |
| $0$ | $1$ |
| $1,5$ | $\sqrt{2} = 1,41$ |
| $2,15$ | $1,64$ |
| $3$ | $2$ |
| $5$ | $\sqrt{10} = 3,16$ |
| $6$ | $4$ |
| $10$ | $10$ |
| $20$ | $100$ |
[table:e_dezibel_leistungsfaktoren:Facteurs de puissance importants en $\unit{\dB}$]

<note>
* Rappel : 1,64 est le facteur entre un dipôle et un radiateur sphérique isotrope
</note>

---
### Calcul avec une calculatrice

Modèles anciens
* Valeur du facteur → touche *log* → $\times 10$ → $\unit{\dB}$
* Valeur en $\unit{\dB}$ → $\div 10$ → touche *$10^x$* → facteur

Modèles récents
* Touche *log* → valeur du facteur → touche *)* → $\times 10$ → touche *=* → $\unit{\dB}$
* Touche *$10^x$* → valeur en $\unit{\dB}$ → $\div 10$ → touche *=* → facteur

---
[question:EA107]