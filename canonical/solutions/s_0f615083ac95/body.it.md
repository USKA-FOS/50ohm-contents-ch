Per USB, la banda laterale superiore deve rientrare nella banda passante del filtro a quarzo da $\qty{9}{\mega\hertz}$.

[picture:941:a_balancemodulator_usb:Modulatore bilanciato con portante soppressa e filtro a quarzo per USB]
[picture:941:a_balancemodulator_lsb:Modulatore bilanciato con portante soppressa e filtro a quarzo per LSB]

Il filtro a quarzo ha una larghezza di banda di circa $\qty{3}{\kilo\hertz}$. I suoi limiti di filtro si trovano quindi approssimativamente $\qty{1,5}{\kilo\hertz}$ al di sotto e al di sopra della frequenza centrale di $\qty{9}{\mega\hertz}$.

Per LSB, la frequenza della portante soppressa viene posizionata al limite superiore del filtro. La banda laterale inferiore si trova quindi all'interno della banda passante del filtro.

Per USB, la frequenza della portante soppressa viene posizionata al limite inferiore del filtro. La banda laterale superiore si trova quindi all'interno della banda passante del filtro:

$f_\mathrm{OSZ} = \qty{9}{\mega\hertz} - \qty{1,5}{\kilo\hertz} = \qty{8,9985}{\mega\hertz}$

Con la BF, viene quindi miscelata una frequenza dell’oscillatore di $\qty{8,9985}{\mega\hertz}$.