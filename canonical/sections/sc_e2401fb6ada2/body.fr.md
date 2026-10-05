Un bloc d'alimentation convertit la tension alternative de $\qty{230}{\volt}$ de la prise murale en une tension continue plus faible. En radioamateurisme, nous utilisons souvent des blocs d'alimentation qui fournissent à leur sortie une tension continue de $\qty{13,8}{\volt}$, par exemple pour alimenter un émetteur-récepteur.

<margin>
[picture:740:n_netzgeraet:Bloc d'alimentation]
</margin>

<indepth>
Pour le *contrôle de l'état de fonctionnement* d'un bloc d'alimentation, il existe des interrupteurs éclairés, des diodes électroluminescentes de contrôle ou des instruments d'affichage éclairés. Les instruments d'affichage peuvent indiquer séparément la tension de service en volts et l'intensité du courant actuellement consommée en ampères. Il existe également des affichages numériques commutables à cet effet.
</indepth>

[question:ND101]
[question:ND102]

<danger>
Les fiches bipolaires ne peuvent être utilisées que pour les appareils à double isolation de protection.
</danger>

---
Un bloc d'alimentation est souvent connecté à la prise murale via une **fiche avec contact de protection**. En Suisse, les systèmes de fiches selon la norme
*SN 441011* sont utilisés à cet effet. Pour une prise tripolaire, les trois connexions sont prévues pour le *conducteur extérieur (L)*, le *conducteur neutre (N)* et le *conducteur de protection (PE)*, comme on peut le voir sur la figure [NE-10.3.2](https://50ohm.uska.ch/50ohm_review_de/NE_netzgeraet_1.html#ref_n_schutzkontakt). La tension secteur de 230 V de tension alternative est présente entre le conducteur extérieur L et le conducteur neutre N.

Le contact de protection de la fiche établit la connexion avec le conducteur de protection PE de la prise lors de l'insertion. « PE » est l'abréviation du terme anglais « protective earth », c'est-à-dire conducteur de protection ou mise à la terre de protection.

Si le bloc d'alimentation est doté d'un boîtier conducteur et d'une connexion pour le conducteur de protection, le boîtier est relié au système de conducteurs de protection de l'installation électrique via le conducteur PE. En cas de défaut d'isolation, un courant de défaut peut ainsi s'écouler via le conducteur de protection et déclencher le dispositif de protection, par exemple un disjoncteur ou un disjoncteur différentiel (FI). Le boîtier ne reste ainsi normalement pas durablement à une tension dangereuse. Une connexion bipolaire, c'est-à-dire sans le conducteur de protection, n'est autorisée que si l'appareil est à double isolation de protection.

---

<margin>
[photo:86:n_schutzkontakt:Fiche suisse avec et sans conducteur de protection]
</margin>

[question:ND109]

---

La sortie du bloc d'alimentation et le câble de connexion à l'émetteur-récepteur sont conçus de manière bipolaire afin de former un circuit fermé. C'est la condition préalable pour que le courant puisse circuler du bloc d'alimentation vers l'émetteur-récepteur, à travers celui-ci, et revenir au bloc d'alimentation.

<webmargin>
[picture:680:n_Netzgeraet_TRX:Connexion du bloc d'alimentation et du TRX]
</webmargin>

Les bornes de sortie pour la tension continue sont codées par couleur : le rouge pour le plus et le noir pour le moins. Cette polarité doit absolument être respectée lors de la connexion du câble à l'émetteur-récepteur. Sinon, cela peut entraîner un court-circuit ou, dans le pire des cas, la destruction de l'émetteur-récepteur. Ce n'est qu'une fois tous les câbles connectés et la polarité vérifiée que le bloc d'alimentation doit être mis sous tension.

[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Dans le bloc d'alimentation et dans le câble de connexion à l'émetteur-récepteur, il y a des fusibles miniatures. Ceux-ci peuvent détecter un cas de défaut (court-circuit ou surcharge) et interrompre le flux de courant. Il s'agit souvent de fusibles à cartouche, dans lesquels un fil fin fond lorsque trop de courant circule. Le circuit n'est alors plus fermé et aucun courant ne peut plus circuler. On parle alors d'un *fusible grillé* ou, dans le langage technique, d'un *déclenchement thermique*.

<margin>
[photo:88:n_feinsicherungen:Fusibles miniatures]
</margin>

<indepth>
*Approfondissement :* Les fusibles miniatures mesurent $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ et sont disponibles dans différentes versions. Ils diffèrent par leur intensité nominale et leurs caractéristiques de déclenchement. Les fusibles lents sont toujours utilisés lorsque le courant d'appel est nettement supérieur au courant nominal, par exemple dans les blocs d'alimentation. Le temps de déclenchement du fusible dépend de l'intensité du courant et de la durée du flux de courant. Le tableau [ref:n_feinsicherung] répertorie les valeurs courantes pour le temps de déclenchement. Des informations plus précises sont fournies par les fabricants via des courbes caractéristiques dans leurs fiches techniques.
</indepth>

Après qu'un fusible à cartouche a déclenché et que la cause a été identifiée et corrigée, il doit être remplacé. Cependant, les fusibles défectueux ne doivent être remplacés que par des fusibles identiques ! Il faut veiller à la fois à l'intensité nominale et à la caractéristique de déclenchement, qui indique la rapidité avec laquelle un fusible déclenche (rapide, temporisé, lent).

<webmargin>
| l: Caractéristique de déclenchement | l: Désignation | X: Temps de coupure |
| rapide | F | max. $\qty{30}{\milli\second}$ |
| temporisé | MT | max. $\qty{90}{\milli\second}$ |
| lent | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Caractéristiques des fusibles miniatures, temps de coupure pour dix fois le courant nominal]
</webmargin>

<danger>
*ATTENTION :* Le court-circuitage d'un fusible défectueux, par exemple avec du papier d'aluminium, parfois pratiqué, est interdit et très dangereux. Il existe un risque d'incendie !
</danger>

Les blocs d'alimentation de haute qualité possèdent souvent également une limitation électronique des courants. En cas de court-circuit, celle-ci veille à ce que l'intensité du courant soit limitée. On appelle cela la *limitation du courant de court-circuit*. Une fois le défaut éliminé, aucun fusible ne doit être remplacé.

[question:ND108]
[question:NK305]
