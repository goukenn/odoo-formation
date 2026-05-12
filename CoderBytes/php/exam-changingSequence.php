<?php

// trop long 
function changingSequenceOld(array $arr){
    $r = -1;
    $ln = count($arr);
    if ($ln < 3){
        return $r;
    }
    $i = 0;
    $s = $arr[0];
    for ($i = 1; $i < $ln; $i++){
        if ($arr[$i] != $s) break;
    }
    if ($i == $ln)
        return $r;

    $is_increase = $arr[$i] > $arr[$i-1];
    for($j = $i; $j < $ln-1;$j++){
        $current_increasing = $arr[$j] < $arr[$j+1];
        if ($current_increasing != $is_increase)
            return $j;
    }
    return $r;
}

function changingSequence(array $arr){
    $count = count($arr);
    $i = 1;
    for(;($count>=3) && $i<$count-1;$i++){
        $prev= $arr[$i-1];
        $cur =  $arr[$i];
        $next = $arr[$i+1];
        if (
            (($prev < $cur) && ($cur>$next)) ||
            (($prev>$cur) && ($cur<$next))
          ){
            return $i;
        }
    }
    return -1;
}


print_r(changingSequence([1, 2, 4, 6, 4, 3, 1])) ; # 3
print_r(changingSequence([1, 2, 3, 4, 5]))   ;      # -1 (croissant uniquement)
print_r(changingSequence([5, 4, 3, 2, 1]))  ;       # -1 (décroissant uniquement)
print_r(changingSequence([1, 5, 10, 5, 1]))    ;    # 2
print_r(changingSequence([5, 1, 2, 5, 10]))    ;    # 1
print_r(changingSequence([1, 1, 1]))    ;    # -1
print_r(changingSequence([1, 2, 3]))    ;    # -1