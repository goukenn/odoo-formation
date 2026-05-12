
1. Formatage d'espaces dans les chaînes
Pour ajouter des espaces (padding) autour d'un mot ou d'une variable lors de l'affichage, 
on utilise généralement les f-strings ou la méthode `.format().Alignement` à gauche (espaces à droite) : 
f"{variable:<10}" réserve 10 caractères et aligne à gauche.
Alignement à droite (espaces à gauche) : f"{variable:>10}".
Centrage : f"{variable:^10}".Méthodes dédiées : 
`str.ljust(10)`,
`str.rjust(10)` ou `str.center(10)` permettent d'obtenir le même résultat sans syntaxe de formatage complexe.