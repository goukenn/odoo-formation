<?php
function multiplicativePersistance(int $num){
    $r = 0;
    while ($num>=10){
        $s = 1;
        array_map(function($a)use(&$s){
            $s *= intval($a);
        }, str_split(''.$num, 1));  
        $num = $s;
        $r++;
    }
    return $r;
}

function multiplicativePersistance2(int $num){
    $r = 0;
    while($num>=10){
        $p = 1;
        while($num>0){
            $p *= $num % 10; // last number 
            $num = floor($num / 10); // reduce decimal
        }
        $r++;
        $num = $p;
    }
    return $r;
}

// echo 'floor: '.floor(24 / 10)."\n";;
// echo 'mod:   '.(24 % 10)."\n";
echo multiplicativePersistance2(251)."\n";
echo multiplicativePersistance(251)."\n";
exit; 

echo multiplicativePersistance(4)."\n";
echo multiplicativePersistance(25)."\n";