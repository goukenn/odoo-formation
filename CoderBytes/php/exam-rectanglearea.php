<?php
function rectanglearea(array $arr){
    (count($arr)!= 4 ) && die('invalid arg');
    $arr = array_map(function($a){
        if (is_string($a)){
            $a = array_map('floatval', 
                explode(' ', trim($a, '()'), 2)
            ); 
        }
        return $a;
    }, $arr);
    $minx = $maxx = $arr[0][0];
    $miny = $maxy = $arr[0][1];
    array_shift($arr);
    foreach ($arr as  $t) {
        $minx = min($t[0], $minx);
        $maxx = max($t[0], $maxx);
        $miny = min($t[1], $miny);
        $maxy = max($t[1], $maxy);
    }
    return ($maxx - $minx) * ($maxy - $miny);
}


echo rectanglearea([
    [0,0],[3,0],[0, 2],[3,2]
]). "\n";


echo rectanglearea([
    '(0 0)','(3 0)','(0 2)', '(3 2)'
]). "\n";