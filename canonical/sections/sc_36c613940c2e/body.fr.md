Les oscillateurs commandés en fréquence peuvent être réalisés de différentes manières. Une possibilité est l’**oscillateur commandé en tension (VCO - Voltage Controlled Oscillator)**.

[question:AD601]

<margin>
[picture:752:a_vco_schaltung:Schéma d’un VCO avec diode à capacité variable]
</margin>

---

Pour rendre la fréquence de l’oscillateur variable, on peut insérer dans son circuit oscillant une diode à capacité variable dont la capacité peut être influencée par une tension continue (cf. figure [ref:a_vco_schaltung]). Une modification de cette tension continue entraîne alors une variation correspondante de la fréquence de l’oscillateur. L’oscillateur devient ainsi accordable au moyen d’une tension de commande.

La diode à capacité variable fonctionne en polarisation inverse. Plus la tension inverse appliquée à la diode est élevée, plus sa capacité diminue, celle-ci étant déterminée par l’épaisseur de la jonction (jonction P-N). La jonction s’élargit lorsque la tension inverse appliquée augmente, ce qui réduit la capacité et, par conséquent, augmente la fréquence du circuit oscillant selon la formule de Thomson.

Inversement, lorsque la tension inverse appliquée diminue, la jonction de la diode à capacité variable se rétrécit, ce qui augmente la capacité et réduit ainsi la fréquence du circuit oscillant. La tension inverse peut être générée, par exemple, par un potentiomètre ou un circuit de commande.

<tip>
Plus la tension aux bornes de la diode à capacité variable est élevée, plus la distance entre les "plaques" ($d$) augmente. Il est toujours judicieux de consulter le recueil de formules pour comprendre ces chaînes d’effets.

$C = \epsilon_0 \cdot \epsilon_r \cdot \frac{A}{d}$

$f = \frac{1}{2\pi\sqrt{L\cdot C}}$

$U \uparrow \quad\rightarrow\quad C \downarrow \quad\rightarrow\quad f \uparrow$

$U \downarrow \quad\rightarrow\quad C \uparrow \quad\rightarrow\quad f \downarrow$
</tip>

[question:AD218]

Pour toutes les configurations d’oscillateurs, quelle que soit leur réalisation, il est important de noter que des couplages parasites indésirables peuvent entraîner des instabilités de fréquence. Cela s’applique aussi bien aux VCO qu’aux VFO (par exemple avec des condensateurs variables) et à d’autres types d’oscillateurs.

[question:AD611]