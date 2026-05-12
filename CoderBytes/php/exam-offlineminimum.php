<?php

/**
 * 
 * @param array $arr 
 * @return mixed[] 
 */
function offlineminimum(array $arr)
{
    $t = [];
    $min = []; 
    foreach ($arr as $v) {
        if ($v == 'E') {
            $t[] = $m = min(...$min);
            array_splice($min, array_search($m, $min), 1);
        } else {
            $c = intval($v);
            $min[] = $c; 
        }
    } 
    return $t;
}


print_r(offlineminimum([5, 4, 6, 'E', 1, 7, 'E', 'E', '3', 2]));
echo "\n";
