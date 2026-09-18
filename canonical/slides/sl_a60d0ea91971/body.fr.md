## Signal différentiel et courants de gaine

* Idéalement, des courants de même amplitude mais de sens opposés circulent dans le conducteur intérieur et le conducteur extérieur d’un câble coaxial
* Leur somme est nulle – signal purement différentiel
* Un signal purement différentiel empêche l’apparition de courants de gaine

---
### Signal en mode commun et courant de gaine

* Si la somme des courants n’est pas nulle, un signal en mode commun apparaît
* La composante en mode commun circule sur la face externe du conducteur extérieur sous forme de courant de gaine
* Le courant de gaine génère une onde de gaine autour du câble

---
[question:AG425]

---
### Self de mode commun

* Un câble coaxial enroulé autour d’un noyau ferrite supprime les ondes de gaine
* Cette configuration est appelée self de mode commun

---
[question:AG426]

---
## Transformateur HF pour le blocage des ondes de gaine

* Alternative : transformateur HF dont les enroulements primaire et secondaire ne sont pas connectés
* Le courant entrant dans un pôle ressort presque intégralement de l’autre pôle – la composante en mode commun est éliminée

<note>
Entre les spires de la bobine, une capacité parasite se forme, qui ne supprime pas totalement la composante en mode commun
</note>

---
[question:AJ115]

---
### Tensions HF et ondes de gaine

* En l’absence de signaux HF en mode commun : le conducteur extérieur ne présente pas de tension haute fréquence par rapport à la terre
* Avec des signaux différentiels, le champ électrique se forme exclusivement entre le conducteur intérieur et le conducteur extérieur
* Effet externe : les courants s’annulent – pas d’ondes de gaine
* Les ondes de gaine sont directement liées aux tensions HF sur le conducteur extérieur

---
## Antennes symétriques et tension sur le conducteur extérieur

* Pour une antenne symétrique, chaque branche du dipôle présente une tension par rapport à la terre
* Le raccordement des branches de l’antenne aux conducteurs du câble coaxial entraîne une tension HF sur le conducteur extérieur

---
### Influence de la mise à la terre des antennes

* Les antennes bien mises à la terre (par exemple, une groundplane avec des radiales accordées ou enterrées) présentent une tension quasi nulle de $\qty{0}{\volt}$ au point d’alimentation
* Les groundplanes mal mises à la terre peuvent être sensibles aux ondes de gaine

---
## Couplage sans contact dans le blindage coaxial

* Les ondes de gaine peuvent apparaître par couplage sans contact
* Si l’on fait passer un câble d’alimentation parallèlement à une branche de dipôle, le champ proche de l’antenne se couple dans le blindage coaxial

---
[question:AG427]

---
### Balun de tension / autotransformateur

<left>
[picture:447:a_mantelwellen_spannungsbalun:Structure d’un balun de tension]
</left>
<right>
* Pour des antennes parfaitement symétriques, un balun de tension peut symétriser les courants dans le câble coaxial
* Autotransformateur typique : le câble coaxial est connecté au milieu et à l’extrémité d’une bobine, l’antenne aux deux extrémités de la bobine
</right>

---

<left>
[picture:447:a_mantelwellen_spannungsbalun:Structure d’un balun de tension]
</left>
<right>
* Le doublement de la tension ($r = 2$) et l’abaissement du courant par deux entraînent une adaptation d’impédance de 1:4
* Un câble coaxial de $\qty{50}{\ohm}$ est idéalement connecté à une antenne d’environ $\qty{200}{\ohm}$
</right>

---
[question:AG421]

---
[question:AG422]

---
## Limites du blocage des ondes de gaine

* Le balun de tension ne fonctionne que si l’antenne connectée est effectivement symétrique
* Une charge asymétrique peut favoriser les ondes de gaine
* Le couplage sans contact via les champs proches électromagnétiques reste possible
* Une self de mode commun supplémentaire, placée à distance, peut apporter un soutien

---
[question:AG428]

---
[question:AG429]
