% Semi-conducteurs II
% DF2DR 2024-08-19

La matière première de notre monde moderne est constituée de matériaux semi-conducteurs. Une raison suffisante pour s'y intéresser de plus près. Les semi-conducteurs ont une structure cristalline, c'est-à-dire que leurs atomes sont disposés de manière périodique.

<margin>
[picture:854:a_silizium_halbleiter:Silizium Halbleiterkristall]
</margin>

Tous les matériaux semi-conducteurs partagent deux propriétés communes :


---

Il existe une *bande interdite* (ou *gap*), qui résulte de la structure périodique. Cela signifie que les électrons dans le cristal ne peuvent pas occuper certaines énergies. L'énergie maximale que les électrons liés aux atomes peuvent avoir est appelée *énergie de la bande de valence*. Comme les électrons sont tous liés aux atomes du réseau, ils ne peuvent pas contribuer au flux de courant. Il existe d'autres états d'énergie que les électrons peuvent atteindre : ils se situent dans la *bande de conduction*, qui se trouve à une énergie supérieure à celle de la bande de valence, d'une valeur égale à la bande interdite. Les électrons dans la bande de conduction peuvent contribuer au flux de courant si une tension est appliquée à l'échantillon semi-conducteur. Pour cela, ils ont besoin d'une énergie supérieure à celle de la bande interdite. Ils peuvent l'absorber sous forme d'énergie thermique, c'est pourquoi les semi-conducteurs très purs sont d'excellents isolants à basse température.

[question:AB104]

<margin>
L'énergie de la bande interdite est déterminée par la composition chimique du semi-conducteur. Comparé au Si, le Ge possède une bande interdite nettement plus petite, le GaAs et l'InP une bande interdite légèrement plus grande, et le GaN une bande interdite bien plus grande.
</margin>

Le silicium (Si) et le germanium (Ge) sont des *semi-conducteurs élémentaires* (comme le diamant, qui est du carbone cristallin). Il existe également des composés chimiques qui sont des semi-conducteurs (*semi-conducteurs composés*), comme l'arséniure de gallium (GaAs), le phosphure d'indium (InP) ou encore le nitrure de gallium (GaN).


---

Les matériaux à bande interdite ne sont qualifiés de semi-conducteurs que s'ils sont en outre *dopables*. Leur conductivité peut être modifiée dans de larges limites par une contamination ciblée du matériau semi-conducteur très pur. Par exemple, l'arsenic (As) possède, comparé aux semi-conducteurs élémentaires, un électron de plus dans sa couche électronique externe. Cet électron peut devenir très facilement et avec peu d'énergie un électron libre dans la bande de conduction. Un tel dopage est appelé *dopage de type N*.

<margin>
[picture:855:a_n_dotierung:n-Dotierung]
</margin>

---

Mais que se passe-t-il si nous contaminons le semi-conducteur avec un matériau qui possède un électron de moins dans sa couche électronique externe ? Un tel manque d'électron est appelé un *trou*. Comme l'atome était neutre auparavant, le manque d'électron porte une charge positive. Les trous peuvent également se déplacer dans le cristal et contribuer au flux de courant. Un tel dopage est appelé *dopage de type P*.

<margin>
[picture:856:a_p_dotierung:p-Dotierung]
</margin>

En résumé, nous pouvons constater que :
* Le dopage de type N produit un excès d'électrons dans le semi-conducteur.
* Le dopage de type P produit un excès de trous dans le semi-conducteur.

[question:AB105]
[question:AB106]
[question:AB107]

---

Si l'on combine, dans un cristal mais séparées spatialement, des zones dopées de type P et de type N, un échange de porteurs de charge se produit au niveau du contact : les électrons se déplacent de la zone dopée de type N vers la zone dopée de type P, et les trous de la zone dopée de type P vers la zone dopée de type N. Ce mouvement de porteurs de charge, provoqué par les différences de densité d'électrons et de trous, est appelé *courant de diffusion*.


Cette séparation de charge génère par ailleurs un *champ électrique* qui s'oppose à ce mouvement et entraîne un *courant de champ*. À l'équilibre (sans tension appliquée de l'extérieur), les effets du courant de diffusion et du champ électrique s'équilibrent. Entre les zones P et N se forme une région sans porteurs de charge libres, appelée *zone d'appauvrissement* ou *couche de blocage*. Une telle structure constitue une *diode PN*.

[question:AB108]

<margin>
[picture:857:a_pn_uebergang:PN-Übergang]
</margin>

---

Maintenant, appliquons une tension de l'extérieur, positive au niveau de la zone P (*anode*) et négative au niveau de la zone N (*cathode*). L'électrode positive attire les électrons à travers la zone d'appauvrissement, et l'électrode négative attire les trous. La zone d'appauvrissement se réduit, ce qui permet un flux de courant. C'est le fonctionnement en *sens direct*.

<margin>
[picture:956:a_pn_uebergang_mit_spannung:PN-Übergang mit externer Spannung]
</margin>

[question:AC402]

---

Si nous inversons la tension, la zone d'appauvrissement s'élargit et le flux de courant s'interrompt. C'est le *mode bloqué* de la diode.

<margin>
[picture:957:a_pn_uebergang_mit_spannung:PN-Übergang mit externer Spannung]
</margin>

[question:AB109]