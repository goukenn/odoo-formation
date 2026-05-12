<?php
function meanmode(array $arr): string
{
    $mode = 0;
    $sum = 0;
    $T = count($arr);
    $t = [];
    while (count($arr) > 0) {
        $q = array_shift($arr);
        $sum += $q;
        if (!isset($t[$q])) {
            $t[$q] = 0;
        }
        $t[$q]++;
    } 
    arsort($t);
    $mean = $sum / $T;
    $mode = key($t); 
    return $mean == $mode ? 'true' : 'false';
}

echo meanmode([1,2,3])."\n";
echo meanmode([5, 3, 3, 3, 1]) . "\n";
