Dans la classe E, nous avons déjà abordé les émissions indésirables sous forme d’*harmoniques* et d’*émissions parasites*. Les harmoniques, ou produits d’harmoniques d’un signal, apparaissent toujours lorsqu’il y a des écarts par rapport à une courbe sinusoïdale idéale. Elles sont toujours des multiples entiers de la fréquence fondamentale, comme illustré dans la figure [ref:a_harmonique].


Un exemple est donné par la question d’examen suivante : si un amplificateur est surmodulé, les sommets de l’amplitude du signal sinusoïdal sont limités – ce qui génère des harmoniques.


[question:AJ207]

<margin>
[picture:868:a_harmonique: Harmoniques (Harm.), produits d’harmoniques (Harm.) et émissions parasites (EP)]
</margin>

---

Lors de l’étude des multiples de la fréquence fondamentale d’un signal, nous distinguons les concepts d’*harmoniques* et de *harmoniques supérieures* du signal. Ces deux termes ne diffèrent que par leur définition et leur mode de comptage. La 1ère harmonique d’un signal correspond à sa fréquence fondamentale. La 2ème harmonique correspond à la 1ère harmonique supérieure du signal, la 3ème harmonique à la 2ème harmonique supérieure, et ainsi de suite. Le tableau ci-contre [ref:a_harmonique] montre cette relation.

<margin>
| l: Multiple de la fréquence fondamentale | l: Harmonique | l: Harmonique supérieure |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonique:Harmoniques et harmoniques supérieures]
</margin>

---

[question:AJ203]
[question:AJ204]


<tip>
La radiodiffusion FM est la "radiodiffusion classique" sur onde ultracourte (UKW). Les programmes radio sont diffusés dans la bande de fréquences de $\qtyrange{87,6}{107,9}{\mega\hertz}$.
</tip>

Pour supprimer individuellement certaines harmoniques ou produits d’harmoniques d’un signal, on peut utiliser, en plus du filtre classique d’harmoniques supérieures (passe-bas), des *circuits bouchons*. Un circuit bouchon supprime au maximum une fréquence précise et laisse passer presque sans atténuation toutes les autres fréquences.


[question:AJ210]

---

Selon le règlement sur la radio amateur (AFuV), les émissions indésirables doivent être réduites au minimum possible. Cependant, la [disposition 33](https://50ohm.de/vfg33) de 2007 fixe des valeurs limites précises que le radioamateur, mais aussi les fabricants d’appareils commerciaux, doivent respecter.

<margin>
[photo:319:a_vfg33:Extrait de la disposition 33 de 2007]
</margin>

Pour la bande VHF/UHF/SHF de $\qtyrange{50}{1000}{\mega\hertz}$, les émissions parasites et les harmoniques supérieures doivent être atténuées d’au moins $\qty{60}{\dB}$ par rapport au niveau de crête maximal du signal d’émission (PEP), tant que la puissance des signaux se situe au-dessus d’un niveau de $\qty{0,25}{\micro\watt}$ (cf. figure [ref:a_uagw]).


[question:AJ225]


<margin>
[picture:918:a_uagw:Atténuation des harmoniques supérieures dans la bande VHF/UHF/SHF]
</margin>

Pour la bande HF de $\qtyrange{1,7}{35}{\mega\hertz}$, les émissions parasites et les harmoniques supérieures doivent être atténuées d’au moins $\qty{40}{\dB}$ par rapport au niveau de crête maximal du signal d’émission (PEP), tant que la puissance des signaux se situe au-dessus d’un niveau de $\qty{0,25}{\micro\watt}$.


[question:AJ224]


%TODO BILD VON DL1COM EINBAUEN
Un analyseur de spectre en mode *spurious emissions* permet de mesurer les harmoniques ou produits d’harmoniques (en anglais *harmonics*), comme illustré dans la figure [ref:a_uagw]. L’analyseur de spectre détecte automatiquement le niveau de la porteuse ainsi que l’atténuation des harmoniques et les affiche à l’écran. Si l’on construit soi-même un appareil, il est essentiel de vérifier par des mesures que les valeurs limites prescrites sont respectées. Un fabricant commercial d’appareils radio certifie par la déclaration CE le respect de ces valeurs limites, mais il arrive que certains appareils ne respectent pas les exigences – dans ces cas, l’Agence fédérale des réseaux peut interdire leur exploitation et leur vente.

Les émissions indésirables ne proviennent pas uniquement des harmoniques supérieures, mais peuvent aussi apparaître lors de la préparation de la fréquence dans les émetteurs – par exemple, en raison de produits de mélange indésirables, de fluctuations de la tension d’alimentation ou d’une surmodulation du signal BF. Nous allons examiner cela plus en détail ci-après.

Pour supprimer les produits de mélange indésirables – mais aussi les harmoniques supérieures –, un filtre passe-bande est souvent utilisé après les mélangeurs. En particulier pour les émetteurs monobande ainsi que pour les appareils destinés aux bandes VHF, UHF et SHF, des filtres passe-bande sont utilisés à la place des filtres passe-bas classiques d’harmoniques supérieures. Avec ces appareils radio, il faut souvent aussi supprimer des composantes de signal qui apparaissent déjà lors de la préparation du signal d’émission et qui peuvent même se situer en dessous de la fréquence d’émission proprement dite.

[question:AJ211]
[question:AJ209]
[question:AJ208]


Les émissions indésirables peuvent aussi se situer à proximité immédiate du signal d’émission. Elles sont difficiles, voire impossibles à supprimer par l’utilisation de filtres et doivent donc être efficacement atténuées dès le début de la préparation du signal par des mesures appropriées. Ces *émissions parasites*, aussi appelées *produits secondaires* (surnommées "splatter" en langage courant), élargissent involontairement le signal d’émission. Elles sont souvent causées par un réglage trop élevé de l’amplificateur microphonique d’un émetteur. Cela déforme le signal BF et entraîne des émissions parasites indésirables. La figure [ref:a_harmonique] montre ces émissions parasites.

[question:AJ219]


Des émissions indésirables peuvent aussi être causées par une tension d’alimentation insuffisamment stabilisée des étages finals de l’émetteur. Par exemple, une alimentation mal filtrée ou stabilisée (présentant une tension de ronflement) sur le côté tension d’alimentation peut entraîner des émissions AM de l’étage final. Des couplages de signaux BF sur le côté alimentation secteur d’un émetteur peuvent aussi conduire à des émissions AM correspondantes. Cela se perçoit souvent lors d’émissions en CW comme une porteuse/ton "ronflante", notamment sur les anciens émetteurs.

[question:AJ222]
[question:AJ223]