<?php
function simpleadding(int $num){
    $sum = 0;
    foreach(range(1, $num) as $k){
        $sum+=$k;
    }
    return $sum;
}

echo simpleadding(4)."\n";
