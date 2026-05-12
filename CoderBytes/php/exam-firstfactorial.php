<?php
function firstfactorial(int $num){
    if  ($num>18 ) 
        die('bad test case');
    $l = 1;
    while($num>1){
        $l *=$num;
        $num--;
    }
    return $l;
}

echo firstfactorial(4)."\n"; // 24
echo firstfactorial(8)."\n"; // 40320