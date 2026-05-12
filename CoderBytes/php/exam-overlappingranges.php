<?php

/**
 * 
 * @param array $arr 
 * @return bool 
 */
function overlapping_ranges(array $arr){
    $ln = count($arr);
    ($ln != 5 ) && igk_die('invalid arg');
    $first_range = range($arr[0], $arr[1]);
    $second_range = range($arr[2], $arr[3]);
    $l = $arr[4];
    $tab = array_intersect($first_range, $second_range);
    return count($tab) >=$l;
}

/**
 * 
 * @param array $arr 
 * @return string 
 */
function overlapping_ranges_2(array $arr){
    list($a, $b, $c, $d, $x) = $arr;
    //$b++; $d++;
    $min = max($a, $c);
    $max = min($b, $d);
    return max(0, ($max - $min) +1) >= $x? 'true' : 'false';
}


echo 'return : '. overlapping_ranges_2([4,10,2,6,3])."\n";
echo 'return : '. overlapping_ranges_2([4,10,2,6,8])."\n";
echo 'return : '. overlapping_ranges_2([4,10,12,16,2])."\n";