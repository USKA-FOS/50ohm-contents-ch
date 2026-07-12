Dans la classe E, nous avons déjà rencontré des émissions indésirables sous forme d'*harmoniques supérieures* et d'*émissions parasites*. Les harmoniques supérieures ou harmoniques d'un signal se produisent toujours lorsque des écarts par rapport à la courbe sinusoïdale idéale se forment et sont toujours des multiples entiers de la fréquence fondamentale, comme le montre la figure [ref:a_harmonische].

Un exemple est donné par la question d'examen suivante : Si un amplificateur est surchargé, les pics de l'amplitude du signal sinusoïdal sont limités – ce qui entraîne la création d'harmoniques supérieures.

[question:AJ207]

<margin>
[picture:868:a_harmonische: Harmoniques supérieures (HS), Harmoniques (Harm.) et émissions parasites (EP)]
</margin>

---

Lors de l'examen des multiples de la fréquence fondamentale d'un signal, nous distinguons les termes *harmoniques et harmoniques supérieures* du signal. Ces deux termes ne diffèrent que par leur définition et leur comptage. La 1ère harmonique d'un signal est sa fréquence fondamentale elle-même. La 2ème harmonique correspond à la 1ère harmonique supérieure d'un signal, la 3ème harmonique à la 2ème harmonique supérieure d'un signal, et ainsi de suite. Le tableau ci-joint [ref:a_harmonique] montre la relation.

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
La radio FM est la "radio classique" sur ondes ultracourtes (FM). La diffusion de programmes radiophoniques se fait dans la bande de fréquences de $\qtyrange{87,6}{107,9}{\mega\hertz}$.
</tip>

Si certaines harmoniques supérieures ou harmoniques d'un signal doivent être supprimées individuellement, cela peut être fait, outre le filtre classique des harmoniques supérieures (passe-bas), également par des circuits bouchons. Un circuit bouchon supprime exactement une fréquence au maximum et laisse passer toutes les autres presque sans entrave.

[question:AJ210]

---

Selon l'ordonnance sur le radioamateur (AFuV), les émissions indésirables doivent être limitées au minimum possible. La [disposition 33](https://50ohm.de/vfg33) de 2007 fixe toutefois des valeurs limites précises, qui doivent être respectées par le radioamateur ainsi que par les fabricants d'appareils commerciaux.

<margin>
[photo:319:a_vfg33:Extrait de la disposition 33 de 2007]
</margin>

Pour la plage VHF/UHF/SHF de $\qtyrange{50}{1000}{\mega\hertz}$, il est stipulé que les émissions parasites et les harmoniques supérieures doivent être atténuées d'au moins $\qty{60}{\dB}$ par rapport au niveau maximal de crête du signal émis de l'émetteur (PEP), tant que la puissance des signaux se situe au-dessus d'un niveau de $\qty{0,25}{\micro\watt}$ (cf. figure [ref:a_uagw]).

[question:AJ225]

<margin>
[picture:918:a_uagw:Atténuation des harmoniques supérieures dans la plage VHF/UHF/SHF]
</margin>

Pour la plage des ondes courtes de $\qtyrange{1,7}{35}{\mega\hertz}$, il est stipulé que les émissions parasites et les harmoniques supérieures doivent être atténuées d'au moins $\qty{40}{\dB}$ par rapport au niveau maximal de crête du signal émis de l'émetteur (PEP), tant que la puissance des signaux se situe au-dessus d'un niveau de $\qty{0,25}{\micro\watt}$.

[question:AJ224]

%TODO INSÉRER IMAGE DE DL1COM
Avec un analyseur de spectre, il est possible de mesurer les harmoniques supérieures ou les harmoniques (en anglais harmonics) dans le mode spurious emissions, comme le montre la figure [ref:a_uagw]. L'analyseur de spectre détecte automatiquement le niveau de la porteuse ainsi que la suppression des harmoniques et les affiche en plus sur l'écran. Si vous construisez vous-même un appareil, il est décisif de vous assurer par des mesures que les valeurs limites prescrites sont respectées. Un fabricant d'appareils radio commerciaux confirme certes le respect de ces valeurs limites avec la déclaration CE, mais il arrive nevertheless que certains appareils ne respectent pas les spécifications – dans de tels cas, l'Agence fédérale des réseaux peut interdire leur exploitation et leur vente.

Les émissions indésirables ne sont pas seulement causées par les harmoniques supérieures, mais peuvent également survenir dans la préparation des fréquences des émetteurs – par exemple par des produits de mélange indésirables, par des fluctuations de la tension d'alimentation ou par une surcharge du signal BF. Nous allons examiner cela de plus près dans la suite.

Pour la suppression des produits de mélange indésirables – mais aussi des harmoniques supérieures – un filtre passe-bande est souvent utilisé après les mélangeurs. En particulier dans le cas des émetteurs à bande unique ainsi que dans les appareils pour les bandes VHF, UHF et SHF, des filtres passe-bande sont utilisés au lieu des passe-bas classiques pour les harmoniques supérieures. Dans ces appareils radio, il est souvent nécessaire de supprimer également des composantes de signal qui se produisent déjà lors de l'élaboration du signal d'émission et qui peuvent même se situer en dessous de la fréquence d'émission proprement dite.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Les émissions indésirables peuvent également se situer à proximité immédiate du signal d'émission. Celles-ci sont difficiles ou impossibles à supprimer par l'utilisation de filtres et doivent donc être supprimées efficacement dès le début de l'élaboration du signal par des mesures appropriées. Souvent, de telles *émissions parasites*, ou également appelées *produits secondaires* (familièrement également désignées comme "splatter"), qui élargissent involontairement le signal d'émission, sont causées par un réglage trop élevé de l'amplificateur de microphone d'un émetteur. Cela entraîne une distorsion du signal BF, ce qui a pour conséquence des émissions parasites indésirables. La figure [ref:a_harmonische] montre les émissions parasites.

[question:AJ219]

Des émissions indésirables peuvent également être causées par une tension d'alimentation insuffisamment stabilisée des étages finaux des émetteurs. Par exemple, une alimentation mal filtrée ou stabilisée (affectée par une tension de bruit) du côté de la tension d'alimentation peut entraîner des émissions AM de l'étage final. Des interférences de signaux BF du côté de l'alimentation réseau d'un émetteur peuvent également entraîner des émissions AM correspondantes. Cela est souvent perceptible comme une porteuse/ton "bruitée" lors des émissions CW, en particulier avec les anciens émetteurs.

[question:AJ222]
[question:AJ223]