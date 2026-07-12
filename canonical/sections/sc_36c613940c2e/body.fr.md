Les oscillateurs à fréquence réglable peuvent être réalisés de différentes manières. Une possibilité est l'oscillateur commandé en tension VCO - Voltage controlled oscillator.

[question:AD601]

---

Pour que la fréquence de l'oscillateur soit variable, on peut insérer dans son circuit oscillant une diode à capacité, dont la capacité peut être influencée par une tension continue (voir figure [ref:a_vco_schaltung]). Une modification de cette tension continue entraîne alors une modification correspondante de la fréquence de l'oscillateur. De cette manière, l'oscillateur peut être accordé au moyen d'une tension de commande. 

<margin>
[picture:752:a_vco_schaltung:Circuit VCO avec diode à capacité]
</margin>

La diode à capacité est utilisée en polarisation inverse. Plus la tension inverse de la diode est élevée, plus sa capacité est faible, laquelle est déterminée par la taille de la couche de jonction (jonction P-N). La couche de jonction s'agrandit lorsque la tension inverse appliquée augmente, ce qui réduit la capacité et donc la fréquence du circuit oscillant selon la formule d'oscillation de Thomson.

Inversement, la couche de jonction de la diode à capacité se réduit lorsque la tension inverse appliquée diminue, ce qui augmente la capacité et donc la fréquence du circuit oscillant devient plus petite. La tension inverse peut être générée, par exemple, par un potentiomètre ou un circuit de commande.

%TODO: Éventuellement, un graphique sur la couche de blocage et le comportement dans la diode à capacité.

[question:AD218] 

Pour tous les circuits oscillateurs, indépendamment de leur conception, il est vrai que les rétroactions indésirables peuvent entraîner des instabilités de fréquence. Cela s'applique aux VCO ainsi qu'aux VFO (par exemple avec des condensateurs rotatifs) et à d'autres oscillateurs.

[question:AD611]