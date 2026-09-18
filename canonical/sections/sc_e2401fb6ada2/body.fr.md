Un bloc d'alimentation convertit la tension alternative de $\qty{230}{\volt}$ du secteur en une tension continue plus faible. En radioamateurisme, on utilise souvent des blocs d'alimentation qui fournissent en sortie une tension continue de $\qty{13,8}{\volt}$, par exemple pour alimenter un émetteur-récepteur.

<margin>
[picture:740:n_netzgeraet:Bloc d'alimentation]
</margin>

<indepth>
Pour *contrôler l'état de fonctionnement* d'un bloc d'alimentation, on trouve des interrupteurs éclairés, des voyants lumineux ou des instruments de mesure éclairés. Les instruments de mesure peuvent afficher séparément la tension de service en volts et l'intensité du courant en ampères. Il existe également des afficheurs numériques commutatifs pour cette fonction.
</indepth>

[question:ND101]
[question:ND102]

<danger>
Les fiches bipolaires ne doivent être utilisées que pour des appareils à double isolation de protection.
</danger>

---
Un bloc d'alimentation est souvent raccordé à la prise de courant secteur au moyen d'une **fiche avec contact de protection**. En Suisse, on utilise pour cela des systèmes de prises conformes à la norme *SN 441011*. Dans une prise tripolaire, les trois bornes sont prévues pour le *conducteur extérieur (L)*, le *conducteur neutre (N)* et le *conducteur de protection (PE)*, comme illustré dans la figure [NE-10.3.2](https://50ohm.uska.ch/50ohm_review_de/NE_netzgeraet_1.html#ref_n_schutzkontakt). Entre le conducteur extérieur L et le conducteur neutre N, la tension secteur de $\qty{230}{\volt}$ de tension alternative est présente.

Le contact de protection de la fiche établit, lors de l'insertion, la connexion avec le conducteur de protection PE de la prise. « PE » est l'abréviation de l'anglais « protective earth », c'est-à-dire conducteur de protection ou mise à la terre de protection.

Si le bloc d'alimentation est doté d'un boîtier conducteur et d'une connexion au conducteur de protection, le boîtier est relié au système de mise à la terre de l'installation électrique via le conducteur PE. Ainsi, en cas de défaut d'isolation, un courant de défaut peut s'écouler par le conducteur de protection et déclencher le dispositif de protection, par exemple un disjoncteur ou un disjoncteur différentiel (FI). Le boîtier ne reste donc normalement pas durablement sous une tension dangereuse. Une connexion bipolaire, c'est-à-dire sans conducteur de protection, n'est autorisée que si l'appareil est à double isolation de protection.

---

<margin>
[photo:86:n_schutzkontakt:Fiche suisse avec et sans contact de protection]
</margin>

[question:ND109]

---

La sortie du bloc d'alimentation et le câble de connexion vers l'émetteur-récepteur sont conçus avec deux pôles afin de former un circuit fermé. C'est la condition nécessaire pour que le courant puisse circuler du bloc d'alimentation vers l'émetteur-récepteur, le traverser et revenir au bloc d'alimentation.

<webmargin>
[picture:680:n_Netzgeraet_TRX:Raccordement d'un bloc d'alimentation et d'un émetteur-récepteur]
</webmargin>

Les bornes de sortie pour la tension continue sont colorées : le rouge indique le plus et le noir le moins. Lors du raccordement du câble à l'émetteur-récepteur, cette polarité doit être impérativement respectée. Sinon, un court-circuit peut survenir, voire, dans le pire des cas, la destruction de l'émetteur-récepteur. Il ne faut mettre l'appareil sous tension qu'une fois tous les câbles raccordés et la polarité vérifiée.

[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Dans le bloc d'alimentation et dans le câble de connexion vers l'émetteur-récepteur, on trouve des **fusibles miniatures**. Ceux-ci peuvent détecter un défaut (court-circuit ou surcharge) et interrompre le flux de courant. Il s'agit souvent de fusibles à fusion, dans lesquels un fil fin fond lorsque le courant est trop élevé. Le circuit n'est alors plus fermé et plus aucun courant ne peut circuler. On parle alors de *fusible grillé* ou, dans le jargon technique, de *coupure thermique*.

<margin>
[photo:88:n_feinsicherungen:Fusibles miniatures]
</margin>

<indepth>
*Approfondissement :* Les fusibles miniatures mesurent $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ et sont disponibles en différentes versions. Ils se distinguent par leur intensité nominale et leurs caractéristiques de déclenchement. Les fusibles lents sont utilisés lorsque le courant d'appel est nettement supérieur au courant nominal, par exemple dans les blocs d'alimentation. Le temps de déclenchement du fusible dépend de l'intensité du courant et de la durée du flux de courant. Le tableau [ref:n_feinsicherung] présente les valeurs usuelles des temps de déclenchement. Les fabricants fournissent des informations plus précises sous forme de courbes caractéristiques dans leurs fiches techniques.
</indepth>

Une fois qu'un fusible à fusion a déclenché et que la cause a été identifiée et corrigée, il doit être remplacé. Les fusibles défectueux ne doivent être remplacés que par des fusibles de même type ! Il faut veiller à respecter l'intensité nominale ainsi que la caractéristique de déclenchement, qui indique à quelle vitesse un fusible réagit (rapide, moyenne, lente).

<webmargin>
| l: Caractéristique de déclenchement | l: Symbole | X: Temps de coupure |
| rapide | F | max. $\qty{30}{\milli\second}$ |
| moyenne | MT | max. $\qty{90}{\milli\second}$ |
| lente | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Caractéristiques des fusibles miniatures, temps de coupure à dix fois l'intensité nominale]
</webmargin>

<danger>
*ATTENTION :* Le contournement d'un fusible défectueux, par exemple avec du papier aluminium, est interdit et très dangereux. Il existe un risque d'incendie !
</danger>

<attention>
*PRÉCAUTION :* Si un appareil radio est directement raccordé à la batterie d'un véhicule, les câbles positif et négatif doivent chacun être protégés par un fusible. Les fusibles doivent être installés le plus près possible de la batterie.

Le fusible sur le câble négatif protège le câblage dans le cas rare où la connexion de masse normale de la batterie au véhicule est interrompue et qu'un courant élevé du véhicule pourrait circuler par une autre connexion de masse de l'appareil radio.
</attention>

Les blocs d'alimentation de haute qualité disposent souvent également d'une *limitation électronique* des courants. En cas de court-circuit, celle-ci limite l'intensité du courant. On parle alors de *limitation du courant de court-circuit*. Une fois le défaut éliminé, il n'est pas nécessaire de remplacer un fusible.

[question:ND108]
[question:NK305]
