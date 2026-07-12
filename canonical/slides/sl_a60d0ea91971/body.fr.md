## Signal différentiel et ondes de gaine

* Idéalement, des courants de même amplitude mais de sens opposés circulent dans le conducteur intérieur et extérieur d'un câble coaxial
* Leur somme est nulle – signal différentiel pur
* Un signal différentiel pur empêche l'apparition d'ondes de gaine

---
### Signal commun et courant de gaine

* Si la somme des courants n'est pas nulle, un signal commun est créé
* La composante commune circule sur la face extérieure du conducteur extérieur en tant que courant de gaine
* Le courant de gaine génère une onde de gaine autour du câble

---
[question:AG425]

---
### Bobine de compensation de courant

* Un câble coaxial enroulé autour d'un noyau de ferrite supprime les ondes de gaine
* Cette forme de construction est appelée bobine de compensation de courant

---
[question:AG426]

---
## Transformateur HF pour la suppression des ondes de gaine

* Alternative : transformateur HF dont les enroulements primaire et secondaire ne sont pas connectés
* Le courant qui entre par un pôle sort presque entièrement par l'autre – la composante commune est éliminée

<note>
Entre les enroulements, une capacité se forme, qui ne supprime pas complètement la composante commune
</note>

---
[question:AJ115]

---
### Tensions HF et ondes de gaine

* En l'absence de signaux HF communs : le conducteur extérieur ne présente aucune tension haute fréquence par rapport à la terre
* Dans le cas des signaux différentiels, le champ électrique se forme exclusivement entre le conducteur intérieur et le conducteur extérieur
* Effet extérieur : les courants s'annulent – pas d'ondes de gaine
* Les ondes de gaine sont directement liées aux tensions HF sur le conducteur extérieur

---
## Antennes symétriques et tension du conducteur extérieur

* Dans le cas d'une antenne symétrique, chaque branche du dipôle présente une tension par rapport à la terre
* La connexion des branches d'antenne aux conducteurs du câble coaxial entraîne une tension HF sur le conducteur extérieur

---
### Influence de la mise à la terre des antennes

* Les antennes bien mises à la terre (par exemple, Groundplane avec radiales accordées ou enterrées) ont presque $\qty{0}{\volt}$ au point d'alimentation
* Les antennes Groundplane mal mises à la terre peuvent être sensibles aux ondes de gaine

---
## Couplage sans contact dans le blindage coaxial

* Les ondes de gaine peuvent être générées par couplage sans contact
* Si un câble d'alimentation est amené parallèlement à une branche de dipôle, le champ proche de l'antenne se couple dans le blindage coaxial

---
[question:AG427]

---
### Balun de tension / Transformateur d'autotransformateur

<left>
[picture:447:a_mantelwellen_spannungsbalun:Structure d'un balun de tension]
</left>
<right>
* Dans le cas d'antennes entièrement symétriques, un balun de tension peut symétriser les courants dans le câble coaxial
* Transformateur typique : câble coaxial connecté au milieu et à l'extrémité d'une bobine, antenne connectée aux deux extrémités de la bobine
</right>

---

<left>
[picture:447:a_mantelwellen_spannungsbalun:Structure d'un balun de tension]
</left>
<right>
* Doublement de la tension ($ü = 2$) et division par deux du courant entraînent une transformation d'impédance de 1:4
* Une antenne d'environ $\qty{200}{\ohm}$ est idéalement connectée à un câble coaxial de $\qty{50}{\ohm}$
</right>

---
[question:AG421]

---
[question:AG422]

---
## Limites de la suppression des ondes de gaine


* Le balun de tension ne fonctionne que si l'antenne connectée est effectivement symétrique
* Une charge asymétrique peut favoriser les ondes de gaine
* Le couplage sans contact via les champs proches électromagnétiques reste possible
* Une suppression supplémentaire des ondes de gaine avec un espacement spatial peut avoir un effet de soutien

---
[question:AG428]

---
[question:AG429]
