Dans les sections [sec:unerwuenschte_aussendungen_1] et [sec:unerwuenschte_aussendungen_2], nous avons déjà rencontré des émissions indésirables sous forme d'*harmoniques* et d'*émissions parasites*. Les harmoniques supérieures ou harmoniques d'un signal se produisent toujours lorsque des écarts par rapport à la courbe sinusoïdale idéale se forment et sont toujours des multiples entiers de la fréquence fondamentale, comme illustré dans la figure [ref:a_harmonique].

Un exemple est montré dans la question d'examen suivante : Si un amplificateur est surmodulé, les pics de l'amplitude du signal sinusoïdal sont limités – ce qui génère des harmoniques.

[question:AJ207]

<margin>
[picture:868:a_harmonique: Harmoniques supérieures (OW), Harmoniques (Harm.) et émissions parasites (NA)]
</margin>

---

Lors de l'examen des multiples de la fréquence fondamentale d'un signal, nous distinguons les termes *harmoniques et harmoniques supérieures* du signal. Ces deux termes ne diffèrent que par leur définition et leur méthode de comptage. La 1ère harmonique d'un signal est sa fréquence fondamentale elle-même. La 2ème harmonique correspond à la 1ère harmonique supérieure d'un signal, la 3ème harmonique à la 2ème harmonique supérieure d'un signal, et ainsi de suite. Le tableau adjacent [ref:a_harmonique] montre la relation.

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
La radiodiffusion FM est la radiodiffusion "classique" sur onde ultracourte (FM). La diffusion des programmes radio s'effectue dans la bande de fréquences de $\qtyrange{87,6}{107,9}{\mega\hertz}$.
En Suisse, contrairement aux plans précédents, les émetteurs FM doivent continuer à fonctionner de manière limitée.
</tip>
%TODO: Helvetisation

Si certaines harmoniques supérieures ou harmoniques d'un signal doivent être supprimées individuellement, cela peut être réalisé, en plus du filtre classique pour harmoniques supérieures (passe-bas), par des *circuits bouchons*. Un circuit bouchon supprime au maximum exactement une fréquence et laisse passer presque toutes les autres sans entrave.

[question:AJ210]

---

Selon l'Ordonnance sur les radioamateurs (AFuV), les émissions indésirables doivent être limitées au minimum possible. La [Disposition 33](https://50ohm.de/vfg33) de 2007 fixe cependant des valeurs limites précises, qui doivent être respectées par le radioamateur ainsi que par les fabricants d'appareils commerciaux.
%TODO: Helvetisation

<margin>
[photo:319:a_vfg33:Extrait de la Disposition 33 de 2007]
</margin>

Pour la gamme VHF/UHF/SHF de $\qtyrange{50}{1000}{\mega\hertz}$, il est stipulé que les émissions parasites et les harmoniques supérieures doivent être atténuées d'au moins $\qty{60}{\dB}$ par rapport au niveau de crête maximal du signal d'émission de l'émetteur (PEP), tant que la puissance des signaux se situe au-dessus d'un niveau de $\qty{0,25}{\micro\watt}$ (cf. figure [ref:a_uagw]).

[question:AJ225]

<margin>
[picture:918:a_uagw:Atténuation des harmoniques supérieures gamme VHF/UHF/SHF]
</margin>

Pour la gamme des ondes courtes de $\qtyrange{1,7}{35}{\mega\hertz}$, il est stipulé que les émissions parasites et les harmoniques supérieures doivent être atténuées d'au moins $\qty{40}{\dB}$ par rapport au niveau de crête maximal du signal d'émission de l'émetteur (PEP), tant que la puissance des signaux se situe au-dessus d'un niveau de $\qty{0,25}{\micro\watt}$.

[question:AJ224]

%TODO INTÉGRER IMAGE DE DL1COM
Avec un analyseur de spectre, une mesure des harmoniques supérieures ou harmoniques (angl. harmonics) peut être effectuée en mode émissions parasites, comme illustré dans la figure [ref:a_uagw]. L'analyseur de spectre capture automatiquement le niveau de la porteuse ainsi que la suppression des harmoniques et les affiche en plus sur l'écran. Lorsqu'on construit soi-même un appareil, il est crucial de s'assurer par des mesures que les valeurs limites prescrites sont respectées. Un fabricant d'équipements radio commerciaux confirme le respect de ces limites par la déclaration CE, mais il arrive que certains appareils individuels ne respectent pas les exigences – dans de tels cas, l'Agence fédérale des réseaux peut interdire leur fonctionnement et leur vente.

Les émissions indésirables ne proviennent pas seulement des harmoniques supérieures, mais peuvent également survenir dans la préparation de fréquence des émetteurs – par exemple par des produits de mélange indésirables, par des fluctuations de la tension d'alimentation ou par une surmodulation du signal BF. Nous allons examiner cela de plus près dans ce qui suit.

Pour supprimer les produits de mélange indésirables – mais aussi les harmoniques supérieures – un filtre passe-bande est souvent utilisé après les mélangeurs. En particulier pour les émetteurs monobande ainsi que pour les appareils destinés aux gammes VHF, UHF et SHF, des filtres passe-bande sont utilisés à la place des filtres passe-bas classiques pour harmoniques supérieures. Pour ces équipements radio, des composantes de signal qui se produisent déjà lors de la préparation du signal d'émission et peuvent même se situer en dessous de la fréquence d'émission réelle doivent souvent être supprimées.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Les émissions indésirables peuvent également être présentes à proximité immédiate du signal d'émission. Celles-ci sont difficiles voire impossibles à supprimer par l'utilisation de filtres et devraient donc être efficacement supprimées dès le début de la préparation du signal par des mesures appropriées. De telles *émissions parasites*, également appelées *produits secondaires* (communément appelés "splatter"), qui élargissent involontairement le signal d'émission, sont souvent générées par un réglage trop élevé de l'amplificateur de microphone d'un émetteur. Cela déforme le signal BF, ce qui entraîne des émissions parasites indésirables. La figure [ref:a_harmonique] montre les émissions parasites.

[question:AJ219]

Des émissions indésirables peuvent également provenir d'une tension d'alimentation insuffisamment stabilisée des étages finals d'émetteur. Par exemple, une alimentation mal filtrée ou stabilisée (avec une tension de ronflement) du côté de la tension d'alimentation peut entraîner des émissions AM de l'étage final. Des interférences de signaux BF sur le côté de l'alimentation secteur d'un émetteur peuvent également conduire à des émissions AM correspondantes. Cela est souvent perceptible lors d'émissions CW comme une porteuse/tonalité "ronflante", en particulier avec les émetteurs plus anciens.

[question:AJ222]
[question:AJ223]
