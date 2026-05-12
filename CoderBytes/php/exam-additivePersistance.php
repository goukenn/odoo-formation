<?php
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


echo additivePersistance(4)."\n";
echo additivePersistance(2718)."\n";
echo additivePersistance(487945)."\n";