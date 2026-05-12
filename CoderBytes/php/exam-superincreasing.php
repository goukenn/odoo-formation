<?php
/**
 * sum of previous element is greather than the current element
 * @return string 
 */
function superincreasing(array $arr): string{
    $sum = 0;
    while(count($arr)>0){
        $q = array_shift($arr);
        if ($q<$sum)
            return 'false';
        $sum += $q;
    }
    return 'true';
}


echo superincreasing([1,2,3,4])."\n";
echo superincreasing([1,3,6,13,54])."\n";