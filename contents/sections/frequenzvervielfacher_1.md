Um früher in Amateurfunk-Mehrbandsendern nicht für jeden Frequenzbereich einzelne Oszillatoren bauen und abstimmen zu müssen, verwendete man das Prinzip der Frequenzvervielfachung. Hierbei wurde ein stabiler Oszillator auf der Frequenz des niedrigsten Bandes (z.B. $\qty{3,5}{\mega\hertz}$) betrieben, dessen Ausgangssignal dann anschließend mittels Frequenzvervielfachern auf die jeweils gewünschten Amateurfunkbänder umgesetzt wurde. Hierbei ist es von Vorteil, dass die einzelnen Frequenzbänder zueinander in festen Verhältnissen stehen (z.B. $\qty{3,5}{\mega\hertz}$, $\qty{7}{\mega\hertz}$, $\qty{14}{\mega\hertz}$ usw.) und meist ganzzahlige Vielfache des niedrigsten Bandes sind. Hierdurch fallen auch Oberwellen wieder in einen Amateurfunkbereich, was seitens der Regulierungsbehörden durchaus gewünscht ist, um Störungen anderer Dienste durch Oberwellen zu vermeiden. Generell kann man Oszillatoren auf niedrigen Frequenzen mit höherer Stabilität einfacher konstruieren und bauen als auf hohen Frequenzen. 

---

Abbildung [ref:n_f_vervielfacher] zeigt das Blockschaltbild eines Frequenzvervielfachers mit dem Faktor $2$ bei dem die Eingangsfrequenz von $\qty{3,5}{\mega\hertz}$ auf $\qty{7}{\mega\hertz}$ angehoben wird. Ein Frequenzvervielfacher wird dabei typischerweise durch eine Nichtlinearität (z. B. Diode) erzeugt, die gezielt Oberwellen des Eingangssignals erzeugt, aus denen anschließend mit einem Bandpassfilter die gewünschte Vielfachfrequenz ausgewählt wird.

<margin>
[picture:1042:n_f_vervielfacher:Blockschaltbild eines Frequenzvervielfachers]
</margin>

Häufig verwendet man eine Kette von Frequenzvervielfachern, um die gewünschten Multiplikationsfaktoren zu erreichen. Hierbei werden bei Reihenschaltung von Vervielfachern die einzelnen Faktoren miteinander multipliziert.
Umgekehrt kann eine solche Schaltung natürlich auch rückgerechnet werden. Hierbei muss durch die entsprechenden Teilfaktoren dann dividiert werden.

[question:EF303]
[question:EF302]
[question:EF301]