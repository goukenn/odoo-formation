[X]WaveSorting


[X]OtherProduct
create a function that take an array of item then and create a new list of the products 
of all the other numbers in the array for each element. For example if arra is 
[1,2,3,4,5] then the new array, where feach location in the new array is the product of all other elements , is [120,60,40,30,24]. the following calculations were performed to get this answer is: [(2*3*4*5),(1*3*4*5)...] . You should generate this new array and then
return the numbers os a string joined by a hyphen: 120-60-....The array will contain at most 10 elements and at list 1 of only positive integers.


[X]RectangleArea
- Rectangle area on element if any order . arr is an array of 4 element of (x,y) or string '(x y)'. your program should return the area.


[X]HammingDistance
Taking array of 2 string of equal length and termine the distance of position where the characters are different. 
Example 
```bash
["coder", "codec"] == 1
["10011", "10100"] == 3
```

[X]Superincreating
`arr` of integer that the sum of previous elements of each is greather return `true` or `false`


[X] **OverlappingRanges**
Take an arr of 5 integers  where indices[0,1] first range. [2,3] second range and [4] the  x that determine if range intersection. return 'true' when overlapping of x element.
Example:
```bash
[4,10,2,6,3] = 'true'
```

[X] **ChangingSequence**

**Énoncé :**
La fonction `ChangingSequence(arr)` doit prendre un tableau de nombres et retourner l'**index** auquel la séquence change de direction (passe de croissant à décroissant ou vice versa).

**Détails :**
- Retourner l'index où les nombres **arrêtent d'augmenter** et **commencent à diminuer** (ou l'inverse)
- Le tableau contient au minimum 3 nombres
- Si le tableau contient une **seule séquence** (uniquement croissante ou uniquement décroissante), retourner `-1`
- L'indexation commence à 0

**Exemple :**
- `arr = [1, 2, 4, 6, 4, 3, 1]`
- Croissance : 1 → 2 → 4 → 6
- Décroissance commence à l'index 3 (après 6)
- Résultat : `3` (car 6 est le dernier point croissant, et 4 commence la décroissance)

---

**Solution Python :**

```python
def ChangingSequence(arr):
    """
    Trouve l'index où la séquence change de direction.
    
    Args:
        arr: tableau de nombres
    
    Returns:
        Index où le changement se produit, ou -1 si pas de changement
    """
    if len(arr) < 3:
        return -1
    
    # Détecter la direction initiale (croissant ou décroissant)
    i = 0
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
    
    # Si tous les éléments sont égaux
    if i == len(arr) - 1:
        return -1
    
    # Déterminer la direction initiale
    is_increasing = arr[i] < arr[i + 1]
    
    # Chercher le point de changement
    for j in range(i + 1, len(arr) - 1):
        current_increasing = arr[j] < arr[j + 1]
        
        # Si la direction change
        if current_increasing != is_increasing:
            return j
    
    return -1


# Tests
print(ChangingSequence([1, 2, 4, 6, 4, 3, 1]))  # 3
print(ChangingSequence([1, 2, 3, 4, 5]))         # -1 (croissant uniquement)
print(ChangingSequence([5, 4, 3, 2, 1]))         # -1 (décroissant uniquement)
print(ChangingSequence([1, 5, 10, 5, 1]))        # 2
print(ChangingSequence([5, 1, 2, 5, 10]))        # 1
```

**Explication :**
1. Ignorer les éléments égaux au début pour déterminer la direction initiale
2. Mémoriser si la séquence commence croissante ou décroissante
3. Parcourir le tableau et chercher le premier changement de direction
4. Retourner l'index du changement

**Cas de test supplémentaires :**
```python
print(ChangingSequence([1, 2, 4, 6, 4, 3, 1]))    # 3
print(ChangingSequence([2, 2, 2, 2]))             # -1 (tous égaux)
print(ChangingSequence([1, 2, 2, 1]))             # 2 (changement après les égaux)
```

[X] **OffLineMinimum**

Take an array and return a set that correspond to the digit string
I any iteger, E get the minimuf all inter add it to result 

[X] **MultiplicativePresistance**
Enter a number `num` get number of multiplicative per digit until the result of digit i equal to 1;
Example:
39 => 3*9 = 27 (1) => 2*7 = 14 (2) 1*4 = 4 (3)
return is 3

[X] **AdditivePersistance**
Same as multiplicative persitance but with multiplication 

```php
function additivePersistance(int $num){
    $r = 0;
    while($num>=10){
        $p = 0;
        while($num>0){
            $p += $num % 10;
            $num = floor($num / 10);
        }
        $num = $p;
        $r++;
    }
    return $r;
}
```

[X] **PowerofTwo**
```php
function poweroftwo(int $num):string{
     while(($num>=2) && (($num %2) ==0)){ 
        $num = floor($num/2);
    }
    return $num == 1? 'true':'false';
}
```
[X] **ThirdGreatest**
from arr of min 3 element return the third logest word.


[X] **NumberAddition**
in a string add each detected number

[X] **SwapCase**
return a string of swap case from input litteral.

[X] **DashInsert**
insert dash between 2 odd number.

[X] **MeanMode**

mean(moyenne) , mode occurence dictionary and counting.

[X] **CountingMinutes**
counting minute ansd pass day 

[X] **DivisionStringified**

[X] **SecondGreatLow**
Have the function that take `arr` and return the second lowest and second greatest numbers, respectively, separated by a space.
Example:
[7,7,12,98,106] => [12 98]
[1, 42,42,180] => [42 42]

[X] **LetterCount**
count letter greatest return word. or -1

[X] **ArithGeo**

[X] **Palindrome**
give an str and burn 
[X] **WordCount**
[X] **VowelCount**

[X] **AlphabetSoup**
[X] **TimeConvert**

[X] **CheckNums**
- too easy 
[X] **SimpleSymbol**

[X] **LetterCapitalize**

[X] **SimpleAdding**
-> adding sum
[X] **LetterChange**
- apply algorithm to a string 
every letter to next , and every voyel to upper case .

[X] **LongestWord**


[X] **FirstFactorial**
calculate factorial - for n!
n*(n-1)*(n-2)...1;

[X] **FirstReverse**
reverse string

[X] **FizzBuzz**
fizz buzz exo
[ ] **FindIntersection**

[x] - **CodeLangUserNameValidation**
## **CodeLangUserNameValidation**

- Have the function CodeLangUsernameValidation(str)
take the str parameter being passe and determine if the string is a valid username according to the following
rules:
1. the username is between 4 and 25 characters.
2. it must start with a letter.
3. it can only contain letters, numbers, and the underscore character.
4. it cannont ent with and underscore character.

if the username is a valid then your program should return the string `true`, otherwise return the string `false`
