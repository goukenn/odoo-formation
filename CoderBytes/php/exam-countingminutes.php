<?php
function countingminutes(string $str){
    $t = explode('-', $str, 2);
    $hu = substr($t[0], -2);
    $hp = substr($t[1], -2);
    $l = 0;
    if ($hu!=$hp){
        if ($hu=='pm')
            $l = 12;
        else 
            $l = -12;
    }
    foreach($t as $k=>$mt){
        $r = substr($mt,0, -2);
        list($h, $min) = explode(':', $r, 2);
        $h = intval($h);
        if(substr($mt,-2)=='pm'){
            $h = $h-$l;
        }
        $t[$k] = ($h *60) + intval($min); 
    }
    $r= abs($t[1] - $t[0]);  
    return $r;

}


echo countingminutes('1:00pm-11:00am')."\n";
echo countingminutes('9:00am-10:00am')."\n"; 
echo countingminutes('11:00am-1:00pm')."\n";