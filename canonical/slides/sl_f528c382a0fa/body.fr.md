## Bande passante des modes numériques

* Contrairement à la voix, de nombreux modes numériques nécessitent une bande passante plus étroite
* Par exemple, BPSK31 avec $\qty{31,25}{\hertz}$ ou FT8 avec $\qty{50}{\hertz}$
* Les tonalités générées sont modulées en SSB
* La bande passante du signal émis reste alors identique

---
[question:EE403]
---
[question:EE402]
--- style="font-size: smaller;"

## Réception des modes numériques

<left>
* Lors de la réception en SSB, plusieurs modes numériques à bande étroite peuvent être reçus dans la bande passante habituelle de $\qty{2,4}{\kilo\hertz}$
* FT8 : $\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$ = max. $\num{48}$ signaux
* BPSK31 : $\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$ = max. $\num{76}$ signaux
* Sur l'ordinateur, le signal du mode numérique souhaité est ensuite sélectionné
</left>
<right>
[picture:718:e_digimode_ssb_ft8_wasserfall:Diagramme en cascade de la réception de plusieurs signaux de modes numériques dans la bande passante SSB de $\qty{2,4}{\kilo\hertz}$. Chaque colonne représente la transmission d'un signal différent]
</right>

---
[question:EE404]

---
## SSTV

<left>
* *Slow-Scan Television* est la transmission d'images fixes au moyen de modes numériques
* Transmission ligne par ligne d'images
* Différentes méthodes avec différentes résolutions et vitesses de transmission
* Bande passante inférieure à $\qty{3}{\kilo\hertz}$ et utilisable dans les bandes HF
</left>
<right>
[photo:84:e_digimode_ssb_sstv:Confirmation d'une liaison SSTV avec F1BIB de ON1GA avec le RST 575 et en plus l'image reçue initialement]
</right>

---
## ATV
* *Amateur Television* est la transmission d'images animées
* Nécessite plusieurs MHz de bande passante ($\qty{6}{\mega\hertz}$ et plus)
* C'est pourquoi elle n'est utilisable qu'à partir de la bande $\qty{70}{\centi\meter}$ et au-dessus

---
[question:EE415]