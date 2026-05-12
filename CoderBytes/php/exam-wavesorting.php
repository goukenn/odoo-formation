<?php

// + | --------------------------------------------------------------------
// + | Wave Sorting problem - check that
// + | Have a function that take the array of positive integers stored in `arr` and
// + | return a string `true` if the numbers can be arranged in a wave pattern: 
// + | q0<q1>q2<q3.... for example if is : [0,1,2,4,1,4] then a possible ordering of the numbers is : 
// + | [2,0,4,1,4,1]. the result should be the string `true`. the array will always
// + | contain at least 2 elements.

// + | --------------------------------------------------------------------
// + | solution: 
// + | order t
// + |

/**
 * 
 * @param array $arr 
 * @return string 
 */
function wavesorting(array $arr): string{
    $ln = count($arr);
    $f = [];
    // calculate frequency  
    array_map(function($a)use(& $f){
        $max = max($max ?? $a, $a); 
        if (!isset($f[$a]))
            $f[$a] = 0;
        $f[$a]++;
    }, $arr);
    // max must be greater than halv
    $cmax = max(array_values($f)); 

    return ($cmax>($ln/2)) ? "false" : "true";
}
$cond = [
    [0,1,2,4,1,1,1],
    [2,0,4,1,4,1]
];

foreach($cond as $t){
    print_r ( implode(' = ', [json_encode($t), json_encode(wavesorting($t))]));
    echo "\n";
}

exit;