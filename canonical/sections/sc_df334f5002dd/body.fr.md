Les composants CMS ne mesurent que quelques millimètres. CMS signifie *Composant Monté en Surface* (en anglais : *Surface-Mounted Device*). Contrairement aux composants classiques, ils ne possèdent pas de broches de connexion, mais sont directement soudés sur la carte de circuit imprimé, sans trou métallisé. Nous allons maintenant nous intéresser à la désignation des résistances CMS.

<margin>
[photo:318:e_platine_smd:Carte de circuit imprimé avec composants CMS]
</margin>

---

La figure [ref:e_smd] montre une résistance CMS. Pour indiquer la valeur de la résistance, des chiffres y sont imprimés – dans ce cas, les chiffres 113. La valeur de la résistance s’obtient alors de la manière suivante : toutes les chiffres sauf le *dernier* sont considérés comme une valeur numérique pure. Dans l’exemple 113, cela donne donc *11* comme valeur numérique. Le *dernier* chiffre indique la *puissance de dix* par laquelle multiplier les autres chiffres. Un 1 correspond à la première puissance de dix $10^1$, un 2 à la deuxième puissance de dix $10^2$, etc.

<margin>
[picture:1006:e_smd:Composant CMS]
</margin>

Dans notre exemple, nous obtenons donc : $11 \cdot 10^3$, soit $\qty{11000}{\ohm}$ ou encore $\qty{11}{\kilo\ohm}$.

[question:EC114]
[question:EC115]
[question:EC116]
[question:EC117]